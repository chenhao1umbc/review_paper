"""
Generate figures for the humanoid healthcare review paper.
Run with: uv run python scripts/gen_figures.py
Output: paper/figures/trl_readiness.pdf
         paper/figures/evidence_landscape.pdf
         paper/figures/tech_timeline.pdf
         paper/figures/regulatory_pathways.pdf
         paper/figures/capability_radar.pdf
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
from collections import defaultdict

OUTPUT_DIR = "paper/figures"


def gen_trl_readiness():
    """
    TRL heatmap / domain readiness chart.
    Five clinical domains x TRL scale (1-9).
    """
    domains = [
        "Clinical Procedures",
        "Elderly / Nursing Care\n(bipedal)",
        "Rehabilitation",
        "Mental Health / HRI",
        "Hospital Logistics",
    ]
    trl_low  = [3, 3, 3, 4, 2]
    trl_high = [4, 4, 4, 5, 2]

    fig, ax = plt.subplots(figsize=(10, 5))

    bar_height = 0.5
    y_positions = np.arange(len(domains))
    colors = ["#2c7bb6", "#abd9e9", "#fdae61", "#d7191c", "#a6d96a"]

    for i, (yl, yh, col) in enumerate(zip(trl_low, trl_high, colors)):
        width = max(yh - yl + 1, 0.5)
        ax.barh(y_positions[i], width, left=yl - 0.5, height=bar_height,
                color=col, edgecolor="none", alpha=0.85)
        label = f"TRL {yl}" if yl == yh else f"TRL {yl}-{yh}"
        ax.text(yh + 0.15, y_positions[i], f"  {label}",
                va="center", ha="left", fontsize=10, color="#333333")

    # TRL-5 target line
    ax.axvline(x=4.5, color="#1a1a1a", linestyle="--", linewidth=1.6,
               label="TRL 5 target")
    ax.legend(loc="upper right", fontsize=10, framealpha=0.9)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(domains, fontsize=10)
    ax.set_xlabel("Technology Readiness Level (ISO 16290:2013)", fontsize=11)
    ax.set_xlim(0.5, 10.5)
    ax.set_xticks(range(1, 10))
    ax.xaxis.set_tick_params(labelsize=10)
    ax.set_title(
        "Clinical Domain TRL Assessment: Humanoid Robots in Healthcare (March 2026)",
        fontsize=11, pad=14,
    )
    ax.grid(axis="x", linestyle=":", linewidth=0.6, color="#cccccc")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout(pad=1.5)
    path = f"{OUTPUT_DIR}/trl_readiness.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_evidence_landscape():
    """
    Evidence landscape: 14 papers by domain x year, sized by study type.
    Manual offsets per P-code label; no x-jitter — papers at true publication year.
    Labels P1–P14 correspond to Table 1 in the paper.
    """
    papers = [
        (0, 2025, "P1",  150),
        (0, 2025, "P2",  150),
        (0, 2026, "P3",  180),
        (1, 2024, "P7",  200),
        (1, 2025, "P8",  100),
        (1, 2024, "P9",  120),
        (1, 2024, "P10", 120),
        (2, 2024, "P5",  120),
        (2, 2022, "P6",  200),
        (2, 2025, "P13", 150),
        (3, 2023, "P11", 300),
        (3, 2024, "P14", 150),
        (3, 2025, "P4",  120),
        (3, 2025, "P12", 100),
    ]

    # Manual (xytext_dx_pts, xytext_dy_pts, ha) per label — no automated jitter.
    _offsets = {
        "P1":  ( 15,  14, "left"),
        "P2":  (-15, -14, "right"),
        "P3":  ( 15,  14, "left"),
        "P7":  ( 15,  14, "left"),
        "P9":  (-15, -14, "right"),
        "P10": ( 15,  30, "left"),
        "P8":  (-20,  14, "right"),
        "P5":  ( 15,  14, "left"),
        "P6":  (-15,  14, "right"),
        "P13": ( 15,  14, "left"),
        "P11": (-15,  14, "right"),
        "P14": ( 15,  14, "left"),
        "P4":  (-15,  30, "right"),
        "P12": ( 15, -14, "left"),
    }

    domains = [
        "Clinical\nProcedures",
        "Elderly /\nNursing Care",
        "Rehabilitation",
        "Mental Health\n/ HRI",
    ]

    fig, ax = plt.subplots(figsize=(10, 6.5))

    domain_colors = {0: "#2c7bb6", 1: "#2b8a3e", 2: "#e67700", 3: "#c92a2a"}

    for domain_idx, year, label, size in papers:
        ox, oy, ha_val = _offsets[label]
        ax.scatter(year, domain_idx, s=size,
                   color=domain_colors[domain_idx], edgecolors="#555555",
                   linewidths=0.8, alpha=0.85, zorder=3)
        ax.annotate(label, (year, domain_idx),
                    textcoords="offset points", xytext=(ox, oy),
                    ha=ha_val, fontsize=10, color="#333333",
                    arrowprops=dict(arrowstyle="->", color="#aaaaaa",
                                   lw=0.7, mutation_scale=10))

    ax.set_yticks(range(len(domains)))
    ax.set_yticklabels(domains, fontsize=11)
    ax.set_xlabel("Publication Year", fontsize=11)
    ax.set_xlim(2021.2, 2027.8)
    ax.set_xticks([2022, 2023, 2024, 2025, 2026])
    ax.xaxis.set_tick_params(labelsize=10.5)
    ax.set_ylim(-0.7, len(domains) - 0.3)
    ax.set_title(
        "Evidence Landscape: 14 Qualifying Papers by Domain and Year\n"
        "(bubble size \u221d study design strength: RCT > case series > engineering > pilot;"
        " labels P1\u2013P14 per Table 1)",
        fontsize=10.5, pad=10,
    )

    legend_elements = [
        mpatches.Patch(facecolor=domain_colors[0], label="Clinical Procedures"),
        mpatches.Patch(facecolor=domain_colors[1], label="Elderly / Nursing Care"),
        mpatches.Patch(facecolor=domain_colors[2], label="Rehabilitation"),
        mpatches.Patch(facecolor=domain_colors[3], label="Mental Health / HRI"),
    ]
    ax.legend(handles=legend_elements, loc="lower left",
              bbox_to_anchor=(0.01, 0.01), fontsize=10,
              framealpha=0.9, edgecolor="#cccccc")

    ax.grid(axis="x", linestyle=":", linewidth=0.6, color="#cccccc")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout(pad=1.5)
    path = f"{OUTPUT_DIR}/evidence_landscape.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_tech_timeline():
    """
    Technology timeline: key humanoid milestones + healthcare research events.
    Dual-track horizontal timeline.
    """
    def year_to_x(y):
        """Non-linear year mapping: compress 1996-2022, expand 2022-present."""
        break_year = 2022
        if y <= break_year:
            return (y - 1996) * 0.46
        else:
            return (break_year - 1996) * 0.46 + (y - break_year) * 2.5

    fig, ax = plt.subplots(figsize=(22, 12))

    year_end  = 2026   # last tick mark
    x_shade   = 2026.9 # right edge of era shading
    x_right   = 2027.0 # xlim right boundary (small gap after shading, mirrors left gap)
    ax.set_xlim(year_to_x(1994.5), year_to_x(x_right))
    ax.set_ylim(-6.5, 6.5)
    ax.axis("off")

    # Central axis line
    ax.axhline(0, color="#555555", linewidth=3.0, zorder=1)

    # Platform / technology milestones (above axis)
    # x positions staggered for same-year events to avoid horizontal overlap
    platform_events = [
        (1996,   "Honda P3\nbipedal demo"),
        (2000,   "ASIMO\nlaunched"),
        (2004,   "HRP-2\n(AIST)"),
        (2012,   "DARPA\nRobotics\nChallenge"),
        (2013.6, "Atlas\n(Boston Dynamics)"),
        (2018,   "HRP-5P\n(AIST)"),
        (2022,   "Tesla Optimus\nprototype"),
        (2023,   "Figure 01\nAnnounced"),
        (2023.8, "Unitree G1\nreleased"),
        (2024.6, "Figure 02\n+ BMW pilot"),
        (2025,   "$\\pi_0$\n(Physical Intelligence)"),
        (2026,   "13 commercial\nplatforms"),
    ]
    platform_y = [3.5, 2.8, 2.1, 3.5, 2.8, 2.1, 3.2, 2.0, 5.5, 3.8, 4.8, 2.8]

    # Healthcare research events (below axis)
    health_events = [
        (2003,   "NAO first\npediatric pilot"),
        (2010,   "PARO\nclinical RCT"),
        (2013,   "NAO ASD\ntherapy studies"),
        (2018,   "Pepper dementia\npilot"),
        (2020,   "COVID:\nrobots in hospitals"),
        (2022.5, "SPRING project\n(ARI, Paris)"),
        (2023.5, "RHP Friends\nIREX nursing demo"),
        (2024,   "Unitree G1\nrehab / EEG"),
        (2025,   "Atar et al.\n7 procedures"),
        (2026,   "Cho et al.\nhumanoid surgery"),
    ]
    health_y = [-2.0, -3.0, -2.0, -3.0, -4.0, -1.8, -3.8, -2.5, -1.5, -4.3]

    blue  = "#2166ac"
    green = "#1a9641"

    def draw_event(year, label, y_base, color, fontsize=20):
        x = year_to_x(year)
        ax.plot([x, x], [0, y_base], color=color, linewidth=2.5,
                linestyle="-", zorder=2, alpha=0.6)
        ax.plot(x, y_base, "o", color=color, markersize=10, zorder=3)
        va = "bottom" if y_base > 0 else "top"
        y_text = y_base + (0.18 if y_base > 0 else -0.18)
        ax.text(x, y_text, label, ha="center", va=va,
                fontsize=fontsize, color=color,
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                          edgecolor="none", alpha=0.85),
                zorder=4, clip_on=False)

    for (yr, lbl), yv in zip(platform_events, platform_y):
        draw_event(yr, lbl, yv, blue)

    for (yr, lbl), yv in zip(health_events, health_y):
        draw_event(yr, lbl, yv, green)

    # Era shading
    era_spans = [
        (1995, 2010, "#e8f4f8", "Locomotion era\n(1996-2010)"),
        (2010, 2022, "#fff3cd", "Manipulation era\n(2010-2022)"),
        (2022, x_shade, "#d4edda", "Commercial scale-up\n(2022-present)"),
    ]
    era_label_x = {  # explicit label centres — independent of span boundaries
        "Locomotion era\n(1996-2010)":    year_to_x(2002.5),
        "Manipulation era\n(2010-2022)":  year_to_x(2016),
        "Commercial scale-up\n(2022-present)": year_to_x(2024),
    }
    for xstart, xend, color, label in era_spans:
        ax.axvspan(year_to_x(xstart), year_to_x(xend), alpha=0.28, color=color, zorder=0)
        ax.text(era_label_x[label], -5.8, label, ha="center", va="bottom",
                fontsize=18, color="#444444", style="italic",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="white",
                          edgecolor="none", alpha=0.75),
                clip_on=False, zorder=5)

    # Year ticks on the axis — 4-year intervals in historical zone, 1-year in modern zone
    for yr in range(1996, 2022, 4):
        ax.text(year_to_x(yr), -0.35, str(yr), ha="center", va="top", fontsize=18,
                color="#555555")
        ax.plot([year_to_x(yr), year_to_x(yr)], [-0.14, 0.14], color="#888888", linewidth=1.8)
    for yr in range(2022, 2027, 1):
        ax.text(year_to_x(yr), -0.35, str(yr), ha="center", va="top", fontsize=18,
                color="#555555")
        ax.plot([year_to_x(yr), year_to_x(yr)], [-0.14, 0.14], color="#888888", linewidth=1.8)


    # Legend
    legend_elements = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=blue,
               markersize=9, label="Platform / technology milestones"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor=green,
               markersize=9, label="Healthcare research events"),
    ]
    ax.legend(handles=legend_elements, loc="lower center",
              bbox_to_anchor=(0.5, -0.08), fontsize=24, ncol=2,
              framealpha=0.9, edgecolor="#cccccc")

    ax.set_title(
        "Technology Timeline: Humanoid Robotics and Healthcare Research Events\n"
        "(1996\u20132026; x-axis compressed before 2022, expanded after)",
        fontsize=18, pad=20,
    )

    fig.tight_layout(pad=1.2)
    path = f"{OUTPUT_DIR}/tech_timeline.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_regulatory_pathways():
    """
    Regulatory pathway flowchart: FDA De Novo (US) and EU MDR/AI Act (EU)
    parallel tracks for a clinical humanoid robot.
    """
    fig, ax = plt.subplots(figsize=(7.5, 9.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    def box(ax, x, y, w, h, text, bg="#dce8f5", edge="#2c7bb6",
            fontsize=13, bold=False):
        rect = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                              boxstyle="round,pad=0.1",
                              facecolor=bg, edgecolor=edge, linewidth=1.5,
                              zorder=2)
        ax.add_patch(rect)
        weight = "bold" if bold else "normal"
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
                weight=weight, zorder=3, multialignment="center")

    def arrow(ax, x1, y1, x2, y2, color="#555555"):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=color,
                                   lw=1.4, mutation_scale=14),
                    zorder=2)

    # Column headers
    ax.text(3.0, 8.77, "United States\n— FDA Pathway",
            ha="center", va="center", fontsize=13, weight="bold",
            color="#154360")
    ax.text(9.0, 8.77, "European Union\n— MDR + AI Act",
            ha="center", va="center", fontsize=13, weight="bold",
            color="#145a32")

    # Divider — limited to flow area only, does not touch the critical gap box
    ax.plot([6.0, 6.0], [1.40, 9.0], color="#bbbbbb",
            linewidth=1.5, linestyle="--", zorder=1)

    # Arrow helper values: pad=0.1 (boxstyle), gap=0.03 (breathing room)
    # arrow tail  = box_center - h/2 - 0.13
    # arrow head  = next_box_center + h/2 + 0.13

    # US track (x = 3.0)
    box(ax, 3.0, 8.1, 5.0, 0.65,
        "Clinical Humanoid Robot\n(novel device, no predicate)",
        bg="#d6eaf8", edge="#2874a6", fontsize=13, bold=True)

    arrow(ax, 3.0, 7.645, 3.0, 7.31)   # 8.1-0.325-0.13=7.645 → 6.9+0.28+0.13=7.31
    box(ax, 3.0, 6.9, 5.0, 0.56,
        "510(k): no predicate\nDe Novo (21 CFR 513(f)(2))",
        bg="#eaf4fb", edge="#2874a6")

    arrow(ax, 3.0, 6.49, 3.0, 6.16)    # 6.9-0.28-0.13=6.49 → 5.75+0.28+0.13=6.16
    box(ax, 3.0, 5.75, 5.0, 0.56,
        "Pre-Sub meeting with FDA\n(risk class, evidence plan)",
        bg="#eaf4fb", edge="#2874a6")

    arrow(ax, 3.0, 5.34, 3.0, 5.01)    # 5.75-0.28-0.13=5.34 → 4.60+0.28+0.13=5.01
    box(ax, 3.0, 4.60, 5.0, 0.56,
        "De Novo request submission\n(bench + non-clin. + clinical)",
        bg="#eaf4fb", edge="#2874a6")

    arrow(ax, 3.0, 4.19, 3.0, 3.86)    # 4.60-0.28-0.13=4.19 → 3.45+0.28+0.13=3.86
    box(ax, 3.0, 3.45, 5.0, 0.56,
        "FDA review (~12 months)\nClassification order issued",
        bg="#eaf4fb", edge="#2874a6")

    arrow(ax, 3.0, 3.04, 3.0, 2.71)    # 3.45-0.28-0.13=3.04 → 2.30+0.28+0.13=2.71
    box(ax, 3.0, 2.30, 5.0, 0.56,
        "Market auth. (Class II)\nPost-mkt. surveillance req.",
        bg="#d5f5e3", edge="#1e8449", bold=True, fontsize=11)

    # EU track (x = 9.0) — same y-positions, same offsets
    box(ax, 9.0, 8.1, 5.0, 0.65,
        "Clinical Humanoid Robot\n(novel device, no CE pred.)",
        bg="#d5f5e3", edge="#1e8449", fontsize=13, bold=True)

    arrow(ax, 9.0, 7.645, 9.0, 7.31)
    box(ax, 9.0, 6.9, 5.0, 0.56,
        "EU MDR Class IIb/III\n(Notified Body required)",
        bg="#eafaf1", edge="#1e8449")

    arrow(ax, 9.0, 6.49, 9.0, 6.16)
    box(ax, 9.0, 5.75, 5.0, 0.56,
        "EU AI Act: High-Risk AI\n(Art. 6; conformity Aug 2026)",
        bg="#fef9e7", edge="#d4ac0d")

    arrow(ax, 9.0, 5.34, 9.0, 5.01)
    box(ax, 9.0, 4.60, 5.0, 0.56,
        "Clinical invest. MDR Art. 62\n(Competent Auth. + ethics)",
        bg="#eafaf1", edge="#1e8449")

    arrow(ax, 9.0, 4.19, 9.0, 3.86)
    box(ax, 9.0, 3.45, 5.0, 0.56,
        "CE marking by Notified Body\n+ AI Act declaration",
        bg="#eafaf1", edge="#1e8449")

    arrow(ax, 9.0, 3.04, 9.0, 2.71)
    box(ax, 9.0, 2.30, 5.0, 0.56,
        "EU market authorization\nPost-mkt. follow-up (PMCF)",
        bg="#d5f5e3", edge="#1e8449", bold=True, fontsize=11)

    # Gap annotation — explicit line breaks, width fits within xlim 0-12
    box(ax, 6.0, 0.9, 11.5, 0.70,
        "Critical gap (both tracks): no safety standard for\n"
        "bipedal gait in patient-proximate environments\n"
        "(ISO 13482 excl. medical devices; ISO/TS 15066: fixed-base arms)",
        bg="#fdebd0", edge="#e67e22", fontsize=13)

    ax.set_title(
        "Regulatory Pathways for Clinical Humanoid Robots: FDA (US) vs. EU MDR + AI Act",
        fontsize=13, pad=8,
    )

    fig.tight_layout(pad=1.2)
    path = f"{OUTPUT_DIR}/regulatory_pathways.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_capability_radar():
    """
    Capability gap radar chart: current state vs. required thresholds.
    """
    categories = [
        "Force\nPrecision",
        "Gait\nSafety",
        "Tactile\nSensing",
        "Tool Kinematics",
        "AI\nGeneralization",
        "Clinical\nValidation",
    ]
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    current           = [4, 3, 3, 4, 5, 1]
    required_clinical = [8, 7, 7, 8, 7, 8]
    required_elderly  = [5, 8, 6, 5, 7, 7]

    current           += current[:1]
    required_clinical += required_clinical[:1]
    required_elderly  += required_elderly[:1]

    fig, ax = plt.subplots(figsize=(9, 8), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=10, color="#888888")
    ax.tick_params(axis="y", labelsize=10)

    ax.plot(angles, current, "o-", linewidth=2.2, color="#2166ac",
            label="Current state (best commercial, 2026)")
    ax.fill(angles, current, alpha=0.15, color="#2166ac")

    ax.plot(angles, required_clinical, "s--", linewidth=2.2, color="#d73027",
            label="Required: clinical procedures")
    ax.fill(angles, required_clinical, alpha=0.08, color="#d73027")

    ax.plot(angles, required_elderly, "^--", linewidth=2.2, color="#1a9641",
            label="Required: elderly / nursing care")
    ax.fill(angles, required_elderly, alpha=0.08, color="#1a9641")

    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25),
              ncol=1, fontsize=10, framealpha=0.9, edgecolor="#cccccc")

    ax.set_title(
        "Capability Gap: Current State vs.\nRequired Thresholds for Clinical Deployment",
        fontsize=11, pad=22,
    )

    fig.tight_layout(pad=1.5)
    path = f"{OUTPUT_DIR}/capability_radar.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    gen_trl_readiness()
    gen_evidence_landscape()
    gen_tech_timeline()
    gen_regulatory_pathways()
    gen_capability_radar()
    print("All figures generated successfully.")
