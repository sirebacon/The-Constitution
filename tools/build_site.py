from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
CONTENT_DIR = DOCS_DIR / "content"
ASSETS_DIR = DOCS_DIR / "assets"


PAGE_SOURCES = [
    ("index", "Constitution Index", ROOT / "CONSTITUTION.md", "Overview", "Master index and drafting status"),
    ("overview", "Project Overview", ROOT / "design-notes" / "constitutional-overview.md", "Overview", "High-level explanation of the constitutional model"),
    ("overview-zh", "Project Overview (中文)", ROOT / "design-notes" / "constitutional-overview.zh.md", "Overview", "Chinese-language overview of the constitutional model"),
    ("comparison", "Comparison", ROOT / "design-notes" / "comparison.md", "Overview", "Comparison with the current U.S. Constitution"),
    ("rationale", "Design Rationale", ROOT / "design-notes" / "rationale.md", "Overview", "Why the major structural choices were made"),
    ("scorecard", "Scorecard", ROOT / "design-notes" / "scorecard.md", "Overview", "Current quality assessment and next targets"),
    ("findings", "Simulation Findings", ROOT / "design-notes" / "simulation-findings.md", "Research", "What the simulator is currently showing"),
    ("finalization-plan", "Finalization Plan", ROOT / "design-notes" / "finalization-plan.md", "Research", "Current remaining work and near-finalization sequence"),
]

COMMENTARY_OVERVIEW_SOURCES = [
    ("commentary-overview", "Using Commentary Notes", ROOT / "commentary" / "overview" / "using-commentary-notes.md", "Commentary", "How the website separates constitutional text from explanatory notes"),
    ("commentary-choices", "Why Keep Commentary Separate?", ROOT / "commentary" / "overview" / "why-commentary-is-separate.md", "Commentary", "Why the constitutional text stays clean while design notes stay public"),
]

CLAUSE_COMMENTARY_SOURCES = [
    (
        "clause-unamendable-core",
        "Clause Note: The Unamendable Core",
        ROOT / "commentary" / "clauses" / "unamendable-core.md",
        "Clause Notes",
        "Why some democratic foundations are intentionally placed beyond amendment",
        ["xi-amendments"],
    ),
    (
        "clause-naturalized-president",
        "Clause Note: Naturalized Citizens And The Presidency",
        ROOT / "commentary" / "clauses" / "naturalized-president.md",
        "Clause Notes",
        "Why the draft rejects a natural-born-only presidency",
        ["iii-executive", "ix-citizenship-membership"],
    ),
    (
        "clause-high-impact-directives",
        "Clause Note: Fast-Track Review For High-Impact Directives",
        ROOT / "commentary" / "clauses" / "high-impact-directives.md",
        "Clause Notes",
        "Why major presidential directives receive a narrow fast-track path",
        ["iii-executive", "iv-judiciary"],
    ),
    (
        "clause-supreme-court-delay",
        "Clause Note: Supreme Court Delay Backstop",
        ROOT / "commentary" / "clauses" / "supreme-court-delay-backstop.md",
        "Clause Notes",
        "Why expedited constitutional cases cannot be frozen indefinitely by nondecision",
        ["iv-judiciary"],
    ),
    (
        "clause-term-limits",
        "Clause Note: Presidential Term Limits",
        ROOT / "commentary" / "clauses" / "presidential-term-limits.md",
        "Clause Notes",
        "Why presidential term limits remain part of this safer presidential design",
        ["iii-executive"],
    ),
    (
        "clause-constitutional-organs",
        "Clause Note: Why Constitutional Organs Exist",
        ROOT / "commentary" / "clauses" / "constitutional-organs.md",
        "Clause Notes",
        "Why some democratic functions are kept outside ordinary partisan control",
        ["xii-constitutional-organs", "xix-ratification-transition"],
    ),
    (
        "clause-healthcare-floor",
        "Clause Note: The Healthcare Floor",
        ROOT / "commentary" / "clauses" / "healthcare-floor.md",
        "Clause Notes",
        "Why the Constitution protects access to basic and emergency healthcare without fixing one program model",
        ["xviii-social-economic-rights"],
    ),
    (
        "clause-war-powers-backstop",
        "Clause Note: War Powers Backstops",
        ROOT / "commentary" / "clauses" / "war-powers-backstop.md",
        "Clause Notes",
        "Why unauthorized force triggers concrete constitutional consequences instead of open-ended drift",
        ["xvi-war-powers-national-security"],
    ),
    (
        "clause-political-speech-floor",
        "Clause Note: Political Speech And Democratic Dissent",
        ROOT / "commentary" / "clauses" / "political-speech-floor.md",
        "Clause Notes",
        "Why political expression receives especially strong protection in a democracy-defending constitution",
        ["v-rights", "vi-integrity"],
    ),
    (
        "clause-peaceful-transfer",
        "Clause Note: Peaceful Transfer Of Power",
        ROOT / "commentary" / "clauses" / "peaceful-transfer.md",
        "Clause Notes",
        "Why lawful transfer of power is protected as a constitutional core commitment rather than a political norm",
        ["vi-integrity", "xix-ratification-transition"],
    ),
    (
        "clause-campaign-finance-equality",
        "Clause Note: Campaign Finance And Political Equality",
        ROOT / "commentary" / "clauses" / "campaign-finance-equality.md",
        "Clause Notes",
        "Why constitutional democracy permits strong limits on political money without freezing one permanent regulatory model",
        ["vii-campaign-finance"],
    ),
]

