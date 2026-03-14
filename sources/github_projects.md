# Open-Source GitHub Projects — Humanoid Robots & Healthcare/Medical AI

> Purpose: Technical reference for our review paper on humanoid robots in healthcare (ACM Computing Surveys).
> Compiled: 2026-03-10. Star counts verified via GitHub API on 2026-03-10.
> Medical relevance column: CONFIRMED USE OR DIRECT RELEVANCE ONLY. Speculative future use noted separately.
> Scope: humanoid robot control, embodied AI, VLA models, medical/care HRI, simulation frameworks.

---

## Category A: Robot Learning Frameworks & Foundation Models

### A1. LeRobot — HuggingFace

| Field | Value |
|-------|-------|
| **Repo** | huggingface/lerobot |
| **URL** | https://github.com/huggingface/lerobot |
| **Stars** | 22,179 (2026-03-10) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **Last active** | 2026-03-10 (actively maintained) |

**Description:** End-to-end robot learning framework providing models, datasets, and tools for real-world robotics in PyTorch. Hardware-agnostic Python interface standardizing control across platforms from low-cost arms (SO-100, Koch) to full humanoids (Unitree G1, Reachy2). Provides standardized `LeRobotDataset` format (Parquet + MP4) hosted on HuggingFace Hub.

**Supported algorithms:** ACT, Diffusion Policy, TDMPC, VQ-BeT, pi0 (Physical Intelligence), LIBERO VLA benchmark integration (130+ tasks), Meta-World (50+ tasks).

**Supported humanoid hardware:** Unitree G1 (dual-arm manipulation with dexterous hands), Reachy2 (Pollen Robotics; HuggingFace acquired Pollen Robotics 2025).

**Relevance to humanoid medical/healthcare use:**
- Primary open-source framework for training imitation learning and VLA policies on humanoid hardware; directly enables data-driven task learning for nursing/care tasks.
- Unitree G1 integration means researchers can train manipulation policies (object grasping, tool use) directly applicable to ADL (activities of daily living) assistance.
- HuggingFace Hub hosts community-contributed robot datasets, enabling transfer learning for care scenarios.
- Reachy2 acquisition (2025) provides HuggingFace with a commercially available social humanoid platform.

---

### A2. openpi (π0 / Physical Intelligence)

| Field | Value |
|-------|-------|
| **Repo** | Physical-Intelligence/openpi |
| **URL** | https://github.com/Physical-Intelligence/openpi |
| **Stars** | 10,551 (2026-03-10) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **Last active** | 2026-03-10 (actively maintained) |

**Description:** Official open-source release of π0 (pi-zero) by Physical Intelligence — a flow-matching-based vision-language-action (VLA) foundation model for generalist robot control. Pre-trained on 10,000+ hours of real robot demonstrations across diverse manipulation tasks. Provides base checkpoints for fine-tuning on custom tasks.

**Available models:**
- π0: flow-based VLA (original)
- π0-FAST: autoregressive VLA with FAST action tokenizer (15× faster inference)
- π0.5 (Sep 2025): upgraded open-world generalization with knowledge insulation
- π0.6 (Jan 2026): RECAP training; frozen backbone fine-tuning; 85%+ success on ALOHA benchmarks

**Relevance to humanoid medical/healthcare use:**
- Generalist manipulation policy directly applicable to care task learning (medication dispensing, object handover, patient positioning assistance).
- FAST tokenizer enables high-frequency bimanual control — relevant for dexterous assistive tasks.
- Fine-tuning capability allows adaptation to hospital-specific manipulation tasks with minimal demonstrations.
- No confirmed medical deployment, but represents the highest-capability open foundation model for robot manipulation as of early 2026.

---

### A3. OpenVLA — Stanford / Berkeley / Toyota Research Institute

| Field | Value |
|-------|-------|
| **Repo** | openvla/openvla |
| **URL** | https://github.com/openvla/openvla |
| **Stars** | 5,479 (2026-03-10) |
| **Language** | Python |
| **License** | MIT |
| **Last active** | 2026-03-10 (actively maintained) |

**Description:** 7B-parameter open-source vision-language-action model trained on 970k real-world robot demonstrations (Open X-Embodiment dataset). Architecture: SigLIP + DinoV2 visual encoder → projector → Llama 2 7B backbone predicting tokenized actions. Outperforms RT-2-X (55B parameters) by 16.5% absolute on 29 manipulation tasks with 7× fewer parameters.

