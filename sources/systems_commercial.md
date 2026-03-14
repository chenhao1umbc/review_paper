# Commercial Humanoid Robot Systems — Specifications & Healthcare Deployment Status

> Purpose: Technical reference for our review paper on humanoid robots in healthcare (ACM Computing Surveys).
> Compiled: 2026-03-10. Coverage: systems announced/updated 2024–2026.
> Medical deployment column: CONFIRMED REAL DEPLOYMENTS ONLY. Marketing claims and future plans excluded.

---

## 1. Figure AI — Figure 02

**Manufacturer:** Figure AI, Inc.
**Country:** USA (Sunnyvale, CA)
**Announced/Released:** August 2024

| Spec | Value |
|------|-------|
| Height | 168 cm |
| Weight | 70 kg |
| Total DOF | 28 |
| Hand DOF | 16 (per pair) |
| Max walking speed | 1.2 m/s (4.3 km/h) |
| Payload capacity | 20–25 kg |
| Battery | 2.25 kWh lithium-ion (torso-integrated) |
| Runtime | ~5 hours; 1.5 hr rapid charge |
| Cameras | 6 cameras |
| LiDAR | Not specified |
| Force-torque sensors | Not publicly detailed |

**LLM/AI Integration:** Confirmed. Initially co-developed with OpenAI (speech-to-speech, VLM-based task planning); partnership terminated mid-2025. Figure then developed fully in-house end-to-end neural model (Figure Neural Networks). No external LLM dependency as of late 2025.

**Open-Source Repos:** None. Closed commercial platform.

**Medical/Healthcare Deployment:** None confirmed. All reported deployments are automotive manufacturing (BMW Spartanburg, SC: 11-month pilot, 90,000+ parts loaded, 30,000+ vehicles contributed to production).

**Primary Source:** https://www.figure.ai/news/production-at-bmw | https://humanoid.guide/product/figure-02/

---

## 2. Tesla Optimus Gen 2

**Manufacturer:** Tesla, Inc.
**Country:** USA (Fremont / Austin, TX)
**Announced/Released:** December 2023 (Gen 2); internal factory deployment mid-2024; Gen 3 hands production January 2026

