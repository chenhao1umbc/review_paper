# Post-Paper Audit Report — v3

**Paper**: Humanoid Robots in Healthcare: Current Systems, Research Frontiers, and Clinical Opportunities
**Venue**: ACM Computing Surveys (CSUR)
**Date**: 2026-03-25
**Pages**: 31
**References**: 99 cited / 99 in .bib
**Abstract**: 95 words

---

## Severity Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 1 |
| MAJOR    | 4 |
| MINOR    | 2 |

**Verdict**: FAIL — 1 CRITICAL issue (`soransen2022workforce` unverifiable, likely fabricated)

Fix the CRITICAL and MAJOR items; structural changes below are tracked separately.

---

## 1. Reference Audit

### 1a. Pipeline Results

- **Total references**: 99
- **Pipeline REAL**: 93 (94%)
- **Pipeline SUSPICIOUS**: 6 — all investigated below

### 1b. Suspicious Entries — Verified

| BibKey | Pipeline Confidence | Verification Result | Severity |
|--------|---------------------|---------------------|----------|
| `who2016workforce` | 0.00 | **REAL** — WHO 2016 workforce report, government document not in academic DBs | OK |
| `japancabinet2023` | 0.00 | **REAL** — Japanese Cabinet Office annual report, government document | OK |
| `cadene2024lerobot` | 0.00 | **REAL** — GitHub software repository; `@misc` is correct | OK |
| `fda2021aiml` | 0.00 | **REAL** — FDA AI/ML SaMD action plan, official government document | OK |
| `fda2024pccp` | 0.00 | **REAL** — FDA PCCP guidance, official government document | OK |
| `geminiroboticsTeam2025` | 0.00 | **REAL** — arXiv:2503.20020 verified, Google DeepMind March 2025 | OK |
| `iso10218_2` | 0.00 | **REAL** — ISO 10218-2:2011 standard; `iso10218_1` verified REAL, Part 2 same series | OK |

All 6 "suspicious" entries are real — they are government documents, standards, or software repositories that are not indexed in academic databases.

### 1c. CRITICAL: Unverifiable Reference

| BibKey | Entry | Severity |
|--------|-------|----------|
| `soransen2022workforce` | Sørensen et al., "Nurses' Experiences with Robot-Assisted Hospital Logistics: A Qualitative Study", Journal of Advanced Nursing, 2022, vol 78, no 5, pp 1448–1459, DOI: 10.1111/jan.15099 | **CRITICAL** |

**Findings:**
- DOI `10.1111/jan.15099` returns 403 (access denied / not found) on Wiley Online Library
- Journal of Advanced Nursing Vol. 78, Issue 5 (May 2022) exists but this article title does not appear
- No database match found via PubMed, Google Scholar, or Semantic Scholar for this exact title + author + journal + year combination
- **This reference cannot be verified and appears fabricated or substantially incorrect**

**Required action**: Remove `soransen2022workforce` from both the .bib and the `\cite{soransen2022workforce}` call in main.tex (line ~919). The claim it supports ("Academic research attention in 2022–2026 was directed toward clinical procedure and HRI domains") does not require this specific citation — it is a structural observation from the review itself.

### 1d. MAJOR: Wrong DOI

| BibKey | Current DOI | Correct DOI | Severity |
|--------|-------------|-------------|----------|
| `krebs1998robot` | `10.1109/86.681185` | `10.1109/86.662623` | MAJOR |

Verified against PubMed (PMID 9535526) and IEEE Xplore. The paper is real and all other fields (authors, journal, year, volume, pages) are correct. Only the DOI needs updating.

### 1e. MAJOR: Wrong Entry Types

| BibKey | Current Type | Correct Type | Venue | Severity |
|--------|-------------|--------------|-------|----------|
| `cheng2024expressive` | `@misc` | `@inproceedings` | Robotics: Science and Systems (RSS) 2024 | MAJOR |
| `stasse2017talos` | `@article` | `@inproceedings` | IEEE-RAS 17th International Conference on Humanoid Robots (ICHR 2017) | MAJOR |

**`cheng2024expressive` fix:**
```bibtex
@inproceedings{cheng2024expressive,
  author    = {Cheng, Xuxin and Ji, Yandong and Chen, Junming and Yang, Ruihan and Yang, Ge and Wang, Xiaolong},
  title     = {Expressive Whole-Body Control for Humanoid Robots},
  booktitle = {Robotics: Science and Systems ({RSS})},
  year      = {2024},
  note      = {arXiv:2402.16796},
}
```

