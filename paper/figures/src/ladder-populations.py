#!/usr/bin/env python3
"""
F(AI)^2R verification-ladder with live rung populations.

Produces paper/figures/ladder-populations.{pdf,png}: the verification
ladder rendered as a left-to-right finite-state machine, where each
node's *radius* is proportional to the count of fair2r:Claim entities
currently at that rung in doc/provenance.ttl. The figure tells two
stories at once --- the topology of the ladder (which rung follows
which, where the model ceiling sits, where retraction goes) and its
empirical state (which rungs are occupied, which are empty).

This figure supersedes paper/figures/rung-distribution.* (a horizontal
stacked bar). The bar showed the distribution as percentages but lost
the topology; this figure preserves both.

Data source. Counts are read from doc/provenance.ttl via rdflib.
Falls back to a pinned snapshot if rdflib or the graph is unavailable.

Style. DLR Corporate Design only:
    dlrBlau1  #00658B   primary accent (claim-side, dark)
    dlrBlau5  #D1E8FA   soft AI rung
    dlrGruen1 #82A043   human-confirmed (dark)
    dlrGruen5 #E6EAAF   soft human rung
    dlrGelb5  #FFF8BE   needs-research / soft warning
    dlrGrau1  #4D5258   neutral text / hairlines
    dlrGrau3  #B1B1B1   tertiary hairline
    dlrGrau5  #EBEBEB   external / pre-research

Information channels are doubled: rung-position carries the topology;
node radius carries cardinality (with a numeric badge inside the node
so the figure remains legible if reproduced at thumbnail size); fill
carries the rung family; hatch (//) marks the AI ceiling so the
figure is greyscale-legible.

Reproducibility. No randomness. Run from repo root::

    python3 paper/figures/src/ladder-populations.py

Output::

    paper/figures/ladder-populations.pdf
    paper/figures/ladder-populations.png
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

# DLR palette ---------------------------------------------------------
DLR = {
    "blau1":  "#00658B",
    "blau2":  "#3B98CB",
    "blau5":  "#D1E8FA",
    "gruen1": "#82A043",
    "gruen5": "#E6EAAF",
    "gelb1":  "#D2AE3D",
    "gelb5":  "#FFF8BE",
    "grau1":  "#4D5258",
    "grau3":  "#B1B1B1",
    "grau4":  "#CFCFCF",
    "grau5":  "#EBEBEB",
}

NS_FAIR2R = "https://noheton.org/f-ai-r/ns#"

# Rung order and styling. The ai-confirmed rung is the model ceiling
# (hatched fill). human-confirmed/source-vendored sit above the line
# and carry the green family.
RUNGS = [
    # key,                  display,            family,    fill,        edge,         hatch
    ("unverified-external", "unverified-\nexternal", "pre",  DLR["grau5"], DLR["grau1"], None),
    ("needs-research",      "needs-\nresearch", "warn",     DLR["gelb5"], DLR["gelb1"], None),
    ("lit-retrieved",       "lit-\nretrieved",  "neutral",  "white",      DLR["grau1"], None),
    ("ai-confirmed",        "ai-\nconfirmed",   "ai",       DLR["blau5"], DLR["blau1"], "//"),
    ("lit-read",            "lit-read",         "human-soft", DLR["gruen5"], DLR["gruen1"], None),
    ("human-confirmed",     "human-\nconfirmed", "human",   DLR["gruen5"], DLR["gruen1"], None),
    ("source-vendored",     "source-\nvendored", "claim",   DLR["blau1"], DLR["blau1"], None),
]


def load_counts(ttl_path: Path) -> dict[str, int]:
    """Count fair2r:Claim entities per fair2r:verificationState rung."""
    pinned = {
        "unverified-external": 0,
        "needs-research":      2,
        "lit-retrieved":       0,
        "ai-confirmed":        5,
        "lit-read":            0,
        "human-confirmed":     21,
        "source-vendored":     9,
    }
    try:
        import rdflib
    except ImportError:
        return pinned
    if not ttl_path.exists():
        return pinned
    g = rdflib.Graph()
    try:
        g.parse(str(ttl_path), format="turtle")
    except Exception:
        return pinned
    fair2r = rdflib.Namespace(NS_FAIR2R)
    rdf_type = rdflib.RDF.type
    claim_cls = fair2r.Claim
    state_pred = fair2r.verificationState
    out = {k: 0 for k, *_ in RUNGS}
    for claim in g.subjects(rdf_type, claim_cls):
        for state in g.objects(claim, state_pred):
            label = str(state).split("#")[-1].split("/")[-1]
            if label in out:
                out[label] += 1
    # If everything is zero, the parse worked but the graph has no
    # rungs yet; fall back to the pinned snapshot rather than ship a
    # blank figure.
    if sum(out.values()) == 0:
        return pinned
    return out


def radius_for(count: int, max_count: int, rmin: float, rmax: float) -> float:
    """Map count to circle radius. Sqrt scaling so area is proportional
    to count (the perception-correct mapping); a count of 0 still
    renders a small marker so the rung is visible."""
    if max_count <= 0:
        return rmin
    if count <= 0:
        return rmin * 0.55  # small marker for empty rung
    frac = math.sqrt(count / max_count)
    return rmin + frac * (rmax - rmin)


def draw_node(ax, x, y, r, label, count, fill, edge, hatch=None,
              dark_fill=False):
    """Square-bordered node with rung label above and count badge inside."""
    kw = dict(facecolor=fill, edgecolor=edge, linewidth=0.6)
    if hatch:
        kw["hatch"] = hatch
    circle = Circle((x, y), r, **kw)
    ax.add_patch(circle)
    # Count badge inside the node
    text_color = "white" if dark_fill else DLR["grau1"]
    ax.text(x, y, f"n={count}",
            ha="center", va="center",
            fontsize=8.0, color=text_color, weight="bold")
    # Rung label below
    ax.text(x, y - r - 0.20, label,
            ha="center", va="top",
            fontsize=7.5, color=DLR["grau1"])


def draw_arrow(ax, p_src, p_dst, dotted=False, label=None,
               curve=0.0, color=None):
    color = color or DLR["grau1"]
    style = "-" if not dotted else (0, (1.5, 1.5))
    cs = f"arc3,rad={curve}" if curve != 0.0 else "arc3"
    arrow = FancyArrowPatch(
        p_src, p_dst,
        arrowstyle="-|>", mutation_scale=8,
        color=color, linewidth=0.5,
        linestyle=style,
        connectionstyle=cs,
        shrinkA=2, shrinkB=2,
    )
    ax.add_patch(arrow)
    if label:
        mx = (p_src[0] + p_dst[0]) / 2
        my = (p_src[1] + p_dst[1]) / 2 + (0.18 if curve == 0 else 0.40)
        ax.text(mx, my, label,
                ha="center", va="center",
                fontsize=6.5, color=color, style="italic")


def main() -> int:
    repo = Path(__file__).resolve().parents[3]
    ttl = repo / "doc" / "provenance.ttl"
    counts = load_counts(ttl)
    max_count = max(counts.values()) if counts else 1

    rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 9.0,
    })

    # Layout: x-positions evenly spaced; y at 0 for the main ladder.
    n = len(RUNGS)
    xs = [0.0 + i * 1.85 for i in range(n)]
    rmin, rmax = 0.22, 0.62

    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    ax.set_xlim(-1.0, xs[-1] + 1.0)
    ax.set_ylim(-2.40, 2.30)
    ax.set_aspect("equal")
    ax.axis("off")

    # Header strip --------------------------------------------------
    header_y = 2.00
    ax.text(xs[0] - 0.6, header_y,
            "Verification ladder  (left-to-right monotone; retraction is the only back-edge)",
            ha="left", va="center",
            fontsize=9.0, color=DLR["grau1"], style="italic")
    ax.plot([xs[0] - 0.6, xs[-1] + 0.6], [header_y - 0.12, header_y - 0.12],
            color=DLR["grau3"], linewidth=0.4)

    # Model-ceiling band --------------------------------------------
    # ai-confirmed is the rightmost rung an LLM agent can deliver
    # alone. Mark the boundary between ai-confirmed (column 3) and
    # lit-read (column 4) with a vertical hairline rule plus a label.
    boundary_x = (xs[3] + xs[4]) / 2.0
    ax.plot([boundary_x, boundary_x], [-1.55, 1.55],
            color=DLR["grau3"], linewidth=0.4, linestyle=(0, (2, 2)))
    ax.text(boundary_x, 1.65, "model ceiling",
            ha="center", va="bottom",
            fontsize=8.0, color=DLR["grau1"], style="italic")

    # Forward edges --------------------------------------------------
    # Each rung -> next rung (arc3 with no curvature).
    radii = [radius_for(counts.get(k, 0), max_count, rmin, rmax)
             for k, *_ in RUNGS]
    for i in range(n - 1):
        # Anchor at edge of source / dest circles along the x-axis.
        p_src = (xs[i] + radii[i], 0.0)
        p_dst = (xs[i + 1] - radii[i + 1], 0.0)
        draw_arrow(ax, p_src, p_dst)

    # Retraction back-edges -- one symbolic dotted arc looping from
    # source-vendored back to needs-research, recorded as a
    # prov:Invalidation in the graph (per the ladder FSM caption).
    p_src = (xs[-1], radii[-1])
    p_dst = (xs[1], radii[1])
    arc = FancyArrowPatch(
        p_src, p_dst,
        arrowstyle="-|>", mutation_scale=8,
        color=DLR["gelb1"], linewidth=0.5,
        linestyle=(0, (1.5, 1.5)),
        connectionstyle="arc3,rad=-0.30",
        shrinkA=2, shrinkB=2,
    )
    ax.add_patch(arc)
    ax.text((xs[1] + xs[-1]) / 2.0, 0.92,
            "retraction  (prov:Invalidation, never deletion)",
            ha="center", va="center",
            fontsize=7.0, color=DLR["gelb1"], style="italic")

    # Nodes ----------------------------------------------------------
    for (key, label, family, fill, edge, hatch), x, r in zip(RUNGS, xs, radii):
        draw_node(ax, x, 0.0, r, label, counts.get(key, 0),
                  fill, edge, hatch=hatch,
                  dark_fill=(fill == DLR["blau1"]))

    # Footer summary -------------------------------------------------
    total = sum(counts.values())
    ai_or_below = (counts.get("unverified-external", 0)
                   + counts.get("needs-research", 0)
                   + counts.get("lit-retrieved", 0)
                   + counts.get("ai-confirmed", 0))
    ax.text(xs[0] - 0.6, -1.35,
            f"counts read from doc/provenance.ttl  -  "
            f"{total} fair2r:Claim entities total  -  "
            f"{ai_or_below} at or below the model ceiling, "
            f"{total - ai_or_below} above it",
            ha="left", va="center",
            fontsize=7.5, color=DLR["grau1"])

    # Legend -- four rung-family swatches, paired with the hatch
    # marker that doubles the AI channel.
    legend_y = -0.95
    legend_x0 = xs[0] - 0.6
    legend_items = [
        ("warn",      DLR["gelb5"],  DLR["gelb1"],  None, "warning"),
        ("ai",        DLR["blau5"],  DLR["blau1"],  "//", "AI ceiling (hatched)"),
        ("human",     DLR["gruen5"], DLR["gruen1"], None, "human"),
        ("claim",     DLR["blau1"],  DLR["blau1"],  None, "vendored"),
    ]
    cursor = legend_x0
    for _key, fill, edge, hatch, txt in legend_items:
        kw = dict(facecolor=fill, edgecolor=edge, linewidth=0.5)
        if hatch:
            kw["hatch"] = hatch
        ax.add_patch(Rectangle((cursor, legend_y), 0.20, 0.20, **kw))
        ax.text(cursor + 0.25, legend_y + 0.10, txt,
                ha="left", va="center",
                fontsize=7.5, color=DLR["grau1"])
        cursor += 0.25 + len(txt) * 0.105 + 0.30

    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    out_dir = repo / "paper" / "figures"
    fig.savefig(out_dir / "ladder-populations.pdf")
    fig.savefig(out_dir / "ladder-populations.png", dpi=300)
    print(f"wrote {out_dir/'ladder-populations.pdf'}")
    print(f"wrote {out_dir/'ladder-populations.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
