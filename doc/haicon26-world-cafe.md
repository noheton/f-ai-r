# HAICON26 — AI World Café topic proposal (draft)

Fill-in-ready draft for the
[HAICON26 AI World Café topic submission](https://haicon.cc/contributions/).
Field order mirrors the live form. The human author copies each field
across, adjusts to the platform's exact form-field expectations, and
submits. Submission window: **2 February – 2 June 2026**; the
conference is **8–11 June 2026, Munich, in-person only**.

Proposing a World Café table (interactive discussion format, small
rotating groups) rather than the closed scientific-abstract or
workshops tracks. The table format suits F(AI)²R better than a
one-way oral slot: F(AI)²R is a position paper that explicitly
invites contestation (eight integrated practices, recursive case
study, Author's Note novelty conviction). A discussion is the form
in which it can be argued with.

This file does **not** flip `paper/publication-consent.md`. A World
Café topic proposal is a community-discussion submission, not a DOI-
minting release.

---

## Title

*(Form guidance: short, catchy, informative; often a question.)*

> **The human–AI partition in scholarly writing: accelerator or cultural blender?**

(11 words, embeds the diagnostic and the two alternatives.)

## Description

*(Form guidance: describe the topic; may include links to supporting
material.)*

> Almost every paper you read this year had an LLM in the room. The
> question is no longer whether the cooperation happened — it's where
> the partition between human and model actually sits, and whether
> the partition is the same in your discipline as in mine.
>
> F(AI)²R (FAIR research with AI in the loop, twice) names a
> *coupling rule* drawn from a year of cooperative writing under the
> DLR Corporate Design: the cooperation works as an **accelerator**
> when the model stays on the prose-craft side of the partition —
> drafting, cross-referencing, structuring — and collapses toward a
> **cultural blender** when the model is allowed across into the
> abstracting layer, where its failure mode is to smooth the
> unfamiliar into the nearest familiar shape. The diagnostic that
> tells you which side the model just stood on is one question:
> *would the abstraction have been thinkable without the model?*
>
> This table opens that question to the room. **Where does the
> partition sit in your discipline?** Foundation-model researchers,
> physics-informed ML practitioners, medical-imaging groups, the
> ethics-and-sustainability track — each will draw the line in a
> different place, and the differences are interesting. We will
> compare diagnostics, surface failure modes participants have
> actually seen, and ask what the *receipts* of an LLM-assisted
> paper should look like: the eight integrated practices F(AI)²R
> proposes (transcript preservation, verification-status labelling,
> per-claim provenance maps, mirror discipline, recursive
> meta-process, base-rate-anchored disclosure, legal honesty about
> authorship, FAIR alignment as precondition) are one offer to argue
> against, not a standard to ratify.
>
> A short visual primer (the coupling-rule figure from the paper)
> introduces the partition; the rest of the table is yours.
>
> **Material supporting the discussion:**
>
> - Project site: <https://noheton.github.io/f-ai-r/>
> - Repository (paper + companion technical report + agent prompts +
>   PROV-O graph + logbook): <https://github.com/noheton/f-ai-r>
> - Latest draft PDF (DRAFT watermark): <https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf>
> - Methodology page: <https://noheton.github.io/f-ai-r/methodology.html>
> - Author's Note (the partition + coupling rule are stated there):
>   <https://noheton.github.io/f-ai-r/methodology.html#authors-note>

## Poster (optional)

*(Form guidance: not a classical scientific poster, but a visual
that highlights the guiding question and key starting points for
discussion.)*

> Bring a **single-figure board** built from `paper/figures/coupling-rule.tex`
> (the partition diagram already in the manuscript) at A1 or smaller.
> The figure literally shows the two regimes — accelerator versus
> cultural blender — with the diagnostic question as the caption.
> Three discussion-starter questions around the figure:
>
> 1. *Where does the partition sit in your discipline today?*
> 2. *Which failure modes have you actually seen — and on which side
>    of the partition?*
> 3. *What receipts would you ask a colleague's paper to ship?*
>
> No new scientific data; the visual is shaped for conversation, not
> for one-way reading. DLR Corporate Design (consistent with the
> conference deck and the A0 conference poster already in the
> repository).

## Host(s)

*(Form guidance: names and e-mail addresses of all people involved.
At least one; more welcome.)*

| Name | E-mail | Role |
|---|---|---|
| Florian Krebs | florian.krebs@dlr.de | Primary host (DLR ZLP, Augsburg; Helmholtz · NFDI4Ing · HMC) |

> Open slot for a co-host with a complementary disciplinary angle
> (suggested: someone from medical imaging or physics-informed ML to
> draw out where the partition sits outside engineering / scholarly-
> communication research). Add a co-host before submitting if one is
> available; the platform allows multiple hosts and the table is
> stronger with two voices from different communities.

---

## Notes for the human author before submitting

1. **Deadline.** Submissions accepted **2 February – 2 June 2026**.
   Today's date and the submission window leave a short runway;
   submit at least a few days before the cut-off in case the platform
   needs corrections.
2. **In-person attendance is binding** (8–11 June 2026, Munich) —
   only submit if attendance is realistic.
3. **Co-host.** Strongly recommended to add one; reach out to a
   non-DLR Helmholtz colleague this week.
4. **Visual.** If you decide to bring a discussion-starter board,
   render `paper/figures/coupling-rule.tex` at A1 or smaller via
   `latexmk` on the standalone scaffold (the conference A0 poster is
   too dense for World Café — that one is for the science-track
   poster session, not for a discussion table).
5. **Consent gate.** This submission is a community-discussion
   proposal; it does **not** trigger
   `paper/publication-consent.md`. The draft PDF link you supply
   carries the existing DRAFT watermark, which is consistent with
   the consent state.
6. **Fit with the existing P27 draft.** The RDA P27 Ideas Pitch
   draft (`doc/rda-p27-ideas-pitch.md`) is a different format
   (90-minute or formal pitch) and a different community (RDA, the
   data alliance). Both can coexist — HAICON is the home community,
   P27 is the cross-community venue.
