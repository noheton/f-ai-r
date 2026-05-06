# Human–AI collaboration process

A short, blunt description of who decides what.

## The human author decides
- Research question, scope, contributions claimed.
- Which sources are admissible and how disagreements between sources are
  resolved.
- Whether a claim has crossed from `ai-confirmed` to `human-confirmed`.
- When to publish, where to publish, and who gets author credit.
- Anything ethically loaded.

## The AI agents do
- Draft prose, propose figures, condense, audit.
- Maintain `doc/provenance.ttl` *under the curator agent's mediation*.
- Refuse to invent citations or paper over evidence gaps.

## Disagreements
If an agent and a human disagree on a factual matter:
1. The agent records its position with a quoted source.
2. The human records the counter-position with a quoted source.
3. Both go into the manuscript as a hedged sentence ("X has been argued
   [cite-A] and disputed [cite-B]") and into the graph as two
   `fair2r:Claim`s linked by `fair2r:contradicts`.

## Authorship credit
AI agents are not authors. The CITATION.cff lists human authors only.
Substantial AI contributions are acknowledged in the paper's
*Acknowledgements* and recorded in `doc/provenance.ttl` as
`prov:wasAttributedTo` an `fair2r:AIAgent` individual.

## Audit trail
Every working session ends with a logbook entry and (where claims changed)
new triples in `provenance.ttl`. No silent edits.
