# Reading queue

Auto-generated from `doc/provenance.ttl` and `paper/references.bib`. Regenerated on every build; do not edit by hand.

Compact one-row-per-source table for verification triage. Per-source narrative blocks (bib note, full citation, claim labels) live in [`reading-queue-details.md`](reading-queue-details.md).

## State at the time of this build

- Sources in queue: **54**
- `lit-retrieved` (full text not yet fetched): 3
- `ai-confirmed` (abstract / agent-confirmed only): 50
- `no-rung` (graph-cleanliness defect): 1

**Verdict roll-up** (from [`reading-queue-verdicts.md`](reading-queue-verdicts.md)): **0** advance, **0** hold, **0** retire, **54** pending.

**How to read the table.** Sources are ranked by the number of dependent `fair2r:Claim` entries that cite them. *Open* gives a one-click link (DOI, arXiv, or publisher URL). *Rung* is the verification state in `doc/provenance.ttl`. *Questions to verify* lists, one per dependent claim, the question the author must answer on full reading. *Verdict* is read from [`reading-queue-verdicts.md`](reading-queue-verdicts.md) — edit that file (one line per source: `bibkey: <advance|hold|retire|pending> — note`) to record the answer; the table regenerates on the next build of `scripts/build_reading_queue.py`. A source with a verdict of *advance* is cleared to move to `verif:lit-read` in `doc/provenance.ttl`.

