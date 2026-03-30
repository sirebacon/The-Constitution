# Constitutional Visualization Plan

The goal is to make the constitution legible to people who will never read a long legal document, while keeping the visual layer maintainable inside the site that already exists.

This plan replaces the idea of a separate visualization mini-site with a visualization layer integrated into the current GitHub Pages reader.

---

## Core Decision

Visualizations should live inside the existing `docs/` site, not in a separate `visualization/` directory with standalone HTML pages.

Why:

- the current site already has navigation, translation support, mobile behavior, and published content generation
- the project already has a `build_site.py` pipeline that can publish new document types
- a second site would duplicate layout, translation, styling, and maintenance work
- visual explainers should feel like part of the constitution reader, not a side project

So the right model is:

- add a new site content layer for visual guides
- generate those guides through the existing build pipeline
- use the same locale switching and fallback logic as the rest of the site

---

## Design Principles

- **Visual first.** The diagram should answer the question before the user reads a long paragraph.
- **Integrated, not separate.** Use the current site shell, not a second website.
- **SVG first.** Prefer inline SVG and light interaction over heavy graph engines.
- **Mobile readable.** Every visualization must still work on a phone.
- **Translated labels.** Visual text should flow through the existing locale system where practical.
- **Progressive disclosure.** Start with a simple diagram, then allow details, references, and section links.
- **Static delivery.** No backend, no runtime data fetches beyond the site manifest and local assets.

---

## Built

These are complete and live on the site.

### 1. Rights At A Glance — DONE
Question: `What rights does this constitution protect?`

Card grid, filterable by category: political rights, civil liberties, due process, equality, digital rights, social and economic rights, non-derogable rights. English, Spanish, and Chinese.

### 2. Emergency Powers Lifecycle — DONE
Question: `What happens when an emergency is declared?`

Step-by-step flow with three paths: ordinary, lapse, and abuse. Filterable by path. English, Spanish, and Chinese.

### 3. How Power Is Distributed — DONE
Question: `Who can do what, and who checks whom?`

Card grid showing all seven constitutional actors and their power links, filterable by type: electoral, checks, accountability.

### 4. Congress: Then vs. Now — DONE
Question: `How is the legislature different from the current U.S. Congress?`

Comparison table, filterable by category: composition, terms and elections, exclusive powers, procedural rules.

---

## Built In Phase 2

These are now complete and live on the site.

### 5. How Officials Are Removed — DONE
Question: `What happens when someone abuses power?`

Comparison-table guide covering President, Congress members, federal judges, and Constitutional Organs.

### 6. How Elections Work — DONE
Question: `What is different about voting here?`

Card-grid guide covering voting methods, access and registration, integrity protections, and recall.

### 7. The Amendment Process — DONE
Question: `How hard is it to change this constitution?`

Track 1 vs. Track 2 comparison plus pre-clearance and unamendable-core treatment.

### 8. What The Accountability Commission Does — DONE
Question: `What is this new institution and who controls it?`

Card-grid explainer covering composition, powers, limits, and anti-capture protections.

---

## What To Build Next

These are now the highest-value remaining guides for general readers.

### 9. Presidential Powers: Then vs. Now
Question: `What can the President actually do — and what can’t they?`

Format: comparison table, same pattern as congress-comparison. Covers veto, appointments, emergency declarations, pardons, military command, executive orders, firing agency heads.

Why next:

- likely the most shareable high-level comparison after Congress
- answers the most common reader question about presidentialism
- helps clarify that the draft is constrained presidentialism, not executive supremacy

### 10. How A Bill Becomes Law
Question: `What is the legislative path?`

Format: step-by-step flow filterable by path: ordinary, vetoed, deadlocked. Covers the no-filibuster default and the 60-day deadlock resolution mechanism.

Why next:

- explains one of the most important practical differences from the current U.S. system
- ties together Articles I, II, and III in a way readers can follow quickly

### 11. From Election To Transfer Of Power
Question: `What happens from voting day to a lawful transition?`

Format: timeline flow from vote casting to certification, dispute resolution, oath, continuity, and transfer safeguards.

Why next:

- directly ties together election administration, anti-subversion, courts, and transition rules
- highly relevant to ordinary readers who want to know how the system survives pressure

### 12. How Rights Are Enforced
Question: `What happens if the government violates a right?`

Format: process guide showing standing, courts, expedited review, non-derogable rights, and enforcement backstops.

Why next:

- complements `Rights At A Glance` with enforcement rather than enumeration
- helps readers understand that the rights section is judicially meaningful, not aspirational only

### 13. Federalism And The Democratic Floor
Question: `What can states still do, and what can they no longer do?`

