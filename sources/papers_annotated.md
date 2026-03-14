# Task 1.1 — Annotated Paper Summaries

> 14 papers total. High-relevance papers have extended summaries. Medium/borderline have standard 2–3 sentence summaries.
> All section placement recommendations are provisional — reviewer may adjust.

---

## PRIORITY SOURCE

### P1 — Atar et al. 2025 [CLINICAL-PROCEDURE] — High
**Humanoids in Hospitals: A Technical Study of Humanoid Robot Surrogates for Dexterous Medical Interventions**
*Atar S, Liang X, Joyce C, Richter F, Wood R, Goldberg C, Suresh P, Yip MC — UC San Diego*
arXiv:2503.12725

**Extended Summary:**
This paper is the most directly relevant work in the current literature and warrants prominent treatment in Sections 3, 4, and 5. The authors address a concrete framing of the humanoid healthcare opportunity: the global shortage of healthcare workers (WHO projects a deficit of 10 million by 2030) and the need for systems that can operate in existing clinical environments without infrastructure modification. Their technical contribution is a bimanual teleoperation system built atop the Unitree G1 humanoid, integrating Inspire Gen4 dexterous hands (4-finger, 12 DOF each), bilateral impedance control for compliant tool grasping, and real-time motion retargeting from operator hand motion to robot end-effectors.

The evaluation spans seven clinical procedures spanning a meaningful range of complexity: (1) cardiac and pulmonary auscultation (stethoscope placement), (2) respiratory assistance (bag-valve mask ventilation), (3) Leopold maneuvers (fetal position assessment), (4) otoscopic examination, (5) IV/intravenous catheter insertion, (6) point-of-care ultrasound (POCUS), and (7) blood glucose finger-stick testing. Non-clinician operators achieved approximately 70% procedural success across tasks in controlled lab conditions. Auscultation and ultrasound yielded the strongest results; IV insertion and finger-stick testing were most challenging due to force precision requirements. The paper identifies two specific technical gaps for clinical translation: (a) insufficient force output in the current actuator configuration for procedures requiring high grip forces, and (b) sensor sensitivity limitations in tactile feedback loops needed for fine manipulation. No human subjects were involved; a clinical simulator and mannequin were used.

**Significance for our paper:** This is the first study to systematically evaluate a modern commercial humanoid (Unitree G1) on an operationally meaningful suite of clinical tasks with quantified success rates. It provides the empirical anchor for our argument that humanoid robots can plausibly enter the clinical procedure space, while its documented gaps directly inform Section 5 (technical challenges). It should be cited in the introduction as the leading example of current capability, in Section 3 when describing the Unitree G1, in Section 4.1 as the primary reference for clinical procedure work, and in Section 5 on force control and sensing challenges.

---

## HIGH-RELEVANCE PAPERS

### P2 — Liang et al. 2025 [CLINICAL-PROCEDURE] — High
**LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy**
*Liang Z, Liang X, Atar S, Das S, Chiu Z, Zhang P, Joyce C, Richter F, Liu S, Yip MC — UC San Diego*
arXiv:2510.03529

This paper from the same UCSD Yip Lab extends humanoid clinical teleoperation to laparoscopic surgery — a significantly more demanding manipulation context. The key technical contribution is an inverse-mapping strategy that adapts the humanoid robot's arm kinematics to control manual-wristed laparoscopic instruments while enforcing remote center-of-motion (RCM) constraints at the trocar site, a safety requirement for all abdominal laparoscopy. The authors validate the framework through user studies and position it explicitly as a path toward surgical access in geographically underserved settings where specialist surgeons are unavailable. The paper establishes that humanoid form factor (two anthropomorphic arms at human height) maps naturally to the ergonomic conventions of laparoscopic surgery. Section placement: Sec. 4.1 (clinical procedures) and Sec. 5 (manipulation challenges, safety).

