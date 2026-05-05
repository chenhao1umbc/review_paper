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
import matplotlib as mpl
import numpy as np
from matplotlib.patches import FancyBboxPatch
from matplotlib.lines import Line2D
from collections import defaultdict, Counter

OUTPUT_DIR = "paper/figures"

# --- Publication style foundation ---
PALETTE = {
    "primary": "#2166ac",
    "secondary": "#4dac26",
    "accent": "#d6604d",
    "neutral": "#636363",
    "subtle": "#f7f7f7",
    "gold": "#f4a261",
}

mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 14,
        "axes.titlesize": 16,
        "axes.labelsize": 14,
        "xtick.labelsize": 12,
        "ytick.labelsize": 12,
        "legend.fontsize": 12,
        "legend.title_fontsize": 13,
        "figure.titlesize": 18,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "axes.grid": True,
        "grid.color": "#d0d0d0",
        "grid.linewidth": 0.5,
        "grid.linestyle": "--",
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "axes.prop_cycle": mpl.cycler(
            color=["#2166ac", "#4dac26", "#d6604d", "#f4a261", "#636363"]
        ),
    }
)

# Shared domain colors — consistent across all figures
DOMAIN_COLORS = {
    "Clinical Procedures": "#2166ac",
    "Elderly / Nursing Care": "#4dac26",
    "Rehabilitation": "#d6604d",
    "Mental Health / HRI": "#f4a261",
    "Hospital Logistics": "#636363",
}