**`stasse2017talos` fix:**
```bibtex
@inproceedings{stasse2017talos,
  author    = {Stasse, Olivier and Flayols, Thomas and ...},
  title     = {{TALOS}: A New Humanoid Research Platform Targeted for Industrial Scenarios},
  booktitle = {2017 {IEEE-RAS} 17th International Conference on Humanoid Robots ({Humanoids})},
  year      = {2017},
  pages     = {689--695},
  doi       = {10.1109/HUMANOIDS.2017.8246947},
}
```

### 1f. BibTeX Cross-Reference Check

- **Orphaned entries**: None — all 99 bib entries are cited
- **Undefined citations**: None
- **Note field contamination**: None
- **Reference density**: 99 references — well above CSUR's 60-reference floor

### 1g. Progress from Previous Audits

All issues from v1 and v2 audits resolved:

| Previous issue | Status |
|----------------|--------|
| `decker2017medical` (fabricated) | REMOVED ✓ |
| `sharkey2014granny` key mismatch | FIXED → `sharkey2012granny` ✓ |
| `young2011toward` key mismatch | FIXED → `young2009toward` ✓ |
| `wen2024hirt` — @misc → @inproceedings | FIXED ✓ |
| `he2024omnikh` — @misc → @inproceedings | FIXED ✓ |
| `lu2025gentlehumanoid` author names | FIXED ✓ |
| `robinson2023brief` — @misc → @article | FIXED ✓ |
| `sayis2024technology` — @misc → @inproceedings | FIXED ✓ |
| `sobrepera2022feasibility` — @misc → @inproceedings | FIXED ✓ |

---

## 2. Writing Style Audit

### 2a. AI Writing Verdict: CLEAN

Zero blacklist violations found in the current version:

- `paradigm`: 0 instances ✓
- `landscape` (body prose): 0 instances ✓ (only in internal figure label `fig:landscape`)
- `robust`: 0 instances ✓
- `notably`: 0 instances ✓
- Em-dashes: 0 instances ✓ (all replaced)
- Banned phrases: 0 instances ✓
- Banned paragraph transitions (Moreover/Furthermore/Additionally): 0 instances ✓
- Section 5 rigid template: CLEARED ✓
- Contributions ordinal list: CLEARED ✓

**`leverage` at L1463**: "most leverage-intensive investment the field can make" — compound modifier/noun, NOT the verb usage. Not a violation.

**All `navigate/navigating` uses are literal** (robot physically traversing physical space). Not violations.

### 2b. Sentence Length Distribution

- Count: 538 sentences
- Mean: 24.1 words, StdDev: **21.8** — excellent variation
- Short (<11 words): 16%
- Mid (15–25 words): 36%
- Long (>34 words): 14%
- Verdict: **Healthy variation. No AI uniformity detected.**

### 2c. Style Assessment

The paper reads consistently in the author's voice. Key strengths in the current version:
- Introduction opens with a direct declarative fact, no preamble
- Gaps in prior work stated without praising existing work first ("Cunha et al. is the closest: a 2025 scoping review... which predates the LLM/VLA integration wave entirely")
- Claims backed by specific numbers throughout (14 qualifying papers, 147 screened, 70% task success, specific TRL levels)
- No hollow emphasis; "statistically significant" used with RCT evidence at L884 — correct

**Minor observation** (not CRITICAL): The contributions block (lines 156–167) uses a `\begin{itemize}` list. The author's published style uses direct prose ("The central contribution of this paper is..."). In a CSUR survey context, a brief bulleted list is acceptable — but if further revisions happen, consider one sentence introducing the HCDR framework as the key intellectual contribution, with the other items as supporting work.

---

## 3. Venue Format Compliance

### 3a. Compilation

- **Undefined citations**: None
- **Overfull hbox**: None detected above threshold
- **Pages**: 31 — appropriate for CSUR
- **Document class**: `manuscript,screen` — correct for submission draft

### 3b. Abstract

- **Word count**: 95 — within CSUR 100-word hard cap with 5-word margin
- **No citations, no first person, no math**: All correct
- **Claims substantiated in body**: Verified

### 3c. Figures

| Figure | Caption | Issues |
|--------|---------|--------|
| `fig:timeline` (tech history) | Self-contained | OK |
| `fig:landscape` (evidence distribution) | Caption says "Evidence distribution" — correct | OK |
| `fig:trl` (TRL bar chart) | Self-contained | OK |
| `fig:capability_gap` (capability gap) | Self-contained | OK |
| `fig:regulatory` (regulatory pathways) | Self-contained | OK |

### 3d. Tables

All 6 tables use `\toprule/\midrule/\bottomrule` (booktabs). No `\hline`. No `\scriptsize` or `\tiny`. All have captions and labels.

---

## 4. Structural Alignment — User Outline vs. Current Paper

You provided a desired paper structure. Here is the alignment check:

### Introduction (4 paragraphs)

