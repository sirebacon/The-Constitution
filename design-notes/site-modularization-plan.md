# Site Modularization Plan

The website already has a good base: a static GitHub Pages deployment, a generator, locale support, commentary support, and a modularized app shell. The next step is not a rebuild. The next step is to make the content and rendering model more modular so the site can keep growing without turning into a single expanding set of special cases.

This plan is about targeted modularization, not framework migration.

---

## Goal

Make the site easier to maintain, extend, translate, and explain by turning its major content layers into clear first-class modules.

That means:

- clearer document types
- cleaner site metadata
- reusable rendering patterns
- more predictable navigation
- easier future addition of visual guides and translated explainers

The goal is not:

- React
- a new frontend stack
- a second site
- a complex build system

---

## Current Strengths

The site already has several good foundations:

- static deployment through GitHub Pages
- `tools/build_site.py` as a central publisher
- locale-aware manifests
- separate constitutional text and commentary
- modular app files under `docs/assets/app/`
- mobile and accessibility improvements

This means the site is already partly modular.

The remaining issue is that content growth is starting to outpace the current metadata structure.

---

## Current Problems

### 1. Content Types Are Implicit More Than Formal

The site currently distinguishes documents mostly through combinations of:

- `kind`
- `group`
- hardcoded slug lists

That works, but it is getting harder to reason about as more layers appear.

Examples of current and emerging content types:

- constitution text
- preamble
- overview pages
- research/design notes
- commentary overviews
- article commentary
- clause commentary
- testing guides
- policy pages
- translated copies
- future visual guides

These should become more explicit in the site model.

### 2. `build_site.py` Is Becoming a Mixed Compiler and Content Registry

Right now, `build_site.py` does too much in one place:

- locale labels
- group labels
- page metadata
- document source lists
- commentary mappings
- navigation structure
- some relationship logic

That makes it powerful, but it will get harder to maintain as more guides and visualizations are added.

### 3. Rendering Logic Is Still Partly Slug-Driven

The app renderer still uses explicit slug arrays in places such as:

- homepage sections
- clause note groupings
- commentary groupings
- start-here cards

That is manageable now, but it will not scale cleanly as more modules appear.

### 4. New Content Layers Need Clear Homes

The next likely additions are:

- visual guides
- more shareable explainers
- more translated design-note pages

Without a clearer module model, these will become special-case additions rather than coherent site layers.

---

## Modularization Targets

### 1. Make Content Types First-Class

The site should formally model document families such as:

- `constitution`
- `overview`
- `research`
- `commentary_overview`
- `commentary_article`
- `commentary_clause`
- `guide`
- `policy`
- `visual_guide`

These do not all need different page templates immediately, but they should exist in the metadata model.

This gives the site:

- cleaner grouping
- cleaner navigation rules
- cleaner rendering decisions
- easier future analytics and visual layers

### 2. Separate Site Metadata From Publishing Logic

Move the growing registries out of `build_site.py` and into structured data files.

Recommended candidates:

- `site/page-meta.json`
- `site/navigation.json`
- `site/relationships.json`

Examples of what should move:

- titles and summaries
- per-locale labels where practical
- navigation grouping
- companion relationships
- related clause note relationships

`build_site.py` should primarily compile and publish, not remain the only source of content structure.

### 3. Make Homepage Sections Data-Driven

The homepage should stop depending on hardcoded slug arrays in the renderer.

Instead, the manifest should explicitly publish:

- featured docs
- start-here docs
- homepage modules
- key clause docs
- commentary overview docs

Then `render.js` can render those sections generically.

This matters because the homepage is now doing real editorial work, not just showing raw navigation.

### 4. Add a First-Class `Visual Guide` Module

Before building the first visualization, make `visual_guide` a recognized content type.

That should include:

- source directory
- nav grouping
- render path
- translation path
- homepage/entry-point behavior

This avoids bolting visual explainers onto generic design-note handling.

### 5. Add a First-Class `Guide` Module

Some pages are not just research notes. They are public explainers or contributor guides.

Examples:

- `How Testing Works`
- `How To Write Simulation Tests`
- future issue explainers

These should not remain lumped into generic overview/research behavior forever.

Making `guide` explicit would improve:

- homepage organization
- translation planning
- user expectations

---

## Recommended Information Architecture

The site should increasingly behave like a modular civic reader with stable entry points.

Recommended top-level modules:

- `Start Here`
- `Read the Constitution`
- `Commentary`
- `Key Clauses`
- `Guides`
- `Visual Guides`
- `Research`

That does not mean the nav must become huge. It means each new content piece should have a clear module home.

---

## Rendering Plan

Do not build a separate renderer per page.

Instead, support a small set of rendering modes:

- text document
- commentary document
- guide document
- visual guide document

Possible approach:

- keep the current markdown rendering base
- branch lightly by `content_type`
- allow guide pages to expose structured companion blocks
- allow visual guide pages to mount SVG/interactive blocks

This gives enough flexibility without fragmenting the app.

---

## Translation Plan

Modularization should directly support translation.

Each module should have a predictable translation path.

For example:

- `translation/translations/es/articles/...`
- `translation/translations/es/commentary/articles/...`
- `translation/translations/es/commentary/clauses/...`
- `translation/translations/es/design-notes/...`
- `translation/translations/es/visual-guides/...`

The more predictable the module structure is, the easier it is to:

- identify missing translations
- generate locale manifests
- keep language switching coherent

This is one of the strongest reasons to modularize further.

---

## Implementation Order

### Phase 1 — Metadata Cleanup

1. Add explicit `content_type` support in the manifest model
2. Move page metadata and navigation config out of `build_site.py`
3. Make homepage sections data-driven

Outcome:

- cleaner generator
- cleaner renderer
- easier addition of future modules

### Phase 2 — Guide Layer Cleanup

1. Formalize `guide` as a content type
2. Group testing and explainer pages accordingly
3. Update homepage and navigation to surface them intentionally

Outcome:

- contributor and public explainers stop feeling like miscellaneous notes

### Phase 3 — Visual Guide Foundation

1. Add `visual_guide` content type
2. Create source directory and manifest support
3. Add rendering support for inline SVG visual pages

Outcome:

- the site is ready for the first visualization without hacks

### Phase 4 — Relationship Cleanup

1. Move clause/article relationships into structured metadata
2. Move featured homepage document selections into data
3. Reduce hardcoded slug lists in `render.js`

Outcome:

- future content changes require less code editing

---

## What Not To Do

Do not:

- rewrite the site in React
- split the site into multiple apps
- add a heavy client-side routing framework
- introduce a CMS
- overengineer the build just to avoid a few lists

The problem is not the stack.
The problem is that the content model needs one more layer of structure.

---

## Best Immediate Next Step

The best first step is:

1. add explicit `content_type` fields to the generated manifest
2. make homepage sections derive from manifest data rather than hardcoded slugs

That gives the project the biggest modularization gain for the least disruption.
