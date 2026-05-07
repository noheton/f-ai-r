#!/usr/bin/env python3
"""
F(AI)^2R contribution-type histogram.

Produces paper/figures/contribution-histogram.{pdf,png}: a horizontal
bar chart of fair2r:HumanContribution counts per type, read from
doc/user-contributions.md (the human-readable shadow of the
provenance graph's hc:* IRIs). The figure answers the paper's
recurring "what does the human actually do?" question quantitatively
and lands in paper/sections/authors-note.tex alongside the prose
description of the partition.

Data source. Lines of the form '*Type:* `<name>`' in
doc/user-contributions.md are counted by type. The type vocabulary
is fixed by the schema header in that file:
structural-decision, corrective-intervention, content-prompt,
rule-shape, observation, responsibility-uptake, experience-meta.

Style. DLR Corporate Design only. The five 'core' contribution
types share the dlrBlau1 family (the model-collaborator surface);
the responsibility-uptake type uses dlrGruen1 because it is the
contribution the AI structurally cannot share, and the
observation type uses dlrGelb1 because it sits one rung short of a
rule-shape. Greyscale-legible: the colour pairs with hatch and
label position rather than carrying the only signal.

Reproducibility. No randomness; deterministic count per file. Run
from the repo root::

    python3 paper/figures/src/contribution-histogram.py

Output::

    paper/figures/contribution-histogram.pdf
    paper/figures/contribution-histogram.png
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

# Type -> (display label, family fill, family edge, hatch, family text)
TYPE_STYLE = {
    "structural-decision":     ("structural-decision",      DLR["blau1"], DLR["blau1"], None,  "structural"),
    "rule-shape":              ("rule-shape",               DLR["blau1"], DLR["blau1"], None,  "structural"),
    "content-prompt":          ("content-prompt",           DLR["blau5"], DLR["blau1"], None,  "directive"),
    "corrective-intervention": ("corrective-intervention",  DLR["blau5"], DLR["blau1"], "//",  "corrective"),
    "observation":             ("observation",              DLR["gelb5"], DLR["gelb1"], None,  "meta"),
    "experience-meta":         ("experience-meta",          DLR["gelb5"], DLR["gelb1"], "//",  "meta"),
    "responsibility-uptake":   ("responsibility-uptake",    DLR["gruen5"],DLR["gruen1"],None,  "uptake"),
}

# Stable display order: heaviest interventions on top, then directive,
# then meta, then the leg only the human carries at the bottom.
ORDER = [
    "structural-decision",
    "rule-shape",
    "content-prompt",
    "corrective-intervention",
    "observation",
    "experience-meta",
    "responsibility-uptake",
]


def parse_contributions(path: Path) -> dict[str, int]:
    """Count '*Type:* `<name>`' lines per type. Returns a dict keyed by
    type, zero-filled for types that the schema lists but no entry has
    yet exercised."""
    counts = {k: 0 for k in ORDER}
    if not path.exists():
        return counts
    txt = path.read_text(encoding="utf-8")
    for m in re.finditer(r"^\*Type:\*\s*`([a-z][a-z\-]+)`", txt,
                          flags=re.MULTILINE):
        key = m.group(1)
        if key in counts:
            counts[key] += 1
    return counts


def main() -> int:
    repo = Path(__file__).resolve().parents[3]
    contribs = repo / "doc" / "user-contributions.md"
    counts = parse_contributions(contribs)

    rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 9.0,
        "axes.edgecolor": DLR["grau1"],
        "axes.labelcolor": DLR["grau1"],
        "xtick.color": DLR["grau1"],
        "ytick.color": DLR["grau1"],
    })

    fig, ax = plt.subplots(figsize=(7.0, 3.6))

    # Vertical layout: top-of-chart = first ORDER entry.
    # We render bottom-up (matplotlib y increasing) but reverse the
    # data so item 0 ends up at the top.
    keys = list(reversed(ORDER))
    ys = list(range(len(keys)))

    max_count = max(counts.values()) if counts else 1
    for y, key in zip(ys, keys):
        n = counts.get(key, 0)
        label, fill, edge, hatch, family = TYPE_STYLE[key]
        bar_kw = dict(color=fill, edgecolor=edge, linewidth=0.5,
                      height=0.62, align="center")
        if hatch:
            bar_kw["hatch"] = hatch
        ax.barh(y, n, **bar_kw)
        # Numeric badge: inside the bar if room, else just to the right.
        if n >= max(1, max_count * 0.10):
            text_color = "white" if fill in (DLR["blau1"], DLR["gruen1"]) else DLR["grau1"]
            ax.text(n - 0.30, y, f"{n}",
                    ha="right", va="center",
                    fontsize=8.5, color=text_color, weight="bold")
        else:
            ax.text(n + 0.25, y, f"{n}",
                    ha="left", va="center",
                    fontsize=8.5, color=DLR["grau1"])
        # Family annotation on the right edge.
        ax.text(max_count + 1.6, y, family,
                ha="left", va="center",
                fontsize=7.5, color=DLR["grau1"], style="italic")

    # Tick / spine config
    ax.set_yticks(ys)
    ax.set_yticklabels([TYPE_STYLE[k][0] for k in keys],
                       fontsize=9, color="black")
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", labelsize=8)
    ax.set_xlim(0, max_count * 1.50)
    ax.set_xlabel("count of human-author contributions to date",
                  color=DLR["grau1"], fontsize=8.5)

    # Hairline vertical guide at every integer up to max_count
    for v in range(0, max_count + 1, max(1, max_count // 5)):
        ax.axvline(v, color=DLR["grau5"], linewidth=0.3, zorder=0)

    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_linewidth(0.4)
        ax.spines[spine].set_color(DLR["grau3"])

    # Title strip (kept inside the figure so the rendered PNG is
    # legible standalone in README / Pages).
    total = sum(counts.values())
    ax.set_title(
        f"Human-author contributions by type  -  n = {total}  "
        f"(read from doc/user-contributions.md)",
        fontsize=9.0, color=DLR["grau1"],
        loc="left", pad=10.0,
    )

    fig.subplots_adjust(left=0.24, right=0.92, top=0.88, bottom=0.14)

    out_dir = repo / "paper" / "figures"
    fig.savefig(out_dir / "contribution-histogram.pdf")
    fig.savefig(out_dir / "contribution-histogram.png", dpi=300)
    print(f"wrote {out_dir/'contribution-histogram.pdf'}")
    print(f"wrote {out_dir/'contribution-histogram.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