SCORECARD_KEYS = {
    "preamble": "Preamble",
    "I-electoral-system.md": "Article I — Electoral System",
    "II-legislature.md": "Article II — Legislature",
    "III-executive.md": "Article III — Executive",
    "IV-judiciary.md": "Article IV — Judiciary",
    "V-rights.md": "Article V — Civil and Political Rights",
    "VI-integrity.md": "Article VI — Democratic Integrity",
    "VII-campaign-finance.md": "Article VII — Campaign Finance and Political Money",
    "VIII-government-ethics.md": "Article VIII — Government Ethics",
    "IX-citizenship-membership.md": "Article IX — Citizenship and National Membership",
    "X-federalism.md": "Article X — Federalism and the States",
    "XI-amendments.md": "Article XI — Amendments",
    "XII-constitutional-organs.md": "Article XII — Constitutional Organs",
    "XIII-federal-agencies.md": "Article XIII — Federal Agencies",
    "XIV-taxation-public-revenue.md": "Article XIV — Taxation and Public Revenue",
    "XV-budget-public-credit-appropriations.md": "Article XV — Budget, Public Credit, and Appropriations",
    "XVI-war-powers-national-security.md": "Article XVI — War Powers and National Security",
    "XVII-foreign-policy-national-security.md": "Article XVII — Foreign Policy and National Security",
    "XVIII-social-economic-rights.md": "Article XVIII — Social, Economic, and Affirmative Rights",
    "XIX-ratification-transition.md": "Article XIX — Ratification and Transition",
}


ARTICLE_ORDER = [
    "I-electoral-system.md",
    "II-legislature.md",
    "III-executive.md",
    "IV-judiciary.md",
    "V-rights.md",
    "VI-integrity.md",
    "VII-campaign-finance.md",
    "VIII-government-ethics.md",
    "IX-citizenship-membership.md",
    "X-federalism.md",
    "XI-amendments.md",
    "XII-constitutional-organs.md",
    "XIII-federal-agencies.md",
    "XIV-taxation-public-revenue.md",
    "XV-budget-public-credit-appropriations.md",
    "XVI-war-powers-national-security.md",
    "XVII-foreign-policy-national-security.md",
    "XVIII-social-economic-rights.md",
    "XIX-ratification-transition.md",
]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_status(markdown: str) -> str | None:
    match = re.search(r"\*\*Status:\*\*\s*`?\[\s*([A-Z]+)\s*\]`?", markdown)
    return match.group(1) if match else None


