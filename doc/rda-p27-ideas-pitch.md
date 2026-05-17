# RDA P27 — Ideas Pitch Session submission (draft)

Fill-in-ready draft for the
[RDA P27 Ideas Pitch Session Submission Form](https://www.rd-alliance.org/plenaries/p27/ideas-pitch-session-submission-form-p27/).
Field order and guidance text mirror the live form. The human author
copies each field across, adjusts to the platform's exact character
counters, ticks the acknowledgement, and submits. Nothing here fires
publication consent (`paper/publication-consent.md`); an Ideas Pitch
is a community-presentation submission, not a DOI-minting release.

---

## Applicant serving as a contact person

| Field | Value |
|---|---|
| Full Name | Florian Krebs |
| First Name | Florian |
| Last Name | Krebs |
| Affiliation | Deutsches Zentrum für Luft- und Raumfahrt (DLR), Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg — Helmholtz-Gemeinschaft; NFDI4Ing; HMC (Helmholtz Metadata Collaboration) |
| Email | florian.krebs@dlr.de |
| Country | Germany |

ORCID: [0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X)

---

## Tell us about your pitch idea

### Pitch Idea Title

*(Form guidance: keep the title brief — 10 words is optimal.)*

> **F(AI)²R: Provenance for AI-Assisted Scholarly Writing**

(7 words.)

### Idea Pitch Overview & Objectives

*(Form guidance: ~350-word summary, captivating, clearly explaining
the importance at a global level with specific reference to how it
supports global open research and open science. The text below is
~350 words — trim to the platform's exact counter if it differs.)*

> FAIR was written for data, then extended to research software
> (FAIR4RS) and to machine-learning models (FAIR4ML). None of these
> covers the artefacts that LLM-assisted scholarly *writing* now
> produces: conversation transcripts, versioned prompt files,
> model-and-tool manifests, verification-status ladders, and
> per-claim provenance maps. Every researcher who writes with an LLM
> in the room generates these artefacts; almost no one preserves
> them. When they vanish, the audit trail vanishes with them — a
> reader can no longer ask *who wrote this sentence, what evidence
> supports this claim, and how was it verified?* — at a moment when
> fabricated citations, claim–evidence drift, and reviewer-capacity
> exhaustion are already documented at scale.
>
> F(AI)²R ("FAIR with AI in the loop, twice") re-reads the FAIR
> principles for that situation. The (AI) factor is multiplied
> through every FAIR axis and *squared*, because each artefact is
> touched twice: an authoring pass in which LLM agents help draft
> under human direction, and an audit pass in which a machine-
> readable PROV-O graph records who did what, when, and from which
> sources, so that another human — or another AI — can later
> verify, replay, or contest each claim. The contribution is the
> integration of eight individually unoriginal practices into one
> discipline, enforced by an agent pipeline with strict separation
> between prose-owning and audit-owning roles.
>
> The pitch is fully reproducible: the paper, its companion
> technical report, the agent prompts, the provenance graph, the
> logbook, and the build pipeline are openly published under
> permissive licences, and the paper was produced by the pipeline
> it prescribes. This matters globally because the volume problem
> is global: the response to AI-scale scholarly output will look
> less like new detection tools and more like shared provenance
> schemas — the bioinformatics precedent under data-volume
> pressure. F(AI)²R is one concrete, adoptable offer toward an
> open-science norm that lets claims, sources, and authoring
> activities reference each other across institutional and national
> boundaries, on day one rather than as a forensic retrofit.

### Pitch Unique Selling Point (USP)

*(Form guidance: why this presentation should be selected, how it is
of value and interest to the global RDA community.)*

> Three things distinguish this pitch for an RDA audience. First, it
> is not a proposal that *will* be built — it already exists and is
> fully open: a working PROV-O graph (extended with project-local
> subclasses), agent prompts as versioned source, a public site, and
> a build pipeline, all under MIT / CC-BY-4.0. RDA members can clone
> it during the session. Second, it is recursive evidence: the
> manuscript was produced by the discipline it prescribes, so the
> provenance graph that travels with it is a worked example a
> working group could adopt or contest immediately rather than
> re-derive. Third, it sits squarely on RDA's own trajectory: it
> composes with FAIR4RS, FAIR4ML, and MLCommons Croissant rather than
> competing with them, and it extends the PROV-O / DCTERMS stack RDA
> communities already use. The pitch is deliberately framed as an
> *offer*, not a standard — the asset to the community is a concrete
> substrate to argue from.

### From Idea Pitch to RDA Group

*(Form guidance: how this idea could lead to the formation of an RDA
Working Group or Interest Group.)*

> The natural next step is an **Interest Group** on *Provenance for
> AI-Assisted Scholarly Authoring*, scoped to the artefact classes
> that current FAIR re-readings do not cover (transcripts, prompts,
> tool/model manifests, verification-status ladders, per-claim
> provenance). The IG would convene FAIR4RS and FAIR4ML
> participants, the PROV-O / metadata communities (HMC, NFDI), and
> publishers / preprint-server operators facing AI-scale submission
> volume. A focused **Working Group** could then deliver a minimal
> interoperable schema and a SHACL shape set for the audit pass,
> with this repository as a candidate reference implementation and
> conformance test-bed. The 18-month WG output would be a
> recommendation other RDA groups can cite by IRI — explicitly
> modelled on the FAIR4RS / FAIR4ML precedent of adding
> sub-principles for a new artefact class rather than absorbing it.

### Additional Links to Informative Material(s)

- Repository: <https://github.com/noheton/f-ai-r>
- Project site: <https://noheton.github.io/f-ai-r/>
- Latest draft PDF (DRAFT watermark):
  <https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf>
- Provenance graph (PROV-O over Turtle):
  <https://github.com/noheton/f-ai-r/blob/main/doc/provenance.ttl>
- Methodology / pipeline:
  <https://noheton.github.io/f-ai-r/methodology.html>

### Applicable Thematic Area

*(Single select. Author's choice: Engineering and technology — aligns
with the DLR / NFDI4Ing home community and the data-infrastructure /
tooling thrust.)*

> **Engineering and technology**

---

## Pitch Idea Presenter(s)

| Field | Value |
|---|---|
| Full Name(s) of Presenter(s) | Florian Krebs |
| Link(s) to Short Bio(s) | ORCID: <https://orcid.org/0000-0001-6033-801X> — *(add a one-paragraph DLR/ZLP bio page or institutional profile URL before submitting)* |

---

## Acknowledgements (tick on the live form)

- [ ] **Applicant Acknowledgment** — *If my application is
  successful, I understand that I must be present in person at the
  RDA 27th Plenary Meeting to deliver my pitch.* — to be confirmed
  by the human author (in-person attendance is a hard requirement).
- [ ] **Privacy Policy** — *Yes, I agree.*

---

## Notes for the human author before submitting

1. **Bio link.** The form asks for a short-bio link; supply a stable
   DLR/ZLP profile or an ORCID record with employment filled in.
2. **Word counter.** The overview is ~350 words by manual count; the
   platform's counter may differ by a few words — trim the closing
   sentence first if over.
3. **In-person requirement.** The acknowledgement is binding: only
   submit if attendance at P27 in person is realistic.
4. **Consent gate.** This submission presents the work to a
   community; it does not publish or mint an identifier, so
   `paper/publication-consent.md` does **not** need to flip. If P27
   later leads to a proceedings/DOI, that step is gated separately.
