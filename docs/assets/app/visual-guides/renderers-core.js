import {
  rightsDataForLocale,
  emergencyDataForLocale,
  powerDataForLocale,
  rightsEnforcementDataForLocale,
} from "./data-core.js";
import {
  rightsCards,
  renderEmergencyGuide,
  renderFlowGuide,
  renderPowerGuide,
} from "./rendering.js";

export const CORE_GUIDE_RENDERERS = {
  "rights-at-a-glance": (doc, siteData) => {
    const data = rightsDataForLocale(siteData.locale);
    return `
      <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
        <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
          <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
          ${data.categories
            .map(
              (category) =>
                `<button class="filter-chip" type="button" data-guide-filter="${category.key}">${category.label}</button>`
            )
            .join("")}
        </div>
        <p class="visual-guide__note">${data.note}</p>
        <div class="visual-guide__body">
          ${rightsCards(data.categories)}
        </div>
      </section>
    `;
  },
  "emergency-powers-lifecycle": (doc, siteData) => renderEmergencyGuide(doc, emergencyDataForLocale(siteData.locale)),
  "power-distribution": (doc, siteData) => renderPowerGuide(doc, powerDataForLocale(siteData.locale)),
  "how-rights-are-enforced": (doc, siteData) =>
    (() => {
      const data = rightsEnforcementDataForLocale(siteData.locale);
      return renderFlowGuide(doc, data, [
        { key: "ordinary", label: data.ordinary },
        { key: "expedited", label: data.expedited },
        { key: "emergency", label: data.emergency },
      ]);
    })(),
};

export const CORE_GUIDE_FILTERS = {
  "rights-at-a-glance": "basic",
  "emergency-powers-lifecycle": "basic",
  "power-distribution": "power",
  "how-rights-are-enforced": "basic",
};