### P3 — Cho et al. 2026 [CLINICAL-PROCEDURE] — High
**Humanoid Robots as First Assistants in Endoscopic Surgery**
*Cho SM, Mangulabnan JE, Zhang H, Mao Z, He Y, Guo P, Xu D, Hager G, Ishii M, Unberath M — Johns Hopkins University*
arXiv:2602.24156

The most recent and clinically significant paper in this search: a proof-of-concept in which a teleoperated Unitree G1 humanoid acts as first assistant providing endoscopic visualization during an actual cadaveric sphenoidectomy (sinus surgery) performed by an attending otolaryngologist. This is, to our knowledge, the first use of a modern commercial humanoid in a real surgical procedure, even if teleoperated and on a cadaver. The authors document specific engineering targets required for clinical translation (endoscope stability, force compliance, autonomous scope positioning) and identify autonomous diagnostic scoping — where the humanoid independently navigates an endoscope through anatomical cavities — as the most tractable near-term autonomous capability. Section placement: Sec. 4.1 (most prominent citation alongside P1), Sec. 6 (discussion of near-term autonomy roadmap).

### P5 — Nguyen et al. 2024 [REHABILITATION] — High
**Exploring EEG Responses during Observation of Actions Performed by Human Actor and Humanoid Robot**
*Nguyen AT, Anand A, Johnson MJ — IEEE BioRob 2024, pp. 1795–1801*
arXiv:2506.10170

Pilot neuroimaging study examining whether observing a humanoid robot performing actions activates the same sensorimotor (mirror neuron system) circuits as observing a human — a foundational question for action observation therapy (AOT) in stroke rehabilitation. EEG recordings from healthy participants show common neural response patterns during humanoid robot observation comparable to human observation, providing neuroscientific grounding for the use of humanoid robots as rehabilitation movement demonstrators. The humanoid form specifically (as opposed to non-humanoid robots) is theorized to be the mechanistic basis for this effect, making this directly relevant to our argument about form-factor importance. Section placement: Sec. 4.3 (rehabilitation) and Sec. 2.2 (form factor rationale).

### P6 — Sobrepera et al. 2022 [REHABILITATION] — High
**Feasibility and Acceptability of Remote Neuromotor Rehabilitation via Social Robot Augmented Telepresence**
*Sobrepera MJ, Lee VG, Garg S, Johnson MJ*
arXiv:2202.13433

Earliest qualifying paper in the set. Develops a Social Robot Augmented Telepresence (SRAT) system combining a humanoid robot (head, arms, face) with mobile telepresence to enable remote neuromotor rehabilitation. Case series with 6 participants (3 adult stroke survivors, 3 pediatric typically developing); 5/6 rated SRAT superior to standard video telepresence for therapeutic interaction, citing the physical embodiment and expressive capacity of the humanoid as key differentiators. The paper frames the humanoid component as essential for conveying movement demonstrations and emotional cues that text/video cannot replicate. Section placement: Sec. 4.3 (rehabilitation telehealth).

### P7 — Alameda-Pineda et al. 2024 [ELDERLY-CARE] — Medium (SCOPE CAVEAT: wheeled robot)
**Socially Pertinent Robots in Gerontological Healthcare (SPRING Project)**
*Alameda-Pineda X et al. (44 authors; H2020 SPRING project)*
arXiv:2404.07560

**Platform verified: ARI robot by PAL Robotics — wheeled (differential drive), NOT bipedal.** Despite being described as "full-sized humanoid" in the paper, ARI does not meet our bipedal scope definition. Must NOT be cited as evidence of bipedal humanoid deployment.

Large-scale EU H2020 project deploying the ARI wheeled social robot in a real geriatric day-care facility in Paris with over 60 older adult participants. The paper reports acceptability (AES) and usability (SUS) evaluation data; results indicate positive user reception when robot perception (speech, face recognition, navigation) is sufficiently robust. The human-form and eye-level conversational capability were cited by end-users as important for dignified interaction — this finding remains relevant to our form-factor argument (Sec. 2.2) but must be cited with explicit platform caveat. Relevance downgraded from High to Medium. Section placement: Sec. 4.2 supporting citation (with caveat) or Sec. 2.5 (non-humanoid alternatives comparison); NOT as primary bipedal humanoid deployment evidence.

