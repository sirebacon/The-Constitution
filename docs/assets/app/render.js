import { refs } from "./dom.js";
import { parseMarkdown } from "./markdown.js";
import { docMatchesFilter, matchingDocs } from "./search.js";

function bySlug(siteData, slug) {
  return siteData.docs.find((doc) => doc.slug === slug);
}

function sourceUrl(doc) {
  return `./content/${doc.source}`;
}

function scorePill(doc) {
  if (!doc.score) return "";
  return `<span class="pill"><strong>${doc.score}</strong> ${doc.score_status ?? ""}</span>`;
}

function metaPills(doc, strings) {
  const pills = [];
  if (doc.kind === "article" || doc.kind === "preamble") {
    pills.push(
      `<span class="pill"><strong>${doc.kind === "article" ? strings.articleLabel : strings.textLabel}</strong> ${
        doc.kind === "article" ? strings.constitutionLabel : strings.preambleLabel
      }</span>`
    );
  } else {
    pills.push(`<span class="pill"><strong>${strings.documentLabel}</strong> ${doc.group}</span>`);
  }
  if (doc.status) {
    pills.push(`<span class="pill"><strong>${strings.statusLabel}</strong> ${doc.status}</span>`);
  }
  if (doc.score) {
    pills.push(scorePill(doc));
  }
  return pills.join("");
}

function makeDocCards(docs, strings) {
  return docs
    .map(
      (doc) => `
        <article class="doc-card">
          <div class="card-kicker">${doc.kind === "article" ? strings.articleLabel : doc.group}</div>
          <h3>${doc.title}</h3>
          <p>${doc.summary}</p>
          <div class="reader-meta">${doc.score ? scorePill(doc) : ""}${doc.status ? `<span class="pill"><strong>${strings.statusLabel}</strong> ${doc.status}</span>` : ""}</div>
          <a class="card-link" href="#doc/${doc.slug}" aria-label="${strings.openDocument}: ${doc.title}">${strings.openDocument}</a>
        </article>
      `
    )
    .join("");
}

export function renderNavigation({ siteData, currentFilter, strings }) {
  const filter = currentFilter.trim().toLowerCase();
  refs.navGroups.innerHTML = siteData.navigation
    .map((group) => {
      const items = group.items
        .map((slug) => bySlug(siteData, slug))
        .filter(Boolean)
        .filter((doc) => docMatchesFilter(doc, filter));
      if (!items.length) return "";
      return `
        <section class="nav-group">
          <h2 class="nav-group__title">${group.group}</h2>
          <div class="nav-list">
            ${items
              .map(
                (doc) => `
                  <a class="nav-link ${location.hash === `#doc/${doc.slug}` ? "is-active" : ""}" href="#doc/${doc.slug}" ${
                    location.hash === `#doc/${doc.slug}` ? 'aria-current="page"' : ""
                  }>
                    <span class="nav-link__title">${doc.title}</span>
                    <span class="nav-link__meta">${doc.score ? `Score ${doc.score}` : doc.group}</span>
                  </a>
                `
              )
              .join("")}
          </div>
        </section>
      `;
    })
    .join("");
}

