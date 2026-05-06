# Submission plan

A living checklist of where this paper might land.

## Candidate venues

| Venue | Form | Page limit | Fit | Status |
|---|---|---|---|---|
| TBD workshop on AI & scholarly communication | short | 4 | high | shortlist |
| TBD journal on research data management       | full  | 12-20 | high | shortlist |
| arXiv (cs.DL)                                  | preprint | none | always | planned |
| Zenodo deposit                                 | archival | none | always | planned |

## Pre-submission checklist

- [ ] Author block, affiliations, ORCIDs filled in.
- [ ] All `\todo` removed from `paper/main.tex`.
- [ ] FAIR audit report passes (`doc/fair-audit-*.md`).
- [ ] Provenance graph validates (`riot --validate`).
- [ ] Condensed version compiles within page limit.
- [ ] Camera-ready figures vector or ≥300dpi raster.
- [ ] Bibliography reviewed for hallucinated entries.
- [ ] Acknowledgements include AI tooling per venue policy.
- [ ] Zenodo deposit drafted; DOI placeholder in CITATION.cff.

## Post-acceptance checklist

- [ ] Final version archived to Zenodo, DOI written into CITATION.cff.
- [ ] `git tag` the submitted commit.
- [ ] Logbook entry: "submitted to <venue> on <date>; commit <sha>".
- [ ] Provenance graph snapshot exported alongside the PDF.