**Key updates:**
- OFT (Mar 2025): 25–50× faster inference, multi-image input, high-frequency bimanual control
- FAST tokenizer (Jan 2025): action chunking compressed into fewer tokens

**Relevance to humanoid medical/healthcare use:**
- Language-conditioned manipulation directly enables natural language task specification for care scenarios ("pick up the medicine bottle," "hand the glass to the patient").
- Open weights allow fine-tuning on medical/care-specific datasets without proprietary dependencies.
- Multi-image input (OFT) enables multi-camera setups relevant to bedside manipulation scenarios.

---

## Category B: Simulation & Training Environments

### B1. Genesis — Genesis-Embodied-AI

| Field | Value |
|-------|-------|
| **Repo** | Genesis-Embodied-AI/Genesis |
| **URL** | https://github.com/Genesis-Embodied-AI/Genesis |
| **Stars** | 28,254 (2026-03-10) |
| **Language** | Python |
| **License** | Apache 2.0 |
| **Last active** | 2026-03-10 (actively maintained) |

**Description:** Universal physics simulation platform rebuilt from scratch for general-purpose robotics, embodied AI, and physical AI applications. Supports rigid bodies, liquids, gases, deformable objects, thin-shell objects, and granular materials in a unified differentiable framework. Ultra-fast GPU-accelerated simulation; Python-native. Released publicly December 2024; rapidly became one of the most-starred robotics simulation repos.

**Supported robot types:** Robotic arms, legged robots, humanoids, drones, soft robots.

**Relevance to humanoid medical/healthcare use:**
- Deformable object simulation (tissues, flexible medical tools, soft anatomy) is directly relevant for surgical simulation with humanoid-mounted arms.
- Differentiable physics enables gradient-based policy optimization for delicate manipulation (wound care, patient positioning).
- Granular material support enables simulation of pill dispensing, powder handling.
- No confirmed medical use cases yet; foundational infrastructure enabling future medical simulation research.

---

### B2. Isaac Lab — NVIDIA (isaac-sim)

| Field | Value |
|-------|-------|
| **Repo** | isaac-sim/IsaacLab |
| **URL** | https://github.com/isaac-sim/IsaacLab |
| **Stars** | 6,544 (2026-03-10) |
| **Language** | Python |
| **License** | BSD-3-Clause |
| **Last active** | 2026-03-10 (actively maintained) |

**Description:** GPU-accelerated, open-source framework for robot learning built on NVIDIA Isaac Sim. Unifies reinforcement learning, imitation learning, and motion planning workflows with fast and accurate physics/sensor simulation for sim-to-real transfer. Includes 16+ robot models and 30+ pre-built training environments. Compatible with RSL-RL, SKRL, RL Games, Stable Baselines. Isaac Sim 5.0 + Isaac Lab 2.2 released at SIGGRAPH 2025.

**Relevance to humanoid medical/healthcare use:**
- Standard training infrastructure for humanoid locomotion and manipulation policies (Unitree G1, H1 supported).
- Sim-to-real transfer validated for humanoid locomotion; critical for deploying care robots safely.
- NVIDIA announced humanoid development tools specifically at Dec 2024 event — targeting industrial and service robot training.
- unitree_sim_isaaclab (391 stars) provides ready-to-use Isaac Lab integration for Unitree humanoids.

---

## Category C: Humanoid Robot Organization Repositories

### C1. Unitree Robotics — unitreerobotics

| Field | Value |
|-------|-------|
| **Org** | unitreerobotics |
| **URL** | https://github.com/unitreerobotics |
| **Last active** | 2026-03-10 |

**Description:** Official GitHub organization for Unitree Robotics. Maintains open-source SDKs, simulation environments, and learning frameworks for Unitree G1 and H1 humanoid robots.

**Key repos by stars (2026-03-10):**