export function renderHome({ siteData, currentFilter, strings }) {
  const constitutionDocs = siteData.docs.filter((doc) => doc.group === "Constitution");
  const overviewDocs = ["overview", "comparison", "scorecard", "finalization-plan"].map((slug) => bySlug(siteData, slug)).filter(Boolean);
  const stats = siteData.overview;
  const results = matchingDocs(siteData.docs, currentFilter.trim().toLowerCase());
  const searchSection = currentFilter.trim()
    ? `
    <section aria-labelledby="search-results-title">
      <h2 class="section-title" id="search-results-title">${strings.searchResults}</h2>
      ${
        results.length
          ? `<div class="card-grid">${makeDocCards(results.slice(0, 12), strings)}</div>`
          : `<div class="empty-message">${strings.noSearchResults(currentFilter)}</div>`
      }
    </section>
  `
    : "";

  refs.heroPanel.innerHTML = `
    <section class="hero">
      <div class="eyebrow">${strings.publicDraftSite}</div>
      <h1>${stats.title}</h1>
      <p>${stats.subtitle}</p>
      <div class="hero-actions">
        <a class="hero-action hero-action--primary" href="#doc/preamble">${strings.startWithPreamble}</a>
        <a class="hero-action" href="#doc/overview">${strings.readOverview}</a>
        <a class="hero-action" href="#doc/scorecard">${strings.seeScorecard}</a>
      </div>
    </section>

    <div class="stats-grid">
      <article class="stat-card">
        <span class="stat-card__label">${strings.articles}</span>
        <span class="stat-card__value">${stats.article_count}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">${strings.simulationScenarios}</span>
        <span class="stat-card__value">${stats.scenario_count}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">${strings.overallScore}</span>
        <span class="stat-card__value">${stats.overall_score ?? "—"}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">${strings.unresolvedObligations}</span>
        <span class="stat-card__value">${stats.unresolved_obligations}</span>
      </article>
    </div>
  `;

  refs.contentPanel.innerHTML = `
    ${searchSection}
    <section aria-labelledby="start-here-title">
      <h2 class="section-title" id="start-here-title">${strings.startHere}</h2>
      <div class="card-grid">${makeDocCards(overviewDocs, strings)}</div>
    </section>
    <section aria-labelledby="constitution-title">
      <h2 class="section-title" id="constitution-title">${strings.readConstitution}</h2>
      <div class="card-grid">${makeDocCards(constitutionDocs, strings)}</div>
    </section>
  `;

  refs.tocContent.innerHTML = `
    <a class="toc-link" href="#doc/overview">Overview</a>
    <a class="toc-link" href="#doc/preamble">Preamble</a>
    <a class="toc-link" href="#doc/scorecard">Scorecard</a>
  `;
  refs.tocContent.setAttribute("aria-label", strings.homeTocLabel);
}

export async function renderDoc({ siteData, slug, strings }) {
  const doc = bySlug(siteData, slug);
  if (!doc) {
    renderHome({ siteData, currentFilter: "", strings });
    return;
  }

  const markdown = await fetch(sourceUrl(doc)).then((response) => response.text());
  const rendered = parseMarkdown(markdown);

  refs.heroPanel.innerHTML = "";
  refs.contentPanel.innerHTML = `
    <section class="reader-shell">
      <header class="reader-header">
        <div class="eyebrow">${doc.group}</div>
        <h1>${doc.title}</h1>
        <div class="reader-summary">${doc.summary}</div>
        <div class="reader-meta">${metaPills(doc, strings)}</div>
        <a class="source-link" href="${sourceUrl(doc)}" target="_blank" rel="noreferrer">${strings.openSourceMarkdown}</a>
      </header>
      <article class="reader-body">
        <div class="markdown-body" id="markdownBody">${rendered}</div>
      </article>
    </section>
  `;

  renderToc(doc, strings);
}

export function renderToc(doc, strings) {
  if (!doc.headings?.length) {
    refs.tocContent.innerHTML = `<div class="empty-message">${strings.noSectionMap}</div>`;
    return;
  }
  refs.tocContent.setAttribute("aria-label", strings.onThisPageLabel);
  refs.tocContent.innerHTML = doc.headings
    .map(
      (heading) => `
        <a class="toc-link level-${heading.level}" href="#doc/${doc.slug}/${heading.anchor}">
          ${heading.text}
        </a>
      `
    )
    .join("");
}

export function applyAnchorFromHash() {
  const [, route, , anchor] = location.hash.match(/^#([^/]+)?\/?([^/]+)?\/?(.*)?$/) || [];
  if (route !== "doc" || !anchor) return;
  const target = document.getElementById(anchor);
  if (target) {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "start" });
  }
}
