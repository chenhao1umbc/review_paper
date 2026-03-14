# Clinical Trials & Hospital Pilots — Humanoid Robots in Healthcare

> Research notes for ACM Computing Surveys paper on humanoid robots in healthcare.
> Compiled: 2026-03-10.
> Scope note: "humanoid" in this file means a robot with a recognizably human-form body — head, torso, two arms. We distinguish bipedal (legs; free-standing locomotion) from wheeled-humanoid (human-form upper body, wheeled base). We further distinguish clinical trial (IRB-approved protocol, patient subjects, outcomes tracked) from research demonstration and hospital deployment/pilot.

---

## 1. ClinicalTrials.gov Search Results

### 1.1 Search Strategy

Searches conducted 2026-03-10 via ClinicalTrials.gov API v2:
- Query: `humanoid robot`
- Query: `NAO robot`
- Query: `Pepper robot` + healthcare
- Query: `social robot hospital clinical`
- Query: `Unitree medical`

Results below exclude trials where "robot" refers to robotic surgery (da Vinci system), exoskeletons, or rehabilitation robots that are not humanoid-form.

### 1.2 NAO Robot Trials (most-studied humanoid platform)

NAO (SoftBank Robotics, 58 cm, bipedal, 25 DOF) is the humanoid platform with the largest number of registered clinical trials. All confirmed NAO trials involve small-form humanoid interaction for therapy or assessment, not clinical procedures.

| NCT ID | Title | Condition | Status | N | Dates |
|---|---|---|---|---|---|
| NCT03323931 | DREAM Project: Robot-Enhanced Therapy for ASD | Autism Spectrum Disorder | Completed | 70 | 2017–2018 |
| NCT06181864 | Emotional Regulation for Anxiety/Anger in Autism | Autism Spectrum Disorder | Recruiting | 40 | 2023–2025 |
| NCT06278155 | Enhancing Social Relations: NAO vs. Therapist for ASD | Autism Spectrum Disorder | Recruiting | 60 | 2023–2025 |
| NCT07283211 | NAO-Assisted Occupational Therapy for Cerebral Palsy | Cerebral Palsy, ADL | Completed | 15 | 2024 |
| NCT06948227 | Social Robots for ADL Training in Cerebral Palsy | Cerebral Palsy | Not yet recruiting | 30 | Est. 2025 |
| NCT07426328 | NAO for Developmental Language Disorder (RCT) | Developmental Language Disorder | Enrolling by invitation | 50 | 2025–2026 |
| NCT05835856 | e-VITA: Virtual Coach with NAO for Elderly (EU-Japan) | Older Adults, Quality of Life | Active, not recruiting | 240 | 2023–2024 |
| NCT07002411 | HOSPER: NAO/Pepper for Hospital Reception (Italy) | Quality of Hospital Reception | Recruiting | 200 | 2024–2025 |
| NCT03314415 | NAO for Weight Loss Engagement | Obesity | Withdrawn | 0 | Never started |

**Important notes on NAO trials:**
- NAO is 58 cm tall — it is bipedal and humanoid in form, but it is a small-scale social robot, not a full-size clinical assistant
- All NAO trials involve therapeutic interaction (HRI, engagement, instruction-following) — none involve clinical procedures, physical patient care tasks, or diagnostic operations
- DREAM (NCT03323931) is the largest completed RCT: 70 children with ASD, NAO vs. standard behavioral therapy for social skills development; completed 2018
- NCT05835856 (e-VITA) has the largest enrollment (N=240) and most clinically meaningful patient population (elderly adults, active aging) but is a virtual coaching study — NAO is one component of a digital platform
- NCT07002411 (HOSPER) is the only registered trial deploying NAO (and Pepper) in a hospital building — specifically for entrance reception and wayfinding, not for patient care

### 1.3 Pepper Robot Trials

Pepper (SoftBank Robotics, 120 cm, wheeled base, human-form upper body) — classified as wheeled-humanoid, not bipedal. Included here because it is frequently described as "humanoid" in the clinical literature.

