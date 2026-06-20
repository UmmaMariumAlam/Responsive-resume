# HTML CV Generator

A small tool that takes my portfolio site's HTML/CSS and generates a
pixel-accurate PDF — preserving the dark-mode design instead of falling
back to a plain white background like most browser print exports.

## Contents
- `cv.html` — the CV layout and styling
- `export.py` - Playwright script that renders the page and exports it as PDF

## How it works
Uses [Playwright](https://playwright.dev/python/) to launch a real headless
browser, load the HTML page, and export it as a PDF. Because it's an actual
browser rendering the page (not a basic HTML-to-PDF converter), all CSS —
including the dark theme, gradients, and custom fonts — is preserved exactly
as it appears on the live site.

## Why I built this
Editing a CV in Canva or Word is slow once you need fine layout control.
This lets me edit plain HTML/CSS and instantly export a styled, accurate PDF —
much faster to iterate on, and the output actually matches my site's design.

## Running it

\`\`\`bash
pip install playwright
playwright install chromium
python export.py
\`\`\`