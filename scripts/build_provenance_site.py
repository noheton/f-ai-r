#!/usr/bin/env python3
"""Build the F(AI^2)R static site to ``_site/``.

Renders Markdown pages from ``doc/``, ``agents/``, and ``site/`` and a
human-readable view of ``doc/provenance.ttl`` grouped by class.

Usage:
    python scripts/build_provenance_site.py

Dependencies (see scripts/requirements.txt):
    - markdown
    - rdflib
"""
from __future__ import annotations

import datetime as _dt
import html
import shutil
import sys
from pathlib import Path
from typing import Iterable

import markdown  # type: ignore[import-not-found]
from rdflib import Graph, Namespace, RDF, RDFS  # type: ignore[import-not-found]
from rdflib.term import URIRef  # type: ignore[import-not-found]

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
TTL = ROOT / "doc" / "provenance.ttl"
SITE_SRC = ROOT / "site"

PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
FAIR2R = Namespace("https://noheton.org/f-ai-r/ns#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

# (slug, title, source markdown path)
PAGES: list[tuple[str, str, Path]] = [
    ("index",                "Home",                   SITE_SRC / "index.md"),
    ("methodology",          "Methodology",            ROOT / "doc" / "methodology.md"),
    ("fair",                 "FAIR",                   ROOT / "doc" / "fair.md"),
    ("collab",               "Human-AI collaboration", ROOT / "doc" / "human-ai-collaboration-process.md"),
    ("research-protocol",    "Research protocol",      ROOT / "doc" / "research-protocol.md"),
    ("submission",           "Submission",             ROOT / "doc" / "submission-plan.md"),
    ("logbook",              "Logbook",                ROOT / "doc" / "logbook.md"),
    ("user-contributions",   "User contributions",     ROOT / "doc" / "user-contributions.md"),
    ("user-observations",    "Observations log",       ROOT / "doc" / "user-observations-log.md"),
    ("reading-queue",        "Reading queue",          ROOT / "doc" / "reading-queue.md"),
    ("provenance-graph",     "Provenance topology",    ROOT / "doc" / "provenance-graph.md"),
    ("provenance-explorer",  "Provenance explorer",    SITE_SRC / "provenance-explorer.md"),
]

# Order in which nav items appear, with their final slugs.
NAV: list[tuple[str, str]] = [
    ("index",                "Home"),
    ("methodology",          "Methodology"),
    ("fair",                 "FAIR"),
    ("collab",               "Collab"),
    ("agents",               "Agents"),
    ("logbook",              "Logbook"),
    ("user-contributions",   "Contributions"),
    ("user-observations",    "Observations"),
    ("reading-queue",        "Reading queue"),
    ("provenance",           "Provenance"),
    ("provenance-explorer",  "Explorer"),
    ("provenance-graph",     "Topology"),
    ("submission",           "Submission"),
]

MD_EXT = ["fenced_code", "tables", "toc", "sane_lists"]

TEMPLATE = """<!doctype html>
<html lang="en" data-variant="a">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-cache, must-revalidate">
<meta name="build-version" content="{cache_bust}">
<title>{title} - F(AI)²R</title>
<link rel="stylesheet" href="static/style.css?v={cache_bust}">
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
</script>
</head>
<body>
<div class="utility">
  <div class="inner">
    <a href="https://github.com/noheton/f-ai-r">Repository</a>
    <a href="https://orcid.org/0000-0001-6033-801X">ORCID</a>
    <span>EN</span>
  </div>
</div>
<div class="header">
  <div class="inner">
    <img class="logo" src="static/dlr/dlr-logo.svg" alt="DLR Logo">
    <div class="org-line">
      <span class="big">F(AI)²R &mdash; FAIR Research with AI in the Loop, Twice</span>
      DLR Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg
      &middot; Helmholtz-Gemeinschaft &middot; NFDI4Ing &middot; HMC
    </div>
  </div>
</div>
<nav class="nav">
  <div class="inner">{nav}</div>
</nav>
<section class="hero">
  <div class="inner">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{hero_title}</h1>
    <div class="build-tag" title="Hash over content; if you're seeing an old version your browser or CDN cache is stale.">
      build <code>{cache_bust}</code>
    </div>
  </div>
</section>
<main>
  <aside class="sidebar">
    <h4>On this site</h4>
    <ul>{sidebar}</ul>
    <h4>External</h4>
    <ul>
      <li><a href="https://github.com/noheton/f-ai-r">GitHub repository</a></li>
      <li><a href="https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf">Latest draft (PDF)</a></li>
      <li><a href="https://orcid.org/0000-0001-6033-801X">ORCID 0000-0001-6033-801X</a></li>
      <li><a href="https://www.dlr.de/zlp">DLR ZLP Augsburg</a></li>
    </ul>
  </aside>
  <article class="content">{body}</article>
</main>
<footer>
  <div class="inner">
    <div>
      <h4>F(AI)²R</h4>
      <p>FAIR research with AI in the loop, twice. Working paper plus
         reproducible writing pipeline. Built {built} from
         <a href="https://github.com/noheton/f-ai-r">noheton/f-ai-r</a>
         (build {cache_bust}).</p>
    </div>
    <div>
      <h4>Imprint</h4>
      <p>Florian Krebs<br>
         ORCID 0000-0001-6033-801X<br>
         DLR ZLP, Augsburg</p>
    </div>
    <div>
      <h4>Affiliations</h4>
      <p><a href="https://www.helmholtz.de/">Helmholtz-Gemeinschaft</a><br>
         <a href="https://nfdi4ing.de/">NFDI4Ing</a><br>
         <a href="https://helmholtz-metadaten.de/">HMC</a></p>
    </div>
  </div>
  <div class="legal">
    <div class="inner">
      <span>Code: MIT &middot; Prose: CC-BY-4.0</span>
      <span>Photo credit (where present): DLR (CC BY-NC-ND 3.0) sofern nicht anders angegeben.</span>
    </div>
  </div>
</footer>
</body>
</html>
"""


_MERMAID_FENCE = __import__("re").compile(
    r"^```mermaid\s*\n(.*?)^```\s*$", __import__("re").MULTILINE | __import__("re").DOTALL
)


def render_md(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    # Pull Mermaid fenced blocks out before markdown runs so that the
    # markdown library does not HTML-escape their contents (which would
    # break client-side rendering: Mermaid needs raw " and <br/>).
    blocks: list[str] = []

    def _stash(match):
        blocks.append(match.group(1))
        return f"\n\nMERMAIDPLACEHOLDER{len(blocks) - 1}END\n\n"

    text = _MERMAID_FENCE.sub(_stash, text)
    rendered = markdown.markdown(text, extensions=MD_EXT)
    # Re-inject the original (un-escaped) Mermaid source.
    for i, src in enumerate(blocks):
        rendered = rendered.replace(
            f"<p>MERMAIDPLACEHOLDER{i}END</p>",
            f'<div class="mermaid">\n{src}</div>',
        )
    return rendered


def nav_html(active: str) -> str:
    parts: list[str] = []
    for slug, title in NAV:
        cls = ' class="active"' if slug == active else ""
        parts.append(f'<a href="{slug}.html"{cls}>{title}</a>')
    return "".join(parts)


def sidebar_html(active: str) -> str:
    parts: list[str] = []
    for slug, title in NAV:
        cls = ' class="active"' if slug == active else ""
        parts.append(f'<li><a href="{slug}.html"{cls}>{title}</a></li>')
    return "".join(parts)


_CACHE_BUST = ""  # Set by main() once per build.


def write_page(slug: str, title: str, body_html: str, eyebrow: str = "F(AI)²R") -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{slug}.html"
    out.write_text(
        TEMPLATE.format(
            title=html.escape(title),
            hero_title=html.escape(title),
            eyebrow=html.escape(eyebrow),
            body=body_html,
            nav=nav_html(slug),
            sidebar=sidebar_html(slug),
            built=_dt.date.today().isoformat(),
            cache_bust=_CACHE_BUST,
        ),
        encoding="utf-8",
    )


def label_of(graph: Graph, subject: URIRef) -> str:
    for o in graph.objects(subject, RDFS.label):
        return str(o)
    s = str(subject)
    return s.rsplit("/", 1)[-1].split("#")[-1]


def render_provenance(graph: Graph) -> str:
    groups: list[tuple[str, list[URIRef]]] = [
        ("Agents",                  [FAIR2R.AIAgent, FAIR2R.HumanResearcher]),
        ("Activities",              [PROV.Activity, FAIR2R.AuthoringPass,
                                     FAIR2R.AuditPass, FAIR2R.Build]),
        ("Manuscripts and parts",   [FAIR2R.Manuscript, FAIR2R.Section, FAIR2R.Figure]),
        ("Sources",                 [FAIR2R.Source]),
        ("Prompts (plans)",         [FAIR2R.Prompt]),
        ("Claims",                  [FAIR2R.Claim]),
    ]

    out: list[str] = []
    out.append("<h2>Provenance graph</h2>")
    out.append(
        "<p class='callout'>Authoritative source: "
        "<a href='https://github.com/noheton/f-ai-r/blob/main/doc/provenance.ttl'>"
        "<code>doc/provenance.ttl</code></a>. This page is a rendered view; "
        "see <a href='provenance-graph.html'>Topology</a> for the diagram.</p>"
    )

    seen: set[URIRef] = set()
    for group_title, types in groups:
        rows: list[tuple[str, str, str]] = []
        for t in types:
            for s in graph.subjects(RDF.type, t):
                if not isinstance(s, URIRef):
                    continue
                if s in seen:
                    continue
                seen.add(s)
                attrs: list[str] = []
                for o in graph.objects(s, FAIR2R.verificationState):
                    attrs.append(f"verification: <code>{html.escape(label_of(graph, o))}</code>")
                for o in graph.objects(s, DCT.created):
                    attrs.append(f"created: {html.escape(str(o))}")
                for o in graph.objects(s, PROV.wasGeneratedBy):
                    attrs.append(f"generated by: <code>{html.escape(label_of(graph, o))}</code>")
                for o in graph.objects(s, PROV.wasAttributedTo):
                    attrs.append(f"attributed to: <code>{html.escape(label_of(graph, o))}</code>")
                for o in graph.objects(s, PROV.wasAssociatedWith):
                    attrs.append(f"associated with: <code>{html.escape(label_of(graph, o))}</code>")
                for o in graph.objects(s, FOAF.name):
                    attrs.append(f"name: {html.escape(str(o))}")
                rows.append((label_of(graph, s), str(s), "; ".join(attrs)))
        if not rows:
            continue
        out.append(f"<h3>{html.escape(group_title)}</h3>")
        out.append("<table><thead><tr><th>Label</th><th>IRI</th><th>Attributes</th></tr></thead><tbody>")
        for lbl, iri, attrs in sorted(rows, key=lambda r: r[0].lower()):
            out.append(
                f"<tr><td>{html.escape(lbl)}</td>"
                f"<td><code>{html.escape(iri)}</code></td>"
                f"<td>{attrs}</td></tr>"
            )
        out.append("</tbody></table>")

    return "\n".join(out)


def render_agents() -> str:
    agents_dir = ROOT / "agents"
    readme = render_md(agents_dir / "README.md")
    files = sorted(p for p in agents_dir.glob("*.md") if p.name != "README.md")
    links = "<h3>Per-role prompts</h3><ul>"
    for p in files:
        links += f'<li><a href="agent-{p.stem}.html"><code>{p.stem}</code></a></li>'
    links += "</ul>"
    return readme + links


CLASS_FOR_TYPE = {
    str(FAIR2R.AIAgent):          "agent",
    str(FAIR2R.HumanResearcher):  "agent",
    str(PROV.Activity):           "activity",
    str(FAIR2R.AuthoringPass):    "activity",
    str(FAIR2R.AuditPass):        "activity",
    str(FAIR2R.Build):            "activity",
    str(FAIR2R.Manuscript):       "entity",
    str(FAIR2R.Section):          "entity",
    str(FAIR2R.Figure):           "entity",
    str(FAIR2R.Source):           "source",
    str(FAIR2R.Prompt):           "prompt",
    str(FAIR2R.Claim):            "claim",
    str(PROV.Entity):             "entity",
}


def export_provenance_json(g: Graph, out_path: Path) -> None:
    """Project the PROV-O graph to a vis-network friendly JSON file
    (nodes + directed edges) for the interactive explorer page.
    """
    import json

    # Pass 1: collect nodes for every named subject/object that has a
    # label, a type we recognise, or participates in a PROV/dcterms edge.
    nodes: dict[str, dict[str, object]] = {}

    def add_node(uri):
        if not isinstance(uri, URIRef):
            return
        s = str(uri)
        if s in nodes:
            return
        cls = "other"
        for t in g.objects(uri, RDF.type):
            cls = CLASS_FOR_TYPE.get(str(t), cls)
            if cls != "other":
                break
        nodes[s] = {
            "id": s,
            "iri": s,
            "label": label_of(g, uri),
            "cls": cls,
        }

    interesting_predicates = {
        PROV.wasGeneratedBy,
        PROV.wasAttributedTo,
        PROV.wasDerivedFrom,
        PROV.used,
        PROV.wasAssociatedWith,
        PROV.actedOnBehalfOf,
        PROV.hadPlan,
        PROV.wasInformedBy,
        PROV.wasRevisionOf,
        PROV.invalidated,
        PROV.hadPrimarySource,
        FAIR2R.verificationState,
        FAIR2R.contradicts,
    }

    edges: list[dict[str, str]] = []
    for s, p, o in g.triples((None, None, None)):
        if p in interesting_predicates and isinstance(s, URIRef) and isinstance(o, URIRef):
            add_node(s)
            add_node(o)
            edges.append({
                "from": str(s),
                "to": str(o),
                "label": p.n3(g.namespace_manager).replace("prov:", "")
                                                  .replace("fair2r:", ""),
            })
    # Also surface all top-level typed subjects, even if disconnected.
    for cls_iri in CLASS_FOR_TYPE.keys():
        for s in g.subjects(RDF.type, URIRef(cls_iri)):
            add_node(s)

    out = {"nodes": list(nodes.values()), "edges": edges}
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def _compute_cache_bust() -> str:
    """Hash the inputs that affect rendered pages so the build emits a
    fresh asset version per content change. The version is appended to
    every internal asset URL (style.css, provenance.json) so a stale
    GitHub-Pages CDN cache cannot serve an outdated bundle to a reader.
    """
    import hashlib
    h = hashlib.sha1()
    candidates: list[Path] = [
        SITE_SRC / "static" / "style.css",
        TTL,
        ROOT / "site" / "index.md",
        SITE_SRC / "provenance-explorer.md",
    ]
    for p in candidates:
        if p.is_file():
            h.update(p.read_bytes())
    return h.hexdigest()[:10]


def main(argv: Iterable[str]) -> int:
    global _CACHE_BUST
    _CACHE_BUST = _compute_cache_bust()
    print(f"Build cache-bust version: {_CACHE_BUST}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    # Static assets
    static_src = SITE_SRC / "static"
    if static_src.is_dir():
        shutil.copytree(static_src, OUT / "static", dirs_exist_ok=True)

    # GitHub Pages defaults to running Jekyll on the deployed artefact;
    # the .nojekyll marker disables that pass so paths starting with
    # underscores (and our static/ tree) are served verbatim. Also acts
    # as a small heartbeat: if this file is missing on the deployed
    # site, the build did not run.
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    # Markdown pages
    for slug, title, src in PAGES:
        write_page(slug, title, render_md(src))

    # Agents
    write_page("agents", "Agents", render_agents())
    for p in sorted((ROOT / "agents").glob("*.md")):
        if p.name == "README.md":
            continue
        write_page(f"agent-{p.stem}", f"Agent: {p.stem}", render_md(p))

    # Provenance
    g = Graph()
    g.parse(TTL, format="turtle")
    write_page("provenance", "Provenance", render_provenance(g))

    # Interactive explorer JSON: emitted alongside the static assets.
    export_provenance_json(g, OUT / "static" / "provenance.json")

    pages = sorted(OUT.glob("*.html"))
    print(f"Built {len(pages)} pages to {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
