# Academic & Research Humanoid Platforms — Specifications & Healthcare/HRI Use

> Purpose: Technical reference for our review paper on humanoid robots in healthcare (ACM Computing Surveys).
> Compiled: 2026-03-10. Coverage: research/academic platforms developed prior to the commercial wave.
> Healthcare column: CONFIRMED RESEARCH USE ONLY. Speculative or planned applications excluded.
> These are non-commercial platforms; pricing is not applicable unless noted.

---

## 1. HRP Series (Humanoid Robotics Project) — AIST / CNRS-AIST JRL

**Developer:** National Institute of Advanced Industrial Science and Technology (AIST), Japan; CNRS-AIST Joint Robotics Laboratory (JRL) for later variants
**Country:** Japan / France (joint)
**Active Period:** 1998–present (HRP-1 through HRP-5P)

### Key variants

| Model | Height | Weight | DOF | Notes |
|-------|--------|--------|-----|-------|
| HRP-2 | 154 cm | 58 kg | 30 | Most widely used in research labs globally |
| HRP-4 | 150 cm | 39 kg | 34 | Lightweight slim body; 6-axis F/T in wrists/ankles |
| HRP-4C | 158 cm | 43 kg | 42 | Female-appearance; facial expression actuation |
| HRP-5P | 182 cm | 101 kg | 37 | Heavy construction labor (neck 2, waist 3, arms 8, legs 6, hands 2 DOF breakdown) |

**Unique features:** Series elastic actuators (HRP-4 onward); torque-controlled joints; whole-body motion planning framework (OpenHRP/mc-rtc).

**Primary research focus:** Bipedal walking, whole-body loco-manipulation, industrial task execution, teleoperation.

**Healthcare / HRI research:**
- HRP-4C used in social HRI studies (facial expression, gait naturalness evaluation).
- HRP-2 used as reference platform in dozens of HRI studies via CNRS-AIST JRL; foundation for the RHP Friends nursing robot (see entry 10).
- No confirmed clinical deployments for HRP-2/4/5P.

**Open-source:** Partial. Controller framework `mc-rtc` (MIT License, GitHub: jrl-umi3218/mc_rtc) is open-source. URDF models and simulation packages available. Full hardware design not publicly released.

**Status:** HRP-2/4 — active in research labs. HRP-5P — prototype, not mass-produced. HRP-4C — display/research; no longer manufactured.

**Primary sources:**
- https://www.aist.go.jp/aist_e/list/latest_research/2010/20101108/20101108.html (HRP-4)
- https://www.aist.go.jp/aist_e/list/latest_research/2018/20181116/en20181116.html (HRP-5P)
- https://robotsguide.com/robots/hrp4

---

## 2. ASIMO — Honda Research Institute

**Developer:** Honda Research Institute Japan / Honda R&D
**Country:** Japan
**Active Period:** 2000–2022 (retired March 2022)

| Spec | Value |
|------|-------|
| Height | 130 cm |
| Weight | 54 kg |
| Total DOF | 57 (final 2011 version) |
| Max walking speed | 9 km/h (running) |
| Battery | 51.8 V Li-ion; ~1 hour runtime |

**Unique features:** First humanoid to run and climb stairs reliably; multi-modal sensing (face/voice/gesture recognition); all-electric actuation.

**Primary research focus:** Bipedal locomotion, HRI (gesture + voice recognition), mobility assist device spin-offs.

**Healthcare / HRI research:**
- Honda leveraged ASIMO technology to develop wearable walking assist devices: Stride Management Assist and Bodyweight Support Assist — these are the primary healthcare spin-offs.
- ASIMO itself was not deployed clinically; used in public demonstrations and HRI research contexts (emotion recognition, social acceptance).
- Nursing/road transport robot programs cited as successor direction after ASIMO retirement.

**Open-source:** None. Fully proprietary closed platform.

**Status:** Discontinued. Honda officially retired ASIMO in March 2022 to redirect resources toward practical avatar-style robotic applications.

