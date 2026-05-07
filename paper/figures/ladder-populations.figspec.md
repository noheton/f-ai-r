# ladder-populations.figspec.md

## Slug
`ladder-populations`

## Source
- `paper/figures/src/ladder-populations.py` --- matplotlib script,
  the canonical artefact. Reproducible (no randomness; reads
  `doc/provenance.ttl` via rdflib and falls back to a pinned
  snapshot if rdflib or the graph is unavailable).
- `paper/figures/ladder-populations.pdf` --- rendered for the LaTeX
  build. Build: `python3 paper/figures/src/ladder-populations.py`.
- `paper/figures/ladder-populations.png` --- 300 dpi raster for the
  README and the Pages site, written by the same script.

## Caption (one sentence)
The verification ladder rendered as a left-to-right finite-state
machine where each rung's circle area is proportional to the count
of `fair2r:Claim` entities currently at that rung in
`doc/provenance.ttl`, with a dotted vertical rule marking the model
ceiling and a dotted yellow back-edge marking retraction as
`prov:Invalidation`.

## Why matplotlib (not pure TikZ or Mermaid)
The figure is data-bound: node sizes encode live counts from
`doc/provenance.ttl`. TikZ would require encoding counts by hand
(drift-prone) and Mermaid does not support proportional node sizes
without a layout engine plugin. matplotlib gives full control over
node radii, hatch fills, and the model-ceiling rule while keeping
the script reproducible and reading the live graph at render time.

## Data / relations the figure must show
- Seven rungs in left-to-right reading order: `unverified-external`,
  `needs-research`, `lit-retrieved`, `ai-confirmed`, `lit-read`,
  `human-confirmed`, `source-vendored`.
- Each rung as a circle whose area is proportional (sqrt-scaled to
  preserve visual area) to the count of `fair2r:Claim` entities at
  that rung. Empty rungs render a small marker so they remain
  visible.
- Numeric badge inside the circle (`n=<count>`) and the rung label
  below.
- Forward edges between consecutive rungs (solid hairline arrows).
- A dotted vertical rule between `ai-confirmed` and `lit-read`
  labelled "model ceiling".
- A dotted yellow back-edge from `source-vendored` to
  `needs-research` labelled
  "retraction (prov:Invalidation, never deletion)".
- A four-swatch legend pairing fill colour with hatch (the AI
  ceiling rung is the only hatched cell) so the figure is
  greyscale-legible.
- A footer line summarising the total claim count and the
  fraction sitting at or below the model ceiling.

## Style
DLR Corporate Design palette: `dlrBlau1` `#00658B`, `dlrBlau5`
`#D1E8FA`, `dlrGruen1` `#82A043`, `dlrGruen5` `#E6EAAF`,
`dlrGelb1` `#D2AE3D`, `dlrGelb5` `#FFF8BE`, `dlrGrau1` `#4D5258`,
`dlrGrau3` `#B1B1B1`, `dlrGrau5` `#EBEBEB`. Hairline 0.4--0.6 pt
strokes; square edges; sans-serif (Helvetica/Arial fallback DejaVu
Sans). The `ai-confirmed` rung carries a `//` hatch in addition to
the soft-blue fill so the AI-ceiling channel survives in
greyscale.

## Placement
- Loaded by `paper/sections/provenance-analysis.tex`, replacing the
  retired `figures/rung-distribution.pdf`, with a `figure` float
  and the cross-reference `Figure~\ref{fig:ladder-populations}`.
- The Pages topology view may pick up the PNG as a status-of-the-
  ladder widget alongside the existing topology preview.

## Supersedes
`paper/figures/rung-distribution.{pdf,png,figspec.md}` ---
horizontal stacked bar that lost the topology. Recorded as
`ent:figure-rung-distribution prov:wasInvalidatedBy
act:add-illustrations-pass-4` in `doc/provenance.ttl`.

## Provenance IRI
`ent:figure-ladder-populations` in `doc/provenance.ttl`. Generated
by `act:add-illustrations-pass-4`; informed by
`act:add-illustrations-pass-3`; derived from
`ent:figure-rung-distribution` and `ent:figure-ladder-fsm`;
attributed to `agent:illustration` and `agent:human-author`; uses
`ent:section-provenance-analysis`.
