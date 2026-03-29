#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".txt", ".py", ".json"}


def load_map(path: Path) -> dict:
    return json.loads(path.read_text())


def iter_audit_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for relative in paths:
        path = ROOT / relative
        if path.is_file():
            files.append(path)
            continue
        if path.is_dir():
            files.extend(sorted(p for p in path.rglob("*") if p.is_file() and p.suffix in TEXT_EXTENSIONS))
    return files


def build_changed_articles(article_map: dict) -> list[dict]:
    changed: list[dict] = []
    for article in article_map["articles"]:
        old_number = article.get("old_number")
        old_name = Path(article["source_path"]).name
        new_name = article["dest_filename"]
        if old_number and (old_number != article["new_number"] or old_name != new_name):
            changed.append(article)
    return changed


def audit_files(files: list[Path], changed_articles: list[dict], target_dir: str) -> list[str]:
    findings: list[str] = []
    link_pattern = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")
    changed_filename_map = {
        Path(article["source_path"]).name: article["dest_filename"]
        for article in changed_articles
        if Path(article["source_path"]).name != article["dest_filename"]
    }
    target_to_number = {article["dest_filename"]: article["new_number"] for article in changed_articles}

    for path in files:
        text = path.read_text()
        lines = text.splitlines()

        for old_name, new_name in changed_filename_map.items():
            for line_no, line in enumerate(lines, start=1):
                if old_name in line:
                    findings.append(
                        f"- {path.relative_to(ROOT)}:{line_no}: stale filename `{old_name}` should migrate to `{target_dir}/{new_name}`"
                    )

        for article in changed_articles:
            old_number = article.get("old_number")
            old_title = article.get("old_title")
            if not old_number or not old_title:
                continue
            marker = f"Article {old_number} — {old_title}"
            for line_no, line in enumerate(lines, start=1):
                if marker in line:
                    findings.append(
                        f"- {path.relative_to(ROOT)}:{line_no}: stale titled reference `{marker}` should become `Article {article['new_number']} — {article['new_title']}`"
                    )

        for match in link_pattern.finditer(text):
            label = match.group("label")
            target = Path(match.group("target")).name
            label_match = re.search(r"\bArticle (?P<number>[IVX]+)\b", label)
            expected_number = target_to_number.get(target)
            if not label_match or not expected_number:
                continue
            if label_match.group("number") != expected_number:
                line_no = text[: match.start()].count("\n") + 1
                findings.append(
                    f"- {path.relative_to(ROOT)}:{line_no}: link label `{label_match.group(0)}` does not match target `{target}`"
                )

    deduped: list[str] = []
    seen: set[str] = set()
    for finding in findings:
        if finding in seen:
            continue
        seen.add(finding)
        deduped.append(finding)
    return deduped


def write_report(report_path: Path, audited_paths: list[str], findings: list[str]) -> None:
    lines = [
        "# Repo Reorder Audit",
        "",
        "## Audited Paths",
        "",
    ]
    lines.extend(f"- `{path}`" for path in audited_paths)
    lines.extend(["", "## Findings", ""])
    if findings:
        lines.extend(findings)
    else:
        lines.append("- None found.")
    report_path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit repo files for reorder-related reference drift.")
    parser.add_argument("--map", dest="map_path", default="design-notes/article-order-map.json")
    args = parser.parse_args()

    article_map = load_map(ROOT / args.map_path)
    audited_paths = article_map.get("repo_audit_paths", [])
    report_path = ROOT / article_map.get("repo_audit_report_path", "design-notes/repo-reorder-audit.md")
    changed_articles = build_changed_articles(article_map)
    files = iter_audit_files(audited_paths)
    findings = audit_files(files, changed_articles, article_map["target_directory"])
    write_report(report_path, audited_paths, findings)

    print(f"Wrote repo audit report to {report_path.relative_to(ROOT)}")
    if findings:
        print(f"Found {len(findings)} repo-wide reorder issues.")
        return 1
    print("No repo-wide reorder issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
