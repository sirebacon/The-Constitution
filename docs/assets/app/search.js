export function searchCorpus(doc) {
  return `${doc.title} ${doc.summary} ${doc.search_text ?? ""}`.toLowerCase();
}

export function docMatchesFilter(doc, filter) {
  if (!filter) return true;
  return searchCorpus(doc).includes(filter);
}

export function matchingDocs(docs, filter) {
  if (!filter) return [];
  return docs
    .filter((doc) => docMatchesFilter(doc, filter))
    .sort((a, b) => {
      const aScore = (a.title.toLowerCase().includes(filter) ? 2 : 0) + (a.summary.toLowerCase().includes(filter) ? 1 : 0);
      const bScore = (b.title.toLowerCase().includes(filter) ? 2 : 0) + (b.summary.toLowerCase().includes(filter) ? 1 : 0);
      return bScore - aScore;
    });
}
