#!/usr/bin/env python3
"""
translate.py — Translate changed (or all) constitutional articles using Claude.

Usage:
    # Translate articles changed since last commit, for all configured languages
    python translate.py

    # Translate everything (first run, or full refresh)
    python translate.py --all

    # Specific language(s) only
    python translate.py --lang es
    python translate.py --lang es,zh-Hans

    # Specific article(s) only
    python translate.py --article articles/III-executive.md

    # Dry run — print what would be translated without calling the API
    python translate.py --dry-run

Requirements:
    pip install anthropic pyyaml
    Set ANTHROPIC_API_KEY in your environment.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

import anthropic
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "translation" / "config.yaml"

SYSTEM_PROMPT = """\
You are a professional constitutional translator. Translate the following constitutional article from English into {lang_name}.

Rules:
- Preserve legal precision. This is formal constitutional text.
- Keep all section numbers, cross-references (e.g., §5.3, Art. III), and structural markers (headings, bold provision numbers) exactly as they appear in the source.
- Preserve markdown formatting (##, **, *, `, ---) exactly.
- Do not add commentary, footnotes, or translator's notes unless explicitly asked.
- Use formal constitutional register throughout.
- Return only the translated article text. No preamble, no explanation.

{glossary_block}\
"""


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_glossary(lang: str, config: dict) -> dict:
    path = REPO_ROOT / "translation" / "glossary" / f"{lang}.json"
    if path.exists():
        import json
        with open(path) as f:
            data = json.load(f)
        return {k: v for k, v in data.items() if not k.startswith("_") and v}
    return {}


def glossary_block(glossary: dict) -> str:
    if not glossary:
        return ""
    lines = ["Use these constitutional terms consistently:\n"]
    for en, trans in glossary.items():
        lines.append(f"  {en} → {trans}")
    return "\n".join(lines) + "\n\n"


def changed_articles(config: dict) -> list[Path]:
    """Return article files changed since the last commit."""
    article_dir = REPO_ROOT / config["source_dir"]
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True
        )
        changed = set(result.stdout.splitlines())
        # Also include staged changes
        result2 = subprocess.run(
            ["git", "diff", "--name-only", "--cached"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True
        )
        changed |= set(result2.stdout.splitlines())
        return [REPO_ROOT / p for p in sorted(changed)
                if p.startswith(config["source_dir"] + "/") and p.endswith(".md")]
    except subprocess.CalledProcessError:
        return []


def all_articles(config: dict) -> list[Path]:
    return sorted((REPO_ROOT / config["source_dir"]).glob("*.md"))


def output_path(article_path: Path, lang: str, config: dict) -> Path:
    out_dir = REPO_ROOT / config["output_dir"] / lang / "articles"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / article_path.name


def translate_article(client: anthropic.Anthropic, article_path: Path,
                       lang: str, lang_name: str, glossary: dict,
                       model: str, max_tokens: int) -> str:
    source = article_path.read_text(encoding="utf-8")
    system = SYSTEM_PROMPT.format(
        lang_name=lang_name,
        glossary_block=glossary_block(glossary),
    )
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": source}],
    )
    return resp.content[0].text.strip()


def main():
    parser = argparse.ArgumentParser(description="Translate constitutional articles")
    parser.add_argument("--all", action="store_true", help="Translate all articles, not just changed ones")
    parser.add_argument("--lang", help="Comma-separated language codes (default: all configured)")
    parser.add_argument("--article", help="Path to a single article file")
    parser.add_argument("--model", help="Override model from config.yaml")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be translated without calling API")
    args = parser.parse_args()

    config = load_config()
    lang_map = {l["code"]: l["name"] for l in config["target_languages"]}

    # Determine languages
    if args.lang:
        langs = [l.strip() for l in args.lang.split(",")]
        for lang in langs:
            if lang not in lang_map:
                print(f"ERROR: {lang!r} not in config.yaml", file=sys.stderr)
                sys.exit(1)
    else:
        langs = list(lang_map.keys())

    # Determine articles
    if args.article:
        articles = [Path(args.article).resolve()]
    elif args.all:
        articles = all_articles(config)
    else:
        articles = changed_articles(config)
        if not articles:
            print("No changed articles detected. Use --all to translate everything.")
            return

    model = args.model or config["model"]
    max_tokens = config.get("max_tokens_per_article", 8000)

    if args.dry_run:
        print(f"Would translate {len(articles)} article(s) into {len(langs)} language(s):")
        for article in articles:
            for lang in langs:
                print(f"  {article.name} → {lang}")
        return

    client = anthropic.Anthropic()

    for lang in langs:
        lang_name = lang_map[lang]
        glossary = load_glossary(lang, config)
        print(f"\n[{lang}] {lang_name}")

        for article_path in articles:
            if not article_path.exists():
                print(f"  SKIP {article_path.name} (not found)")
                continue

            out = output_path(article_path, lang, config)
            print(f"  {article_path.name} → {out.relative_to(REPO_ROOT)} ...", end=" ", flush=True)

            try:
                translated = translate_article(client, article_path, lang, lang_name,
                                               glossary, model, max_tokens)
                out.write_text(translated, encoding="utf-8")
                print("done")
            except anthropic.APIError as e:
                print(f"ERROR: {e}")

    print("\nDone. Review changes with: git diff translation/translations/")


if __name__ == "__main__":
    main()
