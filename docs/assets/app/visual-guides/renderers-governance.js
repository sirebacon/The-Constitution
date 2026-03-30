import {
  congressDataForLocale,
  amendmentDataForLocale,
  accountabilityDataForLocale,
  vacancySuccessionDataForLocale,
  removalDataForLocale,
  electionsDataForLocale,
  presidentialPowersDataForLocale,
  billToLawDataForLocale,
  electionTransferDataForLocale,
  electionToInaugurationDataForLocale,
  federalismFloorDataForLocale,
  organsGuideDataForLocale,
  unamendableCoreDataForLocale,
} from "./data-governance.js";
import {
  renderCardGuide,
  renderTableGuide,
  renderRemovalGuide,
  renderFlowGuide,
} from "./rendering.js";

const CONGRESS_LABELS = {
  en: { feature: "Feature", current: "Current", draft: "This draft", note: "Why" },
  es: { feature: "Característica", current: "Actual", draft: "Este borrador", note: "Por qué" },
  "zh-Hans": { feature: "特征", current: "现行制度", draft: "本草案", note: "说明" },
};

export const GOVERNANCE_GUIDE_RENDERERS = {
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
  "vacancy-and-succession": (doc, siteData) =>
    renderRemovalGuide(doc, vacancySuccessionDataForLocale(siteData.locale)),
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
  "election-to-inauguration": (doc, siteData) =>
    (() => {
      const data = electionToInaugurationDataForLocale(siteData.locale);
      return renderFlowGuide(doc, data, [
        { key: "nomination", label: data.nomination },
        { key: "election", label: data.election },
        { key: "certification", label: data.certification },
        { key: "inauguration", label: data.inauguration },
      ]);
    })(),
  "federalism-and-the-democratic-floor": (doc, siteData) =>
    renderCardGuide(doc, federalismFloorDataForLocale(siteData.locale)),
  "how-organs-work-together": (doc, siteData) =>
    renderCardGuide(doc, organsGuideDataForLocale(siteData.locale)),
  "what-cannot-be-changed": (doc, siteData) =>
    renderCardGuide(doc, unamendableCoreDataForLocale(siteData.locale)),
};

export const GOVERNANCE_GUIDE_FILTERS = {
  "removal-pathways": "basic",
  "how-elections-work": "basic",
  "congress-comparison": "basic",
  "amendment-process": "basic",
  "accountability-commission": "basic",
  "vacancy-and-succession": "basic",
  "presidential-powers-comparison": "basic",
  "how-a-bill-becomes-law": "basic",
  "election-to-transfer-of-power": "basic",
  "election-to-inauguration": "basic",
  "federalism-and-the-democratic-floor": "basic",
  "how-organs-work-together": "basic",
  "what-cannot-be-changed": "basic",
};
