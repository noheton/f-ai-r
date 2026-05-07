# ladder-fsm.figspec.md

## Slug
`ladder-fsm`

## Source
- `paper/figures/ladder-fsm.mmd` --- Mermaid `stateDiagram-v2` source,
  the canonical artefact.
- `paper/figures/ladder-fsm.pdf` --- rendered for the LaTeX build.
  Build: `mmdc -i paper/figures/ladder-fsm.mmd -o paper/figures/ladder-fsm.pdf`.
- `paper/figures/ladder-fsm.png` --- 1600px raster for the README and
  the Pages site. Build:
  `mmdc -i paper/figures/ladder-fsm.mmd -o paper/figures/ladder-fsm.png -w 1600 -b white`.
- `paper/figures/ladder-fsm.tex` --- thin LaTeX shim invoked by
  `\input{figures/ladder-fsm}` from `paper/sections/pattern.tex`;
  wraps the rendered PDF in a `figure` float with the caption.

## Caption (one sentence)
The verification ladder as a finite-state machine: claims progress
left-to-right (\textsc{unverified-external}\,$\to$\,\textsc{needs-research}\,$\to$\,\textsc{lit-retrieved}\,$\to$\,\textsc{ai-confirmed}\,$\to$\,\textsc{lit-read}),
with retraction as the only back-edge.

## Why Mermaid (not TikZ)
A finite-state machine is exactly what `stateDiagram-v2` was designed
for, and the Pages site already renders Mermaid client-side via
`mermaid.min.js` (see `scripts/build_provenance_site.py`). Using
Mermaid as the source of truth gives the paper and the site one
artefact rather than two; the rendered PDF is the LaTeX-side
projection.

## Data / relations the figure must show
- Five rung states with their canonical names.
- Four monotone forward transitions (recognise gap; DOI/URL
  resolves; AI fetch + quoted snippet; human reads).
- One retraction back-edge labelled \texttt{prov:Invalidation} from
  \textsc{lit-read} to \textsc{unverified-external}.
- Visual coding by rung family: external/pre-research (grey-5),
  identifier-resolves (white), AI-only ceiling (blue-5/blue-1),
  human-confirmed (green-5/green-1).

## Style
DLR Corporate Design palette only. Hairline strokes (0.5\,pt). No
rounded corners. Square-edge rectangles. No emoji.

## Placement
- Loaded by `paper/sections/pattern.tex` via
  `\input{figures/ladder-fsm}` --- the shim resolves to the figure
  float around `figures/ladder-fsm.pdf`.
- The Pages site renders `figures/ladder-fsm.mmd` client-side as a
  Mermaid block, with the figure caption mirrored from the manuscript.
- Slide deck: the textual rung-chain in
  `slides/conference-30min.tex` (frame "Verification ladder as a
  finite-state machine") stays as-is; the rendered PNG can be
  swapped in if the slide is rebuilt.

## Provenance IRI
`ent:figure-ladder-fsm` in `doc/provenance.ttl`. Replaces the prior
TikZ source (`prov:wasInvalidatedBy act:add-illustrations-pass-2`);
new derivation tracked under
`act:add-illustrations-pass-2` with
`prov:wasAttributedTo agent:illustration`.