| Desired | Current Paper | Status |
|---------|--------------|--------|
| Para 1: Gap (capability exists, deployment doesn't; hardware + LLM convergence) | Lines 100–121: substantially this content | ALIGNED — minor restructuring may tighten it |
| Para 2: Gap in existing literature (old reviews, mixed platform types) | Lines 122–133: "No existing review covers this territory..." | ALIGNED |
| Para 3: Scope + methodology (one sentence) + contributions narrative | Lines 135–155: present but prose-heavy; methodology embedded in intro ✓ | PARTIALLY ALIGNED — methodology is one paragraph, not one sentence |
| Para 4: Brief contributions list (4 items) | Lines 156–167: 4-item bullet list | ALIGNED — currently 4 items, you noted you wanted 5 (adding TRL assessment as separate contribution) |

**Gap**: You mentioned wanting 5 contributions, including TRL assessment explicitly. The current list has 4 (TRL is embedded in the HCDR discussion, not listed separately). If you want TRL as Contribution 4 and HCDR as Contribution 5, the bullet list needs one item added.

### Background (Section 2 in paper)

| Desired (3.x) | Current subsection | Status |
|--------------|-------------------|--------|
| 3.1 Why need robots (workforce shortage, aging) | §2.1 The Healthcare Imperative | ALIGNED |
| 3.2 Why humanoid (3 reasons: environment, mirror neurons, dignity) | §2.2 Why the Humanoid Form Factor | ALIGNED |
| 3.3 Why now (LLM/VLA inflection) | §2.3 Why Now: The LLM/VLA Inflection Point | ALIGNED |
| 3.4 Brief history (3 eras) | §2.4 Historical Evolution | ALIGNED |
| 3.5 vs. other medical robots | §2.5 Humanoid Robots vs. Other Medical Robots | ALIGNED |

Background is fully aligned. No changes needed.

### Sections 3–7

| Desired | Current title (line) | Status |
|---------|---------------------|--------|
| "What current humanoids can do" (survey results) | §3 "What Can Humanoid Robots Do Today?" (L512) | ALIGNED — title already correct |
| "What healthcare needs from humanoid embodied AI" (requirements) | §4 "What Healthcare Needs from Humanoid Robots" (L748) | PARTIALLY ALIGNED — title acceptable, but you noted it should convey clinical requirements more clearly. Consider: "Clinical Requirements for Humanoid Robots in Healthcare" |
| Challenges of applying in healthcare | §5 "Challenges in Clinical Deployment" (L1015) | ALIGNED |
| Discussion and future work (promising directions) | §6 "Discussion and Future Work" (L1302) | PARTIALLY ALIGNED — §6 has 7 subsections, including TRL assessment, HCDR framework, practitioner guidance, regulatory roadmap, ethics. The research priorities (§6.3) addresses promising future directions, but is only one of many subsections. If the emphasis should shift to future directions, §6.3 (Research Priorities) could be expanded and moved earlier in §6 |

---

## 5. Recommended Actions (prioritized)

### CRITICAL — Fix before any submission

1. **Remove `soransen2022workforce`**: Delete the .bib entry and `\cite{soransen2022workforce}` at line ~919. The surrounding text ("Academic research attention in 2022–2026 was directed toward clinical procedure and HRI domains") stands without a citation — it is a synthesis observation, not an empirical claim requiring external support.

### MAJOR — Fix before submission

2. **Fix `krebs1998robot` DOI**: Change `10.1109/86.681185` → `10.1109/86.662623`

3. **Fix `cheng2024expressive` entry type**: `@misc` → `@inproceedings`, add `booktitle = {Robotics: Science and Systems ({RSS})}`, year remains 2024

4. **Fix `stasse2017talos` entry type**: `@article` → `@inproceedings`, add `booktitle = {2017 {IEEE-RAS} 17th International Conference on Humanoid Robots ({Humanoids})}`, remove `journal` field

### MINOR — Polish before submission

5. **Rename `fig:landscape` label** (optional): Internal LaTeX label says "landscape" but caption says "Evidence distribution". If the label is renamed to `fig:evidence_dist`, update the `\ref{fig:landscape}` at line ~989.

6. **Rerun full compile**: After reference fixes: `pdflatex → bibtex → pdflatex → pdflatex`

### Structural — For writer session

7. **Section 4 title**: Consider "Clinical Requirements for Humanoid Robots" or "What Clinical Deployment Demands from Humanoid Robots" — the current title is acceptable but could be sharper

8. **Contributions count**: If TRL assessment is to be listed as a separate 5th contribution (as suggested in your outline), add it to the bullet list between "Platform capability assessment" and "Regulatory pathway analysis"

9. **Discussion focus**: §6.3 Research Priorities contains the future directions content. If you want future work to be the emphasis of §6, consider moving it to §6.1 and letting TRL + HCDR framework discussion follow from it
