#!/usr/bin/env python3
"""
F(AI)^2R verification-rung distribution figure.

Produces paper/figures/rung-distribution.{pdf,png}: a horizontal stacked
bar showing the share of Claim entities at each verification rung,
plus the share of Source entities at each retrieval-side rung. The
figure is a one-glance companion to the auto-generated table at
paper/sections/_generated/rung-distribution.tex.

Data source. Counts are read from paper/sections/_generated/rung-
distribution.tex if present (the build pipeline regenerates it from
doc/provenance.ttl). The reader script extracts the rung label and
claim count per row; sources are taken from the provenance graph
fallback below.

Style. DLR Corporate Design only:
    dlrBlau1  #00658B   primary accent
    dlrBlau5  #D1E8FA   soft AI rung
    dlrGruen1 #82A043   human-confirmed
    dlrGruen5 #E6EAAF   soft human rung
    dlrGelb5  #FFF8BE   needs-research / soft warning
    dlrGrau1  #4D5258   neutral text
    dlrGrau3  #B1B1B1   hairline
    dlrGrau5  #EBEBEB   external / pre-research

Reproducibility. No randomness. Run from repo root:
    python3 paper/figures/src/rung-distribution.py
Output:
    paper/figures/rung-distribution.pdf
    paper/figures/rung-distribution.png
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

# DLR palette ---------------------------------------------------------
DLR = {
    "blau1":  "#00658B",
    "blau5":  "#D1E8FA",
    "gruen1": "#82A043",
    "gruen5": "#E6EAAF",
    "gelb1":  "#D2AE3D",
    "gelb5":  "#FFF8BE",
    "grau1":  "#4D5258",
    "grau3":  "#B1B1B1",
    "grau5":  "#EBEBEB",
}

# Map rung label -> (display label, fill, edge)
RUNG_STYLE = {
    "needs-research":   ("needs-research",   DLR["gelb5"], DLR["gelb1"]),
    "lit-retrieved":    ("lit-retrieved",    "white",      DLR["grau1"]),
    "ai-confirmed":     ("ai-confirmed",     DLR["blau5"], DLR["blau1"]),
    "lit-read":         ("lit-read",         DLR["gruen5"],DLR["gruen1"]),
    "human-confirmed":  ("human-confirmed",  DLR["gruen5"],DLR["gruen1"]),
    "source-vendored":  ("source-vendored",  DLR["blau1"], DLR["blau1"]),
    "unverified-external": ("unverified-external", DLR["grau5"], DLR["grau1"]),
}
# Reading order (left to right on the bar)
ORDER = [
    "needs-research",
    "lit-retrieved",
    "ai-confirmed",
    "lit-read",
    "human-confirmed",
    "source-vendored",
]


def parse_generated_table(path: Path) -> list[tuple[str, int]]:
    """Extract (rung_label, count) rows from the LaTeX table."""
    rows: list[tuple[str, int]] = []
    if not path.exists():
        return rows
    txt = path.read_text(encoding="utf-8")
    # Each row: "needs-research & 2 & 5.4\,\% \\"
    for m in re.finditer(
        r"^([a-z][a-z\-]+)\s*&\s*(\d+)\s*&\s*[\d.]+\\,\\%\s*\\\\",
        txt, flags=re.MULTILINE,
    ):
        rows.append((m.group(1), int(m.group(2))))
    return rows


def fallback_claim_data() -> list[tuple[str, int]]:
    """Snapshot read from doc/provenance.ttl rung distribution at the
    time of writing this figure. Used only if the generated table is
    missing; the build pipeline normally produces it on every run."""
    return [
        ("needs-research",  2),
        ("ai-confirmed",    5),
        ("human-confirmed", 21),
        ("source-vendored", 9),
    ]


def fallback_source_data() -> list[tuple[str, int]]:
    """Source-side rung distribution from the latest verification pass
    (logbook entry 2026-05-07): 51 ai-confirmed, 21 human-confirmed,
    10 source-vendored, 3 lit-retrieved, 2 needs-research."""
    return [
        ("needs-research", 2),
        ("lit-retrieved",  3),
        ("ai-confirmed",   51),
        ("human-confirmed",21),
        ("source-vendored",10),
    ]


def horizontal_stack(ax, rows, total_label, y, height=0.55):
    """Draw a single horizontal stacked bar at vertical position y."""
    total = sum(n for _, n in rows)
    if total == 0:
        return
    x = 0.0
    for rung in ORDER:
        n = next((cnt for r, cnt in rows if r == rung), 0)
        if n == 0:
            continue
        label, fill, edge = RUNG_STYLE[rung]
        ax.barh(y, n, left=x, height=height,
                color=fill, edgecolor=edge, linewidth=0.5)
        # Numeric label centred on the segment if it has room.
        # Dark fills (the source-vendored solid blue) get white text;
        # all soft / white fills get neutral mid-grey.
        if n / total > 0.05:
            text_color = "white" if fill == DLR["blau1"] else DLR["grau1"]
            ax.text(x + n / 2, y, f"{n}",
                    ha="center", va="center",
                    fontsize=8, color=text_color)
        x += n
    # Right-edge total
    ax.text(total + 1.2, y, f"n = {total}  ({total_label})",
            ha="left", va="center",
            fontsize=8.5, color=DLR["grau1"])


def main() -> int:
    repo = Path(__file__).resolve().parents[3]
    gen = repo / "paper" / "sections" / "_generated" / "rung-distribution.tex"

    claim_rows = parse_generated_table(gen) or fallback_claim_data()
    source_rows = fallback_source_data()

    rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 9.0,
        "axes.edgecolor": DLR["grau1"],
        "axes.labelcolor": DLR["grau1"],
        "xtick.color": DLR["grau1"],
        "ytick.color": DLR["grau1"],
    })

    fig, ax = plt.subplots(figsize=(7.0, 2.2))
    ax.set_xlim(0, max(sum(n for _, n in source_rows),
                       sum(n for _, n in claim_rows)) * 1.30)
    ax.set_ylim(-0.6, 1.6)

    horizontal_stack(ax, source_rows, "fair2r:Source",   y=1.0)
    horizontal_stack(ax, claim_rows,  "fair2r:Claim",    y=0.0)

    ax.set_yticks([0.0, 1.0])
    ax.set_yticklabels(["claims", "sources"],
                       fontsize=9, color="black")
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlabel("entities at each rung", color=DLR["grau1"], fontsize=8.5)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_linewidth(0.4)
        ax.spines[spine].set_color(DLR["grau3"])

    # Legend at the bottom, single row, hairline-bordered cells.
    legend_handles = []
    legend_labels = []
    for rung in ORDER:
        if (any(r == rung for r, _ in source_rows) or
                any(r == rung for r, _ in claim_rows)):
            label, fill, edge = RUNG_STYLE[rung]
            legend_handles.append(
                plt.Rectangle((0, 0), 1, 1,
                              facecolor=fill, edgecolor=edge, linewidth=0.5))
            legend_labels.append(label)
    leg = ax.legend(
        legend_handles, legend_labels,
        loc="upper center", bbox_to_anchor=(0.5, -0.32),
        ncol=len(legend_labels), frameon=False,
        fontsize=8, handlelength=1.0, handleheight=0.8,
        columnspacing=1.0,
    )
    for txt in leg.get_texts():
        txt.set_color(DLR["grau1"])

    fig.subplots_adjust(left=0.10, right=0.98, top=0.95, bottom=0.32)

    out_dir = repo / "paper" / "figures"
    fig.savefig(out_dir / "rung-distribution.pdf")
    fig.savefig(out_dir / "rung-distribution.png", dpi=200)
    print(f"wrote {out_dir/'rung-distribution.pdf'}")
    print(f"wrote {out_dir/'rung-distribution.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
