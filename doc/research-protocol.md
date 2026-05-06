# Research protocol

Owned by `agents/research-protocol.md`. Documents how literature is searched
and screened for this paper.

## Search tools (binding)

Scientific sources are searched, in priority order:

1. **Consensus / Scholar** (the harness's
   `mcp__…__search` tool) — over 200 M peer-reviewed papers across
   Semantic Scholar, PubMed, Scopus, and arXiv. **Default tool for
   peer-reviewed citations.** Filters (`year_min`, `exclude_preprints`,
   `study_types`, `medical_mode`) are used only when the question
   requires them.
2. **Semantic Scholar / OpenAlex / arXiv direct** — fallbacks for
   bibliographic cross-checks and for fields under-covered by
   Consensus.
3. **Google Scholar** — for orientation and citation-graph traversal,
   not as the primary record (its identifiers are not always stable).
4. **Web search** (`WebSearch`, `web_search_exa`) — for
   grey-literature sources (editorial statements, venue policies,
   institutional documents, legal sources such as USCO / UrhG, W3C
   recommendations, RDA recommendations).
5. **`WebFetch`** — used after a candidate URL has been identified, to
   read the actual page and extract the snippet.

A search result is not a citation until its identifier resolves and
its claim has been linked to a `fair2r:Claim` in
`doc/provenance.ttl` per the verification ladder. Promotion through
the rungs follows `agents/source-analyzer.md`.

## Search rounds

### Round 1 — TBD

- **Date:** YYYY-MM-DD
- **Tools used:** Consensus / Scholar (default), plus any of the
  above as required.
- **Queries:**
  - `("FAIR principles" OR "FAIR data") AND ("large language model" OR LLM)`
  - `"PROV-O" AND ("scholarly" OR "manuscript" OR "paper writing")`
  - `"AI co-author" OR "AI-assisted writing" provenance`
- **Inclusion criteria:** peer-reviewed or arXiv preprint with ≥1 citation,
  English, 2016–present.
- **Exclusion criteria:** opinion pieces without empirical or design
  contribution; venue-specific tooling reports without methodology.

## Screening template

```
- bibkey: <slug>
  title: …
  decision: include | exclude | revisit
  reason: …
```

## Disagreement protocol

When two sources disagree on a fact relevant to the paper:

1. Record both, with quoted snippets, in `doc/sources.md`.
2. Add two `fair2r:Claim` IRIs in `provenance.ttl` linked by
   `fair2r:contradicts`.
3. In the manuscript, hedge: "X has been argued [a] and disputed [b]".
