import {
  rightsDataForLocale,
  emergencyDataForLocale,
  powerDataForLocale,
  rightsEnforcementDataForLocale,
} from "./data-core.js";
import {
  congressDataForLocale,
  amendmentDataForLocale,
  accountabilityDataForLocale,
  removalDataForLocale,
  electionsDataForLocale,
  presidentialPowersDataForLocale,
  billToLawDataForLocale,
  electionTransferDataForLocale,
} from "./data-governance.js";
import {
  rightsCards,
  renderCardGuide,
  renderTableGuide,
  renderRemovalGuide,
  renderEmergencyGuide,
  renderFlowGuide,
  renderPowerGuide,
  applyBasicGuideFilter,
  applyPowerGuideFilter,
} from "./shared.js";

const CONGRESS_LABELS = {
  en: { feature: "Feature", current: "Current", draft: "This draft", note: "Why" },
  es: { feature: "Característica", current: "Actual", draft: "Este borrador", note: "Por qué" },
  "zh-Hans": { feature: "特征", current: "现行制度", draft: "本草案", note: "说明" },
};

const GUIDE_RENDERERS = {
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
  "removal-pathways": (doc, siteData) => renderRemovalGuide(doc, removalDataForLocale(siteData.locale)),
  "how-elections-work": (doc, siteData) => renderCardGuide(doc, electionsDataForLocale(siteData.locale)),
  "congress-comparison": (doc, siteData) =>
    renderTableGuide(
      doc,
      congressDataForLocale(siteData.locale),
      CONGRESS_LABELS[siteData.locale] || CONGRESS_LABELS.en
    ),
  "amendment-process": (doc, siteData) => {
    const data = amendmentDataForLocale(siteData.locale);
    return renderTableGuide(doc, data, {
      feature: data.featureLabel,
      current: data.track1Label,
      draft: data.track2Label,
      note: data.whyLabel,
    });
  },
  "accountability-commission": (doc, siteData) =>
    renderCardGuide(doc, accountabilityDataForLocale(siteData.locale)),
  "presidential-powers-comparison": (doc, siteData) =>
    renderTableGuide(
      doc,
      presidentialPowersDataForLocale(siteData.locale),
      CONGRESS_LABELS[siteData.locale] || CONGRESS_LABELS.en
    ),
  "how-a-bill-becomes-law": (doc, siteData) =>
    (() => {
      const data = billToLawDataForLocale(siteData.locale);
      return renderFlowGuide(doc, data, [
        { key: "ordinary", label: data.ordinary },
        { key: "vetoed", label: data.vetoed },
        { key: "deadlocked", label: data.deadlocked },
      ]);
    })(),
  "election-to-transfer-of-power": (doc, siteData) =>
    (() => {
      const data = electionTransferDataForLocale(siteData.locale);
      return renderFlowGuide(doc, data, [
        { key: "vote", label: data.vote },
        { key: "certify", label: data.certify },
        { key: "transfer", label: data.transfer },
      ]);
    })(),
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

const GUIDE_FILTERS = {
  "rights-at-a-glance": "basic",
  "emergency-powers-lifecycle": "basic",
  "power-distribution": "power",
  "removal-pathways": "basic",
  "how-elections-work": "basic",
  "congress-comparison": "basic",
  "amendment-process": "basic",
  "accountability-commission": "basic",
  "presidential-powers-comparison": "basic",
  "how-a-bill-becomes-law": "basic",
  "election-to-transfer-of-power": "basic",
  "how-rights-are-enforced": "basic",
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
