# Humanoid Robots in Healthcare Survey

This workspace contains the organized manuscript for the humanoid robots in healthcare review paper.

## Main Files

- `main.tex`: LaTeX entry point for the current manuscript.
- `sections/`: numbered manuscript sections in reading order.
- `refs.bib`: bibliography.
- `figures/`: paper figures and figure version history.
- `main.pdf`: latest carried-over compiled PDF.

## Evidence and Drafts

- `sources/`: survey evidence base, including paper lists, annotated summaries, systems notes, regulatory notes, and related software/project notes.
- `draft/2026-07-07/original_monolithic_main.tex`: pre-cleanup manuscript snapshot where the full paper was in one file.
- `draft/2026-07-07/current_split_snapshot/`: snapshot of the first organized split version before substantive rewriting.
- `draft/2026-07-07/sec*.md`: earlier Markdown draft material.

## Supporting Files

- `scripts/gen_figures.py`: regenerates manuscript figures into `figures/`.
- `document/`: supplementary materials and non-manuscript documents.
- `progress.html` and `progress/`: project progress dashboard and dated progress pages.
- `build/`: generated LaTeX build output; safe to regenerate.

Use numeric section prefixes such as `0_abstract.tex`, `1_introduction.tex`, and `2_background.tex` so the manuscript order is stable in file browsers and Overleaf.