| NCT ID | Title | Condition | Status | N | Dates |
|---|---|---|---|---|---|
| NCT05788133 | Humanoid Robot for Neuropsychological Assessment and Cognitive Training | Neurodegenerative Diseases, Stroke | Completed | 65 | 2022 |
| NCT07404410 | RAPHAel: Robotic Technologies for Apathy in Dementia (RCT) | Apathy, Dementia | Not yet recruiting | 75 | Est. 2026 |
| NCT03756194 | CARESSES: Culture-Aware Robot for Elderly Support | Aging | Unknown (last: Recruiting) | 90 | 2019–2020 |
| NCT07002411 | HOSPER: NAO/Pepper for Hospital Reception | Hospital Reception | Recruiting | 200 | 2024–2025 |
| NCT05991791 | I-ROBI: Individualized Robot Interactions for ASD | Autism Spectrum Disorder | Unknown | 8 | 2023–2025 |

**Notes on Pepper trials:**
- NCT05788133: The only completed trial using Pepper for a clinical assessment function (neuropsychological evaluation and cognitive training in neurodegeneration/stroke patients); N=65; completed in one quarter (fast pilot study)
- NCT07404410 (RAPHAel): An RCT for dementia apathy — the highest-quality design in the Pepper trial list; not yet started as of March 2026
- CARESSES (NCT03756194): Multicenter (UK, India, Japan); culture-aware companion robot for elderly; primary outcome was psychological wellbeing, not clinical function
- None of the Pepper trials involve physical patient care tasks (transfer, medication administration, wound care) — all involve social/cognitive interaction

### 1.4 Humanoid Robot (General Term) Trials

Searching ClinicalTrials.gov for "humanoid robot" returns studies primarily using NAO and Pepper (covered above). No trial matching "full-size bipedal humanoid robot" in a clinical procedure or physical care context was found in the registry as of 2026-03-10.

### 1.5 Unitree + Medical / Hospital

No registered clinical trials found on ClinicalTrials.gov for Unitree robots (G1, H1, or B series) in any medical or healthcare context as of 2026-03-10. Unitree G1 medical use is documented only in research publications (arXiv preprints), not registered clinical studies.

### 1.6 Summary: ClinicalTrials.gov Findings

- **Zero registered clinical trials** involving full-size (≥150 cm) bipedal humanoid robots in any clinical procedure, physical patient care, or diagnostic application
- All registered humanoid robot trials involve small-form (NAO, 58 cm) or wheeled-humanoid (Pepper, 120 cm) platforms
- All registered trials are in the HRI/social/cognitive therapy domain — not physical care tasks
- Largest completed RCT: DREAM (NCT03323931, N=70, NAO for ASD therapy)
- Most clinically significant active trial: RAPHAel (NCT07404410, N=75, Pepper for dementia apathy, RCT design; not yet started)

---

## 2. Research Demonstrations in Healthcare Settings

These are documented deployments from peer-reviewed sources in our paper collection. They are NOT clinical trials. They represent the state of the art for humanoid robots in real clinical or care environments.

### 2.1 SPRING Project — ARI Robot, Paris (P7)

**Reference:** Alameda-Pineda X et al., arXiv:2404.07560 (EU H2020 SPRING project, 2020–2024)

**Platform:** ARI (PAL Robotics) — CRITICAL SCOPE NOTE: ARI is a wheeled differential-drive robot with a human-form upper body. It is NOT bipedal. Despite being described as "full-sized humanoid" in some contexts, ARI does not meet our bipedal humanoid scope criterion.

**Setting:** Real geriatric day-care facility, Paris (Île-de-France region); continuous deployment over multiple sessions across the 4-year EU project

**Users:** 60+ older adult participants (patients attending day-care sessions)

**Tasks:** Social interaction, orientation/wayfinding assistance, scheduled activity facilitation, multi-party conversation in waiting areas

**Methodology:** Participatory design with end-users; iterative deployment; evaluation using Assistive Experience Scale (AES) and System Usability Scale (SUS)

**Key findings:** Positive user reception when perception (speech recognition, face recognition, navigation) performed reliably; human-form and eye-level conversational positioning cited by users as important for dignified interaction; technology failures (speech misrecognition, navigation errors in crowded spaces) were primary negative experience drivers

