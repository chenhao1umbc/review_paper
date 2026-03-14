# Task 1.1 — Research Papers on Humanoid Robots in Healthcare

> Search date: 2026-03-10. Coverage: 2022–2026.
> Databases: arXiv, PubMed, IEEE Xplore, Google Scholar, ACM DL.
> Scope: original research only (no reviews/surveys). Humanoid-specific or directly applicable.
> Total qualifying papers: 14 (9 high-relevance, 5 medium/borderline).

---

## Category 1: Clinical Procedures / Teleoperation / Dexterous Medical Tasks

### P1 — PRIORITY SOURCE
**Humanoids in Hospitals: A Technical Study of Humanoid Robot Surrogates for Dexterous Medical Interventions**
- Authors: Atar S, Liang X, Joyce C, Richter F, Wood R, Goldberg C, Suresh P, Yip MC (UC San Diego)
- Year: 2025
- Venue: arXiv preprint
- ID/URL: https://arxiv.org/abs/2503.12725
- Summary: Bimanual teleoperation system for Unitree G1; evaluated across 7 clinical procedures (physical exams, emergency interventions, precision needle/ultrasound tasks). Demonstrates feasibility; identifies force output and sensor sensitivity as primary barriers to clinical translation.
- Tags: [CLINICAL-PROCEDURE]
- Relevance: **High**
- Sections: 3, 4, 5 (prominent placement required)

### P2
**LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy**
- Authors: Liang Z, Liang X, Atar S, Das S, Chiu Z, Zhang P, Joyce C, Richter F, Liu S, Yip MC (UC San Diego)
- Year: 2025 (submitted Oct 2025; revised Feb 2026)
- Venue: arXiv preprint (cs.RO)
- ID/URL: https://arxiv.org/abs/2510.03529 | DOI: 10.48550/arXiv.2510.03529
- Summary: First humanoid-robot-based laparoscopic teleoperation framework using inverse-mapping for manual-wristed laparoscopic instruments with remote center-of-motion constraints. Validated via user studies; frames humanoid deployment for surgical access in underserved communities.
- Tags: [CLINICAL-PROCEDURE]
- Relevance: **High**

### P3
**Humanoid Robots as First Assistants in Endoscopic Surgery**
- Authors: Cho SM, Mangulabnan JE, Zhang H, Mao Z, He Y, Guo P, Xu D, Hager G, Ishii M, Unberath M (Johns Hopkins University)
- Year: 2026 (submitted Feb 27, 2026)
- Venue: arXiv preprint (cs.RO)
- ID/URL: https://arxiv.org/abs/2602.24156
- Summary: First proof-of-concept of teleoperated Unitree G1 humanoid providing endoscopic visualization during an actual cadaveric sphenoidectomy performed by an attending otolaryngologist. Documents engineering targets for clinical translation; identifies autonomous diagnostic scoping as near-term opportunity.
- Tags: [CLINICAL-PROCEDURE]
- Relevance: **High**

---

## Category 2: LLM/VLM/VLA + Humanoid for Medical Tasks

### P4
**Integrating Reinforcement Learning and AI Agents for Adaptive Robotic Interaction and Assistance in Dementia Care**
- Authors: Yuan F, Hasnaeen N, Zhang R, Bible B, Taylor JR, Qi H, Yao F, Zhao X
- Year: 2025 (submitted Jan 2025)
- Venue: arXiv preprint (cs.AI / cs.RO)
- ID/URL: https://arxiv.org/abs/2501.17206
- Summary: Framework combining Pepper humanoid, RL, and LLMs for adaptive personalized dementia care; introduces probabilistic cognitive-emotional state modeling and LLM-based behavior simulation to overcome data scarcity in training adaptive caregiving agents.
- Note: Pepper is wheeled (not fully bipedal) but humanoid upper body; paper explicitly uses it as "humanoid robot." LLM integration is the key contribution.
- Tags: [ELDERLY-CARE] [LLM-HUMANOID]
- Relevance: **Medium**

---

## Category 3: Rehabilitation with Humanoid Robots

### P5
**Exploring EEG Responses during Observation of Actions Performed by Human Actor and Humanoid Robot**
- Authors: Nguyen AT, Anand A, Johnson MJ
- Year: 2024/2025 (IEEE BioRob 2024; arXiv submitted 2025)
- Venue: 10th IEEE RAS/EMBS International Conference for Biomedical Robotics and Biomechatronics (BioRob), Heidelberg, 2024, pp. 1795–1801
- ID/URL: https://arxiv.org/abs/2506.10170
- Summary: Pilot EEG study measuring sensorimotor responses in healthy participants observing actions by a humanoid robot vs. a human, targeting action observation therapy (AOT) for stroke rehabilitation. Demonstrates common mirror neuron system activity during humanoid robot observation; supports robot-facilitated AOT.
- Tags: [REHABILITATION]
- Relevance: **High**

