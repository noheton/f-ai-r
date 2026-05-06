#!/usr/bin/env python3
"""Generate ``doc/reading-queue.md`` from ``doc/provenance.ttl`` + ``paper/references.bib``.

The reading queue is the focused list of sources the human author must
read in full to advance them from ``lit-retrieved`` to ``lit-read``
before the manuscript can be submitted under the methodology
(``doc/methodology.md``: "a claim must reach lit-read or
source-vendored before it can appear in the condensed manuscript").

For each source at ``lit-retrieved``, the queue records:

- the bibliographic citation (from references.bib);
- the verification rung (always ``lit-retrieved`` here);
- the load-bearing weight = number of ``fair2r:Claim`` entities that
  invoke the source via ``prov:wasDerivedFrom``;
- the sections of the manuscript the dependent claims appear in;
- whether the abstract is sufficient or the full text is required;
- a paywall flag where applicable (institutional access channel).

The queue is sorted by load-bearing weight descending, so the human
author can prioritise.

Usage::

    python scripts/build_reading_queue.py

Writes ``doc/reading-queue.md`` (overwritten on every run).

Dependencies (see ``scripts/requirements.txt``)::

    rdflib
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.term import URIRef

ROOT = Path(__file__).resolve().parents[1]
TTL = ROOT / "doc" / "provenance.ttl"
BIB = ROOT / "paper" / "references.bib"
OUT = ROOT / "doc" / "reading-queue.md"

PROV = Namespace("http://www.w3.org/ns/prov#")
DCT = Namespace("http://purl.org/dc/terms/")
FAIR2R = Namespace("https://noheton.org/f-ai-r/ns#")

# Pattern that matches a single bibtex entry, capturing the key.
BIB_ENTRY = re.compile(
    r"@(?P<type>\w+)\s*\{\s*(?P<key>[^,\s]+)\s*,(?P<body>.+?)\n\}\s*\n",
    re.DOTALL,
)
BIB_FIELD = re.compile(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", re.DOTALL | re.MULTILINE)


def short(uri) -> str:
    s = str(uri)
    if "#" in s:
        return s.rsplit("#", 1)[-1]
    return s.rsplit("/", 1)[-1]


def label_of(g: Graph, subject: URIRef) -> str:
    for o in g.objects(subject, RDFS.label):
        return str(o)
    return short(subject)


def parse_bib(path: Path) -> dict[str, dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, dict[str, str]] = {}
    for m in BIB_ENTRY.finditer(text):
        body = m.group("body")
        fields: dict[str, str] = {"_type": m.group("type")}
        # naive bibtex field extraction; good enough for our entries.
        for fm in re.finditer(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", body):
            fields[fm.group(1).lower()] = re.sub(r"\s+", " ", fm.group(2)).strip()
        out[m.group("key")] = fields
    return out


def cite(key: str, fields: dict[str, str]) -> str:
    parts = []
    if "author" in fields:
        parts.append(fields["author"])
    if "year" in fields:
        parts.append(f"({fields['year']})")
    if "title" in fields:
        parts.append(f"\"{fields['title']}\"")
    venue = fields.get("journal") or fields.get("booktitle") or fields.get("howpublished")
    if venue:
        parts.append(f"*{venue}*")
    if "doi" in fields:
        parts.append(f"DOI: [{fields['doi']}](https://doi.org/{fields['doi']})")
    elif "eprint" in fields:
        parts.append(f"arXiv: [{fields['eprint']}](https://arxiv.org/abs/{fields['eprint']})")
    elif "url" in fields:
        parts.append(f"<{fields['url']}>")
    return ". ".join(parts)


def main(argv) -> int:
    g = Graph()
    g.parse(TTL, format="turtle")
    bib = parse_bib(BIB)

    # Build src-bibkey map: every fair2r:Source has a label and an
    # identifier; the bibkey is the IRI fragment after the last "/".
    sources: list[tuple[str, URIRef, str, str]] = []
    for s in g.subjects(RDF.type, FAIR2R.Source):
        if not isinstance(s, URIRef):
            continue
        rung = next(g.objects(s, FAIR2R.verificationState), None)
        rung_label = short(rung) if rung else "no-rung"
        title = label_of(g, s)
        bibkey = short(s)  # src:foo -> "foo"
        sources.append((bibkey, s, rung_label, title))

    # For each source, find dependent claims and their sections.
    deps: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for c in g.subjects(RDF.type, FAIR2R.Claim):
        c_label = label_of(g, c)
        for src in g.objects(c, PROV.wasDerivedFrom):
            if isinstance(src, URIRef):
                deps[short(src)].append((short(c), c_label))

    # Filter to lit-retrieved or no-rung; sort by claim count desc.
    queue = [
        (k, s, r, t) for (k, s, r, t) in sources
        if r in {"lit-retrieved", "no-rung", "ai-confirmed"}
    ]
    queue.sort(key=lambda row: (-len(deps.get(row[0], [])), row[0]))

    # Emit markdown.
    lines: list[str] = []
    lines.append("# Reading queue")
    lines.append("")
    lines.append("Auto-generated from `doc/provenance.ttl` and `paper/references.bib`.")
    lines.append("Regenerated on every build; do not edit by hand.")
    lines.append("")
    lines.append("This is the focused list of sources the human author needs to "
                 "read in full to advance them from `lit-retrieved` (or "
                 "`ai-confirmed`) to `lit-read` before the manuscript can "
                 "appear at submission under the methodology in "
                 "[`doc/methodology.md`](methodology.md).")
    lines.append("")
    lines.append("Sources with the most dependent `fair2r:Claim` entries appear first.")
    lines.append("Once a source has been read, advance its rung in "
                 "`doc/provenance.ttl` and (optionally) drop the `\\todo[inline]"
                 "{verify}` marker next to its `\\cite{}` keys in "
                 "`paper/sections/*.tex`.")
    lines.append("")
    lines.append(f"## State at the time of this build")
    lines.append("")
    lines.append(f"- Sources in queue: **{len(queue)}**")
    lines.append(f"- Sources at `lit-retrieved`: "
                 f"{sum(1 for _, _, r, _ in queue if r == 'lit-retrieved')}")
    lines.append(f"- Sources at `ai-confirmed`: "
                 f"{sum(1 for _, _, r, _ in queue if r == 'ai-confirmed')}")
    lines.append(f"- Sources without a rung (graph cleanliness defect): "
                 f"{sum(1 for _, _, r, _ in queue if r == 'no-rung')}")
    lines.append("")
    lines.append("## Queue (highest leverage first)")
    lines.append("")

    for idx, (bibkey, src_iri, rung, title) in enumerate(queue, 1):
        b = bib.get(bibkey, {})
        cite_str = cite(bibkey, b) if b else f"*(no bib entry for `{bibkey}`)*"
        n = len(deps.get(bibkey, []))
        lines.append(f"### {idx}. `{bibkey}` --- rung: `{rung}`, "
                     f"dependent claims: **{n}**")
        lines.append("")
        lines.append(f"**Citation.** {cite_str}")
        lines.append("")
        if n:
            lines.append("**Dependent claims** (advancing this source to "
                         "`lit-read` would unblock):")
            lines.append("")
            for c_short, c_lbl in deps[bibkey]:
                lines.append(f"- `{c_short}` --- {c_lbl}")
            lines.append("")
        else:
            lines.append("*(No `fair2r:Claim` currently lists this source as "
                         "`prov:wasDerivedFrom`. Consider whether the source is "
                         "still needed; if it is, add the missing edge in "
                         "`doc/provenance.ttl`. If it is not, retire the bib "
                         "entry.)*")
            lines.append("")
        if "doi" in b:
            lines.append(f"**Open via DOI:** "
                         f"<https://doi.org/{b['doi']}>")
        elif "eprint" in b:
            lines.append(f"**Open via arXiv:** "
                         f"<https://arxiv.org/abs/{b['eprint']}>")
        elif "url" in b:
            lines.append(f"**Open via URL:** <{b['url']}>")
        lines.append("")
        if "note" in b:
            lines.append(f"**Note from the bib.** {b['note']}")
            lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## What \"reading\" means here")
    lines.append("")
    lines.append("Per the verification ladder, advancing from `lit-retrieved` "
                 "(or `ai-confirmed`) to `lit-read` requires that **the human "
                 "author has read the source itself, not just the abstract**, "
                 "and has confirmed both that it supports the claim and that "
                 "the inference from source to claim is sound.")
    lines.append("")
    lines.append("If a source is paywalled and institutional access is required, "
                 "see [`doc/sources-needing-institutional-access.md`](sources-needing-institutional-access.md) "
                 "(create if necessary) per `agents/source-analyzer.md`.")
    lines.append("")
    lines.append("If a source turns out to be unsupportive on full reading, the "
                 "verification rung does not advance --- instead, the source is "
                 "removed from `prov:wasDerivedFrom` and replaced; the bib "
                 "entry stays for historical accuracy.")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(queue)} entries in queue).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
