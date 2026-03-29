# Translation Plan — Living Constitutional Document

---

## Approach

The English source is a living document. The translation system needs to stay in sync with it, not fight it.

The core insight: the entire constitution is small (19 articles, roughly 100k tokens). Re-translating one changed article takes seconds and costs cents. A complex segment-level memory system is not worth the maintenance burden for a document this size.

**The right approach:**
- Detect changed articles with `git diff`
- Re-translate entire changed articles using Claude with a glossary in the system prompt
- Output to `translation/translations/{lang}/articles/`
- Reviewers use `git diff` on the output files — the same workflow they use for the English source
- Git history is the version history

---

## Toolchain

**Primary engine:** Claude API (`claude-opus-4-6` for quality; `claude-sonnet-4-6` for faster drafts)

**Why not DeepL or Google Translate?**
DeepL is strong for European languages (es, fr, pt) and is worth evaluating for a comparison pass. However, Claude handles constitutional legal register well across all target languages and can be given explicit glossary and formatting instructions that generic MT services cannot enforce. For ratification-facing translations, use a professional translator who post-edits the Claude output regardless of which MT engine produced the first draft.

**Change detection:** `git diff --name-only HEAD` — no custom infrastructure needed.

**Glossary:** A JSON file per language (`translation/glossary/{lang}.json`) mapping English constitutional terms to their approved translations. Injected into the system prompt on every call. This is what ensures "Accountability Commission" always translates consistently within a language.

---

## Directory Structure

```
translation/
  translations/
    es/articles/*.md      ← output files committed to git
    zh-Hans/articles/*.md
    ...
  glossary/
    template.json         ← all terms with empty translation fields
    es.json               ← filled-in glossary for Spanish
    zh-Hans.json
    ...
  scripts/
    translate.py          ← the main script
  config.yaml
  README.md
```

---

## Workflow

### Normal (ongoing)

After any commit that changes an article:

```bash
python translation/scripts/translate.py
# detects changed articles via git diff, translates, writes output
git diff translation/translations/
# review, edit if needed, commit
```

### First run for a new language

1. Fill in `translation/glossary/{lang}.json` (copy from `template.json`; have a native speaker translate the ~40 key terms).
2. `python translation/scripts/translate.py --all --lang {lang}`
3. Review and commit.

### Before a public release

Have a native-speaking reviewer go through the output files directly. They edit the markdown, commit their corrections. No special tooling needed.

---

## Languages

| Priority | Codes | Notes |
|----------|-------|-------|
| 1 | `es`, `zh-Hans` | Largest US communities; start here |
| 2 | `vi`, `tl`, `ko` | Major diaspora communities |
| 3 | `ar`, `fr`, `pt` | International coverage |

---

## Quality Levels

| Level | What it means | Suitable for |
|-------|---------------|-------------|
| Machine draft | Raw Claude output | Internal review |
| Edited draft | Corrections committed to git | Pre-release distribution |
| Legal review | Native constitutional lawyer reviewed | Official/public release |
| Ratification | Certified professional translation | Referendum |

Priority-1 languages should reach legal review before any public distribution. Machine drafts are fine for internal use.

---

## Glossary Management

The glossary is the most important consistency tool. Before translating a new language:

1. A native legal speaker fills in `translation/glossary/{lang}.json`.
2. For each new constitutional term that appears in the source (e.g., a new organ name), add it to the glossary and re-run the affected articles.
3. If a reviewer corrects a term, update the glossary and re-run all articles for that language.

The ~40 terms in `template.json` cover the core constitutional vocabulary. A few hours of glossary work by a native speaker is the single highest-value investment before any translation begins.

---

## What This Approach Doesn't Do

- **No segment-level memory.** Not needed for a document this size. Re-translating a full article is cheap and produces better output than stitching together isolated provision translations.
- **No custom review UI.** Reviewers use git diff like everyone else.
- **No automated quality gating.** Quality is tracked by convention (edit the output → commit → the commit message is the review record), not by tooling.
- **No parallel translation memory across articles.** Glossary injection handles consistency. This is sufficient.

If this document grows significantly in scope (e.g., full statutory implementation code, many thousands of segments), a proper TMS (Weblate, Crowdin, Phrase) would be worth the setup cost. At current scope, it is not.