**Primary sources:**
- https://global.honda/en/robotics/asimo/
- https://www.therobotreport.com/honda-asimo-robot-discontinued/

---

## 3. Atlas (Hydraulic Research Version, pre-2024) — Boston Dynamics / DARPA

**Developer:** Boston Dynamics (originally under DARPA funding)
**Country:** USA
**Active Period:** 2013–April 2024 (hydraulic version retired)

| Spec | Value |
|------|-------|
| Height | 150 cm (final version) |
| Weight | 89 kg |
| Total DOF | 28 |
| Actuation | Hydraulic (unique; enables high force density) |
| Sensors | Stereo cameras, LIDAR, IMU, joint encoders |

**Unique features:** Hydraulic actuation enabling high-torque, dynamic full-body acrobatics; used in DARPA Robotics Challenge (2013–2015) as reference disaster-response platform. Backflips and parkour demonstrated publicly.

**Primary research focus:** Dynamic locomotion, whole-body motion planning, disaster response manipulation (DRC), sim-to-real transfer.

**Healthcare / HRI research:**
- Not directly used in clinical settings.
- Open Humanoids Project (MIT + University of Edinburgh): developed unified control/planning/perception software for Atlas and NASA Valkyrie (GitHub: openhumanoids).
- Served as benchmark platform for whole-body control algorithms that underpin future medical manipulation research.

**Open-source:** Partial. `openhumanoids` organization (GitHub) released control/perception code for Atlas. Drake (MIT) supports Atlas simulation models. Hardware closed.

**Status:** Retired April 2024. Boston Dynamics released fully electric Atlas for commercial deployment (see systems_commercial.md entry 3). The hydraulic Atlas research program has ended.

**Primary sources:**
- https://en.wikipedia.org/wiki/Atlas_(robot)
- https://github.com/openhumanoids

---

## 4. iCub — Italian Institute of Technology (IIT)

**Developer:** Italian Institute of Technology (IIT), Istituto Italiano di Tecnologia; RobotCub consortium (EU FP6 project)
**Country:** Italy
**Active Period:** 2004–present; iCub3 released 2022

| Spec | Value |
|------|-------|
| Height | 104 cm (child-sized, ~3.5-year-old) |
| Weight | ~23 kg |
| Total DOF | 54 |
| Actuation | 150 W brushless motors (shoulders/large joints); DC motors (hands/small joints) |
| Sensors | Stereo cameras, gyroscopes, accelerometers, microphones, encoders, 6-axis F/T sensors, capacitive tactile skin (fingertips and upper body) |

**Unique features:** Full-body tactile skin; child-scale design enabling developmental robotics research; iCub3 (2022) adds immersive telepresence capability (operator inhabits robot via VR). Fully open-source hardware and software.

**Primary research focus:** Cognitive developmental robotics, sensorimotor learning, manipulation, HRI, embodied AI, tactile perception.

**Healthcare / HRI research:**
- Used in cognitive training HRI studies (intentional stance research by Marchesi et al., 2019).
- iCub-HRI framework (GitHub: robotology/icub-hri) provides standardized components for perception (object/face recognition, touch), manipulation, and social interaction (speech, joint attention) — directly applicable to assistive HRI scenarios.
- iCub3 telepresence: potential for remote patient interaction and rehabilitation teleoperation research.
- Over 40 iCub units distributed to research labs worldwide under the RobotCub program.

**Open-source:** Yes. Full open-source: hardware design, software (YARP middleware), and documentation released under GPL. GitHub org: robotology. Primary SW repo: robotology/icub-main (~118 stars; actively maintained as of 2026).

**Status:** Active. iCub3 is the current flagship. Ongoing EU-funded research programs.

**Primary sources:**
- https://icub.iit.it/
- https://pubmed.ncbi.nlm.nih.gov/20864311/ (iCub open platform paper)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7805865/ (iCub-HRI paper)
- https://github.com/robotology/icub-main

---

## 5. NAO — Aldebaran Robotics / SoftBank Robotics

**Developer:** Aldebaran Robotics (France); acquired by SoftBank Robotics 2012
**Country:** France / Japan
**Active Period:** 2006–present (V6 current)

