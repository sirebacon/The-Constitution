import { CORE_GUIDE_FILTERS, CORE_GUIDE_RENDERERS } from "./renderers-core.js";
import { GOVERNANCE_GUIDE_FILTERS, GOVERNANCE_GUIDE_RENDERERS } from "./renderers-governance.js";
import { applyBasicGuideFilter, applyPowerGuideFilter } from "./filters.js";

const GUIDE_RENDERERS = {
  ...CORE_GUIDE_RENDERERS,
  ...GOVERNANCE_GUIDE_RENDERERS,
};

const GUIDE_FILTERS = {
  ...CORE_GUIDE_FILTERS,
  ...GOVERNANCE_GUIDE_FILTERS,
};

export function renderVisualGuide(doc, siteData) {
  const renderer = GUIDE_RENDERERS[doc.slug];
  return renderer ? renderer(doc, siteData) : "";
}

export function activateVisualGuide(doc, container) {
  if (!container) return;
  const filterMode = GUIDE_FILTERS[doc.slug];
  if (filterMode === "power") {
    applyPowerGuideFilter(container);
    return;
  }
  if (filterMode === "basic") {
    applyBasicGuideFilter(container);
  }
}