| Repo | Stars | Description |
|------|-------|-------------|
| unitree_rl_gym | 3,022 | RL locomotion training (MuJoCo/IsaacLab) for H1/G1 |
| xr_teleoperate | 1,309 | Teleoperation of humanoid via XR (Apple Vision Pro, PICO 4, Meta Quest 3) |
| unitree_ros | 1,271 | ROS interface packages for all Unitree robots |
| unifolm-world-model-action | 916 | World model + action prediction for humanoid |
| unitree_sdk2 | 932 | Core SDK v2 for G1/H1 communication |
| unitree_mujoco | 863 | MuJoCo simulation for Unitree robots |
| unitree_rl_lab | 820 | RL training lab (Isaac Lab-based) |
| unitree_lerobot | 568 | LeRobot-based imitation learning for G1 dual-arm |
| unifolm-vla | 326 | UnifoLM-VLA-0: VLA model for general humanoid manipulation |

**Relevance to humanoid medical/healthcare use:**
- xr_teleoperate directly enables remote expert (e.g., nurse/therapist) control of a humanoid for patient care from distance — key for telemedicine/assistive contexts.
- unitree_lerobot enables data collection and imitation learning for ADL tasks on G1 dual-arm dexterous hands.
- unifolm-vla provides a VLA foundation model tuned for Unitree hardware — language-conditioned manipulation.
- Unitree G1 is the only full-size humanoid appearing in published healthcare research context (arXiv:2503.12725, cited in systems_commercial.md as research prototype).

---

### C2. Agility Robotics — agilityrobotics

| Field | Value |
|-------|-------|
| **Org** | agilityrobotics |
| **URL** | https://github.com/agilityrobotics |
| **Stars (primary repo)** | cassie-doc: 60 stars |
| **Last active** | 2025-07-15 |

**Description:** Official GitHub for Agility Robotics (maker of Digit humanoid). Primary public repo is cassie-doc (documentation and software release for Cassie biped). Digit's software stack is largely proprietary; minimal open-source contribution.

**Relevance to humanoid medical/healthcare use:**
- Cassie has been used in academic locomotion research (numerous university labs).
- Digit (successor) deployed in Amazon warehouses; no confirmed healthcare use.
- Low open-source activity limits community healthcare research applications.

---

## Category D: Healthcare/Assistive Robotics Specific

### D1. ros4healthcare — SCAI-Lab (ETH Zurich / University of Alberta)

| Field | Value |
|-------|-------|
| **Repo** | SCAI-Lab/ros4healthcare |
| **URL** | https://github.com/SCAI-Lab/ros4healthcare |
| **Stars** | 8 (2026-03-10) |
| **Language** | Python / ROS |
| **License** | Apache 2.0 |
| **Last active** | 2026-02-06 |

**Description:** ROS 4 Healthcare — physiological human sensing for social, assistive, rehabilitation, and medical robotics. Provides ROS packages for integrating physiological sensing (heart rate, respiration, EEG, EMG) into robot control loops for healthcare scenarios.

**Relevance to humanoid medical/healthcare use:**
- Directly designed for medical robotics integration with ROS (the dominant humanoid middleware).
- Physiological sensing integration is necessary for safe human-robot physical interaction in care tasks (monitoring patient state during assisted transfer, rehabilitation exercise monitoring).
- Low star count reflects niche domain; high direct relevance.

---

### D2. Poppy Humanoid — Inria / Flowers Lab

| Field | Value |
|-------|-------|
| **Repo** | poppy-project/poppy-humanoid |
| **URL** | https://github.com/poppy-project/poppy-humanoid |
| **Stars** | 877 (2026-03-10) |
| **Language** | Python |
| **License** | GPL v3 |
| **Last active** | 2026-03-09 |

**Description:** Open-source 3D-printed humanoid robot (58 cm, 25 DOF, Dynamixel actuators) optimized for research and education. Hardware fully open: STL files, BOM, assembly instructions published. Developed at INRIA (Flowers Lab, Bordeaux). Python and ROS compatible.

**Relevance to humanoid medical/healthcare use:**
- Used in social HRI research including autism therapy interaction studies.
- Low-cost fully open hardware enables accessible research in care settings without expensive commercial platforms.
- 3D-printable design allows customization for specific patient interaction needs.

---

### D3. Berkeley Humanoid Lite — HybridRobotics Lab, UC Berkeley

| Field | Value |
|-------|-------|
| **Repo** | HybridRobotics/Berkeley-Humanoid-Lite |
| **URL** | https://github.com/HybridRobotics/Berkeley-Humanoid-Lite |
| **Stars** | 1,243 (2026-03-10) |
| **Language** | Python |
| **License** | MIT |
| **Last active** | 2026-03-09 |