| Spec | Value |
|------|-------|
| Height | 58 cm |
| Weight | 5.6 kg |
| Total DOF | 25 |
| Actuation | 23 DC motors |
| Sensors | 2× HD cameras, 4× microphones, sonar, IMU, 7 touch sensors, FSRs in feet |
| Battery | Li-ion; ~60-90 min runtime |

**Unique features:** Most widely deployed research humanoid globally (>19,000 units in 70+ countries, 600+ universities and labs); fully programmable in Python/C++/Blockly; ROS-compatible; standard platform for RoboCup SPL (Standard Platform League).

**Primary research focus:** Social HRI, educational robotics, cognitive science, autism spectrum disorder (ASD) therapy research, elderly care interaction.

**Healthcare / HRI research:**
- ASD therapy: NAO used in dozens of clinical studies for autism social training. Science Robotics (2024) review identified robot-assisted therapy for ASD as a validated application with lab-to-clinic translation challenges.
- Elderly care: deployed in care homes for cognitive stimulation exercises, companionship, medication reminders.
- Psychiatry: Social robots in adult psychiatry review (Frontiers 2025) covers NAO as a primary platform in psychiatric HRI studies.
- Patient greeting and information delivery in hospital waiting areas.
- Over 1,000 peer-reviewed papers cite NAO as the experimental platform.

**Open-source:** Partial. SDK (NAOqi) available with academic licensing. ROS interface packages available (naoqi_driver). Hardware closed.

**Status:** Active. V6 is current production version. Aldebaran brand re-emerged separately; SoftBank Robotics continues NAO.

**Primary sources:**
- https://www.aldebaran.com/en/nao
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11850358/ (social robots in psychiatry)
- https://www.science.org/doi/10.1126/scirobotics.adl2266 (ASD therapy efficacy)

---

## 6. Pepper — SoftBank Robotics / Aldebaran

**Developer:** Aldebaran Robotics / SoftBank Robotics (joint development)
**Country:** France / Japan
**Active Period:** 2014–2021 (production paused June 2021 due to weak demand); units still in active research use

| Spec | Value |
|------|-------|
| Height | 120 cm |
| Weight | 28 kg |
| Total DOF | 20 (17 body joints + 3 wheel motors) |
| Mobility | 3-wheeled omnidirectional base (not bipedal) |
| Actuators | 20 DC motors |
| Sensors | 2× HD cameras, depth sensor, 4× microphones, sonar, laser, bump sensors, touch sensors |
| Battery | 30 Ah Li-ion; ~12 hr light-use runtime |
| Tablet | Integrated 10.1" Android chest tablet |

**Unique features:** Emotion recognition via facial expression and voice tone analysis; designed specifically for social interaction; chest tablet for information display. Semi-humanoid (wheeled, not bipedal).

**Primary research focus:** Social robotics, HRI, emotion recognition, customer service, elderly care, education.

**Healthcare / HRI research:**
- Japan: deployed in >2,000 healthcare facilities for patient engagement, cognitive stimulation (dementia patients), companionship.
- Qualitative studies (ScienceDirect, Int. J. Social Robotics): residents in care homes willing to interact; benefits in cognitive/physical activation.
- Dementia care: Pepper used for reminiscence therapy and daily activity prompting.
- ASD therapy: ABA therapist teleop studies via VR interface (Choreographe software).
- Hospital administrative tasks: patient check-in, appointment reminders, health literacy information delivery.
- PMC study: demonstrated 12-week loneliness reduction in elderly residents.

**Open-source:** Partial. NAOqi SDK shared with NAO. ROS interface available. Hardware closed. Production paused.

**Status:** Production paused (2021). Existing units remain in research and deployment. No new units being manufactured as of 2026.

**Primary sources:**
- https://en.wikipedia.org/wiki/Pepper_(robot)
- https://www.sciencedirect.com/science/article/abs/pii/S1130862119305807 (dementia care study)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10265350/ (dementia care qualitative)
- https://www.mdpi.com/2076-3417/14/1/110 (Pepper capabilities review)

