#!/usr/bin/env python3
"""
F(AI)^2R provenance-topology figure.

Produces paper/figures/provenance-topology.{pdf,png}: a node-link
preview of the *shape* of the live provenance graph at
``doc/provenance.ttl``. The figure is generated programmatically
from the graph itself --- it answers the reviewer question 'what
does the graph actually look like?' without obliging the reader to
clone the repository and open the Pages site.

Design decision. We do not draw every triple --- 1700+ triples are
unreadable on a printed page. Instead we draw the *core schema* of
the F(AI)^2R extension as a small layered graph, and decorate each
node with the count of instances from the live graph. The five
columns mirror the five user-facing entity classes the audit
queries read:

    Agents -> Plans -> Activities -> Entities -> Claims

with the cross-cutting Source / Section / Figure / Prompt entities
shown as a satellite ring beneath the Entity column. This is the
same partition the methodology section describes; the figure shows
that the graph really is that shape.

Style. DLR Corporate Design only (Arial / Helvetica fallback,
``dlrBlau1`` ``#00658B`` accent, ``dlrGrau1`` ``#666666`` neutral,
hairline 0.4 pt strokes, square corners, no shadows / gradients).
Information channels are doubled: the column position carries the
PROV-O role, the node fill carries the entity class (with hatch on
the AI-only contribution class so it remains legible in greyscale),
and the count badge carries cardinality.

Reproducibility. No randomness; layout is positioned by hand from
the schema. Counts read from ``doc/provenance.ttl`` via rdflib;
falls back to a pinned snapshot if rdflib is missing. Run from the
repo root::

    python3 paper/figures/src/provenance-topology.py

Output::

    paper/figures/provenance-topology.pdf
    paper/figures/provenance-topology.png
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.patches import FancyArrowPatch, Rectangle

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

# F(AI)^2R namespace short URI for class lookup
NS_FAIR2R = "https://noheton.org/f-ai-r/ns#"
NS_PROV   = "http://www.w3.org/ns/prov#"

# Schema layout: label -> (column, row, class-IRI list, fill-style)
# Columns 0..4 are the five PROV-O lanes; satellite row sits below.
# fill-style: ("solid", colour) | ("hatch", colour, hatch-pattern)
_DX = 2.4   # column spacing
_DY = 1.2   # row spacing within a column
SCHEMA = {
    # AGENTS lane (column 0)
    "HumanResearcher":  (0*_DX, 2*_DY, [NS_FAIR2R + "HumanResearcher"], ("solid",   DLR["gruen5"])),
    "AIAgent":          (0*_DX, 1*_DY, [NS_FAIR2R + "AIAgent"],         ("hatch",   DLR["blau5"], "//")),
    # PLANS lane (column 1)
    "Prompt":           (1*_DX, 1.5*_DY, [NS_FAIR2R + "Prompt"],        ("solid",   DLR["blau5"])),
    # ACTIVITIES lane (column 2)
    "AuthoringPass":    (2*_DX, 3*_DY,   [NS_FAIR2R + "AuthoringPass"], ("solid",   "white")),
    "Activity":         (2*_DX, 2*_DY,   [NS_PROV + "Activity"],        ("solid",   "white")),
    "AuditPass":        (2*_DX, 1*_DY,   [NS_FAIR2R + "AuditPass"],     ("solid",   "white")),
    # ENTITIES lane (column 3)
    "Section":          (3*_DX, 3*_DY,   [NS_FAIR2R + "Section"],       ("solid",   DLR["grau5"])),
    "Source":           (3*_DX, 2*_DY,   [NS_FAIR2R + "Source"],        ("solid",   DLR["grau5"])),
    "Figure":           (3*_DX, 1*_DY,   [NS_FAIR2R + "Figure"],        ("solid",   DLR["grau5"])),
    "Manuscript":       (3*_DX, 0*_DY,   [NS_FAIR2R + "Manuscript"],    ("solid",   DLR["grau5"])),
    # CLAIMS lane (column 4)
    "Claim":            (4*_DX, 2*_DY,   [NS_FAIR2R + "Claim"],         ("solid",   DLR["blau1"])),
    # Satellite ring (lower band): contributions
    "HumanContribution": (1.0*_DX, -1.0, [NS_FAIR2R + "HumanContribution"], ("solid", DLR["gruen5"])),
    "AIContribution":    (2.0*_DX, -1.0, [NS_FAIR2R + "AIContribution"],    ("hatch", DLR["blau5"], "//")),
    "MetaContribution":  (3.0*_DX, -1.0, [NS_FAIR2R + "MetaContribution"],  ("solid", DLR["gelb5"])),
}

# Edges in the schema. Each edge: (src, dst, label-stub).
# Label-stubs are PROV-O / fair2r property short names; rendered only
# at lane-crossing edges to avoid label clutter at intra-lane edges.
EDGES = [
    # PROV-O backbone (left to right)
    ("HumanResearcher", "Activity",    "wasAssociatedWith"),
    ("AIAgent",         "Activity",    "wasAssociatedWith"),
    ("Prompt",          "Activity",    "used"),
    ("Activity",        "Section",     "generated"),
    ("Activity",        "Source",      "used"),
    ("Activity",        "Figure",      "generated"),
    ("Activity",        "Manuscript",  "generated"),
    ("Section",         "Claim",       "contains"),
    ("Source",          "Claim",       "wasDerivedFrom"),
    ("Claim",           "Manuscript",  "appearsIn"),
    # Contributions ring (down to satellites, dotted)
    ("HumanResearcher", "HumanContribution", "contributedBy"),
    ("AIAgent",         "AIContribution",    "contributedBy"),
    ("AIAgent",         "MetaContribution",  "contributedBy"),
]


def count_instances(graph, class_iris: list[str]) -> int:
    """Count rdf:type instances across the given class IRIs."""
    import rdflib
    rdf_type = rdflib.RDF.type
    n = 0
    for iri in class_iris:
        cls = rdflib.URIRef(iri)
        n += sum(1 for _ in graph.triples((None, rdf_type, cls)))
    return n


def load_counts(ttl_path: Path) -> dict[str, int]:
    """Read instance counts from the live graph; pinned fallback if
    rdflib is unavailable or the graph cannot be parsed."""
    pinned = {
        "HumanResearcher": 1, "AIAgent": 13,
        "Prompt": 11,
        "Activity": 29, "AuditPass": 3, "AuthoringPass": 2,
        "Section": 20, "Source": 51, "Figure": 11, "Manuscript": 2,
        "Claim": 37,
        "HumanContribution": 45, "AIContribution": 2, "MetaContribution": 11,
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
    out: dict[str, int] = {}
    for label, (_c, _r, iris, _f) in SCHEMA.items():
        out[label] = count_instances(g, iris)
    return out


def draw_node(ax, x, y, label, count, fill_style, w=2.0, h=0.78):
    """Square-cornered node with class label + instance count."""
    if fill_style[0] == "hatch":
        _, fill, hatch = fill_style
        rect = Rectangle((x - w / 2, y - h / 2), w, h,
                         facecolor=fill, edgecolor=DLR["grau1"],
                         linewidth=0.4, hatch=hatch)
    else:
        _, fill = fill_style
        rect = Rectangle((x - w / 2, y - h / 2), w, h,
                         facecolor=fill, edgecolor=DLR["grau1"],
                         linewidth=0.4)
    ax.add_patch(rect)
    # Class name (top line)
    text_color = "white" if fill_style[1] == DLR["blau1"] else DLR["grau1"]
    ax.text(x, y + 0.13, label,
            ha="center", va="center", fontsize=8.5,
            color=text_color, weight="bold")
    # Instance count badge (bottom line)
    ax.text(x, y - 0.18, f"n = {count}",
            ha="center", va="center", fontsize=8.0,
            color=text_color)


def draw_edge(ax, p_src, p_dst, label, dotted=False):
    style = "-" if not dotted else (0, (1, 1.5))
    arrow = FancyArrowPatch(
        p_src, p_dst,
        arrowstyle="-|>", mutation_scale=8,
        color=DLR["grau1"], linewidth=0.4,
        linestyle=style,
        shrinkA=2, shrinkB=2,
    )
    ax.add_patch(arrow)
    if label:
        # Per-edge label offsets: most edges sit on the midpoint;
        # the AIAgent -> Activity arc rides above its own line so
        # it does not cross the Prompt node, and wasDerivedFrom
        # rides slightly left so it does not collide with the Claim.
        if label == "wasAssociatedWith":
            mx = p_src[0] + 0.45 * (p_dst[0] - p_src[0])
            my = p_src[1] + 0.45 * (p_dst[1] - p_src[1]) + 0.55
        elif label == "wasDerivedFrom":
            mx = p_src[0] + 0.45 * (p_dst[0] - p_src[0])
            my = p_src[1] + 0.45 * (p_dst[1] - p_src[1]) + 0.20
        else:
            mx = (p_src[0] + p_dst[0]) / 2
            my = (p_src[1] + p_dst[1]) / 2 + 0.18
        ax.text(mx, my, label,
                ha="center", va="center", fontsize=6.5,
                color=DLR["grau1"], style="italic")


# Column-edge anchor helpers -----------------------------------------
def node_anchor(label, side, w=2.0, h=0.78):
    """Anchor at the appropriate side of a node centre."""
    cx, cy, _, _ = SCHEMA[label]
    if side == "right":  return (cx + w / 2, cy)
    if side == "left":   return (cx - w / 2, cy)
    if side == "top":    return (cx, cy + h / 2)
    if side == "bottom": return (cx, cy - h / 2)
    return (cx, cy)


def main() -> int:
    repo = Path(__file__).resolve().parents[3]
    ttl = repo / "doc" / "provenance.ttl"
    counts = load_counts(ttl)

    rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": 8.0,
    })

    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    ax.set_xlim(-1.4, 5 * _DX - 0.6)
    ax.set_ylim(-2.1, 3 * _DY + 1.4)
    ax.set_aspect("equal")
    ax.axis("off")

    # Lane headers (column titles, mid-grey hairline rule beneath each)
    lane_titles = [
        (0 * _DX, "Agents"),
        (1 * _DX, "Plans"),
        (2 * _DX, "Activities"),
        (3 * _DX, "Entities"),
        (4 * _DX, "Claims"),
    ]
    header_y = 3 * _DY + 1.0
    for x, name in lane_titles:
        ax.text(x, header_y, name,
                ha="center", va="bottom", fontsize=10.0,
                color=DLR["grau1"], weight="bold")
        ax.plot([x - 1.0, x + 1.0], [header_y - 0.06, header_y - 0.06],
                color=DLR["grau3"], linewidth=0.4)

    # Satellite-band header
    ax.text(2 * _DX, -1.7,
            "Contributions  (HumanContribution / AIContribution / MetaContribution)",
            ha="center", va="center", fontsize=8.0,
            color=DLR["grau1"], style="italic")

    # Draw nodes
    for label, (x, y, _iris, fill_style) in SCHEMA.items():
        draw_node(ax, x, y, label, counts.get(label, 0), fill_style)

    # Draw edges. Pick anchor sides heuristically.
    def pick_sides(src, dst):
        sx, sy, *_ = SCHEMA[src]
        dx, dy, *_ = SCHEMA[dst]
        if abs(dx - sx) > abs(dy - sy):
            return ("right", "left") if dx > sx else ("left", "right")
        return ("bottom", "top") if dy < sy else ("top", "bottom")

    contribution_edges = {("HumanResearcher", "HumanContribution"),
                          ("AIAgent", "AIContribution"),
                          ("AIAgent", "MetaContribution")}
    for src, dst, lbl in EDGES:
        s_side, d_side = pick_sides(src, dst)
        p_src = node_anchor(src, s_side)
        p_dst = node_anchor(dst, d_side)
        # Label only one representative edge per backbone arc, picked
        # so the label sits on a clean diagonal that does not overplot
        # other nodes.
        show_edges = {
            ("AIAgent",  "Activity"):    "wasAssociatedWith",
            ("Prompt",   "Activity"):    "used",
            ("Activity", "Source"):      "generated",
            ("Source",   "Claim"):       "wasDerivedFrom",
            ("Claim",    "Manuscript"):  "appearsIn",
        }
        show = (src, dst) in show_edges
        # Suppress duplicate labels on parallel edges sharing src or dst.
        # (Heuristic: only label one of each property name.)
        draw_edge(ax, p_src, p_dst, lbl if show else "",
                  dotted=(src, dst) in contribution_edges)

    # Footer caption-style label inside the figure (helps the PNG when
    # used standalone on the README / Pages topology preview).
    total = sum(counts.values())
    ax.text(2 * _DX, -2.05,
            f"counts read from doc/provenance.ttl  -  "
            f"{total} typed instances across the schema",
            ha="center", va="center", fontsize=7.5,
            color=DLR["grau1"])

    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    out_dir = repo / "paper" / "figures"
    fig.savefig(out_dir / "provenance-topology.pdf")
    fig.savefig(out_dir / "provenance-topology.png", dpi=300)
    print(f"wrote {out_dir/'provenance-topology.pdf'}")
    print(f"wrote {out_dir/'provenance-topology.png'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