**Status:** Largest real-world social robot deployment in a healthcare facility found in our full literature search. Included in our paper with explicit platform caveat (wheeled, not bipedal). Most relevant for Section 2.5 (non-humanoid alternatives) and Section 4.2 (elderly care, supporting citation with scope note). Must NOT be cited as evidence of bipedal humanoid deployment.

**Funding:** EU H2020 programme, grant no. 871245

---

### 2.2 RHP Friends — IREX 2023, Tokyo (P8)

**Reference:** Benallegue M et al., arXiv:2412.20770; IEEE Robotics and Automation Magazine (in press, 2025)

**Platform:** RHP Friends — CNRS-AIST Joint Robotics Laboratory bipedal humanoid; 168 cm height, ~80 kg, 30 DOF; developed jointly by CNRS, AIST, and Kawasaki Heavy Industries (KHI); designed specifically for nursing assistance contexts

**Setting:** International Robot Exhibition (IREX) 2023, Tokyo — public exhibition event, not a clinical facility; demonstration booth in exhibition hall

**Duration:** 3 live demonstration days

**Users/observers:** Exhibition visitors (general public and robotics professionals); no patients involved

**Tasks demonstrated:**
- Patient transfer: autonomous grasping and repositioning of mannequin from bed to chair and reverse
- Routine physical tasks: walking to patient bedside, handing objects
- Non-routine task (teleoperated): operating a circuit breaker (requiring precise manipulation); a healthcare scenario where an emergency task arises mid-care

**Architecture:** Seamlessly interchangeable autonomous and teleoperated modes; the paper's core contribution is demonstrating that clinical tasks can be partitioned into routine (autonomous) and non-routine (teleoperated) without user-visible mode transitions

**Status:** Academic demonstration only — not a clinical trial, not a hospital deployment. No patients. No IRB protocol. However, it is the most directly nursing-task-relevant demonstration of a purpose-built bipedal humanoid in a structured setting found in our literature search.

**Significance:** RHP Friends is the only academic humanoid platform designed with nursing as the explicit primary application domain, and IREX 2023 is the only structured demonstration of bipedal humanoid patient-transfer tasks found in our search. Sections 3.2, 4.2, and 6.2.

---

### 2.3 Unitree G1 — Clinical Procedure Study, UCSD (P1)

**Reference:** Atar S et al., arXiv:2503.12725 (UC San Diego, Yip Lab, 2025)

**Platform:** Unitree G1 — commercial bipedal humanoid (127 cm, 35 kg, 23 DOF); fitted with Inspire Gen4 dexterous hands (4-finger, 12 DOF each) for this study

**Setting:** Controlled laboratory environment, UC San Diego; clinical mannequins and simulators used; no human patients

**Procedures tested (7 total):**
1. Cardiac and pulmonary auscultation (stethoscope placement)
2. Respiratory assistance (bag-valve mask ventilation)
3. Leopold maneuvers (fetal position assessment)
4. Otoscopic examination
5. IV/intravenous catheter insertion
6. Point-of-care ultrasound (POCUS)
7. Blood glucose finger-stick testing

**Operator:** Non-clinician operators using bimanual teleoperation system with impedance control and motion retargeting

**Results:** Approximately 70% aggregate procedural success rate; auscultation and ultrasound yielded strongest performance; IV insertion and finger-stick most challenging (force precision requirements)

**Status:** Research prototype in controlled lab. Not a clinical trial. No human subjects. No IRB patient protocol. Not CE-marked or FDA-cleared.

**Significance:** First systematic evaluation of a modern commercial humanoid on a clinically meaningful procedure suite with quantified success rates. Primary evidence for clinical procedure domain in Sections 4.1 and 5.

---

### 2.4 Unitree G1 — Cadaveric Sphenoidectomy, Johns Hopkins (P3)

**Reference:** Cho SM et al., arXiv:2602.24156 (Johns Hopkins University, 2026)