---

## 7. TALOS — PAL Robotics

**Developer:** PAL Robotics (Barcelona, Spain)
**Country:** Spain
**Active Period:** 2017–present

| Spec | Value |
|------|-------|
| Height | 175 cm |
| Weight | 95 kg |
| Total DOF | 32 |
| Arm payload | 6 kg per arm (fully extended) |
| Walking speed | Up to 3 km/h |
| Actuation | Torque-controlled joints (series elastic actuators in lower body) |
| Sensors | Stereo cameras, IMU, 6-axis F/T sensors in wrists and ankles |

**Unique features:** High payload per arm for its size; torque-controlled whole-body; designed for industrial tool use. Available for purchase by research institutions.

**Primary research focus:** Torque control, whole-body manipulation, dynamic walking, loco-manipulation. Used by LAAS-CNRS, INRIA, and other EU labs. Part of EU Memmo project (memory of motion for legged robots).

**Healthcare / HRI research:**
- No confirmed healthcare deployments.
- Research focus is industrial and manufacturing applications.
- Torque-controlled arms relevant to force-sensitive manipulation (surgical/care robotics) but no specific medical studies identified.

**Open-source:** Partial. ROS packages and URDF models publicly available (robots.ros.org/talos). Hardware closed commercial platform.

**Status:** Active. Available for institutional purchase.

**Primary sources:**
- https://pal-robotics.com/robot/talos/
- https://ieeexplore.ieee.org/document/8246947/ (TALOS platform paper)
- https://robots.ros.org/talos/

---

## 8. Valkyrie (R5) — NASA Johnson Space Center

**Developer:** NASA Johnson Space Center (JSC) Engineering Directorate
**Country:** USA
**Active Period:** 2013–2024 (University of Edinburgh deployment); returned to JSC 2024

| Spec | Value |
|------|-------|
| Height | 187 cm |
| Weight | 129 kg |
| Total DOF | 44 |
| Actuation | Series elastic actuators (SEA); all-electric |
| Sensors | Carnegie Robotics Multisense SL (stereo + IR structured light + laser); IMU; joint encoders |
| Hands | 3 fingers + thumb (simplified anthropomorphic) |

**Unique features:** 44-DOF SEA-based platform; designed for degraded/damaged human-engineered environments (DRC); 18 years of JSC humanoid design heritage incorporated.

**Primary research focus:** Disaster response manipulation (DRC Trials 2013), planetary exploration (ISS/Mars precursor), whole-body control algorithms.

**Healthcare / HRI research:**
- No direct clinical deployments.
- University of Edinburgh research (10-year deployment): advances cited as potentially applicable to assisted living technologies and healthcare/rehabilitation robotics — no specific medical studies conducted with Valkyrie.
- openhumanoids project (MIT + Edinburgh) developed shared control/perception software for both Atlas and Valkyrie.

**Open-source:** Partial. openhumanoids GitHub organization released research software. Hardware not open-source.

**Status:** Returned to JSC (2024) after decade at University of Edinburgh. Future focus: planetary missions (not healthcare).

**Primary sources:**
- https://www.nasa.gov/technology/r5/
- https://sites.utexas.edu/hcrl/files/2016/01/jfr-nasa-hcrl-final.pdf (Valkyrie JFR paper)
- https://github.com/openhumanoids

---

## 9. WALK-MAN — Italian Institute of Technology (IIT)

**Developer:** Italian Institute of Technology (IIT), Istituto Italiano di Tecnologia; EU FP7 project
**Country:** Italy
**Active Period:** 2014–2018 (main project); evolved into subsequent IIT platforms

| Spec | Value |
|------|-------|
| Height | 185 cm |
| Weight | 102 kg (reduced from original 133 kg in v2) |
| Arm payload | 10 kg per arm (v2; up from 7 kg v1) |
| Materials | Ergal 60%, magnesium alloys 25%, titanium/iron/plastics |
| Battery | 1 kWh; ~2 hr runtime |
| Control | 80% teleoperated / 20% local autonomous stabilization |

