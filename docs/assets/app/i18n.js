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
    understandChoices: "Understand the Choices",
    keyClauses: "Key Clauses",
    searchResults: "Search Results",
    noSearchResults: (term) => `No documents match “${term}”.`,
    searchStatusResults: (count, term) =>
      count
        ? `${count} document${count === 1 ? "" : "s"} found for “${term}”.`
        : `No documents match “${term}”.`,
    searchStatusCleared: "Search cleared.",
    noSectionMap: "No section map for this page.",
    openDocument: "Open document",
    openSourceMarkdown: "Open source markdown",
    articleLabel: "Article",
    textLabel: "Text",
    constitutionLabel: "Constitution",
    preambleLabel: "Preamble",
    documentLabel: "Document",
    commentaryLabel: "Commentary",
    statusLabel: "Status",
    navigationRegionLabel: "Document navigation",
    onThisPageLabel: "On this page",
    homeTocLabel: "Key site pages",
    viewNotes: "View notes",
    readConstitutionText: "Read constitutional text",
    explanatoryNotes: "Explanatory notes",
  },
};

export function getStrings(locale = "en") {
  return STRINGS[locale] ?? STRINGS.en;
}
