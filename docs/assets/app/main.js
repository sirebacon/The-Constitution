import { dataUrlForLocale } from "./config.js";
import { refs } from "./dom.js";
import { getStrings } from "./i18n.js";
import { applyAnchorFromHash, renderDoc, renderHome, renderNavigation } from "./render.js";

const state = {
  siteData: null,
  currentFilter: "",
  locale: "en",
};

function requestedLocale() {
  const params = new URLSearchParams(window.location.search);
  return params.get("lang") || "en";
}

function updateLocaleQuery(locale) {
  const url = new URL(window.location.href);
  if (!locale || locale === "en") {
    url.searchParams.delete("lang");
  } else {
    url.searchParams.set("lang", locale);
  }
  window.history.replaceState({}, "", url);
}

async function loadSiteData(locale) {
  const response = await fetch(dataUrlForLocale(locale));
  if (!response.ok && locale !== "en") {
    return fetch(dataUrlForLocale("en")).then((fallback) => fallback.json());
  }
  return response.json();
}

function populateLocaleSwitcher() {
  if (!refs.localeSelect || !state.siteData?.locales) return;
  refs.localeSelect.innerHTML = state.siteData.locales
    .map(
      (locale) =>
        `<option value="${locale.code}" ${locale.code === state.locale ? "selected" : ""}>${locale.label}</option>`
    )
    .join("");
}

function setMenuExpanded(isExpanded) {
  refs.menuButton.setAttribute("aria-expanded", String(isExpanded));
  refs.sidebar.classList.toggle("is-open", isExpanded);
}

function closeMenu() {
  setMenuExpanded(false);
}

function announceSearch(strings) {
  if (!refs.searchStatus) return;
  const term = state.currentFilter.trim();
  if (!term) {
    refs.searchStatus.textContent = strings.searchStatusCleared;
    return;
  }
  const count = state.siteData.docs.filter((doc) => {
    const content = [doc.title, doc.summary, doc.search_text].filter(Boolean).join(" ").toLowerCase();
    return content.includes(term.toLowerCase());
  }).length;
  refs.searchStatus.textContent = strings.searchStatusResults(count, term);
}

function applyChromeStrings(strings) {
  if (refs.localeLabel) refs.localeLabel.textContent = strings.languageLabel;
  if (refs.searchLabel) refs.searchLabel.textContent = strings.searchLabel;
  if (refs.searchInput) refs.searchInput.placeholder = strings.searchPlaceholder;
  if (refs.searchHelp) refs.searchHelp.textContent = strings.searchHelp;
  if (refs.repoLink) refs.repoLink.textContent = strings.viewRepo;
  if (refs.topbarEyebrow) refs.topbarEyebrow.textContent = strings.topbarEyebrow;
}

async function render() {
  const strings = getStrings(state.locale);
  applyChromeStrings(strings);
  renderNavigation({
    siteData: state.siteData,
    currentFilter: state.currentFilter,
    strings,
  });

  const match = location.hash.match(/^#doc\/([^/]+)/);
  if (!match) {
    renderHome({
      siteData: state.siteData,
      currentFilter: state.currentFilter,
      strings,
    });
    return;
  }

  await renderDoc({
    siteData: state.siteData,
    slug: match[1],
    strings,
  });
  renderNavigation({
    siteData: state.siteData,
    currentFilter: state.currentFilter,
    strings,
  });
  applyAnchorFromHash();
}

async function init() {
  state.locale = requestedLocale();
  state.siteData = await loadSiteData(state.locale);
  state.locale = state.siteData.locale ?? "en";
  document.documentElement.lang = state.locale;
  updateLocaleQuery(state.locale);
  populateLocaleSwitcher();
  applyChromeStrings(getStrings(state.locale));

  refs.searchInput.addEventListener("input", () => {
    state.currentFilter = refs.searchInput.value;
    const strings = getStrings(state.locale);
    announceSearch(strings);
    renderNavigation({
      siteData: state.siteData,
      currentFilter: state.currentFilter,
      strings,
    });

    if (!location.hash || location.hash === "#home") {
      renderHome({
        siteData: state.siteData,
        currentFilter: state.currentFilter,
        strings,
      });
    }
  });

  window.addEventListener("hashchange", () => {
    render();
    closeMenu();
    refs.mainContent.focus();
  });

  refs.menuButton.addEventListener("click", () => {
    const isExpanded = refs.menuButton.getAttribute("aria-expanded") === "true";
    setMenuExpanded(!isExpanded);
  });

  refs.localeSelect?.addEventListener("change", async () => {
    state.locale = refs.localeSelect.value;
    state.siteData = await loadSiteData(state.locale);
    state.locale = state.siteData.locale ?? state.locale;
    document.documentElement.lang = state.locale;
    updateLocaleQuery(state.locale);
    populateLocaleSwitcher();
    applyChromeStrings(getStrings(state.locale));
    render();
  });

  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  render();
}

init();