| Spec | Value |
|------|-------|
| Height | 173 cm (5'8") |
| Weight | 57 kg (125 lb) |
| Total DOF | 28+ body |
| Hand DOF | 11 (Gen 2); 22 (Gen 3 hands, 50 actuators — in mass production Jan 2026) |
| Max walking speed | 8 km/h (5 mph) |
| Payload capacity | 20 kg |
| Battery | Not publicly specified |
| Runtime | Not publicly specified |
| Cameras | Integrated vision system (camera count not disclosed) |
| LiDAR | None (vision-only, similar to FSD stack) |
| Force-torque sensors | Not publicly detailed |

**LLM/AI Integration:** Confirmed. Runs on Tesla's FSD-derived neural network stack. Elon Musk has cited Grok (xAI) integration; specifics not technically documented.

**Open-Source Repos:** None. Closed proprietary system.

**Medical/Healthcare Deployment:** None confirmed. Currently deployed internally at Tesla Fremont and Austin factories performing battery cell sorting, parts handling, and quality inspection. Elon Musk has made unsubstantiated public claims about future surgical applications; no clinical trial or hospital deployment has occurred.

**Primary Source:** https://humanoid.guide/product/optimus-gen2/ | https://en.wikipedia.org/wiki/Optimus_(robot)

---

## 3. Boston Dynamics Atlas (Electric, 2024)

**Manufacturer:** Boston Dynamics (subsidiary of Hyundai Motor Group)
**Country:** USA (Waltham, MA)
**Announced/Released:** April 2024 (hydraulic Atlas retired; electric Atlas unveiled)

| Spec | Value |
|------|-------|
| Height | ~150–175 cm (exact production spec not published) |
| Weight | 89 kg |
| Total DOF | 28 |
| Hand DOF | Not publicly specified (end-effector modular) |
| Max walking speed | 2.5 m/s sprint; typical walking ~1.5 m/s |
| Payload capacity | 50 kg instantaneous; 30 kg sustained; 2.3 m reach |
| Battery | Custom high-density lithium (specs not disclosed) |
| Runtime | Not publicly disclosed |
| Cameras | Integrated vision (exact count not disclosed) |
| LiDAR | Not confirmed in production version |
| Force-torque sensors | Confirmed (used for manipulation and balance) |

**LLM/AI Integration:** Confirmed (partnership). Boston Dynamics and Google DeepMind announced strategic partnership at CES January 2026 to integrate Gemini Robotics 1.5 (VLA) and Gemini Robotics-ER 1.5 (planning) foundation models into Atlas. Testing at Hyundai factories imminent.

**Open-Source Repos:** None. Closed commercial platform.

**Medical/Healthcare Deployment:** None confirmed. Deployment target is Hyundai Motor Group automotive manufacturing facilities. No hospital or clinical deployment reported.

**Primary Source:** https://bostondynamics.com/products/atlas/ | https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/

---

## 4. Agility Robotics Digit v4

**Manufacturer:** Agility Robotics (majority owned by Amazon)
**Country:** USA (Corvallis, OR)
**Announced/Released:** 2023 (v4); commercial deployment 2024

| Spec | Value |
|------|-------|
| Height | 175 cm (5'9") |
| Weight | 65 kg |
| Total DOF | ~arms 3 DOF each (arm DOF only; leg/full body not fully specified) |
| Hand DOF | Simple gripper (0–1 DOF standard); dexterous hands in development |
| Max walking speed | 5 km/h |
| Payload capacity | 16 kg (35 lb) per cycle; v5 target 22 kg (50 lb) |
| Battery | Hot-swappable; runtime not publicly specified |
| Runtime | Not publicly specified |
| Cameras | 4 Intel RealSense depth cameras |
| LiDAR | LiDAR confirmed |
| Force-torque sensors | MEMS IMU; tactile sensors not confirmed |

**LLM/AI Integration:** Announced. Agility has been experimenting with LLM-based natural language task programming (Digit self-programs from verbal commands). NVIDIA partnership for Isaac Lab simulation. No peer-reviewed publication confirming full LLM deployment.

**Open-Source Repos:** GitHub org exists (github.com/agilityrobotics) with limited archived repositories; simulation URDF community repos available (not official full SDK).

**Medical/Healthcare Deployment:** None confirmed. Commercial deployments are exclusively warehouse/logistics: GXO Logistics (Flowery Branch, GA) — 100,000+ totes moved; Amazon fulfillment center pilots; Spanx facility. Healthcare mentioned as long-term vision only.

**Primary Source:** https://www.agilityrobotics.com/ | https://humanoid.guide/product/digit/

---

## 5. Unitree H1 and G1

**Manufacturer:** Unitree Robotics
**Country:** China (Hangzhou)
**Announced/Released:** H1: 2023; G1: May 2024

### Unitree H1

| Spec | Value |
|------|-------|
| Height | 180 cm |
| Weight | 47 kg |
| Total DOF | 19 (standard) |
| Hand DOF | Optional; base model has simple grippers |
| Max walking speed | 6 km/h; running demonstrated |
| Payload capacity | Not publicly specified |
| Battery | Not publicly specified |
| Runtime | Not publicly specified |
| Joint torque | Up to 360 Nm |
| Sensors | IMU, optional depth cameras |
| Price | ~$90,000 (base) |

### Unitree G1

| Spec | Value |
|------|-------|
| Height | 132 cm |
| Weight | 35 kg |
| Total DOF | 23 (base) to 43 (EDU version) |
| Hand DOF | 3-fingered dexterous gripper; optional dexterous hands |
| Max walking speed | 2 m/s (7.2 km/h) |
| Payload capacity | Not officially specified |
| Battery | 9,000 mAh quick-release |
| Runtime | ~2 hours |
| Sensors | Depth cameras, IMU, force-torque (EDU version) |
| Price | ~$13,500–16,000 (base) |

**LLM/AI Integration:** Confirmed (community and official). Unitree maintains an active open-source ecosystem: UnifoLM-VLA (Vision-Language-Action model), UnifoLM-WMA (world model architecture). Third-party integration supports OpenAI, Anthropic Claude, Google Gemini, xAI Grok, Meta LLaMA, DeepSeek via OpenMind OM1 framework.

**Open-Source Repos:** Yes — https://github.com/unitreerobotics (active; includes unitree_rl_gym, unitree_IL_lerobot, unitree_sim_isaaclab, xr_teleoperate)

**Medical/Healthcare Deployment:** Research prototype only. The UC San Diego Yip Lab teleoperated a Unitree G1 (with Inspire Gen4 hands) for 7 medical procedures including auscultation, Leopold maneuvers, and ultrasound-guided injection (70% success rate for non-clinician operators). This is a research study (arXiv:2503.12725), not a clinical deployment. No hospital deployment of Unitree robots as clinical tools confirmed.

**Primary Source:** https://www.unitree.com/g1/ | https://github.com/unitreerobotics | https://arxiv.org/abs/2503.12725

---

## 6. 1X Technologies NEO Beta

**Manufacturer:** 1X Technologies AS
**Country:** Norway (Moss); US operations (Stavanger / Santa Clara)
**Announced/Released:** NEO Beta: August 2024; NEO (consumer): October 2025

| Spec | Value |
|------|-------|
| Height | 165 cm (NEO Beta); ~168 cm (NEO final) |
| Weight | 30 kg |
| Total DOF | 75 (full body) |
| Hand DOF | 22 DOF per hand |
| Max walking speed | ~1.4 m/s typical; claimed 6.2 m/s sprint (not independently verified) |
| Payload capacity | Up to 24.95 kg carry; 68 kg lift claim |
| Battery | 842 Wh |
| Runtime | ~4 hours; fast charge ~24 minutes |
| Noise level | 22 dB |
| Cameras | Integrated (count not specified) |
| LiDAR | Not specified |
| Force-torque sensors | Not publicly detailed |
| Price | $20,000 (early adopter); $499/month subscription |

**LLM/AI Integration:** Confirmed. 1X has a proprietary AI system; the company emphasizes whole-body neural control trained via imitation learning and VLA approaches. Specific external LLM partnerships not disclosed.

**Open-Source Repos:** None. Closed commercial product.

**Medical/Healthcare Deployment:** None confirmed. NEO is positioned as a home assistant robot. Industry analysts have noted elder care as a potential future application. No clinical trial or hospital deployment has occurred.

**Primary Source:** https://www.1x.tech/neo | https://humanoid.guide/product/neo-beta/

---

## 7. Apptronik Apollo

**Manufacturer:** Apptronik, Inc.
**Country:** USA (Austin, TX)
**Announced/Released:** August 2023; commercial pilots 2024–2025

| Spec | Value |
|------|-------|
| Height | 173 cm (5'8") |
| Weight | 72.6 kg (160 lb) |
| Total DOF | Not fully specified; initial end-effectors 0–1 DOF; dexterous hands roadmapped |
| Hand DOF | Simple gripper (initial deployments) |
| Max walking speed | Not publicly specified |
| Payload capacity | 25 kg (55 lb) |
| Battery | Hot-swappable; 4 hours per pack |
| Runtime | 4 hours (continuous hot-swap) |
| Cameras | Integrated (count not specified) |
| LiDAR | Not confirmed |
| Force-torque sensors | Not publicly detailed |

**LLM/AI Integration:** Confirmed (Google partnership). Google invested in Apptronik's $350M Series A (closed 2024); integration of Google AI models for robot cognition is in development. Specific LLM stack not publicly documented.

**Open-Source Repos:** None. Closed commercial system.

**Medical/Healthcare Deployment:** None confirmed. Current pilots: Mercedes-Benz (automotive assembly, March 2025), GXO Logistics, Jabil (electronics manufacturing). Elder care and healthcare cited as long-term expansion targets; no clinical deployment has occurred.

**Primary Source:** https://apptronik.com/apollo | https://humanoid.guide/product/apollo/

---

## 8. Sanctuary AI Phoenix (Gen 8)

**Manufacturer:** Sanctuary AI
**Country:** Canada (Vancouver, BC)
**Announced/Released:** Gen 7: April 2024; Gen 8: January 2025

| Spec | Value |
|------|-------|
| Height | 170 cm (5'7") |
| Weight | 70 kg |
| Total DOF | ~50+ total; 21 DOF per hand (hydraulic) |
| Hand DOF | 21 DOF with haptic feedback; tactile sensors (5 mN sensitivity) |
| Max walking speed | 4.8 km/h (3 mph) |
| Payload capacity | 25 kg (55 lb) |
| Battery | Not publicly specified |
| Runtime | Not publicly specified |
| Cameras | Integrated (updated in Gen 8) |
| LiDAR | Not confirmed |
| Force-torque sensors | Confirmed (tactile sensors, 5 mN resolution) |

**LLM/AI Integration:** Confirmed (proprietary). Powered by Carbon™ AI control system — described as mimicking human brain subsystems (memory, vision, hearing, touch). Microsoft collaboration announced for AI model development. Carbon is closed/proprietary; no external LLM disclosed.

**Open-Source Repos:** None. Strictly enterprise/industrial access only.

**Medical/Healthcare Deployment:** None confirmed. Partnered with Magna (automotive, March 2024). Healthcare and retail listed as future verticals. No hospital or clinical deployment has occurred.

**Primary Source:** https://www.sanctuary.ai/ | https://humanoid.guide/product/phoenix/

---

## 9. Fourier Intelligence GR-2

**Manufacturer:** Fourier Intelligence (rebranded to Fourier, July 2024)
**Country:** China (Shanghai); international offices including Singapore
**Announced/Released:** Late 2024

| Spec | Value |
|------|-------|
| Height | 175 cm |
| Weight | 63–65 kg |
| Total DOF | 53 |
| Hand DOF | 12 DOF per pair (dexterous); 6 array-type tactile sensors |
| Max walking speed | 5 km/h |
| Payload capacity | Not specified |
| Battery | Detachable, hot-swappable |
| Runtime | ~2 hours (doubled vs. GR-1 with detachable battery) |
| Cameras | Integrated (count not specified) |
| LiDAR | Not confirmed |
| Force-torque sensors | Confirmed: 6 tactile sensor arrays; FSA 2.0 actuators (>380 Nm) |

**LLM/AI Integration:** Announced. Fourier has published on NVIDIA Isaac Gym-based reinforcement learning for real-world tasks. LLM integration roadmapped; no confirmed production deployment.

**Open-Source Repos:** Partial. Fourier has shared simulation and RL training code via NVIDIA developer blog; no full SDK open-sourced.

**Medical/Healthcare Deployment:** Research partnership confirmed (not clinical deployment of GR-2 specifically). Fourier Rehab subsidiary has MOU/research collaborations with Shirley Ryan AbilityLab (Chicago), Tan Tock Seng Hospital (Singapore), ETH Zurich, and University of Melbourne. These partnerships involve Fourier's exoskeleton and rehabilitation devices (ArmMotus, CycleMotus), not confirmed GR-2 humanoid clinical use. Fourier presented GR-2 at SHBC 2025 healthcare summit and MEDICA 2025, demonstrating rehabilitation task integration — but confirmed clinical deployment of GR-2 as a clinical tool has not been documented.

**Primary Source:** https://www.fftai.com/products-gr2 | https://humanoid.guide/product/gr-2/

---

## 10. UBTECH Walker X

**Manufacturer:** UBTECH Robotics
**Country:** China (Shenzhen); US operations (Los Angeles)
**Announced/Released:** Walker X: 2021 (mature platform in 2024 context); Walker S2: mass production November 2025

| Spec | Value |
|------|-------|
| Height | 130–145 cm |
| Weight | 63–77 kg |
| Total DOF | 41 |
| Hand DOF | 6 DOF per hand; 7 DOF arms |
| Max walking speed | 3 km/h standard; 10 km/h sprint |
| Payload capacity | 10 kg total; 3 kg per hand |
| Battery | Modular, hot-swappable |
| Runtime | 2–6 hours (modular) |
| Cameras | Quad-eye RGB-D; dual LiDAR |
| LiDAR | Yes (dual RGB-D LiDAR) |
| Force-torque sensors | Tactile sensing confirmed |

**Note:** UBTECH's current commercial focus has shifted to Walker S2 (industrial, 52 DOF, mass production began November 2025, orders exceeding 800M yuan). Walker X remains the research/service platform.

**LLM/AI Integration:** Confirmed. UBTECH integrates multi-modal LLM interaction (real-time dialogue, facial recognition, lip-reading). Specific LLM provider not disclosed.

**Open-Source Repos:** None confirmed for Walker X/S2.

**Medical/Healthcare Deployment:** None confirmed for Walker X as a clinical tool. UBTECH has a separate healthcare product line (Wassi walking assist robot, PathFynder smart wheelchair, Welli companion robot) but these are distinct from Walker X. UBTECH presented an "intelligent healthcare robots" suite at CES-era events (2022 press release); no clinical deployment of Walker X in hospitals has been documented.

**Primary Source:** https://www.ubtrobot.com/en/humanoid/products/walker-x | https://rbtx.com/en-US/components/humanoid/ubtech-walker-x-humanoid-robot-41-dof

---

## 11. AgiBot (Zhiyuan) A2

**Manufacturer:** AgiBot Innovation (Shanghai) Technology Co., Ltd. (also known as Zhiyuan Robotics)
**Country:** China (Shanghai)
**Announced/Released:** 2024; A2 Ultra variant active 2025

| Spec | Value |
|------|-------|
| Height | 175 cm |
| Weight | 55 kg |
| Total DOF | 49+ |
| Hand DOF | 7 DOF per arm; visual fingertip sensors |
| Max walking speed | 0.8 m/s (2.9 km/h) |
| Payload capacity | Not officially specified |
| Battery | Not publicly specified |
| Runtime | Not publicly specified |
| Cameras | Integrated (count not specified) |
| LiDAR | Not confirmed |
| Force-torque sensors | Force-position hybrid control confirmed; visual fingertip sensors |

**LLM/AI Integration:** Confirmed. Real-time dialogue powered by large language models, facial recognition (96% accuracy), lip-reading (99% face wake-up rate). Specific LLM provider not disclosed.

**Open-Source Repos:** None confirmed.

**Medical/Healthcare Deployment:** None confirmed. AgiBot achieved #1 global humanoid shipments in 2025 (estimated 5,168 units, per Omdia) — all industrial/service deployments. A2 Ultra set Guinness record for longest walk by a humanoid (106.286 km). No clinical or hospital deployment documented.

**Primary Source:** https://www.agibot.com/products/A2 | https://humanoid.guide/product/a2/

---

## 12. NEURA Robotics 4NE-1

**Manufacturer:** NEURA Robotics GmbH
**Country:** Germany (Metzingen)
**Announced/Released:** 2023–2024; Gen 3 revealed CES 2026 (Porsche-designed)

| Spec | Value |
|------|-------|
| Height | ~170–180 cm |
| Weight | 60–80 kg (variant-dependent) |
| Total DOF | Not fully specified |
| Hand DOF | Not specified |
| Max walking speed | 3 km/h |
| Payload capacity | 15–20 kg |
| Battery | Not publicly specified |
| Runtime | Not publicly specified |
| Cameras | 3D vision (binocular) |
| LiDAR | Not confirmed |
| Force-torque sensors | Confirmed; 0.1 N sensitivity, ±0.01 mm repeatability |
| Price | $22,000–$44,600 |

**LLM/AI Integration:** Confirmed (proprietary cognitive AI). NEURA refers to the system as "cognitive robotics" with continuous autonomous learning; specific LLM stack not disclosed.

**Open-Source Repos:** None.

**Medical/Healthcare Deployment:** None confirmed. 4NE-1 is marketed for industrial and home use. No hospital or clinical deployment documented.

**Primary Source:** https://neura-robotics.com/products/4ne1/ | https://humanoid.guide/product/4ne-1/

---

## Summary Table

| Robot | Manufacturer | Country | Height | Weight | DOF (total/hand) | Speed | Payload | LLM Integration | Open-Source | Medical Deployment |
|-------|-------------|---------|--------|--------|-------------------|-------|---------|-----------------|-------------|-------------------|
| Figure 02 | Figure AI | USA | 168 cm | 70 kg | 28 / 16 | 1.2 m/s | 20–25 kg | Yes (in-house; prev. OpenAI) | No | None confirmed |
| Optimus Gen 2 | Tesla | USA | 173 cm | 57 kg | 28+ / 11 (Gen 2); 22 (Gen 3) | 8 km/h | 20 kg | Yes (FSD-derived + Grok) | No | None confirmed |
| Atlas (electric) | Boston Dynamics | USA | ~150–175 cm | 89 kg | 28 / N/A | 2.5 m/s | 30–50 kg | Yes (Google DeepMind Gemini, announced) | No | None confirmed |
| Digit v4 | Agility Robotics | USA | 175 cm | 65 kg | N/A / 0–1 DOF | 5 km/h | 16 kg | Announced (LLM task programming) | Partial | None confirmed |
| Unitree H1 | Unitree Robotics | China | 180 cm | 47 kg | 19 / gripper | 6 km/h | N/A | Yes (open ecosystem) | Yes | Research only (arXiv:2503.12725) |
| Unitree G1 | Unitree Robotics | China | 132 cm | 35 kg | 23–43 / dexterous | 7.2 km/h | N/A | Yes (VLA, open ecosystem) | Yes | Research only (arXiv:2503.12725) |
| NEO Beta | 1X Technologies | Norway | 165 cm | 30 kg | 75 / 22 per hand | 1.4 m/s typical | 25 kg | Yes (proprietary) | No | None confirmed |
| Apollo | Apptronik | USA | 173 cm | 72.6 kg | N/A / 0–1 DOF | N/A | 25 kg | Yes (Google AI, in development) | No | None confirmed |
| Phoenix Gen 8 | Sanctuary AI | Canada | 170 cm | 70 kg | ~50+ / 21 per hand | 4.8 km/h | 25 kg | Yes (Carbon™, Microsoft collab) | No | None confirmed |
| GR-2 | Fourier Intelligence | China | 175 cm | 63–65 kg | 53 / 12 per pair | 5 km/h | N/A | Announced | Partial (NVIDIA RL) | None confirmed (research partnerships only) |
| Walker X | UBTECH | China | 130–145 cm | 63–77 kg | 41 / 6 per hand | 3 km/h (10 km/h sprint) | 10 kg | Yes (multi-modal LLM) | No | None confirmed |
| A2 | AgiBot / Zhiyuan | China | 175 cm | 55 kg | 49+ / visual fingertip | 0.8 m/s | N/A | Yes (LLM dialogue, proprietary) | No | None confirmed |
| 4NE-1 | NEURA Robotics | Germany | 170–180 cm | 60–80 kg | N/A / N/A | 3 km/h | 15–20 kg | Yes (cognitive AI, proprietary) | No | None confirmed |

---

## Key Findings for Review Paper

1. **No confirmed clinical deployment** of any post-2023 general-purpose humanoid robot (Figure 02, Optimus, Atlas electric, Digit v4, NEO, Apollo, Phoenix, GR-2, Walker X, A2, 4NE-1) in a hospital or clinical care setting as of March 2026. This is a central finding of our paper.

2. **Unitree G1 is the only system with documented medical procedure execution** — teleoperated in a research context (UC San Diego, arXiv:2503.12725), not deployed clinically. Fourier has rehabilitation research partnerships but not with GR-2 as a clinical tool.

3. **LLM/AI integration is now near-universal** across the field (12 of 13 systems above): Figure (in-house VLA), Tesla (FSD+Grok), Boston Dynamics (Google DeepMind Gemini), Unitree (open VLA ecosystem), Sanctuary (Carbon™), Apptronik (Google AI), UBTECH (multi-modal LLM), AgiBot (LLM dialogue), NEURA (cognitive AI). Agility Robotics is the sole outlier with only announced/experimental LLM use.

4. **Open-source availability is rare**: Only Unitree maintains a substantive open-source SDK and model ecosystem (github.com/unitreerobotics). Agility has a minimal public presence. All others are closed proprietary systems.

5. **Geographic split**: USA (Figure, Tesla, Agility, Apptronik) and China (Unitree, UBTECH, AgiBot, Fourier) dominate; notable European entrants include Norway (1X Technologies) and Germany (NEURA Robotics); Canada (Sanctuary AI).

6. **Fourier Intelligence is the only manufacturer with a healthcare-affiliated subsidiary** (Fourier Rehab) and confirmed hospital research partnerships (Shirley Ryan AbilityLab, Tan Tock Seng Hospital) — but these involve exoskeleton/rehab devices, not the GR-2 humanoid platform.

---

## Source URLs

- Figure 02: https://humanoid.guide/product/figure-02/ | https://www.figure.ai/news/production-at-bmw
- Tesla Optimus Gen 2: https://humanoid.guide/product/optimus-gen2/ | https://en.wikipedia.org/wiki/Optimus_(robot)
- Boston Dynamics Atlas: https://bostondynamics.com/products/atlas/ | https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/
- Agility Digit: https://www.agilityrobotics.com/ | https://humanoid.guide/product/digit/
- Unitree G1/H1: https://www.unitree.com/g1/ | https://github.com/unitreerobotics
- 1X NEO: https://www.1x.tech/neo | https://humanoid.guide/product/neo-beta/
- Apptronik Apollo: https://apptronik.com/apollo | https://humanoid.guide/product/apollo/
- Sanctuary Phoenix: https://www.sanctuary.ai/ | https://humanoid.guide/product/phoenix/
- Fourier GR-2: https://www.fftai.com/products-gr2 | https://humanoid.guide/product/gr-2/
- UBTECH Walker X: https://www.ubtrobot.com/en/humanoid/products/walker-x
- AgiBot A2: https://www.agibot.com/products/A2 | https://humanoid.guide/product/a2/
- NEURA 4NE-1: https://neura-robotics.com/products/4ne1/
- UC San Diego medical study: https://arxiv.org/abs/2503.12725
- Fourier-Tan Tock Seng partnership: https://www.einnews.com/pr_news/568948827/fourier-intelligence-inks-master-research-collaboration-with-tan-tock-seng-hospital-in-singapore
