# Submission plan

A living checklist of where this paper might land.

## Candidate venues

F(AI)²R is published as a single short-form manuscript: ~10 pages of
body, plus references and appendices.

Ranking below is by `(acceptance_chance × impact)` with `fit` as the
tie-break, last refreshed 2026-05-13.

| # | Venue | Type | Format | Fit | Acc | Imp | Deadline | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | [arXiv (cs.DL primary, cs.AI cross-list)](https://arxiv.org/) | preprint | PDF, no length cap | 5 | 5 | 2 | rolling | planned (gated on `paper/publication-consent.md`) |
| 2 | [RIO Journal (Research Ideas and Outcomes)](https://riojournal.com/) | journal (open peer review) | Methods paper or Research Idea | 5 | 5 | 3 | rolling | shortlist (no novelty gate; embeds artefacts) |
| 3 | [RDA P27 Plenary](https://www.rd-alliance.org/plenaries/p27/) (London, 6–8 Oct 2026) | plenary / WG / BoF | BoF session (90 min) + poster | 5 | 5 | 4 | sessions CfP closed 21 Nov 2025; late-breaking poster ~Jul 2026 | shortlist (BoF + WG-affiliated slot route; see notes below) |
| 4 | [Data Science Journal (CODATA)](https://datascience.codata.org/) | journal | research / position, 6–12 pp | 5 | 4 | 4 | rolling | shortlist |
| 5 | [iPRES 2026](https://ipres2026.dk/) (Copenhagen, 21–25 Sep 2026) | conference | Lightning Talk + BoF call open ~May 2026 | 4 | 4 | 4 | peer-reviewed track closed 16 Mar 2026; LT/BoF open now | shortlist |
| 6 | [F1000Research](https://f1000research.com) / [Open Research Europe](https://open-research-europe.ec.europa.eu/) | open post-publication journals | Opinion / Method article | 4 | 5 | 3 | rolling | candidate |
| 7 | [HMC Conference 2026](https://events.geomar.de/event/884/) (Helmholtz Metadata Collaboration) | conference | abstract + talk / poster | 5 | 5 | 2 | HMC 2026 has passed; aim for HMC 2027 + interim workshops | shortlist (Helmholtz-internal) |
| 8 | [JCDL 2026](https://2026.jcdl.org/) (Dallas, 13–16 Oct 2026) | conference | short / full paper, workshops | 4 | 3 | 4 | papers 30 Jun 2026; workshops 31 May 2026 | candidate |
| 9 | [TPDL 2026](https://tpdl2026.ualg.pt/) (Faro, 21–25 Sep 2026) | conference | full / short paper | 4 | 3 | 3 | papers 3 May 2026 — missed; watch poster / workshop track | watchlist |
| 10 | [Patterns (Cell Press)](https://www.cell.com/patterns/) | journal | Perspective (2,000–4,000 words, 2–5 figures) | 3 | 2 | 5 | rolling | stretch |
| 11 | [Dagstuhl Perspectives Workshop](https://www.dagstuhl.de/en/seminars/dagstuhl-perspectives) | invitation workshop | 5-day workshop proposal | 5 | 2 | 5 | 15 Apr 2026 — missed; next ~Apr 2027 | longer-arc bet |
| 12 | [Nature Machine Intelligence](https://www.nature.com/natmachintell/) — Comment / Perspective | journal | editor-gated short opinion | 3 | 1 | 5 | rolling (pre-submission inquiry essential) | stretch |
| -- | Zenodo deposit (Helmholtz / NFDI4Ing / HMC tagged) | archive | DOI mint | 5 | 5 | 2 | rolling | planned (`.zenodo.json` ready; gated on consent) |

### RDA P27 plenary — recommended format

RDA plenaries have **no proceedings**. The formats that exist are:
(i) **Birds-of-a-Feather session** (90 min, proposed in advance);
(ii) **Working-group / Interest-group affiliated session** (slot
inside an existing WG meeting); (iii) **poster** (late-breaking
track). The CfP for sessions closed 21 Nov 2025, so the realistic
2026 path is:

1. **Email the chairs** of the *FAIR for ML/AI WG* and the
   *Provenance Patterns IG* this week proposing a 20-minute slot
   inside their P27 meeting on F(AI)²R's eight integrated practices
   and the PROV-O graph that ships with the manuscript.
2. **Submit a poster** to the late-breaking track when it opens
   (typically ~3 months before the plenary, so July 2026 for the
   October 2026 event in London).
3. **Bring a one-page handout** summarising the 8 practices, the
   10-stage pipeline, and a small PROV-O snippet. The handout is
   the leave-behind that survives the plenary.
4. **Run a BoF on-the-fly** if the WG slot does not land; BoF
   topics can be self-organised on-site.

For the format the user should write: a **~500-word abstract**
(BoF / WG framing) + **A4 one-page handout** (visual: hero figure +
8-practice table + 10-stage pipeline). Both derive directly from
the manuscript and the conference poster; no new prose required.

### Preprint policy

arXiv goes out as soon as `paper/publication-consent.md` is
flipped (see *§ Publication consent*). The preprint is the
canonical citable anchor for every other venue above: each
submission, in cover letter, points at the arXiv ID + the GitHub
commit + the Zenodo DOI.

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
