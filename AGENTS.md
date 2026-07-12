# Research Writing Workspace Instructions

This folder is for an academic paper, survey, or proposal. Keep reusable project organization separate from project-specific motivation and novelty claims.

## Folder Layout

- `main.tex`: LaTeX entry point.
- `sections/`: canonical manuscript/proposal sections.
- `figures/`: figures, diagrams, plots, and timeline components.
- `sources/`: evidence base for surveys and proposals, including paper lists, annotated notes, system inventories, regulatory notes, datasets, and source provenance. Do not confuse `sources/` with LaTeX source sections.
- `draft/`: dated draft snapshots and rough writing. Draft files are not the canonical manuscript.
- `scripts/`: reproducible scripts for figures, checks, or data processing.
- `progress.html`: root progress dashboard.
- `progress/`: one detailed HTML page per meeting or major writing update.
- `document/`: supplementary documents, forms, generated standalone PDFs, checklists, cover letters, and reusable local templates.
- `relatedwork/`: papers, review comments, and literature notes.
- `build/`: generated build artifacts; do not edit by hand.
- `refs.bib`: bibliography.

Use lowercase file and directory names. Prefer plural category folders such as `sections/`, `figures/`, and `progress/`.

## Section Naming and Order

Always number manuscript/proposal section files by reading order, because file browsers and Overleaf sort names alphabetically. Do not rely on English or pinyin ordering.

Use this pattern for survey papers unless the project defines a different order:

- `sections/0_abstract.tex`
- `sections/1_introduction.tex`
- `sections/2_background.tex`
- `sections/3_systems.tex`
- `sections/4_applications.tex`
- `sections/5_challenges.tex`
- `sections/6_discussion.tex`
- `sections/7_conclusion.tex`

For subsections or multi-part sections, continue the same numeric prefix style, such as `5_1_safety.tex` and `5_2_regulation.tex`. If the paper has no separate abstract file, still reserve `0_abstract.tex` when splitting later.

## Paper and Proposal Claim Modules

For every paper or proposal, keep these claim modules easy to locate in drafts and notes:

- motivation;
- gap;
- novelty;
- architecture;
- evidence or validation;
- impact.

Do not mix motivation and novelty unless explicitly writing a compressed abstract.

Project-specific motivation, gap, novelty, selling points, and contribution framing belong in the local project notes or section drafts, not in the reusable workspace template.

## Draft Snapshots

Keep rough drafts in `draft/`. When freezing a draft state, create a dated folder such as `draft/2026-07-07/` and put that day's draft files there. Do not overwrite dated snapshots unless the user explicitly asks.

Use the canonical manuscript in `sections/` and `main.tex` for submission work. Use `draft/` for old prose, alternate framings, meeting-writing outputs, and temporary text that may later be promoted into `sections/`.

## Progress Log

Keep `progress.html` at the root. Put dated detail pages under `progress/yyyy-mm-dd.html`. Each update should record decisions, links, action items, and implications for motivation/gap/novelty/architecture.


## Host-Specific Master Template Rule

This project copy may have been created from a machine-specific master template. Only update the external master template at `C:\Users\xl24j\Documents\codex-writing-templates\research-writing-workspace` when that exact path already exists on the current machine. If the path does not exist, do not create it and do not attempt to modify Xin's Documents folder; update only the local project.
## Editing Rules

- Update LaTeX paths after moving files.
- Keep figures under `figures/`.
- Keep section text under `sections/`.
- Preserve section file numeric prefixes when renaming or splitting sections.
- Keep generated files under `build/` where possible.
- Preserve collaborator-written text unless asked to rewrite.
