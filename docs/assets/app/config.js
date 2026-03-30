export function dataUrlForLocale(locale) {
  return locale && locale !== "en" ? `./assets/site-data.${locale}.json` : "./assets/site-data.json";
}
