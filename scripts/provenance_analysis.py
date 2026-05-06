#!/usr/bin/env python3
"""Generate provenance-analysis fragments for the F(AI)^2R paper.

Reads ``doc/provenance.ttl`` and emits four LaTeX fragments under
``paper/sections/_generated/`` that are ``\\input``'d by
``paper/sections/provenance-analysis.tex``:

- ``rung-distribution.tex`` — verification-rung histogram as a table.
- ``section-coverage.tex``  — which paper sections have a graph entry
                              and how many claims they carry.
- ``source-strength.tex``   — which sources are linked from at least
                              one claim, and how many ghost citations
                              remain.
- ``recent-activities.tex`` — the five most recent ``prov:Activity``
                              entries.

The script is run by the build pipeline; it has no side effects beyond
writing those four files, so a clean checkout always sees the
fragments freshly regenerated.

Usage::

    python scripts/provenance_analysis.py

Dependencies (see ``scripts/requirements.txt``)::

    rdflib

The corresponding Make target is ``make -C paper provenance``; the
``build-paper`` workflow runs the script before ``latexmk``.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

from rdflib import Graph, Namespace  # type: ignore[import-not-found]
from rdflib.namespace import RDF, RDFS  # type: ignore[import-not-found]
from rdflib.term import URIRef  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]
TTL = ROOT / "doc" / "provenance.ttl"
OUT_DIR = ROOT / "paper" / "sections" / "_generated"
PAPER_SECTIONS = ROOT / "paper" / "sections"

PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
FAIR2R = Namespace("https://noheton.org/f-ai-r/ns#")

RUNG_ORDER = [
    ("unverified",      "unverified-external"),
    ("needs-research",  "needs-research"),
    ("lit-retrieved",   "lit-retrieved"),
    ("ai-confirmed",    "ai-confirmed"),
    ("human-confirmed", "human-confirmed"),
    ("source-vendored", "source-vendored"),
    ("lit-read",        "lit-read"),
]


def short(uri: URIRef | str) -> str:
    s = str(uri)
    if "#" in s:
        return s.rsplit("#", 1)[-1]
    return s.rsplit("/", 1)[-1]


def label_of(g: Graph, subject: URIRef) -> str:
    for o in g.objects(subject, RDFS.label):
        return str(o)
    return short(subject)


def latex_escape(s: str) -> str:
    return (
        s.replace("\\", r"\textbackslash{}")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("$", r"\$")
        .replace("#", r"\#")
        .replace("_", r"\_")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("^", r"\^{}")
        .replace("~", r"\~{}")
    )


def write_fragment(name: str, body: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / name).write_text(body, encoding="utf-8")


# ---------------------------------------------------------------------------
# 1. Verification-rung distribution
# ---------------------------------------------------------------------------

def write_rung_distribution(g: Graph) -> None:
    counts: Counter[str] = Counter()
    total = 0
    for c in g.subjects(RDF.type, FAIR2R.Claim):
        for state in g.objects(c, FAIR2R.verificationState):
            counts[short(state)] += 1
            total += 1

    rows: list[str] = []
    seen: set[str] = set()
    for slug, label in RUNG_ORDER:
        n = counts.get(slug, 0)
        seen.add(slug)
        if n == 0 and slug not in {"verif:lit-read",
                                    "verif:human-confirmed",
                                    "verif:ai-confirmed"}:
            continue
        pct = (100 * n / total) if total else 0
        rows.append(f"{label} & {n} & {pct:.1f}\\,\\% \\\\")
    # Catch any extra rungs not in our canonical order.
    for slug in counts.keys() - seen:
        n = counts[slug]
        pct = (100 * n / total) if total else 0
        rows.append(f"{latex_escape(slug)} & {n} & {pct:.1f}\\,\\% \\\\")

    body = (
        "\\begin{tabular}{lrr}\n"
        "\\toprule\n"
        "Rung & Claims & Share \\\\\n"
        "\\midrule\n"
        + "\n".join(rows)
        + f"\n\\midrule\n\\textbf{{Total}} & \\textbf{{{total}}} & \\\\\n"
        "\\bottomrule\n"
        "\\end{tabular}\n"
    )
    write_fragment("rung-distribution.tex", body)


# ---------------------------------------------------------------------------
# 2. Section-to-claim coverage
# ---------------------------------------------------------------------------

# We use the labels of fair2r:Section entities as the truth set, plus a
# scan of paper/sections/*.tex for any \section{...} that is not yet
# represented in the graph.
LABEL_RE = re.compile(r"\\label\{sec:([^}]+)\}")
SECTION_HEAD_RE = re.compile(r"\\section\*?\{([^}]+)\}")


def write_section_coverage(g: Graph) -> None:
    graph_sections: dict[str, URIRef] = {}
    for s in g.subjects(RDF.type, FAIR2R.Section):
        if isinstance(s, URIRef):
            graph_sections[label_of(g, s)] = s

    prose_sections: list[tuple[str, str]] = []
    for tex in sorted(PAPER_SECTIONS.glob("*.tex")):
        if tex.parent.name == "_generated" or tex.name.startswith("_"):
            continue
        text = tex.read_text(encoding="utf-8")
        m_label = LABEL_RE.search(text)
        m_head = SECTION_HEAD_RE.search(text)
        if m_label and m_head:
            head = m_head.group(1).strip()
            # Strip \texorpdfstring{X}{Y} -> Y (the PDF-friendly form);
            # strip \textsuperscript{X} -> X; strip stray \\ ...
            head = re.sub(r"\\texorpdfstring\{[^}]*\}\{([^}]*)\}", r"\1", head)
            head = re.sub(r"\\textsuperscript\{([^}]*)\}", r"\1", head)
            head = re.sub(r"\\\\.*$", "", head)
            head = re.sub(r"\\[a-zA-Z]+\*?", "", head)
            head = head.replace("{", "").replace("}", "").strip()
            prose_sections.append((head, "sec:" + m_label.group(1).strip()))

    rows: list[str] = []
    for head, label in prose_sections:
        # Find a graph section whose label or rdfs:label loosely matches.
        gs = next(
            (s for lbl, s in graph_sections.items()
             if lbl.lower().strip(" .") == head.lower().strip(" .")
             or short(s).endswith(label.split(":")[-1])),
            None,
        )
        if gs is None:
            graph_state = "no"
            n_claims = 0
        else:
            graph_state = "yes"
            n_claims = sum(
                1 for c in g.subjects(RDF.type, FAIR2R.Claim)
                if any(
                    g.subjects(PROV.wasGeneratedBy, gs)
                    for _ in [None]  # placeholder; see below
                )
            )
            # Cleaner count: claims generated by activities that
            # generated this section.
            n_claims = 0
            for act in g.objects(gs, PROV.wasGeneratedBy):
                for c in g.subjects(PROV.wasGeneratedBy, act):
                    for _ in g.triples((c, RDF.type, FAIR2R.Claim)):
                        n_claims += 1
        rows.append(
            f"{latex_escape(head)} & "
            f"\\texttt{{{latex_escape(label)}}} & "
            f"{graph_state} & {n_claims} \\\\"
        )

    body = (
        "\\begin{tabular}{p{4.6cm}p{3.2cm}cr}\n"
        "\\toprule\n"
        "Section heading & Label & In graph? & Claims \\\\\n"
        "\\midrule\n"
        + "\n".join(rows) + "\n"
        "\\bottomrule\n"
        "\\end{tabular}\n"
    )
    write_fragment("section-coverage.tex", body)


# ---------------------------------------------------------------------------
# 3. Source invocation strength
# ---------------------------------------------------------------------------

def write_source_strength(g: Graph) -> None:
    sources: list[URIRef] = [
        s for s in g.subjects(RDF.type, FAIR2R.Source) if isinstance(s, URIRef)
    ]
    invoked: dict[URIRef, int] = {s: 0 for s in sources}
    for c in g.subjects(RDF.type, FAIR2R.Claim):
        for s in g.objects(c, PROV.wasDerivedFrom):
            if s in invoked:
                invoked[s] += 1
    ghost = [s for s, n in invoked.items() if n == 0]

    rows: list[str] = []
    for s in sorted(sources, key=lambda u: short(u)):
        n = invoked[s]
        rows.append(
            f"\\texttt{{{latex_escape(short(s))}}} & "
            f"{latex_escape(label_of(g, s))[:60]} & "
            f"{n} \\\\"
        )

    body = (
        f"\\noindent Sources cited: {len(sources)}; "
        f"invoked by at least one claim: {len(sources) - len(ghost)}; "
        f"\\textbf{{ghost citations: {len(ghost)}}}.\n\n"
        "\\smallskip\n"
        "\\begin{tabular}{p{3.5cm}p{7cm}r}\n"
        "\\toprule\n"
        "Source & Title & Invocations \\\\\n"
        "\\midrule\n"
        + "\n".join(rows) + "\n"
        "\\bottomrule\n"
        "\\end{tabular}\n"
    )
    write_fragment("source-strength.tex", body)


# ---------------------------------------------------------------------------
# 4. Recent activities
# ---------------------------------------------------------------------------

def write_recent_activities(g: Graph) -> None:
    rows: list[tuple[str, URIRef, str]] = []
    for a in g.subjects(RDF.type, PROV.Activity):
        end = next(g.objects(a, PROV.endedAtTime), None) \
              or next(g.objects(a, PROV.startedAtTime), None)
        if end is None:
            continue
        rows.append((str(end), a, label_of(g, a)))
    # Also include subclasses of prov:Activity that are typed via
    # fair2r:AuthoringPass / fair2r:AuditPass / fair2r:Build.
    for cls in [FAIR2R.AuthoringPass, FAIR2R.AuditPass, FAIR2R.Build]:
        for a in g.subjects(RDF.type, cls):
            end = next(g.objects(a, PROV.endedAtTime), None) \
                  or next(g.objects(a, PROV.startedAtTime), None)
            if end is None:
                continue
            rows.append((str(end), a, label_of(g, a)))

    # De-duplicate keeping the most informative label.
    by_uri: dict[URIRef, tuple[str, str]] = {}
    for end, uri, lbl in rows:
        by_uri[uri] = (end, lbl)
    flat = [(end, uri, lbl) for uri, (end, lbl) in by_uri.items()]
    flat.sort(reverse=True)
    flat = flat[:5]

    out_rows: list[str] = []
    for end, uri, lbl in flat:
        date = end[:10]
        out_rows.append(
            f"{latex_escape(date)} & "
            f"\\texttt{{{latex_escape(short(uri))}}} & "
            f"{latex_escape(lbl)[:80]} \\\\"
        )

    body = (
        "\\begin{tabular}{lp{3.0cm}p{6.5cm}}\n"
        "\\toprule\n"
        "Date & Activity & Label \\\\\n"
        "\\midrule\n"
        + "\n".join(out_rows) + "\n"
        "\\bottomrule\n"
        "\\end{tabular}\n"
    )
    write_fragment("recent-activities.tex", body)


def main() -> int:
    g = Graph()
    g.parse(TTL, format="turtle")
    print(f"Parsed {len(g)} triples from {TTL.relative_to(ROOT)}")

    write_rung_distribution(g)
    write_section_coverage(g)
    write_source_strength(g)
    write_recent_activities(g)

    print(f"Wrote four fragments to {OUT_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
