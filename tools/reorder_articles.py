#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_map(path: Path) -> dict:
    return json.loads(path.read_text())


def heading_for(number: str, title: str) -> str:
    return f"# Article {number} — {title}"


def build_replacements(article_map: dict) -> tuple[re.Pattern[str] | None, dict[str, str], dict[str, str], dict[str, str]]:
    article_number_map: dict[str, str] = {}
    filename_map: dict[str, str] = {}
    target_to_number: dict[str, str] = {}
    for article in article_map["articles"]:
        old_number = article.get("old_number")
        new_number = article["new_number"]
        if old_number and old_number != new_number:
            article_number_map[old_number] = new_number
        source_name = Path(article["source_path"]).name
        filename_map[source_name] = article["dest_filename"]
        target_to_number[article["dest_filename"]] = new_number
    if article_number_map:
        joined_numbers = "|".join(sorted((re.escape(number) for number in article_number_map), key=len, reverse=True))
        article_pattern = re.compile(rf"\bArticle (?P<number>{joined_numbers})\b")
    else:
        article_pattern = None
    return article_pattern, article_number_map, filename_map, target_to_number


def rewrite_content(
    text: str,
    article: dict,
    article_pattern: re.Pattern[str] | None,
    article_number_map: dict[str, str],
    filename_map: dict[str, str],
    target_to_number: dict[str, str],
) -> str:
    lines = text.splitlines()
    text = "\n".join(lines)

    if article_pattern:
        text = article_pattern.sub(lambda match: f"Article {article_number_map[match.group('number')]}", text)

    for old_name, new_name in filename_map.items():
        text = text.replace(f"({old_name})", f"({new_name})")
        text = text.replace(f"]({old_name})", f"]({new_name})")
        text = re.sub(rf"\((?:[^)]+/)?{re.escape(old_name)}\)", f"({new_name})", text)

    link_pattern = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")

    def normalize_link_label(match: re.Match[str]) -> str:
        label = match.group("label")
        target = Path(match.group("target")).name
        expected_number = target_to_number.get(target)
        if not expected_number:
            return match.group(0)
        normalized_label = re.sub(r"\bArticle [IVX]+\b", f"Article {expected_number}", label, count=1)
        return f"[{normalized_label}]({match.group('target')})"

    text = link_pattern.sub(normalize_link_label, text)

    lines = text.splitlines()
    if lines and (lines[0].startswith("# Article ") or lines[0].startswith("# Proposed Article ")):
        lines[0] = heading_for(article["new_number"], article["new_title"])
        text = "\n".join(lines)
    return text + ("\n" if not text.endswith("\n") else "")


def audit_old_references(target_dir: Path, article_map: dict) -> list[str]:
    link_pattern = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)]+)\)")
    target_to_number = {article["dest_filename"]: article["new_number"] for article in article_map["articles"]}
    old_filenames = {
        Path(article["source_path"]).name
        for article in article_map["articles"]
        if Path(article["source_path"]).name != article["dest_filename"]
    }
    findings: list[str] = []
    for path in sorted(target_dir.glob("*.md")):
        text = path.read_text()
        for match in link_pattern.finditer(text):
            target = Path(match.group("target")).name
            label = match.group("label")
            line_no = text[: match.start()].count("\n") + 1
            if target in old_filenames:
                findings.append(f"- {path.relative_to(ROOT)}:{line_no}: stale link target `{target}`")
                continue
            label_match = re.search(r"\bArticle (?P<number>[IVX]+)\b", label)
            expected_number = target_to_number.get(target)
            if label_match and expected_number and label_match.group("number") != expected_number:
                findings.append(
                    f"- {path.relative_to(ROOT)}:{line_no}: link label `{label_match.group(0)}` does not match target `{target}`"
                )
    return findings


