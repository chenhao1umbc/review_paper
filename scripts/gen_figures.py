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

PALETTE = {
    "primary": "#0072B2",   # Okabe-Ito blue
    "secondary": "#009E73", # Okabe-Ito teal
    "accent": "#D55E00",    # Okabe-Ito vermillion
    "neutral": "#56B4E9",   # Okabe-Ito sky blue
    "subtle": "#f7f7f7",
    "gold": "#E69F00",      # Okabe-Ito orange
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
            color=["#0072B2", "#009E73", "#D55E00", "#CC79A7", "#56B4E9"]
        ),
    }
)

DOMAIN_COLORS = {
    "Clinical Procedures":    "#0072B2",  # deep blue
    "Elderly / Nursing Care": "#009E73",  # teal
    "Rehabilitation":         "#D55E00",  # vermillion
    "Mental Health / HRI":    "#CC79A7",  # mauve
    "Hospital Logistics":     "#56B4E9",  # sky blue
}


def gen_trl_readiness():
    """TRL horizontal bar chart: five clinical domains with constraint callouts."""
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
        "force precision,\nno predicate",
        "no care facility\npilot",
        "no patient\ntrial",
        "platform\nunspecified",
        "wheeled systems\npreferred",
    ]

    fig, ax = plt.subplots(figsize=(7, 5.5))

    bar_height = 0.55
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
            xh + 0.15,
            y_positions[i],
            constraints[i],
            va="center",
            ha="left",
            fontsize=10.5,
            color="#555555",
            linespacing=1.15,
        )

    ax.axvline(x=4.5, color="#1a1a1a", linestyle="--", linewidth=1.4)
    ax.text(
        4.58,
        len(domains) - 0.35,
        "TRL 5 target",
        ha="left",
        va="bottom",
        fontsize=11,
        color="#1a1a1a",
    )

    ax.set_ylim(-0.5, len(domains) + 0.3)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(domains, fontsize=12)
    ax.set_xlabel("Technology Readiness Level (ISO 16290:2013)")
    ax.set_xlim(0.5, 11)
    ax.set_xticks(range(1, 10))
    ax.set_title("TRL assessment by clinical domain (March 2026)", pad=10)
    ax.grid(axis="x", linestyle=":", linewidth=0.5, color="#cccccc")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout(pad=1.2)
    path = f"{OUTPUT_DIR}/trl_readiness.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_evidence_landscape():
    """Evidence distribution: 14 papers by domain x year with unified legend."""
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
    marker_sizes = {"eng": 85, "obs": 85, "rct": 140}

    fig, ax = plt.subplots(figsize=(10, 5.5))

    coord_count = Counter((d, y) for d, y, _, _ in papers)
    coord_idx = defaultdict(int)

    for domain_idx, year, surname, stype in papers:
        key = (domain_idx, year)
        idx = coord_idx[key]
        total = coord_count[key]
        y_off = (idx - (total - 1) / 2.0) * 0.45
        x_jitter = (idx - (total - 1) / 2.0) * 0.10
        coord_idx[key] += 1

        dot_x = year + x_jitter
        dot_y = domain_idx + y_off

        ax.scatter(
            dot_x,
            dot_y,
            s=marker_sizes[stype],
            marker=shape_markers[stype],
            color=domain_color_list[domain_idx],
            edgecolors="#555555" if stype != "rct" else "none",
            linewidths=0.8,
            alpha=0.9,
            zorder=3,
        )

        text_x = dot_x + 0.15
        ax.plot(
            [dot_x + 0.05, text_x - 0.01],
            [dot_y, dot_y],
            linestyle="--",
            color="#bbbbbb",
            lw=0.8,
            zorder=2,
        )
        ax.text(
            text_x,
            dot_y,
            surname,
            ha="left",
            va="center",
            fontsize=14,
            color="#333333",
        )

    ax.set_yticks(range(len(domain_labels)))
    ax.set_yticklabels(domain_labels, fontsize=14)
    ax.set_xlabel("Publication Year")
    ax.set_xlim(2021.0, 2026.8)
    ax.set_xticks([2022, 2023, 2024, 2025, 2026])
    ax.set_ylim(-1.0, len(domain_labels) + 0.2)
    ax.set_title("Evidence distribution: 14 papers, 2022–2026")

    # Two side-by-side legends: study type (left) and domain (right)
    type_handles = [
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
        handles=type_handles,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        title="Study type",
        ncol=1,
        frameon=False,
        fontsize=12,
        title_fontsize=12,
    )
    ax.add_artist(leg1)
    ax.legend(
        handles=domain_handles,
        loc="upper right",
        bbox_to_anchor=(1.0, -0.18),
        title="Domain",
        ncol=1,
        frameon=False,
        fontsize=12,
        title_fontsize=12,
    )

    ax.grid(axis="x", linestyle=":", linewidth=0.5, color="#cccccc")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.subplots_adjust(bottom=0.30)
    path = f"{OUTPUT_DIR}/evidence_landscape.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_tech_timeline():
    """Technology timeline: dual-track non-linear timeline with era shading."""

    blue = "#2166ac"
    green = "#1a9641"
    axis_color = "#555555"

    # 3-segment piecewise linear scale: compress early years, expand post-2022.
    # No scale-break marker; the non-linearity is implicit in the era bands.
    def year_to_x(y):
        if y <= 2010:
            return 1995.5 + (y - 1996) * 0.35
        elif y <= 2022:
            return 1995.5 + (2010 - 1996) * 0.35 + (y - 2010) * 0.60
        else:
            return (
                1995.5 + (2010 - 1996) * 0.35 + (2022 - 2010) * 0.60 + (y - 2022) * 2.2
            )

    x_min = year_to_x(1990.0)
    x_max = year_to_x(2027.5)

    fig, ax = plt.subplots(figsize=(13, 8))

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-7.0, 8.0)

    ax.axhline(0, color=axis_color, linewidth=2.5, zorder=2)
    ax.grid(False)

    # ---- Era background shading ----
    eras = [
        (1990.0, 2010, "#deebf7", "Locomotion era\n(1996–2010)"),
        (2010, 2022, "#fee6ce", "Manipulation era\n(2010–2022)"),
        (2022, 2027.5, "#d9f0d3", "Commercial\nscale-up (2022–present)"),
    ]
    for x0, x1, color, label in eras:
        ax.axvspan(year_to_x(x0), year_to_x(x1), alpha=0.28, color=color, zorder=0)
        ax.text(
            year_to_x((x0 + x1) / 2),
            7.6,
            label,
            ha="center",
            va="top",
            fontsize=16,
            color="#555555",
            style="italic",
            fontweight="bold",
        )

    # ---- Year ticks ----
    # Every year gets a tick; labels at non-overlapping intervals.
    for yr in range(1996, 2027):
        ax.plot(
            [year_to_x(yr), year_to_x(yr)],
            [-0.18, 0.18],
            color="#888888",
            linewidth=1.4,
            zorder=3,
        )
    # Pre-2022: 1996, 2004, 2012, 2016 — balanced spacing without overlap
    for yr in [1996, 2004, 2012, 2016]:
        ax.text(
            year_to_x(yr),
            -0.55,
            str(yr),
            ha="center",
            va="top",
            fontsize=15,
            color="#444444",
            fontweight="bold",
        )
    # Post-2022: every year, expanded region has plenty of space
    for yr in range(2022, 2027):
        ax.text(
            year_to_x(yr),
            -0.55,
            str(yr),
            ha="center",
            va="top",
            fontsize=15,
            color="#444444",
            fontweight="bold",
        )

    # ---- Platform events (upper track, 4 staggered heights) ----
    platform_events = [
        (1996, "Honda P3\nbipedal demo"),
        (2000, "ASIMO\nlaunched"),
        (2004, "HRP-2\n(AIST)"),
        (2012, "DARPA Robotics\nChallenge"),
        (2013.6, "Atlas\n(Boston Dynamics)"),
        (2018, "HRP-5P\n(AIST)"),
        (2022, "Tesla Optimus\nprototype"),
        (2023, "Figure 01\nannounced"),
        (2023.8, "Unitree G1\nreleased"),
        (2024.6, "Figure 02\n+ BMW pilot"),
        (2025, r"$\pi_0$" + "\n(Physical Intelligence)"),
        (2026, "13 commercial\nplatforms"),
    ]

    # Heights spaced 1.2" apart; top level lowered to avoid era-label overlap.
    p_heights = [1.0, 2.2, 3.4, 4.6]
    p_assign = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]

    # Small x-offsets for events <1 year apart in dense post-2022 region.
    p_xoff = [0, 0, 0, 0, 0, 0, 0, 0, -0.12, -0.15, +0.15, 0]

    for (yr, label), li, xo in zip(platform_events, p_assign, p_xoff):
        yh = p_heights[li]
        x = year_to_x(yr) + xo
        ax.plot([x, x], [0, yh], color=blue, linewidth=1.6, zorder=2, alpha=0.40)
        ax.plot(
            x,
            yh,
            "o",
            color=blue,
            markersize=7,
            zorder=3,
            markeredgecolor="white",
            markeredgewidth=0.5,
        )
        ax.text(
            x,
            yh + 0.28,
            label,
            ha="center",
            va="bottom",
            fontsize=14,
            color=blue,
            zorder=5,
        )

    # ---- Healthcare events (lower track, 4 staggered heights) ----
    health_events = [
        (2003, "NAO first\npediatric pilot"),
        (2010, "PARO\nclinical RCT"),
        (2013, "NAO ASD\ntherapy studies"),
        (2018, "Pepper dementia\npilot"),
        (2020, "COVID: robots\nin hospitals"),
        (2022.5, "SPRING project\n(ARI, Paris)"),
        (2023.5, "RHP Friends\nIREX nursing demo"),
        (2024, "Unitree G1\nrehab / EEG"),
        (2025, "Atar et al.\n7 procedures"),
        (2026, "Cho et al.\nhumanoid surgery"),
    ]

    h_heights = [-1.2, -2.64, -4.08, -5.52]
    h_assign = [0, 1, 2, 0, 1, 2, 3, 0, 1, 2]
    h_xoff = [0, 0, 0, 0, 0, 0, -0.10, +0.10, 0, 0]

    for (yr, label), li, xo in zip(health_events, h_assign, h_xoff):
        yh = h_heights[li]
        x = year_to_x(yr) + xo
        ax.plot([x, x], [0, yh], color=green, linewidth=1.6, zorder=2, alpha=0.40)
        ax.plot(
            x,
            yh,
            "o",
            color=green,
            markersize=7,
            zorder=3,
            markeredgecolor="white",
            markeredgewidth=0.5,
        )
        ax.text(
            x,
            yh - 0.28,
            label,
            ha="center",
            va="top",
            fontsize=14,
            color=green,
            zorder=5,
        )

    # ---- Legend ----
    legend_elements = [
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=blue,
            markersize=8,
            label="Platform / technology milestones",
        ),
        Line2D(
            [0],
            [0],
            marker="o",
            color="w",
            markerfacecolor=green,
            markersize=8,
            label="Healthcare research events",
        ),
    ]
    ax.legend(
        handles=legend_elements,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        fontsize=16,
        ncol=2,
        frameon=False,
    )

    ax.set_title(
        "Technology Timeline: Humanoid Robotics Platforms\nand Healthcare Research Events (1996–2026)",
        fontsize=18,
        pad=16,
    )

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_facecolor("white")

    fig.subplots_adjust(bottom=0.08)
    path = f"{OUTPUT_DIR}/tech_timeline.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_regulatory_pathways():
    """Regulatory pathway flowchart: FDA De Novo (US) and EU MDR/AI Act (EU)."""
    col_us = 3.0
    col_eu = 9.0
    col_mid = 6.0
    box_w = 4.8

    row_y = [8.6, 7.45, 6.30, 5.15, 4.00, 2.75]
    row_h = [0.88, 0.78, 0.78, 0.78, 0.78, 0.88]

    us_pale = "#e8f4fc"
    us_final_bg = "#1a5276"
    us_final_fg = "#ffffff"
    us_edge = "#2166ac"

    eu_pale = "#e8f8f0"
    eu_final_bg = "#1e8449"
    eu_final_fg = "#ffffff"
    eu_edge = "#1e8449"

    fig, ax = plt.subplots(figsize=(10.0, 10.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10.0)
    ax.axis("off")

    def box(cx, row_idx, text, bg, edge, fontsize=13, bold=False, textcolor="#1a1a1a"):
        cy = row_y[row_idx]
        h = row_h[row_idx]
        rect = FancyBboxPatch(
            (cx - box_w / 2, cy - h / 2),
            box_w,
            h,
            boxstyle="round,pad=0.15",
            facecolor=bg,
            edgecolor=edge,
            linewidth=1.2,
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
            color=textcolor,
            zorder=3,
            multialignment="center",
        )

    def arrow(cx, from_row, to_row, color="#555555"):
        y1 = row_y[from_row] - row_h[from_row] / 2 - 0.10
        y2 = row_y[to_row] + row_h[to_row] / 2 + 0.10
        ax.annotate(
            "",
            xy=(cx, y2),
            xytext=(cx, y1),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, mutation_scale=16),
            zorder=2,
        )

    # Column headers
    ax.text(
        col_us,
        9.55,
        "United States\nFDA Pathway",
        ha="center",
        va="center",
        fontsize=13,
        weight="bold",
        color=us_edge,
    )
    ax.text(
        col_eu,
        9.55,
        "European Union\nMDR + AI Act Pathway",
        ha="center",
        va="center",
        fontsize=13,
        weight="bold",
        color=eu_edge,
    )

    # Vertical separator
    ax.plot(
        [col_mid, col_mid],
        [1.95, 9.25],
        color="#cccccc",
        linewidth=1.2,
        linestyle="--",
        zorder=1,
    )

    # US track
    box(
        col_us,
        0,
        "Clinical Humanoid Robot\n(novel device, no predicate)",
        bg=us_pale,
        edge=us_edge,
        bold=True,
        fontsize=12,
    )
    arrow(col_us, 0, 1, color=us_edge)
    box(
        col_us,
        1,
        "510(k): no predicate\nDe Novo (21 CFR 513(f)(2))",
        bg=us_pale,
        edge=us_edge,
        fontsize=13,
    )
    arrow(col_us, 1, 2, color=us_edge)
    box(
        col_us,
        2,
        "Pre-Sub meeting with FDA\n(risk class, evidence plan)",
        bg=us_pale,
        edge=us_edge,
        fontsize=13,
    )
    arrow(col_us, 2, 3, color=us_edge)
    box(
        col_us,
        3,
        "De Novo request submission\n(bench + non-clinical + clinical)",
        bg=us_pale,
        edge=us_edge,
        fontsize=13,
    )
    arrow(col_us, 3, 4, color=us_edge)
    box(
        col_us,
        4,
        "FDA review (~12 months)\nClassification order issued",
        bg=us_pale,
        edge=us_edge,
        fontsize=13,
    )
    arrow(col_us, 4, 5, color=us_edge)
    box(
        col_us,
        5,
        "Market authorization (Class II)\nPost-market surveillance",
        bg=us_final_bg,
        edge=us_edge,
        bold=True,
        fontsize=13,
        textcolor=us_final_fg,
    )

    # EU track
    box(
        col_eu,
        0,
        "Clinical Humanoid Robot\n(novel device, no CE predicate)",
        bg=eu_pale,
        edge=eu_edge,
        bold=True,
        fontsize=12,
    )
    arrow(col_eu, 0, 1, color=eu_edge)
    box(
        col_eu,
        1,
        "EU MDR Class IIb/III\n(Notified Body required)",
        bg=eu_pale,
        edge=eu_edge,
        fontsize=13,
    )
    arrow(col_eu, 1, 2, color=eu_edge)
    box(
        col_eu,
        2,
        "EU AI Act: High-Risk AI\n(Art. 6; conformity Aug 2026)",
        bg="#fef9e7",
        edge="#d4ac0d",
        fontsize=13,
    )
    arrow(col_eu, 2, 3, color=eu_edge)
    box(
        col_eu,
        3,
        "Clinical investigation\nMDR Art. 62 (Competent Auth. + ethics)",
        bg=eu_pale,
        edge=eu_edge,
        fontsize=13,
    )
    arrow(col_eu, 3, 4, color=eu_edge)
    box(
        col_eu,
        4,
        "CE marking by Notified Body\n+ AI Act declaration",
        bg=eu_pale,
        edge=eu_edge,
        fontsize=13,
    )
    arrow(col_eu, 4, 5, color=eu_edge)
    box(
        col_eu,
        5,
        "EU market authorization\nPost-Market Clinical Follow-up (PMCF)",
        bg=eu_final_bg,
        edge=eu_edge,
        bold=True,
        fontsize=13,
        textcolor=eu_final_fg,
    )

    # Bottom banner: critical gap
    gap_h = 1.05
    gap_y = 1.45
    rect = FancyBboxPatch(
        (0.25, gap_y - gap_h / 2),
        11.5,
        gap_h,
        boxstyle="round,pad=0.15",
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
        "(ISO 13482 excludes medical devices; ISO/TS 15066: fixed-base arms)",
        ha="center",
        va="center",
        fontsize=12,
        color="#1a1a1a",
        zorder=3,
        multialignment="center",
    )

    ax.set_title(
        "Regulatory Pathways for Clinical Humanoid Robots: FDA (US) vs. EU MDR + AI Act",
        fontsize=14,
        pad=12,
        weight="bold",
    )

    fig.tight_layout(pad=1.5)
    path = f"{OUTPUT_DIR}/regulatory_pathways.pdf"
    fig.savefig(path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    print(f"Saved: {path}")


def gen_capability_gap():
    """Capability gap: grouped horizontal bar chart with explicit gap annotations."""
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
    gaps = [r - c for r, c in zip(required, current)]

    n = len(dimensions)
    y = np.arange(n)
    bar_height = 0.32

    fig, ax = plt.subplots(figsize=(11, 6.5))

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

    # Value labels on bars
    for bar, val in zip(bars_req, required):
        ax.text(
            val + 0.15,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            ha="left",
            fontsize=16,
            color="#333333",
        )
    for bar, val in zip(bars_cur, current):
        ax.text(
            val + 0.15,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            ha="left",
            fontsize=16,
            color="#333333",
        )

    ax.set_yticks(y)
    ax.set_yticklabels(dimensions, fontsize=16)
    ax.set_xlim(0, 9.5)
    ax.set_xlabel("Score (0–10)", fontsize=16)
    ax.axvline(x=7, color="#aaaaaa", linewidth=0.8, linestyle="--", zorder=2)
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.10),
        ncol=2,
        frameon=False,
        fontsize=16,
    )
    ax.grid(axis="x", linewidth=0.5, color="#dddddd", zorder=1)
    ax.set_axisbelow(True)
    ax.invert_yaxis()

    fig.suptitle(
        "Humanoid Capability Gap: Current vs. Required for Clinical Deployment",
        fontsize=17,
        y=1.02,
    )
    fig.tight_layout(pad=1.8)
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
