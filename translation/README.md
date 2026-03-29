# Translation Pipeline

Translates the English constitutional articles into multiple languages using the Claude API. Translations live in `translation/translations/{lang}/articles/` and are tracked in git like any other file.

---

## Setup

```bash
pip install anthropic pyyaml
export ANTHROPIC_API_KEY=your-key-here
```

---

## Usage

```bash
# Translate articles changed since last commit (normal workflow)
python translation/scripts/translate.py

# First run, or full refresh of all articles
python translation/scripts/translate.py --all

# Specific language only
python translation/scripts/translate.py --lang es

# Specific article only
python translation/scripts/translate.py --article articles/III-executive.md

# See what would be translated without calling the API
python translation/scripts/translate.py --dry-run --all

# Use a faster/cheaper model for a first draft
python translation/scripts/translate.py --all --model claude-sonnet-4-6
```

After running, review the output with standard git tooling:

```bash
git diff translation/translations/
```

---

## Workflow

**When an article changes in English:**

1. Run `translate.py` (no flags needed — it detects changed files via `git diff`).
2. Review the diff: `git diff translation/translations/`.
3. If the translation looks wrong, edit the output file directly and commit — that is the review step.
4. Commit both the source change and the updated translations together, or in a follow-up commit.

**First run for a new language:**

1. Copy `translation/glossary/template.json` to `translation/glossary/{lang}.json`.
2. Fill in the translated terms for that language (the glossary is injected into every translation call to ensure consistency).
3. Run `python translation/scripts/translate.py --all --lang {lang}`.
4. Review and commit.

---

## Glossary

`translation/glossary/{lang}.json` maps English constitutional terms to their approved translations. These are injected into every Claude API call for that language, so terms like "Accountability Commission" always translate consistently.

- Copy `glossary/template.json` as a starting point.
- Fill in translations before running the pipeline for a new language.
- When you approve a new term, add it to the glossary and re-run the affected articles.
- The template includes all constitutional organs, key legal terms, and article names.

---

## Review Quality

| Level | What it means | Suitable for |
|-------|---------------|-------------|
| Machine draft | Raw Claude output | Internal review, cross-reference checking |
| Edited draft | Machine output with human corrections committed to git | Pre-release |
| Legal review | Native-speaking constitutional lawyer reviewed and approved | Official/public release |
| Ratification | Certified professional translation | Ratification referendum |

Mark the quality level in a `TRANSLATION_STATUS.md` file per language if needed.

---

## Output Structure

```
translation/
  translations/
    es/
      articles/
        I-electoral-system.md
        II-legislature.md
        ...
    zh-Hans/
      articles/
        ...
  glossary/
    template.json
    es.json       ← copy of template with Spanish terms filled in
    zh-Hans.json
    ...
  scripts/
    translate.py
  config.yaml
  README.md
```

---

## Notes

- The whole constitution is small enough that re-translating a single article costs cents and takes under a minute. Don't over-optimize.
- Git history is the version history. No separate translation memory store is needed.
- Reviewers work directly on the output markdown files. `git diff` shows what changed.
- For ratification-facing translations, use a professional translation agency and treat the Claude output as a first draft for the human translator to post-edit.
