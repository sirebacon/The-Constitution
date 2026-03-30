export function rightsCards(categories) {
  return categories
    .map(
      (category) => `
        <section class="rights-category" data-rights-category="${category.key}">
          <header class="rights-category__header">
            <div>
              <div class="eyebrow">${category.label}</div>
              <h2 class="rights-category__title">${category.label}</h2>
            </div>
            <p class="rights-category__summary">${category.summary}</p>
          </header>
          <div class="rights-grid">
            ${category.items
              .map(
                (item) => `
                  <article class="rights-card">
                    <h3>${item.title}</h3>
                    <p>${item.text}</p>
                    <div class="rights-card__meta">${item.article}</div>
                  </article>
                `
              )
              .join("")}
          </div>
        </section>
      `
    )
    .join("");
}

export function congressRows(rows) {
  return rows
    .map(
      (row) => `
        <tr>
          <th scope="row">${row.feature}</th>
          <td class="congress-cell congress-cell--current">${row.current}</td>
          <td class="congress-cell congress-cell--draft">${row.draft}</td>
          ${row.note ? `<td class="congress-cell congress-cell--note">${row.note}</td>` : "<td></td>"}
        </tr>
      `
    )
    .join("");
}

export function renderCardGuide(doc, data) {
  return `
    <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
      <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
        <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
        ${data.categories
          .map((cat) => `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`)
          .join("")}
      </div>
      <p class="visual-guide__note">${data.note}</p>
      <div class="visual-guide__body">
        ${data.categories
          .map(
            (cat) => `
              <section class="rights-category" data-rights-category="${cat.key}">
                <header class="rights-category__header">
                  <h2 class="rights-category__title">${cat.label}</h2>
                  ${cat.summary ? `<p class="rights-category__summary">${cat.summary}</p>` : ""}
                </header>
                <div class="rights-grid">
                  ${cat.items
                    .map(
                      (item) => `
                        <article class="rights-card">
                          <h3>${item.title}</h3>
                          <p>${item.text}</p>
                          <div class="rights-card__meta">${item.article}</div>
                        </article>
                      `
                    )
                    .join("")}
                </div>
              </section>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderTableGuide(doc, data, labels) {
  return `
    <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
      <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
        <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
        ${data.categories
          .map((cat) => `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`)
          .join("")}
      </div>
      <p class="visual-guide__note">${data.note}</p>
      <div class="visual-guide__body">
        ${data.categories
          .map(
            (cat) => `
              <section class="rights-category congress-section" data-rights-category="${cat.key}">
                <header class="rights-category__header">
                  <h2 class="rights-category__title">${cat.label}</h2>
                </header>
                <div class="congress-table-wrapper">
                  <table class="congress-table">
                    <thead>
                      <tr>
                        <th scope="col">${labels.feature}</th>
                        <th scope="col" class="congress-cell--current">${labels.current}</th>
                        <th scope="col" class="congress-cell--draft">${labels.draft}</th>
                        <th scope="col" class="congress-cell--note">${labels.note}</th>
                      </tr>
                    </thead>
                    <tbody>${congressRows(cat.rows)}</tbody>
                  </table>
                </div>
              </section>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderRemovalGuide(doc, data) {
  return `
    <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
      <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
        <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
        ${data.categories
          .map((cat) => `<button class="filter-chip" type="button" data-guide-filter="${cat.key}">${cat.label}</button>`)
          .join("")}
      </div>
      <p class="visual-guide__note">${data.note}</p>
      <div class="visual-guide__body">
        ${data.categories
          .map(
            (cat) => `
              <section class="rights-category congress-section" data-rights-category="${cat.key}">
                <header class="rights-category__header">
                  <h2 class="rights-category__title">${cat.label}</h2>
                </header>
                <div class="congress-table-wrapper">
                  <table class="congress-table">
                    <thead>
                      <tr>
                        <th scope="col">${data.pathLabel}</th>
                        <th scope="col">${data.triggerLabel}</th>
                        <th scope="col">${data.decidesLabel}</th>
                        <th scope="col" class="congress-cell--draft">${data.thresholdLabel}</th>
                        <th scope="col">${data.outcomeLabel}</th>
                        <th scope="col" class="congress-cell--note">§</th>
                      </tr>
                    </thead>
                    <tbody>
                      ${cat.paths
                        .map(
                          (path) => `
                            <tr>
                              <th scope="row">${path.path}</th>
                              <td class="congress-cell">${path.trigger}</td>
                              <td class="congress-cell">${path.decides}</td>
                              <td class="congress-cell congress-cell--draft">${path.threshold}</td>
                              <td class="congress-cell">${path.outcome}</td>
                              <td class="congress-cell congress-cell--note">${path.article}</td>
                            </tr>
                          `
                        )
                        .join("")}
                    </tbody>
                  </table>
                </div>
              </section>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderEmergencyGuide(doc, data) {
  return `
    <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
      <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
        <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
        <button class="filter-chip" type="button" data-guide-filter="ordinary">${data.ordinary}</button>
        <button class="filter-chip" type="button" data-guide-filter="lapse">${data.lapse}</button>
        <button class="filter-chip" type="button" data-guide-filter="abuse">${data.abuse}</button>
      </div>
      <p class="visual-guide__note">${data.note}</p>
      <div class="visual-guide__body">
        ${data.sections
          .map(
            (section) => `
              <section class="rights-category emergency-flow" data-rights-category="${section.key}">
                <header class="rights-category__header">
                  <div>
                    <div class="eyebrow">${section.label}</div>
                    <h2 class="rights-category__title">${section.label}</h2>
                  </div>
                  <p class="rights-category__summary">${section.summary}</p>
                </header>
                <ol class="emergency-steps">
                  ${section.steps
                    .map(
                      (step, index) => `
                        <li class="emergency-step">
                          <div class="emergency-step__index">${index + 1}</div>
                          <div class="emergency-step__body">
                            <h3>${step.title}</h3>
                            <div class="rights-card__meta">${step.meta}</div>
                            <p>${step.text}</p>
                          </div>
                        </li>
                      `
                    )
                    .join("")}
                </ol>
              </section>
            `
          )
          .join("")}
      </div>
    </section>
  `;
}

export function renderPowerGuide(doc, data) {
  return `
    <section class="visual-guide visual-guide--${doc.slug}" aria-labelledby="visual-guide-title">
      <div class="visual-guide__toolbar" role="group" aria-label="${data.filterLabel}">
        <button class="filter-chip is-active" type="button" data-guide-filter="all">${data.all}</button>
        <button class="filter-chip" type="button" data-guide-filter="electoral">${data.electoral}</button>
        <button class="filter-chip" type="button" data-guide-filter="checks">${data.checks}</button>
        <button class="filter-chip" type="button" data-guide-filter="accountability">${data.accountability}</button>
      </div>
      <p class="visual-guide__note">${data.note}</p>
      <div class="visual-guide__body">
        <section class="power-map">
          <div class="power-map__grid">
            ${data.nodes
              .map(
                (node) => `
                  <article class="power-node" data-power-node="${node.key}">
                    <div class="eyebrow">${node.label}</div>
                    <h2 class="rights-category__title">${node.label}</h2>
                    <p class="rights-category__summary">${node.summary}</p>
                  </article>
                `
              )
              .join("")}
          </div>
        </section>
        <section class="rights-category">
          <header class="rights-category__header">
            <div class="eyebrow">${data.all}</div>
            <h2 class="rights-category__title">${data.all}</h2>
          </header>
          <div class="rights-grid rights-grid--links">
            ${data.links
              .map(
                (link) => `
                  <article class="rights-card power-link" data-rights-category="${link.category}" data-link-from="${link.from}" data-link-to="${link.to}">
                    <h3>${link.label}</h3>
                    <p>${data.nodes.find((node) => node.key === link.from).label} → ${data.nodes.find((node) => node.key === link.to).label}</p>
                    <div class="rights-card__meta">${link.meta}</div>
                  </article>
                `
              )
              .join("")}
          </div>
        </section>
      </div>
    </section>
  `;
}

export function applyBasicGuideFilter(container) {
  const buttons = [...container.querySelectorAll("[data-guide-filter]")];
  const categories = [...container.querySelectorAll("[data-rights-category]")];
  if (!buttons.length || !categories.length) return;
  const applyFilter = (filter) => {
    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.guideFilter === filter);
    });
    categories.forEach((section) => {
      section.hidden = !(filter === "all" || section.dataset.rightsCategory === filter);
    });
  };
  buttons.forEach((button) => {
    button.addEventListener("click", () => applyFilter(button.dataset.guideFilter));
  });
}

export function applyPowerGuideFilter(container) {
  const buttons = [...container.querySelectorAll("[data-guide-filter]")];
  const powerNodes = [...container.querySelectorAll("[data-power-node]")];
  const powerLinks = [...container.querySelectorAll(".power-link[data-rights-category]")];
  if (!buttons.length || !powerLinks.length) return;
  const applyFilter = (filter) => {
    buttons.forEach((button) => {
      button.classList.toggle("is-active", button.dataset.guideFilter === filter);
    });
    const activeNodes = new Set();
    powerLinks.forEach((link) => {
      const show = filter === "all" || link.dataset.rightsCategory === filter;
      link.hidden = !show;
      if (show) {
        activeNodes.add(link.dataset.linkFrom);
        activeNodes.add(link.dataset.linkTo);
      }
    });
    powerNodes.forEach((node) => {
      node.hidden = !(filter === "all" || activeNodes.has(node.dataset.powerNode));
    });
  };
  buttons.forEach((button) => {
    button.addEventListener("click", () => applyFilter(button.dataset.guideFilter));
  });
}