**Unique features:** Extreme lightweight construction for size; designed specifically for disaster response in human-built environments; firefighting demonstrations (2018 IEEE Spectrum). EU DRC-inspired project.

**Primary research focus:** Disaster response manipulation, semi-autonomous teleoperation in degraded environments, whole-body loco-manipulation.

**Healthcare / HRI research:**
- No healthcare applications. Research focus entirely on disaster response.
- Technical contributions (robust manipulation, force control) are foundational for future medical robotics.

**Open-source:** Limited. Some software released via IIT/WALK-MAN project website. Hardware closed.

**Status:** Project completed (~2018). Hardware evolved into subsequent IIT humanoid platforms.

**Primary sources:**
- https://walk-man.eu/
- https://spectrum.ieee.org/new-version-of-walkman-is-slimmer-quicker-better-at-quenching-your-flames
- https://www.researchgate.net/publication/308972040_WALK-MAN_A_High_Performance_Humanoid_Platform_for_Realistic_Environments

---

## 10. RHP Friends — CNRS-AIST JRL / KHI

**Developer:** CNRS-AIST Joint Robotics Laboratory (JRL); Kawasaki Heavy Industries (KHI); collaborators: LIRMM, UPJV, MIS
**Country:** Japan / France (joint)
**Active Period:** ~2020–present

| Spec | Value |
|------|-------|
| Height | 168 cm |
| Weight | 54 kg |
| Total DOF | 30 (excluding hands): 6 per leg, 7 per arm, 2 torso/neck |
| Head sensors | Azure Kinect RGBD (wide-angle depth), ZED Mini stereo camera |
| Locomotion | Bipedal walking |

**Unique features:** First research humanoid explicitly designed and demonstrated for nursing tasks; seamless autonomous/teleoperated mode switching; multi-contact locomanipulation integrated with teleoperation.

**Primary research focus:** Nursing assistance, teleoperated patient care, locomanipulation in human environments.

**Healthcare / HRI research (confirmed):**
- Demonstrated at IREX 2023 (International Robot Exhibition) over 3 days, 3 sessions/day.
- Task 1 (routine): Patient transfer assistance.
- Task 2 (non-routine): Operate a circuit breaker (adaptability to human-designed environments).
- System integrates: locomanipulation, multi-contact motion, teleoperation, object detection/tracking.
- Published: IEEE Robotics and Automation Magazine (2025); arXiv:2412.20770 (Dec 2024).
- This is among the most directly healthcare-relevant academic humanoid demonstrations published to date.

**Open-source:** Partial. mc-rtc controller framework (jrl-umi3218/mc_rtc) used. Hardware not openly released.

**Status:** Active research platform.

**Primary sources:**
- https://arxiv.org/abs/2412.20770
- https://ieeexplore.ieee.org/document/10852168
- https://hal.science/hal-04844951v2

---

## 11. TORO (TOrque-controlled humanoid RObot) — DLR

**Developer:** German Aerospace Center (DLR), Institute of Robotics and Mechatronics
**Country:** Germany
**Active Period:** 2013–present

| Spec | Value |
|------|-------|
| Height | 174 cm |
| Weight | 79 kg |
| Total DOF | 27 (body); 39 (including hands) |
| Actuation | DLR-KUKA Lightweight Robot (LBR) III drive units; position and torque control modes |
| Arm payload | ~5 kg per arm |

**Unique features:** Based on DLR-KUKA LWR technology (known from surgical robotics context); both position and torque control; anthropomorphic arms with compliant actuation shared lineage with KUKA MED/iiwa arms used in surgery.

**Primary research focus:** Torque-controlled whole-body control, compliant manipulation, bipedal walking.

**Healthcare / HRI research:**
- No direct clinical applications.
- DLR's LWR arm lineage (shared with TORO) feeds into KUKA LBR iiwa (surgical/medical robotics) — indirect technology transfer.
- Compliant torque-controlled design is directly relevant to safe human-robot physical interaction for care tasks.

