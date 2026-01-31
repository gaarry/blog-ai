---
title: "Implementing Dark Mode"
date: 2025-08-15
draft: false
description: "How to add dark mode support to your website."
tags: ["css", "web-design"]
---

Dark mode is expected by users today. Here's how to implement it:

## CSS Approach

Use CSS custom properties:

\`\`\`css
:root {
  --bg-color: #fff;
  --text-color: #111;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg-color: #111;
    --text-color: #e0e0e0;
  }
}

body {
  background: var(--bg-color);
  color: var(--text-color);
}
\`\`\`

## JavaScript Detection

You can also use JavaScript to respect user preference:

\`\`\`javascript
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.body.classList.add('dark');
}
\`\`\`