| # | Source | Year | Open | Rung | Claims | Questions to verify | Verdict |
|---|--------|------|------|------|--------|--------------------|---------|
| 1 | Ashburner et al. `ashburner2000go` | 2000 | [link](https://doi.org/10.1038/75556) | `ai-confirmed` | **2** | `bioinformatics-precedent`: does the source support — *Bioinformatics standardised semantic tagging (Gene Ontology and successors) under data-…*?<br>`future-research-infrastructure`: does the source support — *Future re… | *(pending)* |
| 2 | Magesh et al. `magesh2024legal` | 2024 | — | `ai-confirmed` | **2** | `practice-disclosure`: does the source support — *Base-rate-anchored AI disclosure: disclosure is anchored to numeric base rates for the…*?<br>`base-rates-distinct`: does the source support — *Walters & Wilder report 55… | *(pending)* |
| 3 | Walters et al. `walters2023fabrication` | 2023 | [link](https://doi.org/10.1038/s41598-023-41032-5) | `ai-confirmed` | **2** | `practice-disclosure`: does the source support — *Base-rate-anchored AI disclosure: disclosure is anchored to numeric base rates for the…*?<br>`base-rates-distinct`: does the source support — *Walters & Wilder report 55… | *(pending)* |
| 4 | ACL Rolling Review `aclrr_llm_policy` | 2024 | [link](https://aclrollingreview.org/cfp) | `ai-confirmed` | **1** | `reviewer-side-ai-policies`: does the source support — *Major ML venues (NeurIPS, ICLR, ACL Rolling Review) have published explicit author-and-…*? | *(pending)* |
| 5 | Benjelloun et al. `benjelloun2024croissant` | 2024 | [link](https://docs.mlcommons.org/croissant/docs/croissant-spec.html) | `ai-confirmed` | **1** | `croissant-not-overlap`: does the source support — *Croissant occupies the dataset-metadata slot*? | *(pending)* |
| 6 | Clarke et al. `clarke2009modelchecking` | 2009 | [link](https://doi.org/10.1145/1592761.1592781) | `ai-confirmed` | **1** | `formal-methods-cousin`: does the source support — *F(AI)^2R is structurally a cousin of model checking and theorem proving: each fair2r:Cl…*? | *(pending)* |
| 7 | Conroy `conroy2023sleuths` | 2023 | [link](https://doi.org/10.1038/d41586-023-02477-w) | `ai-confirmed` | **1** | `journal-as-distribution-in-decline`: does the source support — *Traditional publishing is under stress*? | *(pending)* |
| 8 | Curdt et al. `curdt2025hmc` | 2025 | [link](https://doi.org/10.5281/zenodo.15113717) | `ai-confirmed` | **1** | `future-research-infrastructure`: does the source support — *Future research success may depend less on the solitary craft of a single manuscript an…*? | *(pending)* |
| 9 | Eisen et al. `eisen2018preprints` | 2020 | [link](https://doi.org/10.7554/eLife.64910) | `ai-confirmed` | **1** | `journal-as-distribution-in-decline`: does the source support — *Traditional publishing is under stress*? | *(pending)* |
| 10 | Else `else2023chatgpt` | 2023 | [link](https://doi.org/10.1038/d41586-023-00191-1) | `ai-confirmed` | **1** | `ai-rise-motivation`: does the source support — *The rising fraction of LLM-modified prose in scholarly venues makes a discipline of aut…*? | *(pending)* |
| 11 | ICLR `iclr_llm_policy` | 2024 | [link](https://iclr.cc/) | `lit-retrieved` | **1** | `reviewer-side-ai-policies`: does the source support — *Major ML venues (NeurIPS, ICLR, ACL Rolling Review) have published explicit author-and-…*? | *(pending)* |
| 12 | International Committee of Medical Journal Editors `icmje2023` | 2023 | [link](https://www.icmje.org/recommendations/) | `ai-confirmed` | **1** | `practice-legal`: does the source support — *Legal honesty about authorship: AI is acknowledged but not an author*? | *(pending)* |
| 13 | Ioannidis `ioannidis2005` | 2005 | [link](https://doi.org/10.1371/journal.pmed.0020124) | `ai-confirmed` | **1** | `reproducibility-baseline-poor`: does the source support — *The LLM-assisted writing failure modes sit on top of a reproducibility baseline that is…*? | *(pending)* |
| 14 | Janowicz et al. `janowicz2019sosa` | 2019 | [link](https://doi.org/10.1016/j.websem.2018.06.003) | `ai-confirmed` | **1** | `domain-ontologies-extension`: does the source support — *Domain ontologies (SOSA / SSN for sensor data, OM-2 / QUDT for units of measure) plug i…*? | *(pending)* |
| 15 | Klein et al. `klein2009sel4` | 2009 | [link](https://doi.org/10.1145/1629575.1629596) | `ai-confirmed` | **1** | `formal-methods-cousin`: does the source support — *F(AI)^2R is structurally a cousin of model checking and theorem proving: each fair2r:Cl…*? | *(pending)* |
| 16 | Kobak et al. `kobak2024delving` | 2024 | [link](https://arxiv.org/abs/2406.07016) | `ai-confirmed` | **1** | `ai-rise-motivation`: does the source support — *The rising fraction of LLM-modified prose in scholarly venues makes a discipline of aut…*? | *(pending)* |
| 17 | Liang et al. `liang2024mapping` | 2024 | [link](https://arxiv.org/abs/2404.01268) | `ai-confirmed` | **1** | `ai-rise-motivation`: does the source support — *The rising fraction of LLM-modified prose in scholarly venues makes a discipline of aut…*? | *(pending)* |
| 18 | Liu et al. `liu2026ara` | 2026 | [link](https://arxiv.org/abs/2604.24658) | `ai-confirmed` | **1** | `ara-maximalist-alternative`: does the source support — *F(AI)²R declines Ara's bargain: narrative manuscript stays primary*? | *(pending)* |
| 19 | NeurIPS `neurips_llm_policy` | 2024 | [link](https://neurips.cc/) | `lit-retrieved` | **1** | `reviewer-side-ai-policies`: does the source support — *Major ML venues (NeurIPS, ICLR, ACL Rolling Review) have published explicit author-and-…*? | *(pending)* |
| 20 | Pineau et al. `pineau2021reproducibility` | 2021 | [link](https://jmlr.org/papers/v22/20-303.html) | `ai-confirmed` | **1** | `reproducibility-baseline-poor`: does the source support — *The LLM-assisted writing failure modes sit on top of a reproducibility baseline that is…*? | *(pending)* |
| 21 | QUDT.org `qudt` | 2024 | [link](https://www.qudt.org/) | `ai-confirmed` | **1** | `domain-ontologies-extension`: does the source support — *Domain ontologies (SOSA / SSN for sensor data, OM-2 / QUDT for units of measure) plug i…*? | *(pending)* |
| 22 | Rijgersberg et al. `rijgersberg2013om` | 2013 | [link](https://doi.org/10.3233/SW-2012-0069) | `ai-confirmed` | **1** | `domain-ontologies-extension`: does the source support — *Domain ontologies (SOSA / SSN for sensor data, OM-2 / QUDT for units of measure) plug i…*? | *(pending)* |
| 23 | Stankorb et al. `shafer2014xennials` | 2014 | [link](https://www.good.is/articles/generation-xennial) | `ai-confirmed` | **1** | `senior-researcher-bridge`: does the source support — *Senior researchers --- analogous to the Xennial bridge generation --- carry a responsib…*? | *(pending)* |
| 24 | Tennant et al. `tennant2016open` | 2016 | [link](https://doi.org/10.12688/f1000research.8460.3) | `ai-confirmed` | **1** | `journal-as-distribution-in-decline`: does the source support — *Traditional publishing is under stress*? | *(pending)* |
| 25 | Van Noorden et al. `vannoorden2023chatgpt` | 2023 | [link](https://doi.org/10.1038/d41586-023-03930-6) | `lit-retrieved` | **1** | `ai-rise-motivation`: does the source support — *The rising fraction of LLM-modified prose in scholarly venues makes a discipline of aut…*? | *(pending)* |
| 26 | Wilkinson et al. `wilkinson2016fair` | 2016 | [link](https://doi.org/10.1038/sdata.2016.18) | `ai-confirmed` | **1** | `practice-fair-precondition`: does the source support — *FAIR alignment as precondition: do not retrofit FAIR*? | *(pending)* |
| 27 | Alemohammad et al. `alemohammad2023mad` | 2023 | [link](https://arxiv.org/abs/2307.01850) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 28 | Anderson et al. `anderson2024homogenization` | 2024 | [link](https://doi.org/10.1145/3635636.3656204) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 29 | Bender et al. `bender2021stochastic` | 2021 | [link](https://doi.org/10.1145/3442188.3445922) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 30 | Birhane et al. `birhane2022values` | 2022 | [link](https://doi.org/10.1145/3531146.3533083) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 31 | Chen et al. `chen2023drift` | 2023 | [link](https://arxiv.org/abs/2307.09009) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 32 | Chue Hong et al. `chuehong2022fair4rs` | 2022 | [link](https://doi.org/10.15497/RDA00068) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 33 | Clark et al. `clark1998extended` | 1998 | [link](https://doi.org/10.1093/analys/58.1.7) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 34 | Clark `clark2025extending` | 2025 | [link](https://doi.org/10.1038/s41467-025-59906-9) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 35 | Gebru et al. `gebru2021datasheets` | 2021 | [link](https://doi.org/10.1145/3458723) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 36 | Guyatt et al. `guyatt2008grade` | 2008 | [link](https://doi.org/10.1136/bmj.39489.470347.AD) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 37 | Hutchins `hutchins1995cognition` | 1995 | — | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 38 | Kuteeva et al. `kuteeva2024diversity` | 2024 | [link](https://doi.org/10.1093/applin/amae025) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 39 | Li et al. `li2023thirsty` | 2023 | [link](https://doi.org/10.1145/3724499) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 40 | Liu et al. `liu2023prompt` | 2023 | [link](https://doi.org/10.1145/3560815) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 41 | Luccioni et al. `luccioni2024power` | 2024 | [link](https://doi.org/10.1145/3630106.3658542) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 42 | Mitchell et al. `mitchell2019modelcards` | 2019 | [link](https://doi.org/10.1145/3287560.3287596) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 43 | Page et al. `page2021prisma` | 2021 | [link](https://doi.org/10.1136/bmj.n71) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 44 | Patterson et al. `patterson2021carbon` | 2021 | [link](https://arxiv.org/abs/2104.10350) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 45 | Castro et al. `ravi2024fair4ml` | 2024 | [link](https://doi.org/10.5281/zenodo.14002310) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 46 | Reynolds et al. `reynolds2021prompt` | 2021 | [link](https://doi.org/10.1145/3411763.3451760) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 47 | Sadasivan et al. `sadasivan2023reliably` | 2023 | [link](https://arxiv.org/abs/2303.11156) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 48 | Schmitt et al. `schmitt2020nfdi4ing` | 2020 | [link](https://doi.org/10.5281/zenodo.4015201) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 49 | Shumailov et al. `shumailov2024collapse` | 2024 | [link](https://doi.org/10.1038/s41586-024-07566-y) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 50 | Strubell et al. `strubell2019energy` | 2019 | [link](https://doi.org/10.18653/v1/P19-1355) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 51 | Thorp `thorp2023chatgpt` | 2023 | [link](https://doi.org/10.1126/science.adg7879) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 52 | Bundesministerium der Justiz `urhg2` | 1965 | [link](https://www.gesetze-im-internet.de/urhg/__2.html) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 53 | U.S. Copyright Office `usco2023ai` | 2023 | [link](https://www.federalregister.gov/documents/2023/03/16/2023-05321/copyright-registration-guidance-works-containing-material-generated-by-artificial-intelligence) | `ai-confirmed` | **0** | *(retire / wire-up question)* | *(pending)* |
| 54 | W3C `w3c2013provo` | 2013 | [link](https://www.w3.org/TR/prov-o/) | `no-rung` | **0** | *(retire / wire-up question)* | *(pending)* |

## Reading the rung column

- `lit-retrieved` — full text fetched, not yet read in full.
- `ai-confirmed` — an AI agent has confirmed the source supports the claim from its abstract or front matter; the human author has not yet read the full text. This is a *provisional* state and does not satisfy the methodology before submission.
- `no-rung` — graph-cleanliness defect; the source entity has no `fair2r:verificationState`. Fix by adding one in `doc/provenance.ttl`.

## What "reading" means here

Per the verification ladder, advancing from `lit-retrieved` or `ai-confirmed` to `lit-read` requires that **the human author has read the source itself, not just the abstract**, and has confirmed both that it supports the claim and that the inference from source to claim is sound.

If a source is paywalled and institutional access is required, see [`doc/sources-needing-institutional-access.md`](sources-needing-institutional-access.md) (create if necessary) per `agents/source-analyzer.md`.

If a source turns out to be unsupportive on full reading, the verification rung does not advance --- instead, the source is removed from `prov:wasDerivedFrom` and replaced; the bib entry stays for historical accuracy.