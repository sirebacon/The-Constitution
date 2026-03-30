import { DATA_URL } from "./config.js";
import { refs } from "./dom.js";
import { getStrings } from "./i18n.js";
import { applyAnchorFromHash, renderDoc, renderHome, renderNavigation } from "./render.js";

const state = {
  siteData: null,
  currentFilter: "",
  locale: "en",
};

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

async function render() {
  const strings = getStrings(state.locale);
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
  state.siteData = await fetch(DATA_URL).then((response) => response.json());
  state.locale = state.siteData.locale ?? "en";

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

  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
    }
  });

  render();
}

init();
