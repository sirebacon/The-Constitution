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

## What To Build First

Phase 1 should prioritize visualizations that help general readers understand the system quickly and do not require complex graph logic.

### 1. Rights At A Glance
Question:
`What rights does this constitution protect?`

Why first:

- it is immediately useful to ordinary readers
- it can be built with a card grid plus simple filtering
- it translates cleanly
- it does not depend on difficult layout logic

Format:

- visual guide page inside the current site
- HTML/CSS card grid with lightweight filtering
- each card links back to the relevant article or clause note

Categories:

- political rights
- civil liberties
- due process
- equality
- digital rights
- social and economic rights
- non-derogable rights

### 2. Emergency Powers Lifecycle
Question:
`What happens when an emergency is declared?`

Why second:

- it explains one of the most important design choices
- it is more legible as a guided flow than as article text
- it helps readers compare this draft to the current U.S. system

Format:

- static or lightly interactive SVG flow diagram
- optional step toggles for:
  - ordinary path
  - rejection path
  - lapse path
  - abuse path

Important note:

Before implementation, the constitutional references in the diagram must be checked against the current articles. The visual must track the actual final article locations, not older drafting references.

### 3. How Power Is Distributed
Question:
`Who can do what, and who checks whom?`

Why third:

- readers need a structural mental model
- a curated diagram is clearer than a force-directed network
- this can explain the role of the House, Regional Assembly, President, Courts, Electoral Commission, and Accountability Commission

Format:

- structured SVG system map
- boxes for institutions
- labeled arrows for major powers and checks
- click or tap reveals linked article references

This should replace the proposed force-directed graph as the first institutional visualization.

---

## What To Build Second

These visuals answer deeper process questions once the top-level orientation layer exists.

### 4. Amendment Process
Question:
`How hard is it to change this constitution?`

Format:

- two-column infographic
- Track 1 and Track 2 side by side
- locked unamendable core panel below
- optional comparison callout to current U.S. Article V

Why this belongs early:

- it explains one of the project’s most distinctive features
- it is easy to read visually
- it pairs well with existing commentary on the unamendable core

### 5. Removal Pathways
Question:
`How do you remove an official who has gone wrong?`

Format:

- swimlane diagram
- separate lanes for President, judges, commission members, and legislators where relevant

Why second-tier:

- very useful, but more complex than the first three
- more likely to drift out of date if article text changes

### 6. Legislative Path
Question:
`How does a bill become law here?`

Format:

- sequence diagram
- ordinary path, veto path, and special budget path

Why second-tier:

- important, but less attention-grabbing than rights and emergency powers
- needs careful treatment of exceptions

---

## What To Build Later

These are good ideas, but they should come after the basic explainer layer is stable.

### 7. Scenario Explorer
Question:
`What happens when something goes wrong?`

Why later:

- high value, but more work
- best built from the simulator outputs once a clean generation format exists

Best shape:

- group-level overview pages first
- individual scenario drilldown later
- generated from simulation JSON/report data rather than hand-authored HTML

### 8. Article Structure Map
Question:
`How do the articles connect to each other?`

Why later:

- most useful to advanced readers
- cross-reference parsing needs care to avoid misleading graphs

Best shape:

- generated adjacency data
- simple network or matrix view
- article click highlights local neighborhood

### 9. Comparative Matrix
Question:
`How does this compare to other constitutions?`

Why later:

- valuable, but requires careful source discipline and maintenance
- easier to get wrong or stale than the internal explainers

Best shape:

- clean table or card matrix
- hand-curated, not automatically inferred

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

### Phase 1 — Site-Integrated First Wave

Build:

1. `Rights At A Glance`
2. `Emergency Powers Lifecycle`
3. `How Power Is Distributed`

Deliverables:

- new `Visual Guides` nav group
- three published visual guide pages
- mobile-safe inline visuals
- English first, locale-ready structure

Milestone:

The site has a real visual explainer layer that helps first-time readers understand the system quickly.

### Phase 2 — Process Explainers

Build:

1. `Amendment Process`
2. `Removal Pathways`
3. `Legislative Path`

Milestone:

The site can explain the constitution’s main process architecture without requiring article-by-article reading.

### Phase 3 — Generated Advanced Views

Build:

1. scenario explorer
2. article structure map

Milestone:

Advanced readers can inspect simulation and structural relationships visually.

### Phase 4 — Comparative Layer

Build:

1. comparative matrix

Milestone:

The site can position this draft against current and foreign constitutional models in a disciplined way.

---

## Immediate Next Step

The best first implementation target is:

1. add a `Visual Guides` section to the existing site
2. build `Rights At A Glance`
3. use that page to establish the rendering pattern for all later visualizations

That is the highest-value, lowest-risk way to start.
