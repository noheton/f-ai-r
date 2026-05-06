# Submission plan

A living checklist of where this paper might land.

## Candidate venues

F(AI)²R is published as a single short-form manuscript: ~10 pages of
body, plus references and appendices.

| Venue | Page limit | Fit | Status |
|---|---|---|---|
| arXiv (cs.DL)                                       | none | always | planned |
| Zenodo deposit (Helmholtz / NFDI4Ing / HMC tagged)  | none | always | planned |
| FORCE11 workshop / scholarly-communication track    | ~10  | high   | shortlist |
| RDA plenary working-group presentation              | ~10  | high   | shortlist |
| HMC FAIR-metadata symposium                         | ~10  | high   | shortlist |
| Helmholtz Open-Science publication channel          | ~12  | medium | shortlist |
| *Quantitative Science Studies* (MIT Press)          | full | medium | candidate |
| *Data Intelligence* (MIT Press)                     | full | medium | candidate |

## Pre-submission checklist

- [ ] Author block, affiliations, ORCIDs filled in.
- [ ] All `\todo` removed from `paper/main.tex`.
- [ ] FAIR audit report passes (`doc/fair-audit-*.md`).
- [ ] Provenance graph validates (`riot --validate`).
- [ ] Body within page budget (`make -C paper pages` ≤ `PAGE_BUDGET`,
      default 10) excluding references and appendices.
- [ ] Camera-ready figures vector or ≥300dpi raster.
- [ ] Bibliography reviewed for hallucinated entries.
- [ ] Acknowledgements include AI tooling per venue policy.
- [ ] Zenodo deposit drafted; DOI placeholder in CITATION.cff.

## Post-acceptance checklist

- [ ] Final version archived to Zenodo, DOI written into CITATION.cff.
- [ ] `git tag` the submitted commit.
- [ ] Logbook entry: "submitted to <venue> on <date>; commit <sha>".
- [ ] Provenance graph snapshot exported alongside the PDF.