### P6
**Feasibility and Acceptability of Remote Neuromotor Rehabilitation Interactions Using Social Robot Augmented Telepresence: A Case Study**
- Authors: Sobrepera MJ, Lee VG, Garg S, Johnson MJ
- Year: 2022 (submitted Feb 2022)
- Venue: arXiv preprint (cs.RO / cs.HC)
- ID/URL: https://arxiv.org/abs/2202.13433
- Summary: Social Robot Augmented Telepresence (SRAT) system combining humanoid robot with mobile telepresence for remote neuromotor rehabilitation. Case series with 6 subjects (3 stroke survivors, 3 pediatric); 5/6 rated SRAT superior to classical telepresence for rehabilitation interaction.
- Tags: [REHABILITATION]
- Relevance: **High**

---

## Category 4: Elderly Care / ADL / Caregiving

### P7 — SCOPE CAVEAT (wheeled robot, not bipedal)
**Socially Pertinent Robots in Gerontological Healthcare (SPRING Project)**
- Authors: Alameda-Pineda X et al. (44 authors; H2020 SPRING project consortium)
- Year: 2024 (submitted Apr 2024; revised Sep 2025)
- Venue: arXiv preprint (cs.RO / cs.AI / cs.HC)
- ID/URL: https://arxiv.org/abs/2404.07560
- Summary: Empirical evaluation of a robot deployed in a Parisian geriatric day-care facility with 60+ older adult end-users. Measures acceptability (AES) and usability (SUS); finds users receptive when robot perception is robust. Real-world deployment data.
- Note: **PLATFORM VERIFIED: ARI robot by PAL Robotics — wheeled differential drive, NOT bipedal.** Described in paper as "full-sized humanoid" but fails our bipedal scope definition. Retained only as evidence for human-form social robot deployment in healthcare; must NOT be cited as bipedal humanoid. Cite with explicit scope caveat.
- Tags: [ELDERLY-CARE] [NON-BIPEDAL-CAVEAT]
- Relevance: **Medium** (downgraded from High; out of scope for bipedal humanoid claims)

### P8
**Humanoid Robot RHP Friends: Seamless Combination of Autonomous and Teleoperated Tasks in a Nursing Context**
- Authors: Benallegue M et al. (18 authors; CNRS-AIST JRL)
- Year: 2024 (submitted Dec 2024; revised Jan 2025)
- Venue: IEEE Robotics and Automation Magazine (accepted/in press)
- ID/URL: https://arxiv.org/abs/2412.20770
- Summary: RHP Friends humanoid robot combining autonomous and teleoperated modes for nursing tasks; demonstrated at 2023 International Robot Exhibition performing patient transfer (routine) and circuit breaker operation (non-routine). Combines locomanipulation, multi-contact motion, and object detection for care context.
- Tags: [ELDERLY-CARE] [HRI-CLINICAL]
- Relevance: **High**

### P9
**Perceptions of Humanoid Robots in Caregiving: A Study of Skilled Nursing Home and Long Term Care Administrators**
- Authors: Imtiaz R, Khan A
- Year: 2024 (submitted Jan 2024)
- Venue: arXiv preprint (cs.RO / cs.HC)
- ID/URL: https://arxiv.org/abs/2401.02105
- Summary: Survey of 269 nursing home executives on humanoid robot deployment for elderly care; finds potential in resident engagement and staff support, with cost, reduced human contact, and unproven effectiveness as barriers. Provides implementation recommendations.
- Tags: [ELDERLY-CARE] [HRI-CLINICAL]
- Relevance: **Medium**

### P10
**User-Centered Design of Socially Assistive Robot with Non-Immersive VR for Older Adults in Long Term Care**
- Authors: Ghosh R, Khan N, Migovich M, Tate JA, Maxwell C, Latshaw E, Newhouse P, Scharre DW, Tan A, Colopietro K, Mion LC, Sarkar N
- Year: 2024 (submitted Oct 2024)
- Venue: arXiv preprint (cs.HC / cs.RO)
- ID/URL: https://arxiv.org/abs/2410.21197
- Summary: User-centered design study combining NAO humanoid and VR for non-pharmacological apathy management in long-term care; four interactive activities tested with 14 participants, demonstrating caregiver usability improvements.
- Note: NAO is small humanoid; used specifically for humanoid form factor.
- Tags: [ELDERLY-CARE] [HRI-CLINICAL]
- Relevance: **Medium**

---

## Category 5: Hospital Logistics / Navigation

*No qualifying papers found for humanoid-specific hospital logistics in 2022–2026. Zero results.*

---

## Category 5.5: Clinical Support / Data Collection

*No qualifying papers found for humanoid robots performing clinical data collection, documentation, or administrative support tasks in 2022–2026. Zero results. (Searched: humanoid robot clinical documentation, patient data collection, EHR interaction, ward rounds assistance.)*

---

## Category 6: Human-Robot Interaction in Clinical Settings

