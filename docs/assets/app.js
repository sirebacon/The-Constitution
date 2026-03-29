import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const DATA_URL = "./assets/site-data.json";

const heroPanel = document.getElementById("heroPanel");
const contentPanel = document.getElementById("contentPanel");
const tocContent = document.getElementById("tocContent");
const navGroups = document.getElementById("navGroups");
const searchInput = document.getElementById("searchInput");
const sidebar = document.getElementById("sidebar");
const menuButton = document.getElementById("menuButton");

let siteData;
let currentFilter = "";

function searchCorpus(doc) {
  return `${doc.title} ${doc.summary} ${doc.search_text ?? ""}`.toLowerCase();
}

function slugify(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

const renderer = new marked.Renderer();
renderer.heading = ({ tokens, depth }) => {
  const text = tokens.map((token) => token.raw ?? token.text ?? "").join("").trim();
  const anchor = slugify(text);
  return `<h${depth} id="${anchor}">${text}</h${depth}>`;
};

marked.setOptions({ renderer });

function bySlug(slug) {
  return siteData.docs.find((doc) => doc.slug === slug);
}

function sourceUrl(doc) {
  return `./content/${doc.source}`;
}

function scorePill(doc) {
  if (!doc.score) return "";
  return `<span class="pill"><strong>${doc.score}</strong> ${doc.score_status ?? ""}</span>`;
}

function metaPills(doc) {
  const pills = [];
  if (doc.kind === "article" || doc.kind === "preamble") {
    pills.push(`<span class="pill"><strong>${doc.kind === "article" ? "Article" : "Text"}</strong> ${doc.kind === "article" ? "Constitution" : "Preamble"}</span>`);
  } else {
    pills.push(`<span class="pill"><strong>Document</strong> ${doc.group}</span>`);
  }
  if (doc.status) {
    pills.push(`<span class="pill"><strong>Status</strong> ${doc.status}</span>`);
  }
  if (doc.score) {
    pills.push(scorePill(doc));
  }
  return pills.join("");
}

function renderNavigation() {
  const filter = currentFilter.trim().toLowerCase();
  navGroups.innerHTML = siteData.navigation
    .map((group) => {
      const items = group.items
        .map((slug) => bySlug(slug))
        .filter(Boolean)
        .filter((doc) => {
          if (!filter) return true;
          return searchCorpus(doc).includes(filter);
        });
      if (!items.length) return "";
      return `
        <section class="nav-group">
          <div class="nav-group__title">${group.group}</div>
          <div class="nav-list">
            ${items
              .map(
                (doc) => `
                  <a class="nav-link ${location.hash === `#doc/${doc.slug}` ? "is-active" : ""}" href="#doc/${doc.slug}">
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

function matchingDocs() {
  const filter = currentFilter.trim().toLowerCase();
  if (!filter) return [];
  return siteData.docs
    .filter((doc) => searchCorpus(doc).includes(filter))
    .sort((a, b) => {
      const aTitle = a.title.toLowerCase().includes(filter) ? 2 : 0;
      const bTitle = b.title.toLowerCase().includes(filter) ? 2 : 0;
      const aSummary = a.summary.toLowerCase().includes(filter) ? 1 : 0;
      const bSummary = b.summary.toLowerCase().includes(filter) ? 1 : 0;
      return bTitle + bSummary - (aTitle + aSummary);
    });
}

function makeArticleCards(docs) {
  return docs
    .map(
      (doc) => `
        <article class="doc-card">
          <div class="card-kicker">${doc.kind === "article" ? "Article" : doc.group}</div>
          <h3>${doc.title}</h3>
          <p>${doc.summary}</p>
          <div class="reader-meta">${doc.score ? scorePill(doc) : ""}${doc.status ? `<span class="pill"><strong>Status</strong> ${doc.status}</span>` : ""}</div>
          <a class="card-link" href="#doc/${doc.slug}">Open document</a>
        </article>
      `
    )
    .join("");
}

function renderHome() {
  const constitutionDocs = siteData.docs.filter((doc) => doc.group === "Constitution");
  const overviewDocs = ["overview", "comparison", "scorecard"].map(bySlug).filter(Boolean);
  const stats = siteData.overview;

  heroPanel.innerHTML = `
    <section class="hero">
      <div class="eyebrow">Public Draft Site</div>
      <h1>${stats.title}</h1>
      <p>${stats.subtitle}</p>
      <div class="hero-actions">
        <a class="hero-action hero-action--primary" href="#doc/preamble">Start with the Preamble</a>
        <a class="hero-action" href="#doc/overview">Read the overview</a>
        <a class="hero-action" href="#doc/scorecard">See the scorecard</a>
      </div>
    </section>

    <div class="stats-grid">
      <article class="stat-card">
        <span class="stat-card__label">Articles</span>
        <span class="stat-card__value">${stats.article_count}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">Simulation scenarios</span>
        <span class="stat-card__value">${stats.scenario_count}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">Overall score</span>
        <span class="stat-card__value">${stats.overall_score ?? "—"}</span>
      </article>
      <article class="stat-card">
        <span class="stat-card__label">Unresolved obligations</span>
        <span class="stat-card__value">${stats.unresolved_obligations}</span>
      </article>
    </div>
  `;

  const results = matchingDocs();
  const searchSection = currentFilter.trim()
    ? `
    <section>
      <h2 class="section-title">Search Results</h2>
      ${
        results.length
          ? `<div class="card-grid">${makeArticleCards(results.slice(0, 12))}</div>`
          : `<div class="empty-message">No documents match “${currentFilter}”.</div>`
      }
    </section>
  `
    : "";

  contentPanel.innerHTML = `
    ${searchSection}
    <section>
      <h2 class="section-title">Start Here</h2>
      <div class="card-grid">${makeArticleCards(overviewDocs)}</div>
    </section>
    <section>
      <h2 class="section-title">Read the Constitution</h2>
      <div class="card-grid">${makeArticleCards(constitutionDocs)}</div>
    </section>
  `;

  tocContent.innerHTML = `
    <a class="toc-link" href="#doc/overview">Overview</a>
    <a class="toc-link" href="#doc/preamble">Preamble</a>
    <a class="toc-link" href="#doc/scorecard">Scorecard</a>
  `;
}

async function renderDoc(slug) {
  const doc = bySlug(slug);
  if (!doc) {
    renderHome();
    return;
  }

  const markdown = await fetch(sourceUrl(doc)).then((response) => response.text());
  const rendered = marked.parse(markdown);

  heroPanel.innerHTML = "";
  contentPanel.innerHTML = `
    <section class="reader-shell">
      <header class="reader-header">
        <div class="eyebrow">${doc.group}</div>
        <h1>${doc.title}</h1>
        <div class="reader-summary">${doc.summary}</div>
        <div class="reader-meta">${metaPills(doc)}</div>
        <a class="source-link" href="${sourceUrl(doc)}" target="_blank" rel="noreferrer">Open source markdown</a>
      </header>
      <article class="reader-body">
        <div class="markdown-body" id="markdownBody">${rendered}</div>
      </article>
    </section>
  `;

  renderToc(doc);
}

function renderToc(doc) {
  if (!doc.headings?.length) {
    tocContent.innerHTML = `<div class="empty-message">No section map for this page.</div>`;
    return;
  }
  tocContent.innerHTML = doc.headings
    .map(
      (heading) => `
        <a class="toc-link level-${heading.level}" href="#doc/${doc.slug}/${heading.anchor}">
          ${heading.text}
        </a>
      `
    )
    .join("");
}

function applyAnchorFromHash() {
  const [, route, slug, anchor] = location.hash.match(/^#([^/]+)?\/?([^/]+)?\/?(.*)?$/) || [];
  if (route !== "doc" || !anchor) return;
  const target = document.getElementById(anchor);
  if (target) {
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

async function render() {
  renderNavigation();
  const match = location.hash.match(/^#doc\/([^/]+)/);
  if (!match) {
    renderHome();
    return;
  }
  await renderDoc(match[1]);
  renderNavigation();
  applyAnchorFromHash();
}

async function init() {
  siteData = await fetch(DATA_URL).then((response) => response.json());
  render();
}

searchInput.addEventListener("input", () => {
  currentFilter = searchInput.value;
  renderNavigation();
});

window.addEventListener("hashchange", () => {
  render();
  sidebar.classList.remove("is-open");
});

menuButton.addEventListener("click", () => {
  sidebar.classList.toggle("is-open");
});

init();
