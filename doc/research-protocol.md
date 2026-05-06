# Research protocol

Owned by `agents/research-protocol.md`. Documents how literature is searched
and screened for this paper.

## Search tools (binding)

Scientific sources are searched, in priority order. The full
catalogue is in `agents/source-analyzer.md`; the summary here is
the contract every agent invokes.

1. **Consensus / Scholar** (the harness's `mcp__…__search` tool) —
   over 200 M peer-reviewed papers across Semantic Scholar, PubMed,
   Scopus, and arXiv. **Default tool for peer-reviewed citations.**
2. **Direct scientific repositories** for first-party records:
   **arXiv**, **OpenAlex**, **Crossref**, **PubMed / EuropePMC**,
   **IEEE Xplore**, **Springer Link**, **ACM Digital Library**,
   **ScienceDirect / Elsevier**, plus the standards-track surfaces
   **W3C / RDA / NIST / ISO**. Use these to cross-check
   bibliographic records, retrieve abstracts, and confirm DOIs.
3. **Semantic Scholar / OpenAlex / arXiv direct** — fallbacks for
   fields under-covered by Consensus.
4. **Google Scholar** — for orientation and citation-graph traversal,
   not as the primary record (identifiers are not always stable).
5. **Web search** (`WebSearch`, `web_search_exa`) — for
   grey-literature sources (editorial statements, venue policies,
   institutional documents, legal sources such as USCO / UrhG, W3C /
   RDA recommendations).
6. **`WebFetch`** — only after a candidate URL has been identified.

A search result is not a citation until its identifier resolves and
its claim has been linked to a `fair2r:Claim` in
`doc/provenance.ttl` per the verification ladder. Promotion through
the rungs follows `agents/source-analyzer.md`.

## Paywall escalation

When a source is **necessary for a load-bearing claim** but the full
text is paywalled and the abstract is insufficient, the agent must
**not** silently downgrade the claim's rung or skip the source.
Instead, append a structured entry to
[`doc/sources-needing-institutional-access.md`](sources-needing-institutional-access.md).
The human author (Florian Krebs) has DLR institutional access via
TIB, ZB MED, Helmholtz e-journals, and direct publisher
subscriptions, and supplies the PDF; once supplied, the source moves
to `source-vendored` under `doc/sources/<bibkey>/`.

A `pending` request older than 30 days is surfaced as a soft `warn`
by the FAIR Aligner. A claim that has gone unverified for more than
90 days must be hedged in the prose or removed.

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
