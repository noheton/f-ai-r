# TODOs for publication

A flat, prioritised checklist. Move items to `doc/logbook.md` when done.

## P0 — blocks any submission

- [ ] Resolve placeholder author identity in `CITATION.cff`,
      `codemeta.json`, `.zenodo.json`, `paper/main.tex`.
- [ ] Draft Section 1 (Introduction).
- [ ] Draft Section 3 (The F(AI²)R Pattern) — this is the contribution.
- [ ] First pass of `doc/provenance.ttl` populated with at least the
      activities for the introduction and the pattern section.

## P1 — blocks the condensed version

- [ ] Section 4 (Implementation) drafted.
- [ ] Architecture / pipeline figure produced via `agents/illustration.md`.
- [ ] PROV-O graph rendered as a figure for the paper.

## P2 — blocks a clean review pass

- [ ] Related work survey done; hallucination check by `source-analyzer`.
- [ ] Discussion section names the failure modes (prompt drift,
      hallucinated citations, provenance theatre).
- [ ] Readability review reports ≥4/5 on motivation and novelty.

## P3 — nice-to-have before camera-ready

- [ ] CI to compile the PDF on push.
- [ ] CI to validate `provenance.ttl` on push.
- [ ] Browsable HTML rendering of the provenance graph under `doc/site/`.
