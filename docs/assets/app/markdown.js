import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

export function slugify(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/[\s_]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

const renderer = new marked.Renderer();
renderer.heading = ({ tokens, depth }) => {
  const text = tokens.map((token) => token.raw ?? token.text ?? "").join("").trim();
  const anchor = slugify(text);
  return `<h${depth} id="${anchor}">${text}</h${depth}>`;
};

marked.setOptions({ renderer });

export function parseMarkdown(markdown) {
  return marked.parse(markdown);
}
