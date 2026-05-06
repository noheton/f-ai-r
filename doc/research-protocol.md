# Research protocol

Owned by `agents/research-protocol.md`. Documents how literature is searched
and screened for this paper.

## Search rounds

### Round 1 — TBD

- **Date:** YYYY-MM-DD
- **Databases:** Google Scholar, Semantic Scholar, arXiv (cs.DL, cs.DB),
  ACM Digital Library.
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
