# LaTeX CV

A version of my resume written and typeset in LaTeX.

## Contents
- `latex_cv_code.tex` — LaTeX source file
- `resume.pdf` — compiled output (dark mode)

## Why LaTeX
I wanted a version of my CV with precise typographic control and a clean, print-ready format useful for academic or research-facing applications (e.g. alongside my thesis work) where a LaTeX-formatted document is the norm.

## Tools & Compiling
Written and compiled using [Prism](https://prism.openai.com), OpenAI's cloud-based LaTeX editor. Prism compiles using pdfLaTeX under the hood and a successful
run of:

\`\`\`bash
pdflatex -interaction=nonstopmode -halt-on-error latex_cv_code.tex
\`\`\`

To rebuild from source without Prism, run the same command locally with any standard pdfLaTeX installation (e.g. TeX Live, MiKTeX):

\`\`\`bash
pdflatex latex_cv_code.tex
\`\`\`

## Dark Mode / Light Mode

The CV is built with a theme switch where by default it compiles in **dark mode** to match my portfolio site's design. A clean **light mode** (white background, suited for actual paper printing) is also available.

To switch themes, open `latex_cv_code.tex` and find this block near the top of the file:

\`\`\`latex
\newif\ifdarkmode
\darkmodetrue   % <- change to \darkmodefalse for light mode
\`\`\`

Change `\darkmodetrue` to `\darkmodefalse`, then recompile. This single switch automatically updates the page background, main text color, card backgrounds, and muted text colors throughout the document (`latex_cv_code.tex:21`).

Both modes have been tested and build successfully.