### P8 — Benallegue et al. 2024 [ELDERLY-CARE / HRI-CLINICAL] — High
**Humanoid Robot RHP Friends: Seamless Combination of Autonomous and Teleoperated Tasks in a Nursing Context**
*Benallegue M et al. (18 authors; CNRS-AIST JRL)*
IEEE Robotics and Automation Magazine (in press) / arXiv:2412.20770

From CNRS-AIST — one of the longest-running humanoid robotics programs globally. RHP Friends is designed specifically for nursing contexts, combining autonomous navigation and object interaction with teleoperation for non-routine tasks. Demonstrated at the 2023 International Robot Exhibition performing patient transfer (routine, autonomous) and circuit breaker operation (non-routine, teleoperated). The paper's architecture — treating autonomous and teleoperated modes as seamlessly interchangeable — directly maps to our "semi-autonomous assistant under clinical supervision" thesis. Section placement: Sec. 3.2 (academic platforms), Sec. 4.2 (nursing/elderly care), Sec. 6.2 (promising near-term roles).

---

## MEDIUM-RELEVANCE PAPERS

### P4 — Yuan et al. 2025 [ELDERLY-CARE / LLM-HUMANOID] — Medium
**Integrating RL and AI Agents for Adaptive Robotic Interaction in Dementia Care**
*Yuan F et al.*
arXiv:2501.17206

Proposes combining Pepper humanoid robot, reinforcement learning, and large language models for adaptive personalized dementia care. The LLM-based behavior simulation and probabilistic cognitive-emotional state modeling address the data scarcity problem in training caregiving agents for dementia patients. Although Pepper is a wheeled platform (not fully bipedal), the paper's LLM+humanoid integration framework and dementia application domain are directly relevant to Section 4.4 (mental health / social interaction) and Section 2.3 (LLM integration paradigm). Cite with explicit note on platform limitations.

### P9 — Imtiaz & Khan 2024 [ELDERLY-CARE / HRI-CLINICAL] — Medium
**Perceptions of Humanoid Robots in Caregiving: Nursing Home and Long Term Care Administrators**
*Imtiaz R, Khan A*
arXiv:2401.02105

Survey of 269 nursing home and long-term care administrators about humanoid robot deployment for elderly care. Administrators identify potential in resident engagement and staff support, but cite cost, reduction in human contact, and unproven effectiveness as primary barriers. Provides stakeholder perspective data that complements technical papers; useful for Section 5.3 (trust and HRI) and Section 6.5 (ethical considerations) as evidence that deployment barriers are institutional and perceptual, not only technical.

### P10 — Ghosh et al. 2024 [ELDERLY-CARE / HRI-CLINICAL] — Medium
**User-Centered Design of Socially Assistive Robot + VR for Older Adults in Long Term Care**
*Ghosh R et al.*
arXiv:2410.21197

User-centered design study combining NAO humanoid and VR for non-pharmacological apathy management in long-term care residents. Despite using the small NAO platform, the explicit use of humanoid form as a design rationale and the iterative co-design methodology with care facility staff make this relevant for Section 4.2 and Section 5.3 discussions of user acceptance and design process.

### P11 — Robinson et al. 2023 [HRI-CLINICAL] — Medium
**A Brief Wellbeing Training Session Delivered by a Humanoid Social Robot: A Pilot RCT**
*Robinson N et al.*
arXiv:2308.06435

Pilot RCT (n=230) with an autonomous humanoid robot delivering a mindful breathing intervention to a subclinical general population. 53% approached agreed to participate; most found the experience enjoyable and moderately useful. Notable for being a randomized controlled trial design — methodologically stronger than most HRI studies. Relevant to Section 4.4 (mental health / wellbeing) as evidence that people are willing to engage with autonomous humanoid robots for health-relevant interactions. Cite with caveat: subclinical population, not a diagnosed clinical group.