def audit_target_tree(target_dir: Path, article_map: dict) -> list[str]:
    findings: list[str] = []
    expected_files = {article["dest_filename"] for article in article_map["articles"]}
    if not target_dir.exists():
        return [f"- missing target directory `{target_dir.relative_to(ROOT)}`"]

    actual_files = {path.name for path in target_dir.glob("*.md")}
    for missing in sorted(expected_files - actual_files):
        findings.append(f"- missing generated article `{target_dir.relative_to(ROOT) / missing}`")
    for unexpected in sorted(actual_files - expected_files):
        findings.append(f"- unexpected file in target tree `{target_dir.relative_to(ROOT) / unexpected}`")

    for article in article_map["articles"]:
        path = target_dir / article["dest_filename"]
        if not path.exists():
            continue
        first_line = path.read_text().splitlines()[0]
        expected_heading = heading_for(article["new_number"], article["new_title"])
        if first_line != expected_heading:
            findings.append(
                f"- {path.relative_to(ROOT)}: heading `{first_line}` does not match expected `{expected_heading}`"
            )

    findings.extend(audit_old_references(target_dir, article_map))
    return findings


def write_report(report_path: Path, article_map: dict, target_dir: Path, findings: list[str], mode: str) -> None:
    lines = [
        "# Article Reorder Audit",
        "",
        f"- Mode: {mode}",
        f"- Target directory: `{target_dir.relative_to(ROOT)}`",
        "",
        "## Planned Articles",
        "",
    ]
    for article in article_map["articles"]:
        src = article["source_path"]
        dest = target_dir / article["dest_filename"]
        lines.append(f"- `{src}` -> `{dest.relative_to(ROOT)}`")
    lines.extend(["", "## Stale Link References", ""])
    if findings:
        lines.extend(findings)
        lines.extend(["", "Manual review is required for the references listed above."])
    else:
        lines.append("- None found in generated article files.")
    report_path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a reordered article tree from the article order map.")
    parser.add_argument("--map", dest="map_path", default="design-notes/article-order-map.json")
    parser.add_argument("--apply", action="store_true", help="Write the reordered files to the target directory.")
    parser.add_argument("--check", action="store_true", help="Validate the existing target directory without rewriting it.")
    args = parser.parse_args()

    if args.apply and args.check:
        parser.error("--apply and --check cannot be used together")

    map_path = ROOT / args.map_path
    article_map = load_map(map_path)
    target_dir = ROOT / article_map["target_directory"]
    report_path = ROOT / article_map["report_path"]
    article_pattern, article_number_map, filename_map, target_to_number = build_replacements(article_map)

    if args.check:
        findings = audit_target_tree(target_dir, article_map)
        write_report(report_path, article_map, target_dir, findings, "check")
        print(f"Wrote audit report to {report_path.relative_to(ROOT)}")
        if findings:
            print(f"Found {len(findings)} target-tree issues.")
            return 1
        print("Target tree passes reorder checks.")
        return 0

    generated: dict[str, str] = {}
    for article in article_map["articles"]:
        source_path = ROOT / article["source_path"]
        source_text = source_path.read_text()
        generated[article["dest_filename"]] = rewrite_content(
            source_text,
            article,
            article_pattern,
            article_number_map,
            filename_map,
            target_to_number,
        )

    if args.apply:
        if target_dir.exists():
            shutil.rmtree(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in generated.items():
            (target_dir / filename).write_text(content)
        findings = audit_old_references(target_dir, article_map)
        mode = "apply"
    else:
        temp_dir = ROOT / ".tmp-articles-next-audit"
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        temp_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in generated.items():
            (temp_dir / filename).write_text(content)
        findings = audit_old_references(temp_dir, article_map)
        shutil.rmtree(temp_dir)
        mode = "dry-run"

    write_report(report_path, article_map, target_dir, findings, mode)
    print(f"Wrote audit report to {report_path.relative_to(ROOT)}")
    if args.apply:
        print(f"Wrote reordered articles to {target_dir.relative_to(ROOT)}")
    else:
        print("Dry run complete. No article files were written.")
    if findings:
        print(f"Found {len(findings)} stale link references in generated article files.")
    else:
        print("No stale link references found in generated article files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