Format: comparison table or card grid showing protected state authority versus non-negotiable democratic baselines.

Why next:

- clarifies one of the easiest parts of the draft to misunderstand
- would help answer likely criticisms from both centralizers and federalism absolutists

---

## What To Build Later

These are good ideas but depend on the core explainer layer being stable first.

### 14. Scenario Explorer
Question: `What happens when something goes wrong?`

Best built from simulator outputs once a clean generation format exists. Group-level overview pages first, individual scenario drilldown later.

### 15. Article Structure Map
Question: `How do the articles connect to each other?`

Most useful to advanced readers. Requires cross-reference parsing. Network or matrix view, article click highlights local neighborhood.

### 16. Comparative Matrix
Question: `How does this compare to other constitutions?`

Hand-curated table comparing key features against current U.S., Germany, Canada, and South Africa. Requires careful source discipline to avoid going stale.

---

## What Not To Build First

### Do Not Start With A Force-Directed Network

The original checks-and-balances graph is visually attractive but not the best first explainer.

Problems:

- it is harder for ordinary readers to parse
- it creates visual noise
- it is harder to translate cleanly
- it is harder to keep accessible on mobile
- it can feel impressive without being especially informative

A curated system map is better for phase 1.

### Do Not Split Into A Separate Visualization Website

That would create:

- duplicated layout code
- duplicated translation work
- duplicated navigation logic
- duplicated accessibility work

The project already has the site shell it needs.

### Do Not Reach For D3 Or Cytoscape By Default

Use them only when the visualization genuinely needs them.

Most first-wave visualizations can be built with:

- inline SVG
- semantic HTML
- a little vanilla JS

That is easier to maintain and easier to translate.

---

## Recommended Technical Model

### Site Integration

Add a new document group to the current site, for example:

- `Visual Guides`

Publish each guide through `tools/build_site.py` the same way overview and commentary pages are published now.

Possible source layout:

```text
visual-guides/
  rights-at-a-glance.md
  emergency-powers-lifecycle.md
  power-distribution.md
  amendment-process.md
  removal-pathways.md
  legislative-path.md
```

Each guide can include:

- an intro block
- a diagram container
- linked article references
- related commentary links

### Rendering Model

Use `render.js` to detect visual-guide documents and render:

- markdown explanation
- inline SVG block
- optional legend
- optional toggle buttons

If a guide needs structured data, add that data to the site manifest in `build_site.py`.

### Translation Model

Visual guides should follow the same locale structure already used elsewhere.

For example:

```text
translation/translations/es/visual-guides/
translation/translations/zh-Hans/visual-guides/
```

Label text should come from:

- translated guide markdown when possible
- existing UI string tables for shared controls

Avoid baking English labels directly into SVG assets unless they are purely decorative.

### Accessibility Model

Every visualization should include:

- a plain-language title
- a short explanatory summary
- visible text labels, not color alone
- an accessible fallback description in HTML
- mobile-safe scaling

If a diagram is interactive, keyboard access and focus treatment must be part of the initial implementation, not an afterthought.

---

## Directory Plan

Recommended structure:

```text
visual-guides/
  rights-at-a-glance.md
  emergency-powers-lifecycle.md
  power-distribution.md
  amendment-process.md
  removal-pathways.md
  legislative-path.md

docs/assets/app/
  visual-guides.js        ← renderer helpers for diagrams

tools/
  build_site.py           ← extended to publish visual guides
```

Optional later:

```text
tools/
  build_visual_guide_data.py
```

Only add separate data-build scripts when a guide genuinely needs generated data.

---

## Implementation Order

### Phase 1 — DONE

Built: Rights At A Glance, Emergency Powers Lifecycle, How Power Is Distributed, Congress: Then vs. Now.

The site has a Visual Guides nav group, four published guides, mobile-safe inline visuals, and English/Spanish/Chinese locale support.

### Phase 2 — Next

Build in order:

1. `How Officials Are Removed` — most topical, same format as congress-comparison
2. `How Elections Work` — most unfamiliar content, high public interest
3. `The Amendment Process` — most distinctive design feature, unamendable core
4. `What The Accountability Commission Does` — fills largest knowledge gap

Milestone: the site can explain all of the constitution’s major structural innovations without requiring article-by-article reading.

### Phase 3 — Process Depth

Build:

1. `Presidential Powers: Then vs. Now`
2. `How A Bill Becomes Law`

### Phase 4 — Generated Advanced Views

Build:

1. scenario explorer (from simulation JSON)
2. article structure map (from cross-reference parsing)

### Phase 5 — Comparative Layer

Build:

1. comparative matrix vs. current U.S., Germany, Canada, South Africa