**Open-source:** Limited. Some DLR publications with code snippets. Hardware closed.

**Status:** Active research platform at DLR.

**Primary sources:**
- https://ieeexplore.ieee.org/document/7041473/ (TORO overview paper)
- https://www.dlr.de/en/rm/media/videos/control-applications-of-toro
- https://robotsguide.com/robots/toro

---

## 12. LOLA — Technical University of Munich (TU Munich)

**Developer:** Chair of Applied Mechanics, TU Munich (Technische Universität München)
**Country:** Germany
**Active Period:** ~2006–present (ongoing research)

| Spec | Value |
|------|-------|
| Height | 176 cm |
| Weight | 68 kg |
| Total DOF | 26 distributed joints (7-DOF legs with active toe joints) |
| Actuation | Brushless DC motors; modular multi-sensory joint design; decentralized joint controllers |
| Feet sensors | 6-axis F/T sensors + 4 binary contact switches per foot |
| Walking speed | Up to 3.34 km/h (demonstrated at Hannover Messe 2010) |

**Unique features:** Redundant 7-DOF leg kinematics (vs. standard 6-DOF); extremely lightweight construction; autonomous walking in unknown environments; online trajectory planning via constrained QP + spline collocation.

**Primary research focus:** High-speed autonomous bipedal walking, online motion planning, unknown environment navigation.

**Healthcare / HRI research:**
- No healthcare applications. Purely locomotion research platform.
- High-speed walking algorithms are foundational for mobile care robots.

**Open-source:** Limited. Research publications available; no public code repository identified.

**Status:** Active research. Long-running platform with ongoing refinements.

**Primary sources:**
- https://www.mec.ed.tum.de/en/am/research/current-projects/humanoid-robot-lola/
- https://pubmed.ncbi.nlm.nih.gov/19665558/ (LOLA design and walking control)
- https://link.springer.com/content/pdf/10.1007/978-1-4020-9438-5_22.pdf (high-speed walking chapter)

---

## Summary Table

| Robot | Developer | Height | Weight | DOF | Healthcare/HRI Use | Open-Source | Status |
|-------|-----------|--------|--------|-----|-------------------|-------------|--------|
| HRP-2/4/5P | AIST / CNRS-AIST | 150–182 cm | 39–101 kg | 30–37 | HRI studies; RHP Friends predecessor | Partial (mc-rtc) | Active |
| ASIMO | Honda | 130 cm | 54 kg | 57 | Walking assist spin-offs; social HRI | None | Discontinued (2022) |
| Atlas (hydraulic) | Boston Dynamics | 150 cm | 89 kg | 28 | DRC platform; WBC research | Partial (openhumanoids) | Retired (2024) |
| iCub / iCub3 | IIT | 104 cm | 23 kg | 54 | Cognitive HRI; tactile sensing; telepresence | Full (GPL) | Active |
| NAO | Aldebaran/SoftBank | 58 cm | 5.6 kg | 25 | ASD therapy; elderly care; psychiatry | Partial (SDK) | Active |
| Pepper | SoftBank | 120 cm | 28 kg | 20 | Care homes; dementia; hospital admin | Partial (SDK) | Production paused (2021) |
| TALOS | PAL Robotics | 175 cm | 95 kg | 32 | None confirmed | Partial (ROS/URDF) | Active |
| Valkyrie | NASA JSC | 187 cm | 129 kg | 44 | Potential assisted living (not confirmed) | Partial (openhumanoids) | Returned to JSC (2024) |
| WALK-MAN | IIT | 185 cm | 102 kg | N/A | None (disaster response only) | Limited | Project completed (~2018) |
| RHP Friends | CNRS-AIST/KHI | 168 cm | 54 kg | 30 | Nursing: patient transfer (IREX 2023) | Partial (mc-rtc) | Active |
| TORO | DLR | 174 cm | 79 kg | 27–39 | None (compliant manipulation research) | Limited | Active |
| LOLA | TU Munich | 176 cm | 68 kg | 26 | None (locomotion research only) | Limited | Active |
