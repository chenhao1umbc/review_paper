# Regulatory Landscape — Humanoid Robots in Healthcare

> Research notes for ACM Computing Surveys paper on humanoid robots in healthcare.
> Compiled: 2026-03-10. Sources: FDA.gov, EU official documents, ISO abstracts, peer-reviewed literature.

---

## 1. FDA (United States)

### 1.1 Is a Humanoid Clinical Assistant a Medical Device?

The threshold question is whether a humanoid robot qualifies as a medical device under the Federal Food, Drug & Cosmetic Act (FD&C Act), Section 201(h). The statutory definition covers any "instrument, apparatus, implement, machine, contrivance" intended to diagnose, treat, prevent, cure, or mitigate disease, or to affect bodily structure or function.

**Intended use is the determinative factor.** A general-purpose humanoid robot sold for logistics or manufacturing is not a medical device. The same physical platform becomes subject to FDA jurisdiction the moment its labeling or marketing claims a medical intended use — e.g., "assists in clinical procedures," "monitors patient vital signs," or "provides therapeutic interaction." This intended-use boundary is not peculiar to robotics; it is the same principle applied to software apps (the FDA's "Mobile Medical Applications" guidance, 2015 and 2019 updates, establishes this explicitly).

For humanoid systems currently in research (Unitree G1 in Atar et al. 2025, arXiv:2503.12725; Unitree G1 in Cho et al. 2026, arXiv:2602.24156), no medical device claims are made by the manufacturer. Both studies are research prototypes operated under investigator responsibility, not cleared/approved devices.

### 1.2 510(k) vs. PMA Pathway

FDA device regulation assigns all devices to three risk classes (I, II, III) with corresponding premarket submission requirements:

| Pathway | Risk Class | Standard | Typical Timeline |
|---|---|---|---|
| Premarket Notification (510(k)) | Class I/II | Substantial equivalence to predicate | 3–6 months |
| De Novo Classification | Class I/II (novel) | No predicate; general/special controls sufficient | 5–12 months |
| Premarket Approval (PMA) | Class III | Clinical data demonstrating safety/effectiveness | 1–3+ years |

**510(k) — Substantial Equivalence:** Requires the submitter to identify a legally marketed predicate device with the same intended use and substantially equivalent technological characteristics. For a humanoid robot performing clinical assistance tasks, finding a valid 510(k) predicate is currently not feasible — there is no legally marketed humanoid robot performing clinical tasks in the US. A submitter would have to construct a multi-device predicate chain (e.g., prior robotic surgical assistants + telepresence systems), which is possible but creates risk of "substantial equivalence" determinations that do not map cleanly.

**De Novo Classification:** The appropriate entry pathway for a novel device type where (a) no predicate exists and (b) risk is moderate rather than high, such that general and special controls (rather than full PMA clinical evidence) suffice. De Novo devices, once cleared, establish new product codes and can serve as predicates for future 510(k) submissions. The FDA's target review window is 150 days (MDUFA IV). For a first-generation humanoid clinical assistant with limited autonomous decision-making (primarily teleoperated), De Novo is the most plausible regulatory entry pathway. FDA has accepted De Novo submissions from exoskeletal rehabilitation devices, surgical planning software, and other robotic-adjacent systems.

**PMA — Premarket Approval:** Required for Class III devices where general and special controls alone are insufficient. Class III applies to devices that (a) sustain or support life, (b) are implanted, or (c) present potential unreasonable risk. A humanoid robot performing autonomous clinical actions (diagnosis, treatment decisions) without consistent human oversight would likely be classified Class III, requiring full PMA with clinical trial evidence. As of 2026, no humanoid has reached this threshold in a commercial context.

**Key factor — autonomy level:** FDA's framework for software-driven devices distinguishes between systems that inform clinical decisions (lower risk) and systems that autonomously execute clinical actions (higher risk). A teleoperated humanoid (human-in-the-loop at all times) presents a substantially different risk profile than an autonomous surgical assistant. Autonomy level directly affects risk class assignment and determines which pathway applies.

### 1.3 21 CFR Part 820 — Quality System Regulation (Design Controls)

21 CFR Part 820 (Quality System Regulation, QSR) governs the design and manufacturing of medical devices. Subpart C (§ 820.30) establishes "design controls" — the most relevant set of requirements for a software-intensive humanoid system. Key requirements under § 820.30:

- **Design Planning (§ 820.30(b)):** Documented plans for each design project; assign responsibilities and interfaces
- **Design Input (§ 820.30(c)):** Translate intended use and user needs into device requirements; document intended patient population, clinical environment, and use conditions
- **Design Output (§ 820.30(d)):** Complete device specifications meeting design input requirements; must be verifiable/reviewable before release
- **Design Review (§ 820.30(e)):** Formal documented reviews at appropriate stages; include personnel with no direct design responsibility
- **Design Verification (§ 820.30(f)):** Confirm design output meets design input requirements (testing, analysis)
- **Design Validation (§ 820.30(g)):** Ensure the device meets user needs and intended uses; must include testing under simulated or actual use conditions; software validation included here
- **Design Transfer (§ 820.30(h)):** Ensure device design is correctly translated into production specifications
- **Design Changes (§ 820.30(i)):** All design changes must be identified, reviewed, verified, validated, and approved before implementation

For a humanoid robot with embedded AI/ML systems, § 820.30(g) design validation is particularly demanding: the intended clinical use environment (a hospital ward, an operating room, a geriatric care facility) must be characterized, and validation testing must demonstrate safe performance in that environment. The FDA's 2023 guidance on Predetermined Change Control Plans (PCCPs) for ML-enabled devices also intersects here — if the robot's AI components are expected to update post-market, a PCCP must be established during the design phase.

**Note on 2022 QSR Harmonization:** FDA issued a final rule in February 2024 harmonizing Part 820 with ISO 13485:2016 (Medical Devices Quality Management Systems), effective February 2026. The revised rule (renumbered as 21 CFR Part 820, Quality Management System Regulation) adopts ISO 13485 terminology and structure while maintaining substantive requirements. This affects the specific section numbering but not the substantive obligations described above.

### 1.4 FDA AI/ML Software as a Medical Device (SaMD) Action Plan (January 2021)

The FDA published its "Artificial Intelligence and Machine Learning Software as a Medical Device Action Plan" in January 2021 to address the regulatory challenge of continuously learning AI systems. The five action areas are:

1. **Good Machine Learning Practice (GMLP):** Guidance on best practices for ML model development, training, and validation. Published as joint FDA/Health Canada/MHRA document in October 2021 (10 guiding principles).
2. **Patient-Centered Approach / Transparency:** AI device labeling and transparency requirements so clinicians and patients understand what an AI device does and its limitations.
3. **Regulatory Science for Algorithm Change:** Framework for when post-market algorithmic changes require new premarket review vs. can proceed under PCCP.
4. **Real-World Performance Monitoring:** Guidance on post-market performance monitoring of AI devices (PCCP final guidance published December 2024).
5. **Advancing a Real-World Evidence Framework:** Standards for using real-world data to evaluate AI/ML device performance.

**Application to humanoid robot AI:** The AI/ML SaMD framework applies specifically to software components of a humanoid clinical assistant. If the humanoid's decision-making (e.g., which patient to approach, how to interpret vital signs, when to escalate) is software-driven and constitutes a "medical device function" (diagnosis, treatment, monitoring), that software component is regulated as SaMD. The robot hardware (actuators, chassis) and the AI software constitute separate regulatory elements that may be reviewed together or separately depending on their design integration.

**Predetermined Change Control Plans (PCCPs):** The December 2024 final guidance on PCCPs is particularly relevant for AI-driven humanoids that use continuous learning or episodic model updates. A PCCP filed with the premarket submission allows specified, pre-approved types of model updates to be implemented post-market without filing a new 510(k) or De Novo — a critical mechanism for deploying learning systems in clinical environments.

### 1.5 FDA Breakthrough Device Designation

The Breakthrough Devices Program (21st Century Cures Act, 2016; codified at 21 CFR § 515B) provides expedited FDA review for devices that provide more effective treatment or diagnosis of life-threatening or irreversibly debilitating diseases, AND meet at least one of: represent breakthrough technology, no approved alternative exists, offer significant advantages over alternatives, or device availability is in patients' best interests.

**Robotics-related Breakthrough Designations (confirmed):**
- **ReWalk P6.0** (ReWalk Robotics) — lower extremity exoskeleton for spinal cord injury; received designation
- **NeurOlutions IpsiHand** — robotic rehabilitation system for upper extremity recovery post-stroke
- **da Vinci X/Xi Surgical Systems** (Intuitive Surgical) — robotic surgical platform

**Humanoid robots:** As of March 2026, no full-size bipedal humanoid robot has received FDA Breakthrough Device Designation. The existing robotics designations are for single-purpose, narrow-function systems — exoskeletons, surgical platforms, and rehabilitation devices — not general-purpose humanoid assistants.

**Implication:** A humanoid robot manufacturer seeking accelerated review could apply for Breakthrough Designation if their device targets a life-threatening condition with no adequate alternative. However, the general-purpose nature of humanoid assistants works against this pathway — Breakthrough Designation favors highly specific device-indication combinations.

### 1.6 De Novo Pathway — Establishing a Regulatory Predicate

The De Novo pathway (21 U.S.C. § 513(f)(2)) is specifically designed for novel device types without a predicate. A successful De Novo classification:
- Results in a Class I or Class II designation (not Class III, unless risk assessment mandates it)
- Establishes a new product code that future similar devices can cite in 510(k) submissions
- Requires the FDA to create special controls specific to the new device type
- Has a target 150-day review timeline (MDUFA IV)

For a humanoid clinical assistant, De Novo represents the most legally defensible initial regulatory approach in the US, as there is no existing 510(k) predicate. The device manufacturer must demonstrate that general controls (QSR/Part 820 compliance, proper labeling) plus any proposed special controls (performance standards, post-market surveillance requirements) provide reasonable assurance of safety and effectiveness.

---

## 2. EU Medical Device Regulation (EU MDR 2017/745)

### 2.1 Overview and Classification System

EU MDR 2017/745 entered into force in May 2017 and applies from May 2021 (with extended transitions). It establishes four risk classes for medical devices:

| Class | Risk Level | Examples |
|---|---|---|
| Class I | Low | Bandages, wheelchairs, non-invasive examination aids |
| Class IIa | Medium-low | Surgical gloves, short-term implants, active therapeutic devices |
| Class IIb | Medium-high | X-ray machines, intensive care equipment, active devices delivering dangerous energy |
| Class III | High | Cardiac stents, implantable pacemakers, joint prostheses |

Classification is governed by 22 rules in Annex VIII, which consider invasiveness, duration of contact, body location, and whether the device is active (powered). For a humanoid robot performing clinical assistance without body entry:

- **As a non-invasive, active device** providing monitoring or physical assistance: likely **Class IIa** under Rule 9 (active devices intended for diagnosis) or Rule 10/11 (active therapeutic devices)
- **As an autonomous surgical instrument** (operating within body cavities): escalates to **Class IIb or III**
- **As a social/companion robot** with no direct clinical function (cognitive engagement, companionship): potentially **Class I** or outside MDR scope entirely if no medical claim is made

**Key MDR principle:** The classification follows the intended purpose declared by the manufacturer. A humanoid robot without medical claims escapes MDR scope; one with explicit clinical diagnostic or therapeutic claims enters it.

### 2.2 Software as Medical Device (SaMD) Under EU MDR

Article 2(1) of EU MDR defines "medical device software" broadly. IMDRF's "Software as a Medical Device: Possible Framework for Risk Categorization" (2014) — which the EU has adopted as a reference — categorizes SaMD by two dimensions:

1. **Healthcare Situation:** Critical, Serious, or Non-Serious (based on what the software is used for)
2. **Significance of Information:** Treat/diagnose, Drive clinical management, or Inform clinical management

This produces a 3×3 matrix yielding Categories I (lowest) through IV (highest risk). AI-driven humanoid decision-making in a critical care context would land in Category III or IV, triggering mandatory conformity assessment by a Notified Body (not manufacturer self-certification).

EU MDR Article 55 and Annex IX govern conformity assessment for software. High-category SaMD embedded in a humanoid must demonstrate clinical evaluation data (per Article 61 and Annex XIV), post-market clinical follow-up (PMCF) planning, and inclusion in the EUDAMED registry.

### 2.3 EU AI Act (Regulation 2024/1689) — High-Risk AI Classification

The EU AI Act entered into force on 1 August 2024, with a phased implementation timeline. Key milestone: high-risk AI rules take effect **August 2026**; AI systems embedded in regulated products (including medical devices) have an extended transition to **August 2027**.

**Humanoid robots in healthcare as high-risk AI:**
Annex III of the AI Act lists high-risk applications. AI systems that are "safety components of products" regulated under EU MDR fall under the high-risk category. A humanoid clinical assistant whose behavior is AI-driven and directly affects patient safety is a high-risk AI system under this definition.

**Mandatory obligations for high-risk AI systems (Chapter 3 of the AI Act):**
1. Risk management system (Article 9) — documented throughout the lifecycle
2. Data and data governance (Article 10) — training datasets must be relevant, sufficiently representative, and free of discriminatory biases
3. Technical documentation (Article 11) — detailed technical records for compliance assessment
4. Record-keeping / logging (Article 12) — automatic event logs enabling post-hoc traceability
5. Transparency and information provision to deployers (Article 13)
6. Human oversight (Article 14) — systems must be designed to allow effective human oversight and intervention; operators must be able to override AI decisions
7. Accuracy, robustness, cybersecurity (Article 15) — high level of robustness throughout lifecycle

**Interaction with EU MDR:** For a humanoid robot classified as both a medical device (EU MDR) and a high-risk AI system (AI Act), compliance with MDR conformity assessment procedures is treated as partially satisfying AI Act requirements, but the AI Act adds obligations (notably the human oversight and logging requirements) beyond what MDR currently mandates.

**CE marking:** Products subject to EU MDR must bear CE marking following conformity assessment. A humanoid clinical assistant would require CE marking under MDR before market placement in the EU, plus compliance with AI Act requirements for its software components once the August 2026/2027 dates apply.

### 2.4 CE-Marked Medical Robots Currently in Use

Robotic systems with CE marking in clinical contexts include:
- **da Vinci Surgical System** (Intuitive Surgical) — CE-marked Class IIb surgical robot
- **CMR Surgical Versius** — CE-marked laparoscopic surgical robot
- **Stryker Mako** — CE-marked orthopedic robotic system
- **Ekso GT / ReWalk** — CE-marked exoskeletal rehabilitation systems

None of these are full-size bipedal humanoid robots. They are purpose-built for specific surgical or rehabilitation tasks with defined clinical scopes.

---

## 3. ISO Standards

### 3.1 ISO 13482:2014 — Safety Requirements for Personal Care Robots

**Status:** Published February 2014; confirmed 2020; revision (ISO/FDIS 13482) in progress as of early 2026.

ISO 13482 is the most directly applicable standard for a humanoid robot in healthcare or eldercare settings. It defines safety requirements for personal care robots — robots intended to provide benefits to people through physical assistance or through facilitation of daily activities.

**Three robot types covered by ISO 13482:**

| Type | Definition | Typical Form Factor |
|---|---|---|
| Physical Assistant Robot | Worn on or attached to human body; enhances, substitutes, or restores function | Exoskeletons, powered orthotics |
| Person Carrier Robot | Physically supports and transports person | Robotic wheelchairs, transfer devices |
| Mobile Servant Robot | Operates in human environment; performs tasks at a safe distance | Mobile platform robots, humanoid assistants |

**Applicable type for a humanoid healthcare assistant:** The **Mobile Servant Robot** type is most applicable. ISO 13482 does not define a dedicated "humanoid" category — a bipedal humanoid performing room-service or patient monitoring tasks falls under Mobile Servant Robot provisions.

**Key requirements of ISO 13482:**
- Hazard identification and risk assessment (following ISO 12100 methodology)
- Safe speed limits during human proximity operations
- Emergency stop and safe-state requirements
- Stability requirements (particularly relevant to bipedal systems, which face tipping hazards absent in wheeled robots)
- Hygiene and cleanability requirements for patient contact surfaces
- Information for use: labeling must clearly describe intended use, operating conditions, and user requirements

**Important exclusion (§ 1.4):** ISO 13482 explicitly excludes devices regulated as medical devices. This creates a jurisdictional gap: if a humanoid robot is classified as a medical device (under FDA or EU MDR), ISO 13482 is not the governing standard — it defers to the applicable medical device framework. This means a humanoid clinical assistant falls into a regulatory gap: it may be subject to neither a complete ISO 13482 compliance path (excluded as a medical device) nor a specific medical robotics ISO standard (none exists for general-purpose humanoids).

### 3.2 ISO 10218-1/2:2011 — Industrial Robot Safety

ISO 10218-1 (Robots and robotic devices — Safety requirements for industrial robots — Part 1: Robots) and ISO 10218-2 (Part 2: Robot systems and integration) establish the safety framework for industrial robots. They are not directly applicable to personal care or medical robots but form the technical baseline that other robot safety standards (including ISO 13482 and ISO/TS 15066) build upon.

Key contributions of ISO 10218 relevant to humanoid medical contexts:
- Safeguarding zone requirements (safety-rated monitored stops, speed/separation monitoring)
- Risk assessment methodology (feeds into ISO 12100 and ISO 13482)
- Control system safety architecture requirements
- Definition of the robot workspace, restricted space, and operating space

**ISO 10218 revision:** ISO 10218-1/2 is under revision; the updated version (as ISO 10218-1:2025 and ISO 10218-2:2025) is expected to more explicitly address collaborative and autonomous operations, with implications for hospital robots that share space with patients and staff.

### 3.3 ISO/TS 15066:2016 — Collaborative Robots (Cobots)

ISO/TS 15066 specifies safety requirements for collaborative robot operation — situations where humans and robots share the same workspace, potentially with simultaneous or sequential task execution and physical contact.

**Four collaboration modes defined in ISO/TS 15066:**
1. **Safety-Rated Monitored Stop:** Robot pauses when human enters workspace; resumes when human withdraws
2. **Hand Guiding:** Human directly guides robot through physical contact at the end-effector
3. **Speed and Separation Monitoring:** Robot operates at reduced speed when human is in proximity; monitors minimum separation distance
4. **Power and Force Limiting (PFL):** Robot operates with biomechanically safe force and power limits, allowing incidental contact without injury

**PFL biomechanical limits (key for patient safety):** ISO/TS 15066 Annex A provides biomechanically derived force and pressure thresholds for different body regions. For the most vulnerable regions (face, skull): maximum quasi-static contact force of 65 N, maximum pressure of 110 N/cm². For trunk/thorax: 140 N / 210 N/cm². These limits define the outer boundary of "safe" physical contact for any robot operating near patients.

**Relevance to humanoid healthcare robots:** Any humanoid robot that physically contacts patients during care tasks (repositioning, dressing assistance, transfer support) must demonstrate compliance with ISO/TS 15066 PFL limits — or operate under safeguarding regimes (Mode 1 or 3) that prevent contact. The bipedal gait dynamics of a full-size humanoid introduce forces (stumbling, recovery motions) that are not addressed by ISO/TS 15066, which was designed for fixed-base industrial cobots. This is a substantive safety gap.

### 3.4 IEC 62443 — Industrial Cybersecurity

IEC 62443 (Industrial Automation and Control Systems — Security) is the primary international cybersecurity standard for networked industrial control systems. It applies to any networked robot operating in an industrial or healthcare facility environment.

**Structure relevant to hospital robots:**
- **IEC 62443-2-1:** Security management system requirements for asset owners (hospital operators)
- **IEC 62443-3-3:** System security requirements and security levels (SL 1–4)
- **IEC 62443-4-2:** Technical security requirements for components (sensors, controllers, actuators)

**Security Levels:**
- SL 1: Protection against casual/unintentional violations
- SL 2: Protection against intentional violation by unsophisticated attackers
- SL 3: Protection against sophisticated, motivated attackers
- SL 4: Protection against state-sponsored or highly resourced attackers

For a networked humanoid operating in a hospital (connected to EHR systems, receiving teleoperation commands, transmitting video/sensor data), SL 2 is typically the minimum threshold. A humanoid performing clinical procedures with network connectivity would require SL 3 analysis for attack vectors that could cause patient harm.

**Gap for humanoid medical robots:** IEC 62443 was designed for factory/SCADA environments. Hospital-specific cybersecurity standards (NIST SP 800-66, HIPAA Security Rule technical safeguards) add healthcare context but do not specifically address autonomous robots with physical patient contact capabilities. No integrated cybersecurity standard for humanoid medical devices exists as of 2026.

---

## 4. Regulatory Gap: Humanoid-Specific Guidance

### 4.1 Current Status — No Humanoid-Specific Regulatory Framework

As of March 2026, **no regulatory body (FDA, EU, ISO) has issued humanoid-robot-specific guidance for clinical or healthcare use.** This is a significant finding for the paper. The specific gaps are:

**FDA:**
- No 510(k) product code for general-purpose humanoid clinical assistants
- No De Novo classification establishing a humanoid clinical assistant as a device type
- No FDA guidance document addressing the specific safety considerations of bipedal humanoid robots in clinical settings (gait stability near patients, form-factor risk factors, teleoperation latency requirements)
- No Breakthrough Device designation for any full-size humanoid
- The FDA's AI/ML SaMD framework applies to the software components but does not address humanoid-specific physical safety

**EU:**
- No Annex VIII classification rule specifically addresses humanoid robots
- The AI Act addresses AI-driven systems broadly but contains no humanoid-specific provisions
- No CE-marked humanoid robot system for clinical patient care exists as of March 2026
- EUDAMED registry contains no entries for bipedal humanoid medical robots

**ISO:**
- ISO 13482 (Personal Care Robots): excludes medical devices by definition; does not address bipedal stability, gait dynamics, or clinical-grade hygienic requirements
- ISO 10218: industrial context only; no patient-interaction provisions
- ISO/TS 15066: cobot contact limits designed for fixed-base systems; bipedal gait forces not addressed
- No ISO working group has published a humanoid healthcare robot standard as of 2026; WG on service robots (ISO/TC 299) has several standards in development but none specifically targeting bipedal clinical assistants

### 4.2 Confirmed CE-Marked or FDA-Cleared Humanoid Systems for Clinical Use

**Finding: None confirmed as of March 2026.**

Search basis:
- FDA 510(k) and De Novo databases: no entries for "humanoid robot" as medical device
- EUDAMED registry: no entries for bipedal humanoid clinical assistants
- Commercial humanoid manufacturers (Figure AI, Boston Dynamics, Unitree, 1X, Apptronik, Sanctuary, Fourier, UBTECH, AgiBot, NEURA): none have disclosed CE marking or FDA clearance for clinical applications (cross-referenced with `sources/systems_commercial.md`)
- Academic humanoid systems (RHP Friends, NAO, Pepper, iCub, TALOS, Valkyrie): NAO and Pepper are commercial educational/social robots, not FDA-cleared medical devices; RHP Friends is a research prototype (cross-referenced with `sources/systems_academic.md`)

**Existing cleared/approved robots in healthcare that are NOT humanoid:**
- da Vinci Surgical System: FDA-cleared (Class II, 510(k)), CE-marked; robotic arm system, not humanoid
- Intuity Medical PIQTM: insulin delivery robot (not humanoid)
- Various exoskeletons (ReWalk, Ekso GT, Indego): Class II FDA-cleared; wearable, not free-standing humanoid
- TUG/Aethon autonomous mobile robot: FDA registration as Class I for medication delivery (wheeled, not humanoid)

### 4.3 Implication for the Paper

The complete absence of humanoid-specific regulatory guidance — despite the existence of frameworks for care robots (ISO 13482), collaborative robots (ISO/TS 15066), AI software (FDA AI/ML Action Plan, EU AI Act), and medical robots generally — represents a critical barrier to clinical translation. Any humanoid system seeking regulatory approval must navigate a patchwork of frameworks, none of which was designed for a bipedal, general-purpose, AI-driven robot in a clinical setting. This regulatory gap should be foregrounded in Section 5 (Technical Challenges) and Section 6 (Discussion & Future Outlook).

---

## References

- FDA, "Is the Product a Medical Device?", 21 U.S.C. § 321(h), FD&C Act Section 201(h)
- FDA, "Premarket Notification 510(k)", 21 CFR § 510(k); FDA guidance on substantial equivalence
- FDA, "De Novo Classification Request", 21 U.S.C. § 513(f)(2); MDUFA IV target 150-day review
- FDA, "Breakthrough Devices Program", 21st Century Cures Act (2016); 21 CFR § 515B
- FDA, "Design Controls", 21 CFR Part 820 Subpart C (§ 820.30)
- FDA, "Artificial Intelligence and Machine Learning Software as a Medical Device Action Plan", January 2021
- FDA/Health Canada/MHRA, "Good Machine Learning Practice for Medical Device Development: Guiding Principles", October 2021
- FDA, "Predetermined Change Control Plans for Machine Learning-Enabled Medical Devices", Final Guidance, December 2024
- EU MDR, Regulation (EU) 2017/745 on medical devices; Annex VIII classification rules
- IMDRF, "Software as a Medical Device (SaMD): Possible Framework for Risk Categorization and Corresponding Considerations", 2014
- EU AI Act, Regulation (EU) 2024/1689 of the European Parliament; in force 1 August 2024; high-risk rules applicable August 2026 / August 2027 (embedded in regulated products)
- ISO 13482:2014, "Robots and robotic devices — Safety requirements for personal care robots"; 3 robot types; excludes medical devices
- ISO 10218-1:2011 / ISO 10218-2:2011, "Robots and robotic devices — Safety requirements for industrial robots"
- ISO/TS 15066:2016, "Robots and robotic devices — Collaborative robots"; Annex A biomechanical force/pressure limits
- IEC 62443 series, "Industrial Automation and Control Systems — Security"; security levels SL 1–4