def extract_summary(markdown: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if line.strip() == "## Scope":
            collected: list[str] = []
            for follow in lines[index + 1 :]:
                if follow.startswith("## "):
                    break
                if not follow.strip() or follow.strip() == "---":
                    if collected:
                        break
                    continue
                collected.append(follow.strip())
            if collected:
                return " ".join(collected)
    paragraphs = [
        line.strip()
        for line in lines
        if line.strip()
        and not line.startswith("#")
        and line.strip() != "---"
        and not line.startswith("**Status:**")
        and not line.startswith(">")
    ]
    return paragraphs[0] if paragraphs else ""


def extract_headings(markdown: str) -> list[dict[str, str | int]]:
    headings: list[dict[str, str | int]] = []
    for line in markdown.splitlines():
        if line.startswith("## "):
            text = line[3:].strip()
            headings.append({"level": 2, "text": text, "anchor": slugify(text)})
        elif line.startswith("### "):
            text = line[4:].strip()
            headings.append({"level": 3, "text": text, "anchor": slugify(text)})
    return headings


def plain_text(markdown: str) -> str:
    text = markdown
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_>#-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def copy_source(source: Path) -> str:
    relative = source.relative_to(ROOT)
    target = CONTENT_DIR / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    return relative.as_posix()


def parse_scorecard_rows(markdown: str) -> dict[str, dict[str, str]]:
    lines = markdown.splitlines()
    in_summary = False
    rows: dict[str, dict[str, str]] = {}
    for line in lines:
        if line.strip() == "### Summary Baseline":
            in_summary = True
            continue
        if in_summary and line.startswith("### "):
            break
        if not in_summary or not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|")[1:-1]]
        if len(parts) != 6 or parts[0] == "Area" or parts[0].startswith("------"):
            continue
        rows[parts[0]] = {
            "score": parts[1],
            "status": parts[2],
            "strength": parts[3],
            "weakness": parts[4],
            "next": parts[5],
        }
    return rows


def build_manifest() -> dict[str, object]:
    scorecard_md = (ROOT / "design-notes" / "scorecard.md").read_text()
    scorecard = parse_scorecard_rows(scorecard_md)
    aggregate = json.loads((ROOT / "simulation" / "reports" / "aggregate.json").read_text())

    docs: list[dict[str, object]] = []

    preamble_path = ROOT / "preamble.md"
    preamble_md = preamble_path.read_text()
    preamble_rel = copy_source(preamble_path)
    preamble_score = scorecard.get(SCORECARD_KEYS["preamble"], {})
    docs.append(
        {
            "slug": "preamble",
            "title": extract_title(preamble_md, "Preamble"),
            "group": "Constitution",
            "kind": "preamble",
            "source": preamble_rel,
            "status": extract_status(preamble_md),
            "summary": extract_summary(preamble_md),
            "headings": extract_headings(preamble_md),
            "search_text": plain_text(preamble_md),
            "score": preamble_score.get("score"),
            "score_status": preamble_score.get("status"),
        }
    )

    for filename in ARTICLE_ORDER:
        source = ROOT / "articles" / filename
        markdown = source.read_text()
        relative = copy_source(source)
        title = extract_title(markdown, filename)
        score = scorecard.get(SCORECARD_KEYS[filename], {})
        docs.append(
            {
                "slug": slugify(filename.replace(".md", "")),
                "title": title,
                "group": "Constitution",
                "kind": "article",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown),
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "score": score.get("score"),
                "score_status": score.get("status"),
            }
        )

    for slug, title, source, group, fallback_summary in PAGE_SOURCES:
        markdown = source.read_text()
        relative = copy_source(source)
        score = scorecard.get(title, {})
        docs.append(
            {
                "slug": slug,
                "title": title,
                "group": group,
                "kind": "note",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "score": score.get("score"),
                "score_status": score.get("status"),
            }
        )

    for slug, title, source, group, fallback_summary in COMMENTARY_OVERVIEW_SOURCES:
        markdown = source.read_text()
        relative = copy_source(source)
        docs.append(
            {
                "slug": slug,
                "title": title,
                "group": group,
                "kind": "commentary",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
            }
        )

    for slug, title, source, group, fallback_summary, related_slugs in CLAUSE_COMMENTARY_SOURCES:
        markdown = source.read_text()
        relative = copy_source(source)
        docs.append(
            {
                "slug": slug,
                "title": title,
                "group": group,
                "kind": "commentary",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown) or fallback_summary,
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "related_slugs": related_slugs,
            }
        )

    for filename in ARTICLE_ORDER:
        source = ROOT / "commentary" / "articles" / filename
        if not source.exists():
            continue
        markdown = source.read_text()
        relative = copy_source(source)
        article_slug = slugify(filename.replace(".md", ""))
        commentary_slug = f"notes-{article_slug}"
        article_title = extract_title((ROOT / "articles" / filename).read_text(), filename)
        docs.append(
            {
                "slug": commentary_slug,
                "title": f"{article_title} Notes",
                "group": "Commentary",
                "kind": "commentary",
                "source": relative,
                "status": extract_status(markdown),
                "summary": extract_summary(markdown) or f"Explanatory notes for {article_title}",
                "headings": extract_headings(markdown),
                "search_text": plain_text(markdown),
                "companion_slug": article_slug,
                "companion_kind": "article",
            }
        )

    commentary_by_article = {
        doc["companion_slug"]: doc["slug"]
        for doc in docs
        if doc.get("kind") == "commentary" and doc.get("companion_slug")
    }
    for doc in docs:
        if doc["kind"] in {"article", "preamble"} and doc["slug"] in commentary_by_article:
            doc["companion_slug"] = commentary_by_article[doc["slug"]]
            doc["companion_kind"] = "commentary"

    overview = {
        "title": "Constitution of the United States of America",
        "subtitle": "A modern replacement draft built around democratic legitimacy, anti-authoritarian safeguards, and readable constitutional architecture.",
        "article_count": len(ARTICLE_ORDER),
        "scenario_count": aggregate["scenario_count"],
        "overall_score": scorecard.get("Overall Draft", {}).get("score"),
        "overall_status": scorecard.get("Overall Draft", {}).get("status"),
        "unresolved_obligations": aggregate["totals"]["unresolved_obligations"],
        "top_strength": scorecard.get("Overall Draft", {}).get("strength"),
        "top_weakness": scorecard.get("Overall Draft", {}).get("weakness"),
    }

    navigation = [
        {"group": "Start Here", "items": ["overview", "index", "comparison", "scorecard"]},
        {"group": "Read the Constitution", "items": ["preamble"] + [slugify(filename.replace(".md", "")) for filename in ARTICLE_ORDER]},
        {"group": "Commentary", "items": ["commentary-overview", "commentary-choices"]},
        {
            "group": "Key Clauses",
            "items": [
                "clause-unamendable-core",
                "clause-naturalized-president",
                "clause-high-impact-directives",
                "clause-supreme-court-delay",
                "clause-term-limits",
                "clause-constitutional-organs",
                "clause-healthcare-floor",
                "clause-war-powers-backstop",
                "clause-political-speech-floor",
                "clause-peaceful-transfer",
                "clause-campaign-finance-equality",
            ],
        },
        {"group": "Background", "items": ["rationale", "findings", "finalization-plan", "overview-zh"]},
    ]

    return {
        "generated_at": aggregate.get("generated_at", ""),
        "locale": "en",
        "overview": overview,
        "navigation": navigation,
        "docs": docs,
    }


def write_manifest(manifest: dict[str, object]) -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    (ASSETS_DIR / "site-data.json").write_text(json.dumps(manifest, indent=2))


def main() -> None:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    if CONTENT_DIR.exists():
        for child in CONTENT_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    manifest = build_manifest()
    write_manifest(manifest)


if __name__ == "__main__":
    main()
