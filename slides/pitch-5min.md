---
marp: true
theme: dlr
paginate: true
math: true
title: F(AI)²R — 5-minute pitch
author: Florian Krebs
footer: Florian Krebs · DLR ZLP, Augsburg · Helmholtz · NFDI4Ing · HMC
---

<!-- _class: title -->
<!-- _paginate: skip -->

# F(AI)²R

## FAIR research with AI in the loop, twice

Florian Krebs · ORCID 0000-0001-6033-801X
DLR Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg
Helmholtz · NFDI4Ing · HMC — *DRAFT — not yet peer-reviewed*

---

# The problem

- FAIR was drafted for **data**; FAIR4RS for **software**; FAIR4ML for **models**.
- LLM-assisted scholarly writing produces **new artefact classes**:
  transcripts, prompts, version manifests, verification ladders,
  redaction policies, **per-claim provenance maps**.
- None covered by existing FAIR re-readings.
- Volume problem on top: detection-only is an arms-race the reviewer side does not win.
- **Reported fabrication base rates: 18–55 % (Walters & Wilder), 17–34 % (Magesh et al.)**

---

<!-- _class: section-divider -->

# Position

The canonical FAIR axes with an *(AI)* factor multiplied through them, **squared**

— each axis demands two passes: an authoring pass and an audit pass.

---

# Eight integrated practices

| # | Practice                              | Failure mode addressed |
|---|---------------------------------------|--------|
| 1 | Transcript preservation               | session loss |
| 2 | Verification-status labelling (FSM)   | claim–evidence drift |
| 3 | Per-claim provenance maps             | fabricated citations |
| 4 | Mirror discipline                     | placeholder dishonesty |
| 5 | Recursive meta-process documentation  | methodological-tract failure |
| 6 | Base-rate-anchored AI disclosure      | perfunctory disclosure |
| 7 | Legal honesty about authorship        | inflated co-author claims |
| 8 | FAIR alignment as **precondition**    | retrofit cost |

**The integration is the contribution.** None of the eight is novel on its own.

---

# Worked example: this paper

- The pipeline is the team; the team is the methodology.
- Ten-stage agent pipeline (orchestrator, writer, source-analyzer, scrutinizers, curator, site agent) with **handback discipline**.
- Verification ladder as a **finite-state machine**.
- Repository ships: prompts, build CI, PROV-O graph, public site, draft PDF.
- **`https://github.com/noheton/f-ai-r`** · **`https://noheton.github.io/f-ai-r/`**

---

<!-- _class: thanks -->
<!-- _paginate: skip -->

# Try it

**Repository.** github.com/noheton/f-ai-r
**Site.** noheton.github.io/f-ai-r
**Draft PDF.** github.com/noheton/f-ai-r/releases

We invite a second case study — by a different author, on a different
paper, in a different domain — as the precondition for community-
recommendation submission.

*Naming what we are already doing is the first step toward surrendering
it to peer scrutiny.*