**Description:** Sub-$5,000 open-source full-size humanoid robot featuring modular 3D-printed gearboxes and widely available off-the-shelf components. Full hardware (CAD) and software (RL locomotion policies) open-sourced. Designed for accessibility in academic robotics research.

**Relevance to humanoid medical/healthcare use:**
- Open-source low-cost platform removes cost barrier for healthcare robotics research groups.
- RL-trained locomotion policies (trained in Isaac Lab) enable robust navigation in hospital/home environments.
- Modular design allows targeted modifications for assistive use cases (custom end-effectors, sensors).

---

## Category E: iCub Ecosystem (IIT)

### E1. icub-main — IIT Robotology Group

| Field | Value |
|-------|-------|
| **Repo** | robotology/icub-main |
| **URL** | https://github.com/robotology/icub-main |
| **Stars** | 118 (2026-03-10) |
| **Language** | C++ |
| **License** | LGPL v2.1 |
| **Last active** | 2026-02-23 |

**Description:** Main software repository for the iCub humanoid robot platform. Provides the complete software stack (YARP-based middleware, motor control, vision, tactile processing) for all iCub variants including iCub3.

**Relevance to humanoid medical/healthcare use:**
- iCub is the primary fully open-source humanoid used in cognitive HRI and therapeutic research.
- iCub-HRI extension (robotology/icub-hri) adds perception (object recognition, face/agent tracking, speech, touch), manipulation, and social interaction modules directly applicable to assistive scenarios.
- Full GPL hardware + software release makes it the reference platform for open-source humanoid HRI research.

---

## Summary Table

| Repo | Stars | Category | Direct Medical Relevance | Last Active |
|------|-------|----------|--------------------------|-------------|
| Genesis-Embodied-AI/Genesis | 28,254 | Simulator | Deformable object sim (surgical) | 2026-03-10 |
| huggingface/lerobot | 22,179 | Learning framework | Care task imitation learning; G1/Reachy2 | 2026-03-10 |
| Physical-Intelligence/openpi | 10,551 | Foundation model (VLA) | Generalist manipulation; care task fine-tuning | 2026-03-10 |
| isaac-sim/IsaacLab | 6,544 | Simulator/RL | Humanoid locomotion/manipulation training | 2026-03-10 |
| openvla/openvla | 5,479 | Foundation model (VLA) | Language-conditioned care manipulation | 2026-03-10 |
| unitreerobotics/unitree_rl_gym | 3,022 | RL locomotion | G1/H1 locomotion (hospital navigation) | 2026-03-10 |
| unitreerobotics/xr_teleoperate | 1,309 | Teleoperation | Remote expert nursing/therapy control | 2026-03-10 |
| unitreerobotics/unitree_ros | 1,271 | ROS interface | ROS humanoid integration | 2026-03-10 |
| HybridRobotics/Berkeley-Humanoid-Lite | 1,243 | Open hardware | Low-cost accessible research platform | 2026-03-09 |
| unitreerobotics/unitree_sdk2 | 932 | SDK | G1/H1 communication layer | 2026-03-10 |
| unitreerobotics/unitree_mujoco | 863 | Simulator | Unitree humanoid simulation | 2026-03-10 |
| poppy-project/poppy-humanoid | 877 | Open hardware | Social HRI; ASD therapy research | 2026-03-09 |
| unitreerobotics/unitree_rl_lab | 820 | RL training | Humanoid RL (Isaac Lab-based) | 2026-03-10 |
| unitreerobotics/unitree_lerobot | 568 | Imitation learning | LeRobot-based G1 dual-arm learning | 2026-03-10 |
| unitreerobotics/unifolm-vla | 326 | Foundation model (VLA) | Language-conditioned humanoid manipulation | 2026-03-10 |
| agilityrobotics/cassie-doc | 60 | Documentation | Cassie/Digit platform reference | 2025-07-15 |
| robotology/icub-main | 118 | Robot SW stack | iCub HRI/cognitive/therapeutic research | 2026-02-23 |
| SCAI-Lab/ros4healthcare | 8 | Healthcare sensing | Physiological sensing for medical robots | 2026-02-06 |
