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
OUT_DETAILS = ROOT / "doc" / "reading-queue-details.md"
VERDICTS = ROOT / "doc" / "reading-queue-verdicts.md"

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


def open_url(fields: dict[str, str]) -> str | None:
    """Return a single canonical URL for the source, or None if unavailable."""
    if "doi" in fields:
        return f"https://doi.org/{fields['doi']}"
    if "eprint" in fields:
        return f"https://arxiv.org/abs/{fields['eprint']}"
    if "url" in fields:
        return fields["url"]
    return None


def short_author(fields: dict[str, str]) -> str:
    """First author surname + et al. when there are multiple authors.

    Handles bibtex corporate-author convention: ``{ACL Rolling Review}``
    is one entity, not "Review".
    """
    raw = fields.get("author", "").strip()
    if not raw:
        return "(no author)"
    first = raw.split(" and ")[0].strip()
    extras = raw.count(" and ")
    # Corporate author: protected with outer braces, treat as one entity.
    if first.startswith("{") and first.endswith("}"):
        surname = first[1:-1].strip()
    elif "," in first:
        surname = first.split(",", 1)[0].strip().strip("{}")
    else:
        surname = first.rsplit(" ", 1)[-1].strip().strip("{}")
    return f"{surname} et al." if extras else surname


def short_title(fields: dict[str, str], limit: int = 70) -> str:
    title = fields.get("title", "").strip()
    if not title:
        return "(no title)"
    if len(title) <= limit:
        return title
    return title[: limit - 1].rstrip() + "…"


def md_escape_cell(s: str) -> str:
    """Escape characters that would break a Markdown table cell."""
    return s.replace("|", "\\|").replace("\n", " ").strip()


def intervention_note(rung: str, n_claims: int) -> str:
    """One-line note on whether the human author still needs to act."""
    if n_claims == 0:
        return "retire bib entry or add a `prov:wasDerivedFrom` edge"
    if rung == "lit-retrieved":
        return "human read required (rung still at retrieval)"
    if rung == "ai-confirmed":
        return "human read required to advance to `lit-read`"
    if rung == "no-rung":
        return "graph-cleanliness defect: source has no rung"
    return "no intervention needed"


VERDICT_LINE = re.compile(
    r"^\s*(?P<key>[A-Za-z0-9_:.\-]+)\s*:\s*"
    r"(?P<verdict>advance|hold|retire|pending)\b"
    r"(?:\s*[-—]\s*(?P<note>.*))?$"
)

VALID_VERDICTS = {"advance", "hold", "retire", "pending"}


def parse_verdicts(path: Path) -> dict[str, dict[str, str]]:
    """Read ``doc/reading-queue-verdicts.md``, returning ``{bibkey: {verdict, note}}``.

    Format is one line per source::

        bibkey: <advance|hold|retire|pending> — optional free-text note

    Lines that do not match are skipped silently; the file may carry a
    Markdown preamble. Missing file is treated as "no verdicts yet".
    """
    out: dict[str, dict[str, str]] = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        m = VERDICT_LINE.match(line)
        if not m:
            continue
        key = m.group("key")
        verdict = m.group("verdict")
        note = (m.group("note") or "").strip()
        out[key] = {"verdict": verdict, "note": note}
    return out


def render_questions(claims: list[tuple[str, str]], limit: int = 110) -> str:
    """One verification question per dependent claim, joined for a table cell."""
    if not claims:
        return "*(retire / wire-up question)*"
    qs: list[str] = []
    for slug, label in claims:
        # Trim multi-clause labels to a leading clause for readability.
        head = label.split(".")[0].split(";")[0].strip()
        if len(head) > 90:
            head = head[:87].rstrip() + "…"
        qs.append(f"`{slug}`: does the source support — *{head}*?")
    joined = "<br>".join(qs)
    if len(joined) > limit * 2:  # generous cap; questions are the point.
        joined = joined[: limit * 2 - 1].rstrip() + "…"
    return joined


def render_verdict(verdict_row: dict[str, str] | None) -> str:
    """Final-column rendering for a single source's verdict."""
    if not verdict_row:
        return "*(pending)*"
    v = verdict_row.get("verdict", "pending")
    note = verdict_row.get("note", "").strip()
    if v == "advance":
        body = "**advance** ✓"
    elif v == "hold":
        body = "hold"
    elif v == "retire":
        body = "retire"
    else:
        body = "*(pending)*"
    if note:
        body = f"{body} — {md_escape_cell(note)}"
    return body


