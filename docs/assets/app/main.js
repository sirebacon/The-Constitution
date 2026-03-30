import { DATA_URL } from "./config.js";
import { refs } from "./dom.js";
import { getStrings } from "./i18n.js";
import { applyAnchorFromHash, renderDoc, renderHome, renderNavigation } from "./render.js";

const state = {
  siteData: null,
  currentFilter: "",
  locale: "en",
};

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
    refs.sidebar.classList.remove("is-open");
  });

  refs.menuButton.addEventListener("click", () => {
    refs.sidebar.classList.toggle("is-open");
  });

  render();
}

init();
