const STRINGS = {
  en: {
    publicDraftSite: "Public Draft Site",
    startWithPreamble: "Start with the Preamble",
    readOverview: "Read the overview",
    seeScorecard: "See the scorecard",
    articles: "Articles",
    simulationScenarios: "Simulation scenarios",
    overallScore: "Overall score",
    unresolvedObligations: "Unresolved obligations",
    startHere: "Start Here",
    readConstitution: "Read the Constitution",
    searchResults: "Search Results",
    noSearchResults: (term) => `No documents match “${term}”.`,
    noSectionMap: "No section map for this page.",
    openDocument: "Open document",
    openSourceMarkdown: "Open source markdown",
    articleLabel: "Article",
    textLabel: "Text",
    constitutionLabel: "Constitution",
    preambleLabel: "Preamble",
    documentLabel: "Document",
    statusLabel: "Status",
  },
};

export function getStrings(locale = "en") {
  return STRINGS[locale] ?? STRINGS.en;
}