**Platform:** Unitree G1 bipedal humanoid; configured for endoscope holding and positioning

**Setting:** Surgical cadaver laboratory, Johns Hopkins University; fresh cadaver specimen; procedure performed by attending otolaryngologist

**Procedure:** Bilateral sphenoidectomy (endoscopic sinus surgery) with humanoid G1 acting as first assistant — holding and positioning the endoscope under the surgeon's direction via teleoperation

**Outcome:** Successful completion of bilateral procedure; endoscope stability and positioning assessed; surgeon rated performance on standardized scale

**Status:** Cadaver study — not a clinical trial. No living patients. Cadaver use is a standard surgical research methodology prior to human trials. Closest existing work to a pre-clinical evaluation of humanoid surgical assistance.

**Significance:** First documented use of a modern commercial bipedal humanoid in an actual surgical procedure context (cadaveric). Establishes proof of concept for humanoid-as-first-assistant in endoscopic surgery. Section 4.1 (primary citation alongside P1).

---

## 3. Hospital and Clinic Announcements — Institutional Pilots

Search conducted 2026-03-10 for press releases, hospital news, and announcements of humanoid robot pilots in major health systems.

### 3.1 Findings by Institution

**Mayo Clinic:** No confirmed humanoid robot pilot or deployment announced as of March 2026. Mayo Clinic Innovation Exchange has listed robotic care as an area of interest, but no humanoid-specific program has been publicly disclosed.

**Cleveland Clinic:** No confirmed humanoid robot deployment. Cleveland Clinic's Digital Innovation Alliance includes AI and robotics, but public announcements reference surgical robotics (da Vinci) and logistics robots, not bipedal humanoids.

**NHS UK:** NHS England published a robotics roadmap (2023) and has piloted autonomous mobile robots (AMRs) for pharmacy and logistics (e.g., TUG robots, Aethon systems). No NHS trust has publicly announced a full-size bipedal humanoid pilot as of March 2026.

**Singapore Health Services (SingHealth):** Singapore has been among the most active health systems in robotics adoption. SingHealth piloted the Moxi (Diligent Robotics) wheeled logistics robot at Changi General Hospital (announced 2022). No bipedal humanoid pilot confirmed.

**Chinese hospital systems:** Keenon and YOGO wheeled delivery robots are widely deployed in Chinese hospitals for medication and specimen transport (multiple systems in operation as of 2023–2024 per Chinese media reports). China has significant investment in humanoid robotics (Fourier, UBTECH, AgiBot, NOETIX) but no confirmed clinical deployment of a full-size bipedal humanoid has been announced by a hospital system as of March 2026.

**Japanese care facilities:** Japan has the world's most active eldercare robot deployment ecosystem, driven by government subsidies (Ministry of Economy, Trade and Industry, METI "Robot Care Equipment" subsidy program). Deployed eldercare robots include PARO (therapeutic seal robot), Pepper (SoftBank, deployed in approximately 2,000 facilities including hospitals), HAL (Hybrid Assistive Limb exoskeleton, CE-marked and MHLW-approved). IREX 2023 demonstrations (including RHP Friends, Section 2.2) reflect Japanese ambition for humanoid nursing assistance, but no care facility has announced operational deployment of a full-size bipedal humanoid. METI roadmap documentation identifies 2030 as the target horizon for nursing-capable humanoid deployment.

**Figure AI:** Announced (2024) partnership discussions with healthcare system(s) for humanoid deployment exploration. No clinical deployment or even formal pilot announced as of March 2026. CEO Brett Adcock has made public statements about long-term healthcare vision but no clinical program has been disclosed.

**1X Technologies (Oslo):** Deployed EVE wheeled-humanoid (arms + wheeled base) in limited office/commercial settings. No healthcare facility pilot announced.

**Apptronik (Apollo):** Announced pilot deployments in warehouse/logistics contexts (Daifuku partnership, 2024). No healthcare pilot.

**Agility Robotics (Digit):** Deployed in Amazon fulfillment centers for logistics. No healthcare pilot.

**UBTECH (Walker X):** UBTECH has demonstrated Walker X in eldercare promotional content (China market) but no IRB-registered study or facility deployment announcement found.

