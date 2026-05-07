# failure-mode-coverage.figspec.md

## Slug
`failure-mode-coverage`

## Source
- `paper/figures/failure-mode-coverage.tex` — TikZ source loaded by
  `paper/sections/failure-modes.tex` via `\input`.

## Caption (one sentence)
A heat-strip companion to Table~\ref{tab:failure-modes}: each row is
a named failure mode, each column is one of the eight integrated
practices, and the cell colour encodes whether that practice bears
the primary load (solid blue), contributes (soft blue), mitigates
indirectly (yellow), or is out of scope (white) for that mode.

## Data / relations the figure must show
- 8 failure-mode rows (fabricated citations; claim-evidence drift;
  sloppification; model collapse; list-of-lists prose; hedging
  chains; placeholder dishonesty; dual use) plus one residual band
  (leakage, audience fatigue, adversarial review).
- 8 practice columns (transcripts; verification status; per-claim
  provenance; mirror discipline; recursive meta-process; base-rate
  disclosure; legal honesty; FAIR as precondition).
- Cell-level mapping derived from
  `paper/sections/failure-modes.tex` and
  `paper/sections/eight-practices.tex`. The current mapping is
  many-to-many in detail and one-to-one in load-bearing weight.
- Legend: primary load / secondary contribution / indirect or
  residual / out of scope.

## Medium
TikZ. Hairline rules. DLR palette only. Two channels of
information — colour AND cell shape via the legend — to satisfy the
illustration agent's accessibility rule.

## Placement
- `paper/sections/failure-modes.tex`, after Table~1.

## Provenance IRI
`ent:figure-failure-mode-coverage` in `doc/provenance.ttl`. Generated
by `act:add-illustrations-pass`; uses `ent:section-failure-modes`.