VERDICTS_PREAMBLE = """# Reading-queue verdicts

Human-edited companion to [`reading-queue.md`](reading-queue.md).
Each line records the author's verdict on whether a source can advance from
`ai-confirmed` (or `lit-retrieved`) to `lit-read`.

## Format

```
bibkey: <advance|hold|retire|pending> — optional free-text note
```

- `advance` — the source supports every dependent claim as stated; once
  set, also update the rung in `doc/provenance.ttl` to `verif:lit-read`
  and drop the `\\todo[inline]{verify}` marker in the manuscript.
- `hold` — the source has been examined but the verdict is not yet
  clear; the note explains what is outstanding.
- `retire` — the source does not support the claims it is attached to;
  remove the `prov:wasDerivedFrom` edges in `doc/provenance.ttl` (the
  bib entry may stay for historical accuracy).
- `pending` — no verdict yet (the default for newly-added sources).

New sources receive a `pending` line automatically on the next build of
`scripts/build_reading_queue.py`; pre-existing lines are preserved.

## Verdicts (one per source, sorted alphabetically)

"""


def regenerate_verdicts_file(path: Path, bibkeys: list[str]) -> dict[str, dict[str, str]]:
    """Ensure every source in the queue has a verdict line.

    Reads the existing file (if any), preserves manual edits, and appends
    a ``pending`` line for any newly-introduced source. Returns the merged
    dictionary.
    """
    existing = parse_verdicts(path)
    merged = {k: existing.get(k, {"verdict": "pending", "note": ""}) for k in bibkeys}
    lines: list[str] = [VERDICTS_PREAMBLE.rstrip("\n"), ""]
    for k in sorted(merged):
        row = merged[k]
        v = row.get("verdict", "pending")
        note = row.get("note", "").strip()
        if note:
            lines.append(f"{k}: {v} — {note}")
        else:
            lines.append(f"{k}: {v}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return merged


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

    # Counters reused across both files.
    n_lit_retrieved = sum(1 for _, _, r, _ in queue if r == "lit-retrieved")
    n_ai_confirmed = sum(1 for _, _, r, _ in queue if r == "ai-confirmed")
    n_no_rung = sum(1 for _, _, r, _ in queue if r == "no-rung")

    # Human verdicts: read the editable companion file, append `pending`
    # lines for any newly-introduced source, write the merged file back.
    verdicts = regenerate_verdicts_file(VERDICTS, [k for k, _, _, _ in queue])
    n_advance = sum(1 for v in verdicts.values() if v.get("verdict") == "advance")
    n_hold = sum(1 for v in verdicts.values() if v.get("verdict") == "hold")
    n_retire = sum(1 for v in verdicts.values() if v.get("verdict") == "retire")
    n_pending = sum(1 for v in verdicts.values() if v.get("verdict") == "pending")

    # --- Compact table in reading-queue.md ---------------------------------
    table: list[str] = []
    table.append("# Reading queue")
    table.append("")
    table.append("Auto-generated from `doc/provenance.ttl` and "
                 "`paper/references.bib`. Regenerated on every build; do "
                 "not edit by hand.")
    table.append("")
    table.append("Compact one-row-per-source table for verification triage. "
                 "Per-source narrative blocks (bib note, full citation, "
                 "claim labels) live in "
                 "[`reading-queue-details.md`](reading-queue-details.md).")
    table.append("")
    table.append("## State at the time of this build")
    table.append("")
    table.append(f"- Sources in queue: **{len(queue)}**")
    table.append(f"- `lit-retrieved` (full text not yet fetched): {n_lit_retrieved}")
    table.append(f"- `ai-confirmed` (abstract / agent-confirmed only): {n_ai_confirmed}")
    table.append(f"- `no-rung` (graph-cleanliness defect): {n_no_rung}")
    table.append("")
    table.append(f"**Verdict roll-up** (from "
                 f"[`reading-queue-verdicts.md`](reading-queue-verdicts.md)): "
                 f"**{n_advance}** advance, **{n_hold}** hold, "
                 f"**{n_retire}** retire, **{n_pending}** pending.")
    table.append("")
    table.append("**How to read the table.** Sources are ranked by the "
                 "number of dependent `fair2r:Claim` entries that cite "
                 "them. *Open* gives a one-click link (DOI, arXiv, or "
                 "publisher URL). *Rung* is the verification state in "
                 "`doc/provenance.ttl`. *Questions to verify* lists, one "
                 "per dependent claim, the question the author must "
                 "answer on full reading. *Verdict* is read from "
                 "[`reading-queue-verdicts.md`](reading-queue-verdicts.md) "
                 "— edit that file (one line per source: "
                 "`bibkey: <advance|hold|retire|pending> — note`) to "
                 "record the answer; the table regenerates on the next "
                 "build of `scripts/build_reading_queue.py`. A source "
                 "with a verdict of *advance* is cleared to move to "
                 "`verif:lit-read` in `doc/provenance.ttl`.")
    table.append("")
    table.append("| # | Source | Year | Open | Rung | Claims | Questions to verify | Verdict |")
    table.append("|---|--------|------|------|------|--------|--------------------|---------|")

    for idx, (bibkey, _src_iri, rung, _title) in enumerate(queue, 1):
        b = bib.get(bibkey, {})
        claim_list = deps.get(bibkey, [])
        n = len(claim_list)
        author = md_escape_cell(short_author(b)) if b else f"`{bibkey}`"
        year = md_escape_cell(b.get("year", "—"))
        url = open_url(b) if b else None
        open_cell = f"[link]({url})" if url else "—"
        rung_cell = f"`{rung}`"
        questions_cell = md_escape_cell(render_questions(claim_list))
        verdict_cell = md_escape_cell(render_verdict(verdicts.get(bibkey)))
        table.append(
            f"| {idx} | {author} `{bibkey}` | {year} | {open_cell} | "
            f"{rung_cell} | **{n}** | {questions_cell} | {verdict_cell} |"
        )

    table.append("")
    table.append("## Reading the rung column")
    table.append("")
    table.append("- `lit-retrieved` — full text fetched, not yet read in full.")
    table.append("- `ai-confirmed` — an AI agent has confirmed the source "
                 "supports the claim from its abstract or front matter; the "
                 "human author has not yet read the full text. This is a "
                 "*provisional* state and does not satisfy the methodology "
                 "before submission.")
    table.append("- `no-rung` — graph-cleanliness defect; the source entity "
                 "has no `fair2r:verificationState`. Fix by adding one in "
                 "`doc/provenance.ttl`.")
    table.append("")
    table.append("## What \"reading\" means here")
    table.append("")
    table.append("Per the verification ladder, advancing from "
                 "`lit-retrieved` or `ai-confirmed` to `lit-read` requires "
                 "that **the human author has read the source itself, not "
                 "just the abstract**, and has confirmed both that it "
                 "supports the claim and that the inference from source to "
                 "claim is sound.")
    table.append("")
    table.append("If a source is paywalled and institutional access is "
                 "required, see "
                 "[`doc/sources-needing-institutional-access.md`](sources-needing-institutional-access.md) "
                 "(create if necessary) per `agents/source-analyzer.md`.")
    table.append("")
    table.append("If a source turns out to be unsupportive on full reading, "
                 "the verification rung does not advance --- instead, the "
                 "source is removed from `prov:wasDerivedFrom` and "
                 "replaced; the bib entry stays for historical accuracy.")

    OUT.write_text("\n".join(table), encoding="utf-8")

    # --- Verbose detail in reading-queue-details.md ------------------------
    details: list[str] = []
    details.append("# Reading queue — per-source detail")
    details.append("")
    details.append("Auto-generated companion to "
                   "[`reading-queue.md`](reading-queue.md). One narrative "
                   "block per source: full citation, dependent-claim "
                   "labels, bib note. The compact table in "
                   "`reading-queue.md` is the triage view; this file is "
                   "the verification reference.")
    details.append("")
    details.append("Order matches the compact table (highest-leverage "
                   "first).")
    details.append("")

    for idx, (bibkey, _src_iri, rung, _title) in enumerate(queue, 1):
        b = bib.get(bibkey, {})
        cite_str = cite(bibkey, b) if b else f"*(no bib entry for `{bibkey}`)*"
        n = len(deps.get(bibkey, []))
        details.append(f"### {idx}. `{bibkey}` --- rung: `{rung}`, "
                       f"dependent claims: **{n}**")
        details.append("")
        details.append(f"**Citation.** {cite_str}")
        details.append("")
        if n:
            details.append("**Dependent claims** (advancing this source to "
                           "`lit-read` would unblock):")
            details.append("")
            for c_short, c_lbl in deps[bibkey]:
                details.append(f"- `{c_short}` --- {c_lbl}")
            details.append("")
        else:
            details.append("*(No `fair2r:Claim` currently lists this "
                           "source as `prov:wasDerivedFrom`. Consider "
                           "whether the source is still needed; if it "
                           "is, add the missing edge in "
                           "`doc/provenance.ttl`. If it is not, retire "
                           "the bib entry.)*")
            details.append("")
        if "doi" in b:
            details.append(f"**Open via DOI:** "
                           f"<https://doi.org/{b['doi']}>")
        elif "eprint" in b:
            details.append(f"**Open via arXiv:** "
                           f"<https://arxiv.org/abs/{b['eprint']}>")
        elif "url" in b:
            details.append(f"**Open via URL:** <{b['url']}>")
        details.append("")
        if "note" in b:
            details.append(f"**Note from the bib.** {b['note']}")
            details.append("")
        details.append("---")
        details.append("")

    OUT_DETAILS.write_text("\n".join(details), encoding="utf-8")

    print(f"Wrote {OUT.relative_to(ROOT)} and "
          f"{OUT_DETAILS.relative_to(ROOT)} ({len(queue)} entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