### P12 — Lindsay et al. 2022 [HRI-CLINICAL] — Medium
**A Socially Assistive Robot using Automated Planning in a Paediatric Clinical Setting**
*Lindsay A et al.*
arXiv:2210.09753

Automated planning framework for a social robot assisting children during stressful medical procedures. Adapts behavior dynamically to child emotional state and manages interaction with multiple stakeholders (child, parent, clinician) simultaneously. Relevant to Section 4.4 and Section 5.3 for its multi-stakeholder HRI model in a genuine clinical environment. Robot platform not confirmed as bipedal; cite with note pending platform verification.

### P13 — Lu et al. 2025 [SAFETY / ELDERLY-CARE] — Medium
**GentleHumanoid: Learning Upper-body Compliance for Contact-rich Interaction**
*Lu Q, Feng Y, Shi B, Piseno M, Bao Z, Liu CK — Stanford*
arXiv:2511.04679

Compliance framework for the Unitree G1 enabling safe physical contact including sit-to-stand assistance, gentle hugging, and object manipulation. Sit-to-stand is one of the most clinically impactful ADL assistance tasks (fall prevention, post-operative recovery). Reduced peak contact forces vs. rigid control is quantified. Cite in Section 5.1 (safety, force control) and Section 4.3 (rehabilitation/ADL) as a technical enabler for physical assistance tasks.

### P14 — Sayis & Gunes 2024 [HRI-CLINICAL] — Medium
**Technology-assisted Journal Writing: Humanoid Robot vs. Voice Assistant**
*Sayis B, Gunes H*
arXiv:2403.05083

Comparative study (n=42) showing that only the humanoid robot condition (vs. voice-only) produced mood improvements, increased self-disclosure, and positive perception change over time for therapeutic journal writing. Provides direct comparative evidence that physical embodiment matters for mental health interactions — useful evidence for the form-factor argument in Section 2.2. Cite with caveat: educational/wellness population, not clinical; robot model unspecified.

---

## Summary Table

| ID | First Author | Year | Platform | Domain | Relevance | Section |
|----|-------------|------|----------|--------|-----------|---------|
| P1 | Atar | 2025 | Unitree G1 | Clinical procedure (7 tasks) | High | 3,4,5 |
| P2 | Liang Z | 2025 | Unitree G1 | Laparoscopic surgery | High | 4,5 |
| P3 | Cho | 2026 | Unitree G1 | Endoscopic surgery | High | 4,6 |
| P4 | Yuan | 2025 | Pepper | Dementia care + LLM | Medium | 4,2 |
| P5 | Nguyen | 2024 | Unspecified humanoid | Stroke rehabilitation (EEG) | High | 4,2 |
| P6 | Sobrepera | 2022 | Humanoid telepresence | Remote neuromotor rehab | High | 4 |
| P7 | Alameda-Pineda | 2024 | ARI (PAL Robotics, **wheeled**) | Gerontological care | Medium* | 2.5,4 |
| P8 | Benallegue | 2024 | RHP Friends (CNRS-AIST) | Nursing tasks | High | 3,4,6 |
| P9 | Imtiaz | 2024 | N/A (survey) | Admin perceptions | Medium | 5,6 |
| P10 | Ghosh | 2024 | NAO | Elderly care/VR | Medium | 4,5 |
| P11 | Robinson | 2023 | Unspecified humanoid | Wellbeing RCT | Medium | 4 |
| P12 | Lindsay | 2022 | Unspecified | Paediatric clinical | Medium | 4,5 |
| P13 | Lu | 2025 | Unitree G1 | Compliance/safety | Medium | 5,4 |
| P14 | Sayis | 2024 | Unspecified humanoid | Mental health | Medium | 4,2 |
