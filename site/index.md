# F(AI)²R

<p class="lede">FAIR research, with AI in the loop — twice. A short-form
working paper and a reproducible writing pipeline, versioned together
and built under the DLR Corporate Design.</p>

![Hero figure: the F(AI)²R writing pipeline. A manuscript bundle (claims, sources, prompts, transcripts, provenance graph) is the shared substrate between an authoring pass that writes into it from above and an audit pass that reads it back from below. Squared notation: every artefact is touched twice, never in the same role and never in the same commit.](static/figures/hero.png)

<div class="cta-row">
  <a class="cta primary" href="https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf">Read the latest draft (PDF)</a>
  <a class="cta secondary" href="https://github.com/noheton/f-ai-r">View the repository</a>
  <a class="cta tertiary" href="provenance-explorer.html">Open the provenance explorer</a>
</div>

<div class="callout">
The PDF is auto-built on every push to <code>main</code>. It carries a
<strong>DRAFT — not yet peer-reviewed</strong> watermark until a
published version is explicitly authorised. Replay it locally with
<code>make -C paper pdf</code> and compare; any difference is a defect.
</div>

## Slide decks

Two Beamer-rendered slide decks ship as primary artefacts alongside
the manuscript, on the **DLR Corporate Design** Beamer style
(`slides/style/fair2r-beamer.sty`, mirroring the paper's
`paper/style/fair2r.sty`). Same toolchain as the paper PDF
(latexmk + xu-cheng/latex-action); no Marp / Chromium / Node. Both
auto-build on every push to <code>main</code> and live on the
<code>latest-draft-slides</code> release.

<div class="cta-row">
  <a class="cta secondary" href="https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/pitch-5min.pdf">Pitch deck — 5 min (PDF)</a>
  <a class="cta secondary" href="https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/conference-30min.pdf">Conference deck — 25 + 5 min (PDF)</a>
</div>

## What is F(AI)²R?

`F(AI)²R` re-reads the FAIR principles for an era in which Large
Language Models participate in scholarly production. The **(AI)**
factor is multiplied through every FAIR axis, **squared** because each
axis demands two passes over every artefact — an **authoring** pass
(LLM agents help draft) and an **audit** pass (a PROV-O graph records
*who* did *what*, *when*, from *which sources*). Both passes ship
with the manuscript.

The contribution is not the name. It is the **integration of eight
individually unoriginal practices** into a single discipline,
enforced by a ten-stage agent pipeline whose prose-owning and
audit-owning roles are strictly separated through a handback
discipline.

## Three things to read first

<div class="card-grid">
  <div class="dlr-card">
    <div class="body">
      <span class="eyebrow">The pattern</span>
      <h3>Methodology</h3>
      <p>How the paper is actually built: the ten-stage pipeline,
         the verification ladder as a finite-state machine, the
         handback discipline.</p>
      <a class="more" href="methodology.html">Read &rarr;</a>
    </div>
  </div>
  <div class="dlr-card">
    <div class="body">
      <span class="eyebrow">The receipts</span>
      <h3>Provenance graph</h3>
      <p>The PROV-O graph that travels with the manuscript, rendered
         as grouped tables and as an interactive node-link diagram.</p>
      <a class="more" href="provenance.html">Browse &rarr;</a>
    </div>
  </div>
  <div class="dlr-card">
    <div class="body">
      <span class="eyebrow">The rules</span>
      <h3>Agents</h3>
      <p>Ten role-specific prompts. Treat them as source code:
         versioned, diffed, reviewed.</p>
      <a class="more" href="agents.html">Inspect &rarr;</a>
    </div>
  </div>
</div>

## All sections

- [Methodology](methodology.html) — how the paper is actually built.
- [FAIR notes](fair.html) — what we add to FAIR, principle by principle.
- [Human–AI collaboration](collab.html) — who decides what.
- [Agents](agents.html) — the LLM workforce, one prompt per role.
- [Logbook](logbook.html) — append-only, dated, human-readable.
- [Provenance](provenance.html) — the PROV-O graph as grouped tables.
- [Provenance explorer](provenance-explorer.html) — the same graph as a
  click-to-inspect node-link diagram.
- [Topology](provenance-graph.html) — the same graph as a Mermaid
  diagram.
- [Submission plan](submission.html) — venues and pre-flight checklists.

## Imprint

Florian Krebs &middot; ORCID
[0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X) &middot;
[florian.krebs@dlr.de](mailto:florian.krebs@dlr.de)

DLR Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg

Helmholtz-Gemeinschaft &middot;
[NFDI4Ing](https://nfdi4ing.de/) &middot;
[HMC — Helmholtz Metadata Collaboration](https://helmholtz-metadaten.de/)

Code: MIT. Prose: CC-BY-4.0.