### 3.2 Summary of Institutional Search

No major health system (US, UK, EU, Singapore, Japan, China) has publicly confirmed an operational or formal pilot deployment of a full-size bipedal humanoid robot in a patient care setting as of March 2026.

---

## 4. Honest Findings

### 4.1 Zero Confirmed Phase I/II/III Clinical Trials with Full-Size Bipedal Humanoids

**This is the primary finding of the clinical trials search and is scientifically significant.**

As of 2026-03-10:
- There are zero registered Phase I, II, or III clinical trials on ClinicalTrials.gov involving full-size (≥150 cm) bipedal humanoid robots in any clinical procedure, physical patient care, or diagnostic application
- There are zero equivalent registrations on EU Clinical Trials Register (EU CTR), ISRCTN, or UMIN (Japan) for bipedal humanoid clinical trials (spot-checked)
- The full body of clinical evidence for humanoid robots in healthcare consists entirely of: (a) small-form social robot (NAO, 58 cm) HRI/therapy trials, (b) wheeled-humanoid (Pepper) social interaction trials, and (c) research laboratory demonstrations without patient subjects

### 4.2 The Translation Gap

The evidence landscape reveals a clear stratification:

| Evidence Level | Bipedal Humanoid (≥150 cm) | Small/Wheeled Humanoid |
|---|---|---|
| Phase I–III Clinical Trial | Zero | Multiple (NAO, Pepper) |
| Hospital/Care Facility Deployment | Zero confirmed | Multiple (Pepper: ~2000 JP facilities; SPRING/ARI: 60+ users) |
| Research Lab with Patient Subjects | Zero | Several (NAO therapy studies) |
| Research Lab, Mannequin/Cadaver | 2 studies (P1 UCSD, P3 JHU) | Multiple |
| Public Demonstration (non-clinical) | 1 event (P8 RHP Friends, IREX 2023) | Many |

The translation gap between laboratory demonstration and clinical trial for full-size bipedal humanoids is total: no clinical trial exists, and no institutional pilot has been formally announced. This gap is itself a key finding: the field is at Technology Readiness Level (TRL) 3–4 for bipedal humanoid clinical tasks — feasibility demonstrated in controlled settings, but no validated clinical pathway exists.

### 4.3 Why the Gap Exists

Contributing factors (substantiated by the regulatory and technical literature):
1. **Regulatory vacuum:** No FDA pathway or EU MDR product code exists for a general-purpose bipedal humanoid clinical assistant (see `sources/regulatory.md`)
2. **Safety infrastructure absent:** No certified collision-avoidance, fall-detection, or patient-contact safety system exists for bipedal humanoids in healthcare settings
3. **Platform maturity:** The leading commercial platforms (Figure 01/02, Unitree G1, 1X NEO) reached prototype-grade reliability only in 2024–2025; they have not yet been validated for clinical environments
4. **Insurance/liability:** No healthcare liability framework exists for robotic autonomous action errors in patient care; this actively deters hospital adoption
5. **Operator interface:** Clinical workflows require real-time teleoperation by skilled operators (or autonomous competence the platforms do not yet have); neither condition is reliably met at scale

### 4.4 Implication for the Paper

The finding of zero bipedal humanoid clinical trials is not a failure of the literature search — it is the central evidentiary finding that motivates the paper. The state of the field as of 2026 is: strong technical feasibility signals (P1, P2, P3, P8) but no clinical translation, no regulatory framework, and no institutional deployment. This TRL 3–4 characterization should anchor Section 6 (Discussion) and is the core justification for a review paper: the field needs a roadmap from where it is to where clinical deployment requires it to be.

---

## 5. Cross-References

- `sources/papers_annotated.md` — detailed annotations for P1, P3, P7, P8 and all other qualifying papers
- `sources/systems_academic.md` — NAO, Pepper, RHP Friends platform details
- `sources/systems_commercial.md` — Unitree G1, Figure, and other commercial platforms
- `sources/regulatory.md` — regulatory gap analysis that explains the absence of cleared systems