### P11
**A Brief Wellbeing Training Session Delivered by a Humanoid Social Robot: A Pilot RCT**
- Authors: Robinson N, Connolly J, Suddrey G, Kavanagh DJ
- Year: 2023 (submitted Aug 2023)
- Venue: arXiv preprint (cs.HC / cs.RO)
- ID/URL: https://arxiv.org/abs/2308.06435
- Summary: Pilot RCT (n=230) of autonomous humanoid robot delivering mindful breathing technique to subclinical population. 53% recruitment uptake; moderate enjoyment/perceived usefulness; establishes feasibility baseline for robot-delivered wellbeing interventions.
- Note: Robot model not disclosed; not in a clinical patient population.
- Tags: [HRI-CLINICAL]
- Relevance: **Medium**

### P12
**A Socially Assistive Robot using Automated Planning in a Paediatric Clinical Setting**
- Authors: Lindsay A, Ramirez-Duque A, Petrick RPA, Foster ME
- Year: 2022 (submitted Oct 2022)
- Venue: arXiv preprint (cs.RO / cs.HC)
- ID/URL: https://arxiv.org/abs/2210.09753
- Summary: Automated planning system for a social robot assisting children during difficult medical procedures, adapting to child emotional state while maintaining safe multi-stakeholder clinical interaction.
- Note: Robot model not specified; not confirmed bipedal. Included for clinical context relevance.
- Tags: [HRI-CLINICAL]
- Relevance: **Medium** (conditional on robot platform confirmation)

---

## Category 7: Safety / Compliance for Medical Humanoid Use

### P13
**GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction**
- Authors: Lu Q, Feng Y, Shi B, Piseno M, Bao Z, Liu CK (Stanford)
- Year: 2025 (submitted Nov 2025)
- Venue: arXiv preprint (cs.RO)
- ID/URL: https://arxiv.org/abs/2511.04679
- Summary: Spring-based unified compliance framework for Unitree G1 enabling safe physical contact including gentle hugging, sit-to-stand assistance, and object manipulation. Reduced peak contact forces vs. rigid control; directly relevant to ADL/elderly care and safe physical HRI.
- Note: Not clinically scoped, but findings directly applicable to humanoid deployment in care settings.
- Tags: [SAFETY] [ELDERLY-CARE]
- Relevance: **Medium**

---

## Mental Health / Social Interaction

### P14
**Technology-assisted Journal Writing for Improving Student Mental Wellbeing: Humanoid Robot vs. Voice Assistant**
- Authors: Sayis B, Gunes H
- Year: 2024 (submitted Mar 2024)
- Venue: arXiv preprint (cs.HC)
- ID/URL: https://arxiv.org/abs/2403.05083
- Summary: Compares humanoid robot vs. voice assistant for therapeutic journal writing (n=42 university students); only robot condition showed mood improvements, higher self-disclosure, and positive perception over time. Evidence for embodied robot superiority in mental health/wellbeing applications.
- Note: Educational/wellness population, not clinical; robot model unspecified.
- Tags: [HRI-CLINICAL]
- Relevance: **Medium** (borderline — educational not clinical setting)

---

## Key Findings for Review Paper

1. **Field is very sparse**: Only 14 qualifying papers found across 2022–2026. This is itself a major contribution of our review — it confirms the gap identified in Task 1.0.

2. **Strongest cluster**: Three papers from UCSD Yip Lab (P1, P2) and Johns Hopkins (P3) represent the highest-quality novel clinical work with full-scale humanoids. These form the core of Section 4.1.

3. **Zero papers for**: Chinese platforms (Fourier GR-1, UBTECH Walker, AgiBot, NOETIX) in medical contexts; Boston Dynamics Atlas, Figure AI, Apptronik Apollo, Sanctuary AI in any healthcare context; hospital logistics with humanoids.

4. **Rehabilitation pipeline is thin**: Only 2 directly qualifying papers (P5, P6); GentleHumanoid (P13) is safety-focused but has care relevance.

5. **Elderly care**: RHP Friends (P8) is the strongest example of bipedal humanoid deployment in nursing care. SPRING project (P7) used the ARI wheeled robot (PAL Robotics) — retained with scope caveat; cannot be cited as bipedal humanoid evidence.

6. **Most "humanoid robot + healthcare" results are NAO/Pepper**: Largely excluded per scope rules. This confirms our novelty claim — research on modern full-scale humanoids in clinical settings barely exists.

---

## Excluded Papers (with reasons)
- arXiv:2601.17287 (Chen & Bian 2026) — NAO, wheeled, healthcare mention generic
- arXiv:2511.06036 (Hizeh et al. 2025) — Review/survey paper
- arXiv:2602.20362 (Kirschner et al. 2026) — Industrial robot safety, no healthcare application
- arXiv:2512.07765 (Cardona et al. 2025) — Review of physical HRI frameworks, no medical application
- arXiv:2507.05773 (Boguslavskii et al. 2025) — Healthcare as generic future mention only
- arXiv:2407.12189 (Purushottam et al. 2024) — Wheeled humanoid; healthcare brief mention only
- arXiv:2602.10942 (Taheri et al. 2026) — Elephant-shaped robot, not humanoid
- arXiv:2407.12014 (Yang et al. 2024) — NAO in autism classroom, educational not clinical
- arXiv:2512.12208 (Bhattacharjee et al. 2025) — Emotion recognition with NAO, not clinical intervention
