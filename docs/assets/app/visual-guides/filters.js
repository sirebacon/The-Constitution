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
