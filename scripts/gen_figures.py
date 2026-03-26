"""
Generate figures for the humanoid healthcare review paper.
Run with: uv run python scripts/gen_figures.py
Output: paper/figures/trl_readiness.pdf
         paper/figures/evidence_landscape.pdf
         paper/figures/tech_timeline.pdf
         paper/figures/regulatory_pathways.pdf
         paper/figures/capability_gap.pdf
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
    TRL horizontal bar chart: five clinical domains.
    Single bar color; per-domain binding constraint annotation.
    """
    import matplotlib as mpl
    mpl.rcParams.update({
        "font.size": 16,
        "axes.titlesize": 14,
        "axes.labelsize": 14,
        "xtick.labelsize": 13,
        "ytick.labelsize": 14,
    })

    domains = [
        "Clinical Procedures",
        "Elderly / Nursing Care\n(bipedal)",
        "Rehabilitation",
        "Mental Health / HRI",
        "Hospital Logistics",
    ]
    trl_low  = [3, 3, 3, 4, 2]
    trl_high = [4, 4, 4, 5, 2]
    constraints = [
        "force precision, no predicate",
        "no care facility pilot",
        "no patient trial",
        "platform unspecified",
        "wheeled systems preferred",
    ]

    fig, ax = plt.subplots(figsize=(6, 4.8))

    bar_height  = 0.5
    y_positions = np.arange(len(domains))
    bar_color   = "#2c7bb6"

    for i, (yl, yh) in enumerate(zip(trl_low, trl_high)):
        width = max(yh - yl + 1, 0.5)
        ax.barh(y_positions[i], width, left=yl - 0.5, height=bar_height,
                color=bar_color, edgecolor="none", alpha=0.85)
        xh = yh + 0.5
        ax.text(xh + 0.2, y_positions[i], constraints[i],
                va="center", ha="left", fontsize=11, color="#444444")

    ax.axvline(x=4.5, color="#1a1a1a", linestyle="--", linewidth=1.6)
    ax.text(4.62, 4.62, "TRL 5\ntarget", ha="left", va="bottom",
            fontsize=11, color="#1a1a1a", linespacing=1.2)

    ax.set_ylim(-0.5, 5.5)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(domains)
    ax.set_xlabel("Technology Readiness Level (ISO 16290:2013)")
    ax.set_xlim(0.5, 13)
    ax.set_xticks(range(1, 10))
    ax.set_title("TRL assessment by clinical domain (March 2026)", pad=10)
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
    Evidence distribution: 14 papers by domain x year.
    Dot matrix; shape encodes study type; no bubble sizes.
    Colliding points (same domain + year) offset vertically by 0.15 per slot.
    """
    import matplotlib as mpl
    from collections import Counter
    mpl.rcParams.update({
        "font.size": 14,
        "axes.titlesize": 14,
        "axes.labelsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12,
    })

    # (domain_idx, year, surname, study_type)
    # study_type: "eng"=engineering/lab/feasibility,
    #             "obs"=case series/observational,
    #             "rct"=RCT/comparative
    papers = [
        (0, 2025, "Atar",           "eng"),
        (0, 2025, "Liang",          "eng"),
        (0, 2026, "Cho",            "obs"),
        (1, 2024, "Alameda-Pineda", "obs"),
        (1, 2025, "Benallegue",     "eng"),
        (1, 2024, "Imtiaz",         "eng"),
        (1, 2024, "Ghosh",          "eng"),
        (2, 2024, "Nguyen",         "eng"),
        (2, 2022, "Sobrepera",      "obs"),
        (2, 2025, "Lu",             "eng"),
        (3, 2023, "Robinson",       "rct"),
        (3, 2024, "Sayis",          "obs"),
        (3, 2025, "Yuan",           "eng"),
        (3, 2025, "Lindsay",        "eng"),
    ]

    domains = [
        "Clinical\nProcedures",
        "Elderly /\nNursing Care",
        "Rehabilitation",
        "Mental Health\n/ HRI",
    ]

    domain_colors = {0: "#2c7bb6", 1: "#2b8a3e", 2: "#e67700", 3: "#c92a2a"}
    shape_markers  = {"eng": "o", "obs": "D", "rct": "*"}
    marker_sizes   = {"eng": 80,  "obs": 80,  "rct": 130}

    fig, ax = plt.subplots(figsize=(9, 4))

    coord_count = Counter((d, y) for d, y, _, _ in papers)
    coord_idx   = defaultdict(int)

    for domain_idx, year, surname, stype in papers:
        key   = (domain_idx, year)
        idx   = coord_idx[key]
        total = coord_count[key]
        y_off    = (idx - (total - 1) / 2.0) * 0.45
        x_jitter = (idx - (total - 1) / 2.0) * 0.12
        coord_idx[key] += 1

        ax.scatter(year + x_jitter, domain_idx + y_off,
                   s=marker_sizes[stype], marker=shape_markers[stype],
                   color=domain_colors[domain_idx],
                   edgecolors="#555555" if stype != "rct" else "none",
                   linewidths=0.8, alpha=0.9, zorder=3)
        if total == 1:
            ax.text(year, domain_idx + 0.18, surname,
                    ha="center", va="bottom", fontsize=9, color="#333333")
        else:
            ax.text(year + x_jitter + 0.15, domain_idx + y_off, surname,
                    ha="left", va="center", fontsize=9, color="#333333")

    ax.set_yticks(range(len(domains)))
    ax.set_yticklabels(domains)
    ax.set_xlabel("Publication Year")
    ax.set_xlim(2021.0, 2027.5)
    ax.set_xticks([2022, 2023, 2024, 2025, 2026])
    ax.set_ylim(-0.85, len(domains) - 0.15)
    ax.set_title("Evidence distribution: 14 papers, 2022\u20132026")

    legend_elements = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#888888",
               markeredgecolor="#555555", markersize=8,
               label="Engineering / lab"),
        Line2D([0], [0], marker="D", color="w", markerfacecolor="#888888",
               markeredgecolor="#555555", markersize=8,
               label="Case series / observational"),
        Line2D([0], [0], marker="*", color="w", markerfacecolor="#888888",
               markersize=11, label="RCT / comparative"),
        mpatches.Patch(facecolor=domain_colors[0], label="Clinical Procedures"),
        mpatches.Patch(facecolor=domain_colors[1], label="Elderly / Nursing Care"),
        mpatches.Patch(facecolor=domain_colors[2], label="Rehabilitation"),
        mpatches.Patch(facecolor=domain_colors[3], label="Mental Health / HRI"),
    ]
    ax.legend(handles=legend_elements, loc="lower center",
              bbox_to_anchor=(0.5, -0.58), fontsize=10, ncol=4,
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


def gen_capability_gap():
    """
    Capability gap: horizontal grouped bar chart (current vs. required for TRL 5).
    Title: Humanoid Capability Gap: Current vs. Required for Clinical Deployment
    Axes: six capability dimensions, scale 0-10.
    """
    import matplotlib as mpl
    mpl.rcParams.update({
        "font.size": 14,
        "axes.titlesize": 16,
        "axes.labelsize": 14,
        "xtick.labelsize": 13,
        "ytick.labelsize": 14,
        "legend.fontsize": 13,
    })

    dimensions = [
        "Manipulation Precision",
        "Bipedal Gait Stability",
        "LLM/VLA Task\nGeneralization",
        "Contact Safety",
        "Regulatory Compliance\nReadiness",
        "Human Trust Score",
    ]
    current  = [4, 5, 5, 3, 2, 5]
    required = [8, 7, 7, 8, 8, 7]

    n = len(dimensions)
    y = np.arange(n)
    bar_height = 0.35

    fig, ax = plt.subplots(figsize=(11, 6))

    bars_req = ax.barh(y + bar_height / 2, required, height=bar_height,
                       color="#f4a261", label="Required (TRL 5)", zorder=3)
    bars_cur = ax.barh(y - bar_height / 2, current, height=bar_height,
                       color="#2166ac", label="Current (best commercial, 2026)", zorder=3)

    for bar, val in zip(bars_req, required):
        ax.text(val + 0.15, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", ha="left", fontsize=13, color="#333333")
    for bar, val in zip(bars_cur, current):
        ax.text(val + 0.15, bar.get_y() + bar.get_height() / 2,
                str(val), va="center", ha="left", fontsize=13, color="#333333")

    ax.set_yticks(y)
    ax.set_yticklabels(dimensions)
    ax.set_xlim(0, 11)
    ax.set_xlabel("Score (0-10)")
    ax.set_title("Humanoid Capability Gap: Current vs. Required for Clinical Deployment",
                 pad=12)
    ax.axvline(x=7, color="#aaaaaa", linewidth=0.8, linestyle="--", zorder=2)
    ax.legend(loc="lower right", framealpha=0.9)
    ax.grid(axis="x", linewidth=0.5, color="#dddddd", zorder=1)
    ax.set_axisbelow(True)
    ax.invert_yaxis()

    fig.tight_layout(pad=1.5)
    path = f"{OUTPUT_DIR}/capability_gap.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


if __name__ == "__main__":
    gen_trl_readiness()
    gen_evidence_landscape()
    gen_tech_timeline()
    gen_regulatory_pathways()
    gen_capability_gap()
    print("All figures generated successfully.")