def gen_trl_readiness():
    """
    TRL horizontal bar chart: five clinical domains.
    figsize=(6, 4.8) used as width=\\columnwidth (~170mm single-col).
    Rendered scale ≈ 1.12 — fontsize=12 → ~13.4pt rendered.
    """
    domains = [
        "Clinical Procedures",
        "Elderly / Nursing Care\n(bipedal)",
        "Rehabilitation",
        "Mental Health / HRI",
        "Hospital Logistics",
    ]
    domain_keys = [
        "Clinical Procedures",
        "Elderly / Nursing Care",
        "Rehabilitation",
        "Mental Health / HRI",
        "Hospital Logistics",
    ]
    trl_low = [3, 3, 3, 4, 2]
    trl_high = [4, 4, 4, 5, 2]
    constraints = [
        "force precision, no predicate",
        "no care facility pilot",
        "no patient trial",
        "platform unspecified",
        "wheeled systems preferred",
    ]

    fig, ax = plt.subplots(figsize=(6, 4.8))

    bar_height = 0.5
    y_positions = np.arange(len(domains))

    for i, (yl, yh) in enumerate(zip(trl_low, trl_high)):
        color = DOMAIN_COLORS[domain_keys[i]]
        width = max(yh - yl + 1, 0.5)
        ax.barh(
            y_positions[i],
            width,
            left=yl - 0.5,
            height=bar_height,
            color=color,
            edgecolor="none",
            alpha=0.85,
        )
        xh = yh + 0.5
        ax.text(
            xh + 0.2,
            y_positions[i],
            constraints[i],
            va="center",
            ha="left",
            fontsize=11,
            color="#444444",
        )

    ax.axvline(x=4.5, color="#1a1a1a", linestyle="--", linewidth=1.6)
    ax.text(
        4.62,
        4.62,
        "TRL 5\ntarget",
        ha="left",
        va="bottom",
        fontsize=11,
        color="#1a1a1a",
        linespacing=1.2,
    )

    ax.set_ylim(-0.5, 5.5)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(domains, fontsize=12)
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
    Dot matrix; shape = study type; color = domain.
    figsize=(9, 4) at width=\\textwidth (~170mm).
    Rendered scale ≈ 0.744 — fontsize=14 → ~10.4pt rendered for labels.
    """
    papers = [
        (0, 2025, "Atar", "eng"),
        (0, 2025, "Liang", "eng"),
        (0, 2026, "Cho", "obs"),
        (1, 2024, "Alameda-Pineda", "obs"),
        (1, 2025, "Benallegue", "eng"),
        (1, 2024, "Imtiaz", "eng"),
        (1, 2024, "Ghosh", "eng"),
        (2, 2024, "Nguyen", "eng"),
        (2, 2022, "Sobrepera", "obs"),
        (2, 2025, "Lu", "eng"),
        (3, 2023, "Robinson", "rct"),
        (3, 2024, "Sayis", "obs"),
        (3, 2025, "Yuan", "eng"),
        (3, 2025, "Lindsay", "eng"),
    ]

    domain_labels = [
        "Clinical\nProcedures",
        "Elderly /\nNursing Care",
        "Rehabilitation",
        "Mental Health\n/ HRI",
    ]
    domain_color_list = [
        DOMAIN_COLORS["Clinical Procedures"],
        DOMAIN_COLORS["Elderly / Nursing Care"],
        DOMAIN_COLORS["Rehabilitation"],
        DOMAIN_COLORS["Mental Health / HRI"],
    ]

    shape_markers = {"eng": "o", "obs": "D", "rct": "*"}
    marker_sizes = {"eng": 80, "obs": 80, "rct": 130}

    fig, ax = plt.subplots(figsize=(9, 4))

    coord_count = Counter((d, y) for d, y, _, _ in papers)
    coord_idx = defaultdict(int)

    for domain_idx, year, surname, stype in papers:
        key = (domain_idx, year)
        idx = coord_idx[key]
        total = coord_count[key]
        y_off = (idx - (total - 1) / 2.0) * 0.45
        x_jitter = (idx - (total - 1) / 2.0) * 0.12
        coord_idx[key] += 1

        ax.scatter(
            year + x_jitter,
            domain_idx + y_off,
            s=marker_sizes[stype],
            marker=shape_markers[stype],
            color=domain_color_list[domain_idx],
            edgecolors="#555555" if stype != "rct" else "none",
            linewidths=0.8,
            alpha=0.9,
            zorder=3,
        )
        if total == 1:
            ax.text(
                year,
                domain_idx + 0.22,
                surname,
                ha="center",
                va="bottom",
                fontsize=14,
                color="#333333",
            )
        else:
            ax.text(
                year + x_jitter + 0.15,
                domain_idx + y_off,
                surname,
                ha="left",
                va="center",
                fontsize=14,
                color="#333333",
            )

    ax.set_yticks(range(len(domain_labels)))
    ax.set_yticklabels(domain_labels, fontsize=14)
    ax.set_xlabel("Publication Year")
    ax.set_xlim(2021.0, 2027.5)
    ax.set_xticks([2022, 2023, 2024, 2025, 2026])
    ax.set_ylim(-0.85, len(domain_labels) - 0.15)
    ax.set_title("Evidence distribution: 14 papers, 2022\u20132026")

    study_handles = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor="#888888",
            markeredgecolor="#555555",
            markersize=8,
            label="Engineering / lab",
            linestyle="None",
        ),
        Line2D(
            [0],
            [0],
            marker="D",
            color="w",
            markerfacecolor="#888888",
            markeredgecolor="#555555",
            markersize=8,
            label="Case series / observational",
            linestyle="None",
        ),
        Line2D(
            [0],
            [0],
            marker="*",
            color="w",
            markerfacecolor="#888888",
            markersize=11,
            label="RCT / comparative",
            linestyle="None",
        ),
    ]
    domain_handles = [
        mpatches.Patch(facecolor=domain_color_list[0], label="Clinical Procedures"),
        mpatches.Patch(facecolor=domain_color_list[1], label="Elderly / Nursing Care"),
        mpatches.Patch(facecolor=domain_color_list[2], label="Rehabilitation"),
        mpatches.Patch(facecolor=domain_color_list[3], label="Mental Health / HRI"),
    ]
    leg1 = ax.legend(
        handles=study_handles,
        loc="upper left",
        bbox_to_anchor=(0, -0.22),
        title="Study type",
        frameon=True,
        framealpha=0.9,
        fontsize=13,
        title_fontsize=14,
    )
    ax.add_artist(leg1)
    ax.legend(
        handles=domain_handles,
        loc="upper right",
        bbox_to_anchor=(1, -0.22),
        title="Domain",
        frameon=True,
        framealpha=0.9,
        fontsize=13,
        title_fontsize=14,
    )

    ax.grid(axis="x", linestyle=":", linewidth=0.6, color="#cccccc")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.subplots_adjust(bottom=0.32)
    path = f"{OUTPUT_DIR}/evidence_landscape.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_tech_timeline():
    """
    Technology timeline: dual-track horizontal stem plot.
    figsize=(22, 20) at width=\\textwidth (~170mm).
    Rendered scale ≈ 0.304 — fontsize=36 → ~10.9pt; year ticks fontsize=36 → ~10.9pt.
    Era fills use alpha=0.06 (barely visible, scientific publication style).
    Break marker '//' at x=2022 to denote compressed/expanded scale transition.
    """

    def year_to_x(y):
        break_year = 2022
        if y <= break_year:
            return (y - 1996) * 0.46
        return (break_year - 1996) * 0.46 + (y - break_year) * 2.5

    fig, ax = plt.subplots(figsize=(22, 20))

    x_right = 2027.0
    ax.set_xlim(year_to_x(1994.5), year_to_x(x_right))
    ax.set_ylim(-10.5, 10.5)
    ax.axis("off")

    # Main timeline axis
    ax.axhline(0, color="#555555", linewidth=3.0, zorder=1)

    platform_events = [
        (1996, "Honda P3\nbipedal demo"),
        (2000, "ASIMO\nlaunched"),
        (2004, "HRP-2\n(AIST)"),
        (2012, "DARPA\nRobotics\nChallenge"),
        (2013.6, "Atlas\n(Boston Dynamics)"),
        (2018, "HRP-5P\n(AIST)"),
        (2022, "Tesla Optimus\nprototype"),
        (2023, "Figure 01\nAnnounced"),
        (2023.8, "Unitree G1\nreleased"),
        (2024.6, "Figure 02\n+ BMW pilot"),
        (2025, "$\\pi_0$\n(Physical Intelligence)"),
        (2026, "13 commercial\nplatforms"),
    ]
    platform_y = [4.0, 3.0, 2.0, 6.5, 5.0, 3.5, 5.0, 3.0, 9.0, 7.0, 8.5, 5.5]

    health_events = [
        (2003, "NAO first\npediatric pilot"),
        (2010, "PARO\nclinical RCT"),
        (2013, "NAO ASD\ntherapy studies"),
        (2018, "Pepper dementia\npilot"),
        (2020, "COVID:\nrobots in hospitals"),
        (2022.5, "SPRING project\n(ARI, Paris)"),
        (2023.5, "RHP Friends\nIREX nursing demo"),
        (2024, "Unitree G1\nrehab / EEG"),
        (2025, "Atar et al.\n7 procedures"),
        (2026, "Cho et al.\nhumanoid surgery"),
    ]
    health_y = [-2.5, -4.0, -2.5, -4.5, -6.0, -2.5, -5.5, -3.5, -2.0, -7.0]

    blue = "#2166ac"
    green = "#1a9641"

    def draw_event(year, label, y_base, color, fontsize=36):
        x = year_to_x(year)
        ax.plot(
            [x, x],
            [0, y_base],
            color=color,
            linewidth=2.5,
            linestyle="-",
            zorder=2,
            alpha=0.6,
        )
        ax.plot(x, y_base, "o", color=color, markersize=10, zorder=3)
        va = "bottom" if y_base > 0 else "top"
        y_text = y_base + (0.18 if y_base > 0 else -0.18)
        ax.text(
            x,
            y_text,
            label,
            ha="center",
            va=va,
            fontsize=fontsize,
            color=color,
            bbox=dict(
                boxstyle="round,pad=0.2",
                facecolor="white",
                edgecolor="none",
                alpha=0.85,
            ),
            zorder=4,
            clip_on=False,
        )

    for (yr, lbl), yv in zip(platform_events, platform_y):
        draw_event(yr, lbl, yv, blue)

    for (yr, lbl), yv in zip(health_events, health_y):
        draw_event(yr, lbl, yv, green)

    # Era fills — alpha=0.06 only (scientific publication standard)
    era_spans = [
        (1995, 2010, "#c6dbef", "Locomotion era\n(1996-2010)"),
        (2010, 2022, "#fdd0a2", "Manipulation era\n(2010-2022)"),
        (2022, 2026.9, "#c7e9c0", "Commercial scale-up\n(2022-present)"),
    ]
    era_label_x = {
        "Locomotion era\n(1996-2010)": year_to_x(2002.5),
        "Manipulation era\n(2010-2022)": year_to_x(2016),
        "Commercial scale-up\n(2022-present)": year_to_x(2024),
    }
    for xstart, xend, color, label in era_spans:
        ax.axvspan(
            year_to_x(xstart), year_to_x(xend), alpha=0.06, color=color, zorder=0
        )
        ax.text(
            era_label_x[label],
            -9.5,
            label,
            ha="center",
            va="bottom",
            fontsize=34,
            color="#444444",
            style="italic",
            bbox=dict(
                boxstyle="round,pad=0.2",
                facecolor="white",
                edgecolor="none",
                alpha=0.75,
            ),
            clip_on=False,
            zorder=5,
        )

    # Year ticks
    for yr in range(1996, 2022, 4):
        ax.text(
            year_to_x(yr),
            -0.50,
            str(yr),
            ha="center",
            va="top",
            fontsize=36,
            color="#555555",
        )
        ax.plot(
            [year_to_x(yr), year_to_x(yr)],
            [-0.16, 0.16],
            color="#888888",
            linewidth=1.8,
        )
    for yr in range(2022, 2027, 1):
        ax.text(
            year_to_x(yr),
            -0.50,
            str(yr),
            ha="center",
            va="top",
            fontsize=36,
            color="#555555",
        )
        ax.plot(
            [year_to_x(yr), year_to_x(yr)],
            [-0.16, 0.16],
            color="#888888",
            linewidth=1.8,
        )

    # '//' break marker at 2022 to signal compressed→expanded scale
    bx = year_to_x(2022)
    for offset in (-0.15, 0.15):
        ax.plot(
            [bx + offset - 0.05, bx + offset + 0.05],
            [-0.30, 0.30],
            color="#888888",
            linewidth=2.0,
            zorder=5,
        )

    legend_elements = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=blue,
            markersize=9,
            label="Platform / technology milestones",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=green,
            markersize=9,
            label="Healthcare research events",
        ),
    ]
    ax.legend(
        handles=legend_elements,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.08),
        fontsize=34,
        ncol=2,
        framealpha=0.9,
        edgecolor="#cccccc",
    )

    ax.set_title(
        "Technology Timeline: Humanoid Robotics and Healthcare Research Events\n"
        "(1996\u20132026; x-axis compressed before 2022, expanded after)",
        fontsize=34,
        pad=20,
    )

    fig.tight_layout(pad=2.0)
    path = f"{OUTPUT_DIR}/tech_timeline.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_regulatory_pathways():
    """
    Regulatory pathway flowchart: FDA De Novo (US) and EU MDR/AI Act (EU).
    figsize=(7.5, 9.0) at width=\\textwidth (~170mm).
    Rendered scale ≈ 170/(7.5*25.4) = 0.89 — fontsize=16 → ~14.3pt rendered.
    Boxes on explicit grid. Column headers colored bold outside any box.
    """
    col_us = 3.0
    col_eu = 9.0
    col_mid = 6.0
    box_w = 5.0
    row_y = [8.1, 6.9, 5.7, 4.5, 3.3, 2.1]
    row_h = [0.65, 0.56, 0.56, 0.56, 0.56, 0.56]

    fig, ax = plt.subplots(figsize=(7.5, 9.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    def box(cx, row_idx, text, bg="#dce8f5", edge="#2166ac", fontsize=16, bold=False):
        cy = row_y[row_idx]
        h = row_h[row_idx]
        rect = FancyBboxPatch(
            (cx - box_w / 2, cy - h / 2),
            box_w,
            h,
            boxstyle="round,pad=0.1",
            facecolor=bg,
            edgecolor=edge,
            linewidth=1.5,
            zorder=2,
        )
        ax.add_patch(rect)
        weight = "bold" if bold else "normal"
        ax.text(
            cx,
            cy,
            text,
            ha="center",
            va="center",
            fontsize=fontsize,
            weight=weight,
            zorder=3,
            multialignment="center",
        )

    def arrow(cx, from_row, to_row, color="#555555"):
        y1 = row_y[from_row] - row_h[from_row] / 2 - 0.13
        y2 = row_y[to_row] + row_h[to_row] / 2 + 0.13
        ax.annotate(
            "",
            xy=(cx, y2),
            xytext=(cx, y1),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, mutation_scale=14),
            zorder=2,
        )

    # Column headers — bold, colored
    ax.text(
        col_us,
        8.77,
        "United States\n\u2014 FDA Pathway",
        ha="center",
        va="center",
        fontsize=16,
        weight="bold",
        color="#2166ac",
    )
    ax.text(
        col_eu,
        8.77,
        "European Union\n\u2014 MDR + AI Act",
        ha="center",
        va="center",
        fontsize=16,
        weight="bold",
        color="#1e8449",
    )

    # Vertical divider
    ax.plot(
        [col_mid, col_mid],
        [1.40, 9.0],
        color="#bbbbbb",
        linewidth=1.5,
        linestyle="--",
        zorder=1,
    )

    # US track
    box(
        col_us,
        0,
        "Clinical Humanoid Robot\n(novel device,\nno predicate)",
        bg="#d6eaf8",
        edge="#2166ac",
        bold=True,
        fontsize=13,
    )
    arrow(col_us, 0, 1)
    box(
        col_us,
        1,
        "510(k): no predicate\nDe Novo (21 CFR 513(f)(2))",
        bg="#eaf4fb",
        edge="#2166ac",
    )
    arrow(col_us, 1, 2)
    box(
        col_us,
        2,
        "Pre-Sub meeting with FDA\n(risk class, evidence plan)",
        bg="#eaf4fb",
        edge="#2166ac",
    )
    arrow(col_us, 2, 3)
    box(
        col_us,
        3,
        "De Novo request submission\n(bench + non-clin. + clinical)",
        bg="#eaf4fb",
        edge="#2166ac",
    )
    arrow(col_us, 3, 4)
    box(
        col_us,
        4,
        "FDA review (~12 months)\nClassification order issued",
        bg="#eaf4fb",
        edge="#2166ac",
    )
    arrow(col_us, 4, 5)
    box(
        col_us,
        5,
        "Market auth. (Class II)\nPost-mkt. surveillance req.",
        bg="#d5f5e3",
        edge="#1e8449",
        bold=True,
        fontsize=14,
    )

    # EU track
    box(
        col_eu,
        0,
        "Clinical Humanoid Robot\n(novel device,\nno CE pred.)",
        bg="#d5f5e3",
        edge="#1e8449",
        bold=True,
        fontsize=13,
    )
    arrow(col_eu, 0, 1, color="#1e8449")
    box(
        col_eu,
        1,
        "EU MDR Class IIb/III\n(Notified Body required)",
        bg="#eafaf1",
        edge="#1e8449",
    )
    arrow(col_eu, 1, 2, color="#1e8449")
    box(
        col_eu,
        2,
        "EU AI Act: High-Risk AI\n(Art. 6; conformity Aug 2026)",
        bg="#fef9e7",
        edge="#d4ac0d",
    )
    arrow(col_eu, 2, 3, color="#1e8449")
    box(
        col_eu,
        3,
        "Clinical invest. MDR Art. 62\n(Competent Auth. + ethics)",
        bg="#eafaf1",
        edge="#1e8449",
    )
    arrow(col_eu, 3, 4, color="#1e8449")
    box(
        col_eu,
        4,
        "CE marking by Notified Body\n+ AI Act declaration",
        bg="#eafaf1",
        edge="#1e8449",
    )
    arrow(col_eu, 4, 5, color="#1e8449")
    box(
        col_eu,
        5,
        "EU market authorization\nPost-mkt. follow-up (PMCF)",
        bg="#d5f5e3",
        edge="#1e8449",
        bold=True,
        fontsize=14,
    )

    # Gap banner — full width
    gap_h = 0.70
    gap_y = 0.9
    rect = FancyBboxPatch(
        (0.25, gap_y - gap_h / 2),
        11.5,
        gap_h,
        boxstyle="round,pad=0.1",
        facecolor="#fdebd0",
        edgecolor="#e67e22",
        linewidth=1.5,
        zorder=2,
    )
    ax.add_patch(rect)
    ax.text(
        col_mid,
        gap_y,
        "Critical gap (both tracks): no safety standard for\n"
        "bipedal gait in patient-proximate environments\n"
        "(ISO 13482 excl. medical devices; ISO/TS 15066: fixed-base arms)",
        ha="center",
        va="center",
        fontsize=13,
        zorder=3,
        multialignment="center",
    )

    ax.set_title(
        "Regulatory Pathways for Clinical Humanoid Robots: FDA (US) vs. EU MDR + AI Act",
        fontsize=14,
        pad=8,
    )

    fig.tight_layout(pad=1.2)
    path = f"{OUTPUT_DIR}/regulatory_pathways.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_capability_gap():
    """
    Capability gap: grouped horizontal bar chart (current vs. TRL-5 required).
    figsize=(11, 6) at width=\\columnwidth (~170mm).
    Rendered scale ≈ 170/(11*25.4) = 0.608 — fontsize=17 → ~10.3pt for value labels.
    Legend below plot, outside axes.
    """
    dimensions = [
        "Manipulation Precision",
        "Bipedal Gait Stability",
        "LLM/VLA Task\nGeneralization",
        "Contact Safety",
        "Regulatory Compliance\nReadiness",
        "Human Trust Score",
    ]
    current = [4, 5, 5, 3, 2, 5]
    required = [8, 7, 7, 8, 8, 7]

    n = len(dimensions)
    y = np.arange(n)
    bar_height = 0.35

    fig, ax = plt.subplots(figsize=(11, 6))

    bars_req = ax.barh(
        y + bar_height / 2,
        required,
        height=bar_height,
        color=PALETTE["gold"],
        label="Required (TRL 5)",
        zorder=3,
    )
    bars_cur = ax.barh(
        y - bar_height / 2,
        current,
        height=bar_height,
        color=PALETTE["primary"],
        label="Current (best commercial, 2026)",
        zorder=3,
    )

    for bar, val in zip(bars_req, required):
        ax.text(
            val + 0.15,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            ha="left",
            fontsize=17,
            color="#333333",
        )
    for bar, val in zip(bars_cur, current):
        ax.text(
            val + 0.15,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            ha="left",
            fontsize=17,
            color="#333333",
        )

    ax.set_yticks(y)
    ax.set_yticklabels(dimensions, fontsize=17)
    ax.set_xlim(0, 11)
    ax.set_xlabel("Score (0\u201310)")
    ax.set_title(
        "Humanoid Capability Gap: Current vs. Required for Clinical Deployment", pad=12
    )
    ax.axvline(x=7, color="#aaaaaa", linewidth=0.8, linestyle="--", zorder=2)
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.10),
        ncol=2,
        framealpha=0.9,
        fontsize=15,
    )
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
