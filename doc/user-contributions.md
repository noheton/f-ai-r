# User contributions

Append-only log of contributions by the human author (Florian Krebs) to
F(AI)\textsuperscript{2}R. Each entry is mirrored in
[`doc/provenance.ttl`](provenance.ttl) as a
\texttt{fair2r:HumanContribution} entity per the `Contribution`
extension to the schema; this file is the human-readable shadow.

## Why this file exists

The verification ladder grades \emph{claims}; the logbook records
\emph{sessions}; the provenance graph records \emph{activities}. None
of those, on its own, makes the human author's contribution legible at
inspection time. Reviewers, panel discussants, and (especially)
funding bodies asking "what did the human actually do here?" deserve
an answer that is structured and self-updating rather than a heroic
narrative.

This log answers that question with a typed contribution per
intervention. The AI's contributions are mirrored at
[`doc/ai-contributions.md`](ai-contributions.md) (forthcoming) so
that the partition the Author's Note describes
(`paper/sections/authors-note.tex`, *What surprised me about the
cooperation*) is empirically auditable rather than asserted.

## Distribution by type

![Histogram of human-author contributions to the manuscript by type, read from this file at render time and grouped by family (structural / directive / corrective / meta / uptake).](static/figures/contribution-histogram.png)

## Contribution types

Each entry carries one of:

| type | meaning |
|---|---|
| `structural-decision`   | A choice that fixed the shape of the manuscript or the scaffolding for many subsequent sessions (e.g. position-paper reframing, chapter-per-file rule). |
| `corrective-intervention` | A targeted correction of AI drift (e.g. wrong DOI, conflated figures, stale-cache observation). |
| `content-prompt`        | A request for a new section, paragraph, or figure. |
| `rule-shape`            | A binding rule added to the agent prompts or the methodology (e.g. consistency invariant, page budget, Consensus mandate). |
| `observation`           | A meta-observation about the cooperation that may or may not graduate to paper content. Tracked in `user-observations-log.md`; the entry here is the breadcrumb. |
| `responsibility-uptake` | Putting one's name to a published artefact and committing to defend it in interpersonal venues (panels, conferences). The leg of the contribution that the AI cannot share. |
| `experience-meta`       | Use of prior cooperation experience (here: from `noheton/Obscurity-Is-Dead`) to shorten the current session's learning curve. |

## Schema

```
## YYYY-MM-DD --- short title
*Type:* <one of the above>
*Leverage:* high | medium | low
*Triggered:* <description of subsequent work, ideally with file paths>
*Artefacts touched:* <list>
*Provenance IRI:* fair2r:hc-<slug>
```

The `Provenance IRI` matches the corresponding
`fair2r:HumanContribution` entity in `doc/provenance.ttl`.

---

## Back-fill (reconstructed from git log, the conversation transcript, and `doc/logbook.md`)

The entries below were reconstructed in one batch on 2026-05-06 from
the available evidence. Future sessions append in real time.


### 2026-05-07 --- Rule shape: transcript preservation (first time honoured)
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* User asked: *"can you keep a full transcript of our
chat in a separate document?"*. Closes a long-standing gap
between practice 1 of the eight integrated practices (transcript
preservation, prescribed since the bootstrap) and the actual
state of the repository (`doc/transcripts/` did not exist; the
evolution chronology calls this *"Pipeline as target, not yet as
practice."*). Created `doc/transcripts/` plus a README and a
session file `2026-05-07-session.md`. Schema growth: added
`fair2r:Transcript` class to `doc/provenance.ttl` so transcripts
bind as typed entities. The discipline is now active for
subsequent sessions; an active session without a transcript file
is a defect the FAIR aligner can check for.
*Artefacts touched:* `doc/transcripts/README.md` (new),
`doc/transcripts/2026-05-07-session.md` (new),
`doc/provenance.ttl` (schema + new entities),
`doc/logbook.md`, `doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-transcript-preservation`

### 2026-05-07 --- Corrective: poster CI compile fix + README consistency pass
*Type:* `corrective-intervention`
*Leverage:* medium
*Triggered:* User flagged *"poster link not working"* and
*"update readme as well and keep consistent"*. (1) Poster CI:
`slides/poster-A0.tex` `\includegraphics` calls switched to
plain filenames + `\graphicspath` fallback chain;
`.github/workflows/build-slides.yml` gains a *Stage figures
for the poster* step that copies the three needed PNGs into
`slides/` before latex-action runs; `.gitignore` extended for
the staged copies. (2) README updated to mention the poster
as the fifth primary artefact, the mobile-friendly site, the
Get-started page, the transcripts directory, the schema-growth
class list, and the no-parentless-claim invariant; layout tree
brought forward.
*Artefacts touched:* `README.md`, `.gitignore`,
`slides/poster-A0.tex`,
`.github/workflows/build-slides.yml`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-readme-consistency-pass`

### 2026-05-07 --- Corrective: mobile-friendly Pages site
*Type:* `corrective-intervention`
*Leverage:* medium
*Triggered:* User direction *"make the pages mobile friendly"*.
CSS-only fix in `site/static/style.css`: responsive defaults
(`img`, `video`, `iframe` `max-width: 100%`; `pre`
`overflow-x: auto`); phone breakpoint at 720 px (tighter
padding, header stacks, nav wraps, hero H1 26 px, body
headings stepped down, CTAs stack full-width, tables become
horizontally scrollable); narrow-phone breakpoint at 380 px.
Existing 900 px and 720 px breakpoints preserved. No template
change, no JS.
*Artefacts touched:* `site/static/style.css`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-make-pages-mobile-friendly`

### 2026-05-07 --- Structural: conference poster as fifth primary artefact
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* User direction *"add another artifact to the build
chain a conference poster/Infographic. consider distilling the
process to its essentials. how would that change page count for
paper"*, followed by *"go"* against a two-step plan. Step (a)
landed: poster scaffolded (`slides/poster-A0.tex`, tikzposter
A0 landscape, DLR-CD overrides on the `Simple` theme); Makefile
`poster` target; CI workflow extended; rolling release publishes
`poster-A0.pdf` alongside the decks; schema growth
(`fair2r:Poster` class); `CLAUDE.md` primary-artefact list 4 →
5; site CTA link added. The discipline of writing the poster is
the page-count forcing function for step (b).
*Artefacts touched:* `slides/poster-A0.tex` (new),
`slides/Makefile`, `slides/poster-A0.png` (render),
`site/static/figures/poster-A0.png`, `site/index.md`,
`.github/workflows/build-slides.yml`, `CLAUDE.md`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-scaffold-conference-poster`

### 2026-05-07 --- Corrective: hero PNG embedded on Pages Home
*Type:* `corrective-intervention`
*Leverage:* low
*Triggered:* User question *"do we have an eyecatcher graphic
is it also in the pages?"*. PDF carried hero on front matter;
Pages site did not. Rendered `paper/figures/hero.tex` via the
existing standalone wrapper to a 200 dpi PNG (after adding
`\usepackage{amsmath}` to the wrapper); copied to
`site/static/figures/hero.png`; embedded near the top of
`site/index.md` between the lede and the CTA row.
*Artefacts touched:* `paper/figures/hero.standalone.tex`,
`paper/figures/hero.png`, `site/static/figures/hero.png`,
`site/index.md`, `doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-eyecatcher-on-pages`

### 2026-05-07 --- Corrective: scrutinizer-pass fix-up (post PR #43)
*Type:* `corrective-intervention`
*Leverage:* medium
*Triggered:* User direction `"run a scrutinizer pass"`. Three
audit subagents (layout-scrutinizer, readability-reviewer,
fair-aligner) returned punch lists against the focused-narrative
trim state. Small / safe items applied here: 8 newly orphaned bib
entries re-cited in prose (PRISMA / GRADE in pattern.tex
Crosswalk; PROV-O in pattern.tex axes; Datasheets + Model Cards
in eight-practices item 3; ACL ARR + ICLR + NeurIPS LLM policies
in intro.tex venue-policy churn). Three orphan figure labels
cross-referenced from prose. Conclusion forward-ref to
sec:research-infrastructure repaired to point at appendix-g.
Xennial paragraph split. Redundant "None of the eight is novel"
in conclusion + closing roadmap in Author's Note removed.
Trim-artefact paragraph in pattern.tex folded into "Extensions
and cousins". Long-term archivability paragraph in
limits-and-objections.tex dropped (re-trod earlier paragraph).
`paper/sections/self-reference.tex` and
`paper/figures/eight-practices.tex` deleted (orphan files
retired in earlier passes). Bib `Missing $` warning + slug-match
heuristic in `scripts/provenance_analysis.py` deferred.
*Artefacts touched:* `paper/sections/conclusion.tex`,
`paper/sections/authors-note.tex`, `paper/sections/intro.tex`,
`paper/sections/pattern.tex`,
`paper/sections/eight-practices.tex`,
`paper/sections/limits-and-objections.tex`,
`paper/sections/self-reference.tex` (deleted),
`paper/figures/eight-practices.tex` (deleted),
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-scrutinizer-pass-fix-up`

### 2026-05-07 --- Structural: focused-narrative trim pass + update pass
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* Researcher direction `"generate the focused version.
afterwards complete update pass."` against the seven-item triage
filtered by narrative load. Five-beat spine (gap → position →
eight integrated practices + pipeline → recursive case study +
honest-about-limits → why now) was the filter. Cuts:
`background.tex` and `related.tex` removed entirely (substrate
already inline-cited; *Cousins.* paragraph folded into
`pattern.tex`); `sustainability.tex` + `objections.tex` merged
into `limits-and-objections.tex` (~683 w from a combined
~1170 w); `pattern.tex` §domain-ontologies +
§research-infrastructure moved to
`appendix-g-pattern-extensions.tex`; `authors-note.tex` rewritten
~1010 → 561 w; `evolution.tex` three insight paragraphs collapsed
into one; `provenance-analysis.tex` trimmed 436 → 276 w. Net
body 10466 → 6496 words (~38%); PDF 38 → 33 pages.
*Artefacts touched:* `paper/main.tex`,
`paper/sections/authors-note.tex` (rewritten),
`paper/sections/intro.tex` (roadmap),
`paper/sections/position.tex` (cross-refs),
`paper/sections/pattern.tex`,
`paper/sections/eight-practices.tex`,
`paper/sections/provenance-analysis.tex`,
`paper/sections/evolution.tex`,
`paper/sections/limits-and-objections.tex` (new),
`paper/sections/appendix-g-pattern-extensions.tex` (new),
`paper/sections/{background,related,sustainability,objections}.tex`
(removed), `doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-trim-pass-focused-narrative`

### 2026-05-07 --- Structural: trim pass 2 — A–D from further-candidates list
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* Researcher direction `"do a to d"` against the
further-candidates list. (A) `provenance-analysis.tex` mechanics
→ new `appendix-e-provenance-analysis.tex` (body keeps the two
figures + a summary paragraph + the "what the analysis is and is
not" framing). (B) `implementation.tex` →
`appendix-f-implementation.tex` (label retitled
`sec:appendix-implementation`; cross-refs in `intro.tex` and
`position.tex` updated). (C) `statement-of-authorship.tex`
converted to `\section*` with `\addcontentsline` (back-matter).
(D) `self-reference.tex` cut from body `\input` (preserved on
disk; load-bearing claim survives in Author's Note + practice
5). Net body reclaim ~2.0 pp. Two `prov:Invalidation` records;
two new appendix sections.
*Artefacts touched:* `paper/sections/provenance-analysis.tex`,
`paper/sections/appendix-e-provenance-analysis.tex` (new),
`paper/sections/appendix-f-implementation.tex` (renamed from
`implementation.tex`),
`paper/sections/statement-of-authorship.tex`,
`paper/sections/eight-practices.tex`,
`paper/sections/evolution.tex`,
`paper/sections/appendix-d-evolution-chronology.tex`,
`paper/sections/intro.tex`, `paper/sections/position.tex`,
`paper/main.tex`, `doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-trim-pass-2-appendix-routing`

### 2026-05-07 --- Structural: trim pass — evolution chronology -> appendix; pattern §handback de-duplicated
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* User picked items 1 and 2 from the seven-item
complete-loop trim list (`"2 should be an appendix, fix 1"`):
(1) `pattern.tex` §handback trimmed from a three-paragraph
mirror-discipline restatement to a one-paragraph handback
statement plus a forward reference to practice 4 of
`\S\ref{sec:eight}`; (2) `evolution.tex`'s 14 `\paragraph`
chronology blocks moved to a new
`paper/sections/appendix-d-evolution-chronology.tex`. Body
keeps the digest table plus three load-bearing summary
paragraphs (Researcher-as-corrector, Pipeline as target not
yet as practice, Logbook as conscience). Net body reclaim
~1.6 pp toward the 10-pp budget.
*Artefacts touched:* `paper/sections/evolution.tex`,
`paper/sections/appendix-d-evolution-chronology.tex` (new),
`paper/sections/pattern.tex`, `paper/main.tex`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-trim-evolution-and-pattern`

### 2026-05-07 --- Content prompt: getting-started guide + auto-sync from CLAUDE.md
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* User asked: *"to make process usable to other
users can you write a getting started guide (especially for
the page)? basically I want ppl to run a specific
initialization prompt to set the process up. (keep this
instructions always synced to process)"*. New page
`site/getting-started.md` hands an adopter a single
initialization prompt that points the LLM at this repository
as the canonical reference; the *Ground rules* block on the
page is auto-synced from `CLAUDE.md` by
`scripts/sync_getting_started.py`, which the site builder
invokes on every build. Wired into `PAGES` + `NAV`. Site
now publishes 27 pages.
*Artefacts touched:* `site/getting-started.md` (new),
`scripts/sync_getting_started.py` (new),
`scripts/build_provenance_site.py`, `doc/provenance.ttl`,
`doc/logbook.md`, `doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-getting-started-page-and-sync`

### 2026-05-07 --- Observation: associative thinking as the cooperation multiplier
*Type:* `observation`
*Leverage:* high
*Triggered:* End-of-session prompt from the researcher: *"how
far does associative thinking capability help in leveraging llm
cooperation benefits. I mean in the convo you often provide
suggestions which lead me to other angles or ideas"*. Logged at
`hypothesis` stage in `doc/user-observations-log.md`; not
graduated to paper text yet. Reframes the model's value as
*producing near-miss candidates the researcher converts to
usable angles* rather than *being right*. Schema-growth hint
flagged for the next case study (`fair2r:cooperativeOriginType`).
*Artefacts touched:* `doc/user-observations-log.md`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-obs-associative-thinking-as-multiplier`

### 2026-05-07 --- Corrective: complete-loop fix pass (cross-refs, voice, missing graph entity, palette, slides)
*Type:* `corrective-intervention`
*Leverage:* medium
*Triggered:* The complete-loop audit ensemble (five subagents)
returned a punch list; this entry captures the small, safe fixes
applied directly from the findings. Three broken cross-references
repaired (`sec:discussion`, `sec:fm-residual`,
`sec:practice-disclosure`). One voice-drift instance corrected
(`source-analyser` → `Source Analyzer`). Missing
`src:ravi2024fair4ml` graph entity added (FAIR4ML cited five
times in prose but had no `fair2r:Source` triple). Palette
comment in `paper/figures/src/provenance-topology.py:27`
realigned with `paper/style/fair2r.sty` (authoritative source).
AI² grid finally wired into both slide decks (PR #33's claim
that it "lands on the position frame" was unmet; now true).
Page-budget cuts and Xennial-paragraph split deferred — those
are taste calls.
*Artefacts touched:* `paper/sections/intro.tex`,
`paper/sections/objections.tex`,
`paper/sections/appendix-a-ladder.tex`,
`paper/sections/failure-modes.tex`,
`paper/figures/src/provenance-topology.py`,
`slides/pitch-5min.tex`, `slides/conference-30min.tex`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-complete-loop-fix-pass`

### 2026-05-07 --- Content prompt: summary table of process evolutions
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* User asked for "a summary maybe a table what evolutions
(rules, agents, ...) during the process of writing the paper
occurred". Graduated to paper text as a 20-row `longtable` at the
top of `paper/sections/evolution.tex` (Table~1) and mirrored as a
Markdown table on `doc/methodology.md` (and therefore on the
Pages site). Five evolution classes documented: rule, agent,
schema, pipeline, manuscript. `tabularx` + `longtable` added to
`paper/style/fair2r.sty`. New `claim:evolution-summary-table`
born with parent activity per the no-parentless-claim rule.
*Artefacts touched:* `paper/sections/evolution.tex`,
`paper/style/fair2r.sty`, `doc/methodology.md`,
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-evolution-summary-table`

### 2026-05-07 --- New claim: senior-researcher Xennial-like bridging responsibility
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* User proposed: "we as senior researchers who know the
way how things were done and why they were done that have a
responsibility to help build bridges to the unthinkable of the
past (a similar situation as xennials)". Graduated to a new
paragraph *The bridge to what is now unthinkable.* in the
Conclusion (between *The longer arc.* and the closing emphasis
line). New bib entry `shafer2014xennials` (lit-retrieved). New
`claim:senior-researcher-bridge` born with an explicit parent
activity per the no-parentless-claim rule from the 2026-05-07
curator pass.
*Artefacts touched:* `paper/sections/conclusion.tex`,
`paper/references.bib`, `doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-senior-researcher-bridge-claim`

### 2026-05-07 --- Rule shape: expand illustration toolset; pin DLR-CD constraint
*Type:* `rule-shape`
*Leverage:* medium
*Triggered:* User flagged that "Mermaid, matplotlib, and other
publication-ready tools can also be used by the illustrator. if
unsure ask" and, on a follow-up, "but keep dlr design system in
mind". `agents/illustration.md` updated: the "TikZ-only" implicit
rule is retired; the prompt now records the full toolset
(matplotlib, seaborn, plotly, scienceplots, cmocean, colorcet,
proplot, TikZ, PGFPlots, svgwrite, drawsvg, schemdraw,
matplotlib-scalebar, diagrams, graphviz, networkx, mermaid-py,
gridspec, plotnine, patchworklib, bokeh, ipywidgets, plus
molecular / image-processing libraries for sub-domain
instantiations). The DLR Corporate Design (Arial / Helvetica
fallback, `dlrBlau1 #00658B` accent, mid-grey neutrals, square
corners only, hairline rules at 0.4pt, no shadows / glows /
gradients / 3D, no emoji, no clip-art) is now a binding section
above the toolset list and explicitly applies to every tool —
default tool theming counts as an unfinished figure.
*Artefacts touched:* `agents/illustration.md`, `doc/logbook.md`,
`doc/user-contributions.md`, `doc/provenance.ttl`.
*Provenance IRI:* `fair2r:hc-illustration-toolset-and-dlr-cd`

### 2026-05-07 --- Verification pass: 16 sources advanced + 3 bib corrections applied
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* User requested "verification pass". A source-analyzer
subagent walked the reading queue, advancing 16 fair2r:Source
entities from `lit-retrieved` to `ai-confirmed` with verbatim
quoted snippets in `doc/sources.md`. Three paywalled-but-load-
bearing sources (`vannoorden2023chatgpt`, `neurips_llm_policy`,
`iclr_llm_policy`) were escalated into the new
`doc/sources-needing-institutional-access.md` for the human author
to retrieve via DLR institutional access. Four bib corrections
flagged; three applied in this commit (eisen year 2018→2020 and
"Peer Review:" title prefix; kobak title revision; curdt full
author list); the fourth (vannoorden DOI) was already fixed in
PR #11.
*Artefacts touched:* `doc/sources.md`, `doc/provenance.ttl`,
`doc/sources-needing-institutional-access.md` (new),
`paper/references.bib`, `doc/user-contributions.md`,
`doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-verification-pass-and-bib-corrections`

### 2026-05-06 --- Bootstrap request: initialise repo for F(AI)²R
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* Initial 37-file commit; the entire scaffolding (`paper/`,
`doc/`, `agents/`, root metadata).
*Artefacts touched:* whole tree.
*Provenance IRI:* `fair2r:hc-bootstrap`

### 2026-05-06 --- Primary-artefact consistency invariant
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* `Primary-artefact consistency (binding)` block added to
every prompt under `agents/`; orchestrator named ultimate custodian;
provenance-curator named keystone; FAIR aligner surfaces desync as
audit `fail`.
*Artefacts touched:* `CLAUDE.md`, `doc/methodology.md`, `agents/*.md`,
`doc/provenance.ttl`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-consistency-invariant`

### 2026-05-06 --- Site + paper-build CI
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* `scripts/build_provenance_site.py`,
`.github/workflows/pages.yml`, `.github/workflows/build-paper.yml`.
*Artefacts touched:* `scripts/`, `.github/workflows/`, `site/`.
*Provenance IRI:* `fair2r:hc-ci-site`

### 2026-05-06 --- Chapter-per-file rule for `.tex`
*Type:* `rule-shape`
*Leverage:* medium
*Triggered:* `File granularity (binding)` block in
`agents/scientific-writer.md`; `paper/main.tex` refactored as a thin
assembler; one `\section{}` per file under `paper/sections/`.
*Artefacts touched:* `agents/scientific-writer.md`, `paper/main.tex`,
`paper/sections/`.
*Provenance IRI:* `fair2r:hc-chapter-rule`

### 2026-05-06 --- "This paper, generated by this process" section
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* `paper/sections/self-reference.tex`.
*Artefacts touched:* `paper/sections/self-reference.tex`,
`paper/main.tex`.
*Provenance IRI:* `fair2r:hc-self-reference-section`

### 2026-05-06 --- "Process evolution during cooperative writing"
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* `paper/sections/evolution.tex` (the recursive case study
of the cooperation that produced the paper).
*Artefacts touched:* `paper/sections/evolution.tex`.
*Provenance IRI:* `fair2r:hc-evolution-section`

### 2026-05-06 --- Short-form pivot (~10 pages of body)
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* `paper/main-condensed.tex` retired; every section file
compactly rewritten; `agents/condenser.md` repurposed as page-budget
enforcer; `paper/Makefile` gains `pages` target with `PAGE_BUDGET=10`.
*Artefacts touched:* `paper/`, `agents/condenser.md`,
`agents/scientific-writer.md`.
*Provenance IRI:* `fair2r:hc-short-form-pivot`

### 2026-05-06 --- DLR Corporate Design integration
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* `site/static/dlr/` (vendored tokens, fonts, logos);
`paper/style/fair2r.sty`; site CSS rewritten on the DLR token palette;
imprint added to every metadata surface.
*Artefacts touched:* `site/static/dlr/`, `paper/style/fair2r.sty`,
`site/static/style.css`, `CITATION.cff`, `codemeta.json`,
`.zenodo.json`, `README.md`, `paper/main.tex`.
*Provenance IRI:* `fair2r:hc-dlr-design`

### 2026-05-06 --- "Add a section on provenance analysis"
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* `paper/sections/provenance-analysis.tex`,
`scripts/provenance_analysis.py`, four auto-generated LaTeX fragments
(rung distribution, section coverage, source strength, recent
activities).
*Artefacts touched:* `paper/sections/provenance-analysis.tex`,
`scripts/provenance_analysis.py`, `paper/Makefile`,
`.github/workflows/build-paper.yml`.
*Provenance IRI:* `fair2r:hc-provenance-analysis-section`

### 2026-05-06 --- Generate illustrations + interactive graph viewer
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* `paper/figures/pipeline.tex` (TikZ ten-stage pipeline
figure); `site/provenance-explorer.md` (vis-network interactive node-
link viewer); JSON exporter in
`scripts/build_provenance_site.py`.
*Artefacts touched:* `paper/figures/`, `site/provenance-explorer.md`,
`scripts/build_provenance_site.py`.
*Provenance IRI:* `fair2r:hc-illustrations`

### 2026-05-06 --- Splashy homepage; PDF link prominent
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* `site/index.md` rewritten with a hero CTA-row, callout,
three-card grid; the GitHub Pages URL promoted to a top-of-README
section in two passes ("the URL is missing" → promote to dedicated
section; "I mean the pages" → confirm Pages URL not repo URL).
*Artefacts touched:* `site/index.md`, `README.md`,
`site/static/style.css`.
*Provenance IRI:* `fair2r:hc-splashy-homepage`

### 2026-05-06 --- Fix CI; verify build runs
*Type:* `corrective-intervention`
*Leverage:* high
*Triggered:* `paper/style/fair2r.sty` rewritten (five bugs fixed:
slash-prefixed `\ProvidesPackage`, broken `xkeyval` machinery, missing
`colortbl`, fragile `sansmath`, risky `quote` redefinition);
`.github/workflows/pages.yml` Pages-specific steps gated on `main`.
*Artefacts touched:* `paper/style/fair2r.sty`,
`.github/workflows/pages.yml`,
`.github/workflows/build-paper.yml`.
*Provenance IRI:* `fair2r:hc-ci-fix`

### 2026-05-06 --- Vendored DRAFT-watermarked PDFs to reduce CI runs
*Type:* `rule-shape`
*Leverage:* medium
*Triggered:* `\faiarDraft=true` default in `paper/main.tex`; rolling
`latest-draft` GitHub Release published by the build-paper workflow on
pushes to `main` via `softprops/action-gh-release`.
*Artefacts touched:* `paper/main.tex`, `paper/style/fair2r.sty`,
`.github/workflows/build-paper.yml`, `README.md`.
*Provenance IRI:* `fair2r:hc-draft-pdf-release`

### 2026-05-06 --- Source-research mandate; Consensus / Scholar default
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* Source-analyser subagent dispatched; `doc/sources.md`
populated with topic-organised, ladder-graded entries;
`agents/source-analyzer.md` and `doc/research-protocol.md` updated to
mandate Consensus / Scholar as the default scientific-search tool.
*Artefacts touched:* `agents/source-analyzer.md`,
`doc/research-protocol.md`, `doc/sources.md`, `paper/references.bib`.
*Provenance IRI:* `fair2r:hc-source-workflow`

### 2026-05-06 --- Add scientific repositories + paywall escalation
*Type:* `rule-shape`
*Leverage:* medium
*Triggered:* arXiv, OpenAlex, Crossref, PubMed/EuropePMC, IEEE Xplore,
Springer Link, ACM Digital Library, ScienceDirect added to the source
workflow; institutional-access escalation channel introduced (a paper
that cannot be read on the open web is requested via a structured log
that the human author can fulfil through DLR institutional access).
*Artefacts touched:* `agents/source-analyzer.md`.
*Provenance IRI:* `fair2r:hc-scientific-repos`

### 2026-05-06 --- Cache-bust the deployed Pages site
*Type:* `corrective-intervention`
*Leverage:* low
*Triggered:* SHA-1-keyed `?v=` versioning on `style.css` and
`provenance.json`; soft `Cache-Control` meta; build-version footer.
*Artefacts touched:* `scripts/build_provenance_site.py`,
`site/provenance-explorer.md`.
*Provenance IRI:* `fair2r:hc-cache-bust`

### 2026-05-06 --- Mermaid renderer fix for `provenance-graph.md`
*Type:* `corrective-intervention`
*Leverage:* low
*Triggered:* Three GitHub-Mermaid syntactic issues repaired (subgraph
title with parentheses; node labels with colons; edge labels with
colons); companion HTML-escaping fix in the site builder.
*Artefacts touched:* `doc/provenance-graph.md`,
`scripts/build_provenance_site.py`.
*Provenance IRI:* `fair2r:hc-mermaid-fix`

### 2026-05-06 --- Author's Note carried over from Obscurity-Is-Dead
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* `paper/sections/authors-note.tex` adapted from the source
paper's front-matter "Author's Note --- Advice for reading"; positions
F(AI)\textsuperscript{2}R as a position paper; folds in the
"What surprised me about the cooperation" finding.
*Artefacts touched:* `paper/sections/authors-note.tex`,
`paper/main.tex`.
*Provenance IRI:* `fair2r:hc-authors-note`

### 2026-05-06 --- Position-paper reframing
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* `paper/sections/position.tex` (five numbered claims);
`paper/sections/objections.tex` (six anticipated objections with
charitable responses);
`paper/sections/statement-of-authorship.tex`; `paper/sections/
discussion.tex` retired; `paper/sections/conclusion.tex` sharpened.
*Artefacts touched:* `paper/sections/`, `paper/main.tex`.
*Provenance IRI:* `fair2r:hc-position-reframe`

### 2026-05-06 --- "What's my contribution?" — the question that became this file
*Type:* `responsibility-uptake`
*Leverage:* high
*Triggered:* The model's perspective in chat became the seed for the
*What surprised me about the cooperation* paragraph in the Author's
Note; the user's follow-up "yes add it" promoted the question and the
answer into the published paper text; this contributions log and the
companion observations log were created so the partition is empirically
auditable rather than asserted.
*Artefacts touched:* `paper/sections/authors-note.tex`,
`doc/user-contributions.md`, `doc/user-observations-log.md`,
`doc/provenance.ttl` (Contribution class).
*Provenance IRI:* `fair2r:hc-contribution-question`

### 2026-05-06 --- Contribution-tracking rule (this file's existence)
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* This file; companion observations log;
`fair2r:Contribution` / `HumanContribution` / `AIContribution` /
`MetaContribution` extension to the PROV-O schema; binding clause in
`CLAUDE.md` and in `agents/orchestrator.md` requiring that every
material contribution be logged here as a side-effect of the
primary-artefact consistency invariant.
*Artefacts touched:* `doc/user-contributions.md`,
`doc/user-observations-log.md`, `doc/provenance.ttl`, `CLAUDE.md`,
`agents/orchestrator.md`.
*Provenance IRI:* `fair2r:hc-contribution-rule`

### 2026-05-07 --- Claim: F(AI)²R relates to model checking / automatic theorem proving
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* New paragraph in §11 (Related Work) titled
"Formal methods: model checking and theorem proving." The paragraph
maps F(AI)²R machinery onto formal-methods vocabulary
(conjecture / proof-state / proof-checker / invariants /
prover-checker separation), names two future-work imports the
analogy suggests (counter-example witnesses on retracted claims;
lemma libraries citable by IRI), and hedges with "the analogy is
partial". Two new bib entries: `clarke2009modelchecking` (CACM 2009
Turing lecture) and `klein2009sel4` (SOSP 2009 verified microkernel).
*Artefacts touched:* `paper/sections/related.tex`,
`paper/references.bib`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-formal-methods-relationship`

### 2026-05-07 --- Fix Beamer conference deck: enumitem + Beamer enumerate-template conflict
*Type:* `corrective-intervention`
*Leverage:* high
*Triggered:* User pasted the conference-30min.log tail from the
failing build-slides run. Real error:
`TeX capacity exceeded, sorry [grouping levels=255]. \labelenumi -> { \labelenumi }`
--- a recursive macro definition caused by loading `enumitem`
alongside Beamer's `\setbeamertemplate{enumerate item}` in
`slides/style/fair2r-beamer.sty`. Removed `\usepackage{enumitem}`
from `slides/conference-30min.tex` and stripped
`[leftmargin=...,itemsep=...]` from all three `\begin{enumerate}`
calls. The pitch deck never used enumerate, which is why it
compiled all along.
*Artefacts touched:* `slides/conference-30min.tex`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-fix-beamer-enumitem-conflict`

### 2026-05-07 --- Reconcile provenance + new eight-practices figure + scrutiny pass
*Type:* `rule-shape`
*Leverage:* medium
*Triggered:* (a) Deleted `paper/sections/discussion.tex` and
`paper/sections/acknowledgements.tex` (both marked superseded after
the position-paper reframe; unreferenced); the `provenance.ttl`
activity `act:rev-reconcile-and-illustrate` records a
`prov:Invalidation` of `ent:section-discussion`. (b) New
`paper/figures/eight-practices.tex` (4x2 grid colour-coded by
failure-mode family) wired into
`paper/sections/eight-practices.tex`. (c) Scrutiny of all section
files for voice issues; the Author's Note's direct address is
preserved as a documented genre exception
(`claim:authors-note-voice-exception`);
`agents/scientific-writer.md` updated to make the carve-out
explicit; `self-reference.tex`'s closing aphorism reworded to
remove a second-person "you".
*Artefacts touched:* `paper/sections/eight-practices.tex`,
`paper/sections/self-reference.tex`,
`paper/figures/eight-practices.tex` (new),
`paper/sections/discussion.tex` (deleted),
`paper/sections/acknowledgements.tex` (deleted),
`agents/scientific-writer.md`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-reconcile-illustrate-scrutinize`

### 2026-05-07 --- Claim: traditional publishing under stress; journal-as-distribution in decline
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* New third paragraph in §1 of `paper/sections/intro.tex`
titled "The journal as distribution channel may be in decline.".
The paragraph escalates the §1 framing from "LLMs cause failure
modes per paper" to "the journal-as-distribution format itself is
under structural strain"; cites preprint / open-access / overlay-
journal alternatives plus a Nature piece on AI-fabricated
submissions; hedges with "we do not claim the journal is dead".
Three new bib entries: `eisen2018preprints`, `tennant2016open`,
`conroy2023sleuths` (all `lit-retrieved`, TODO-VERIFY at
`lit-read`).
*Artefacts touched:* `paper/sections/intro.tex`,
`paper/references.bib`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-journal-decline`

### 2026-05-07 --- Reconcile: main is default; Pages source = GitHub Actions
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* User switched the GitHub default branch to `main` and
set the Pages source to "GitHub Actions". Docs reconciled:
`CLAUDE.md` branch-policy rewritten + new "Pages source" subsection;
`agents/orchestrator.md` refusal-conditions updated;
`doc/methodology.md` gains a "Branch and deployment policy"
subsection.
*Artefacts touched:* `CLAUDE.md`, `agents/orchestrator.md`,
`doc/methodology.md`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-reconcile-default-branch-and-pages-source`

### 2026-05-07 --- Verify CI; fix the conference-deck Beamer compile failure
*Type:* `corrective-intervention`
*Leverage:* high
*Triggered:* Inspection of PR \#19's check_runs surfaced two
build-slides.yml failures at the "Compile conference deck" step
(exit code 12); logs auth-protected. Four defensive fixes in
`slides/style/fair2r-beamer.sty`: removed `\\renewcommand{\\familydefault}`,
simplified `\\sectiondivider` (no group-local background canvas),
reduced helvet scaling to 0.95, wrapped frametitle in a minipage.
Companion fix in `slides/conference-30min.tex`: single-line
subtitle.
*Artefacts touched:* `slides/style/fair2r-beamer.sty`,
`slides/conference-30min.tex`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-fix-beamer-conference-build`

### 2026-05-06 --- Pages staleness: defensive fixes + forced deploy
*Type:* `corrective-intervention`
*Leverage:* low
*Triggered:* `scripts/build_provenance_site.py` now writes
`_site/.nojekyll`; the page template's hero section gains a
visible `build-tag` printing the cache-bust hash; touching the
script + CSS matches `pages.yml`'s path filter so the merge
triggers a fresh deploy and busts the CDN cache.
*Artefacts touched:* `scripts/build_provenance_site.py`,
`site/static/style.css`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-pages-staleness-fix`

### 2026-05-06 --- Beamer-only: drop Marp, ship Beamer slide decks
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* Switched the slide pipeline from Marp to Beamer at
researcher request ("only ship beamer"). Removed
`slides/pitch-5min.md`, `slides/conference-30min.md`,
`slides/static/dlr/` (vendored Marp theme + assets), and
`scripts/build_slides.py` (the Marp asset-inlining preprocessor).
Added `slides/style/fair2r-beamer.sty` (Beamer companion to
`paper/style/fair2r.sty`); two Beamer decks
`slides/pitch-5min.tex` and `slides/conference-30min.tex`; rewrote
`slides/Makefile` to drive latexmk; rewrote
`.github/workflows/build-slides.yml` to use
`xu-cheng/latex-action` exactly like `build-paper.yml`. Updated
`agents/presentation.md` to be Beamer-only (with explicit refusal
to reintroduce a Marp / HTML / PPTX path); `CLAUDE.md` and
`doc/methodology.md` primary-artefact list now names `.tex`
sources; README and `site/index.md` link the Beamer PDFs only
(no PPTX downloads).
*Artefacts touched:* `slides/`, `agents/presentation.md`,
`.github/workflows/build-slides.yml`, `CLAUDE.md`,
`doc/methodology.md`, `doc/provenance.ttl`,
`doc/user-contributions.md`, `doc/logbook.md`, `README.md`,
`site/index.md`.
*Provenance IRI:* `fair2r:hc-beamer-only-slides`

### 2026-05-06 --- Fix slide rendering (DLR theme) + trigger Pages rebuild
*Type:* `corrective-intervention`
*Leverage:* high
*Triggered:* New `scripts/build_slides.py` ports the marp-dlr
framework's `scripts/run-marp.mjs` asset-inlining preprocessor to
Python: the DLR theme's `url('./assets/...')` references are
replaced with base64 data URIs before Marp ever sees them, so the
title and section-divider background plates plus the DLR logos
actually load in headless Chromium. `slides/Makefile` and
`.github/workflows/build-slides.yml` now invoke the Python
preprocessor instead of calling Marp directly. `site/index.md`
gains a one-line note about the preprocessor, which has the
side effect of triggering `pages.yml` (whose path filter the
slide-only commits did not match), so the deploy refreshes and
busts the CDN cache that made the site look "back to the old
page".
*Artefacts touched:* `scripts/build_slides.py`, `slides/Makefile`,
`.github/workflows/build-slides.yml`, `site/index.md`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`doc/logbook.md`, `doc/user-observations-log.md`.
*Provenance IRI:* `fair2r:hc-fix-slide-rendering`

### 2026-05-06 --- Two slide decks + presentation agent + slides as fourth primary artefact
*Type:* `structural-decision`
*Leverage:* high
*Triggered:* New `slides/` tree with the vendored marp-dlr theme
under `slides/static/dlr/`; two source decks
(`slides/pitch-5min.md` for the 5-minute pitch and
`slides/conference-30min.md` for the 25 + 5 conference talk);
`slides/Makefile` (`make all`, `make pitch`, `make conference`,
`make watch`); new `.github/workflows/build-slides.yml` workflow
that renders both decks to PDF + PPTX + HTML on every push and
publishes the rendered files to a rolling `latest-draft-slides`
GitHub Release on `main`; new `agents/presentation.md` as the
slide-deck custodian; **slides promoted to fourth primary artefact**
in `CLAUDE.md` and `doc/methodology.md`. README and `site/index.md`
gain prominent download links to both decks (PDF and PPTX).
*Artefacts touched:* `slides/`, `.github/workflows/build-slides.yml`,
`agents/presentation.md`, `CLAUDE.md`, `doc/methodology.md`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`doc/logbook.md`, `README.md`, `site/index.md`.
*Provenance IRI:* `fair2r:hc-slide-decks`

### 2026-05-06 --- "yes" --- promote the longer-arc paragraph into the Conclusion
*Type:* `structural-decision`
*Leverage:* medium
*Triggered:* New "The longer arc" paragraph in
`paper/sections/conclusion.tex` restating
`claim:future-research-infrastructure` with reference back to §3.6 and
the Helmholtz cross-centre graph (`curdt2025hmc`). The position-paper
closer now ends on the forward-looking note before the closing
aphorism.
*Artefacts touched:* `paper/sections/conclusion.tex`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-promote-longer-arc`

### 2026-05-06 --- Forward-looking pair: bioinformatics precedent + research-infrastructure vision
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* New §3.6 *Looking forward: provenance graphs as research
infrastructure* in `paper/sections/pattern.tex`. The researcher
posed two paired claims: (a) "future research success might depend a
lot more on provenance models for hypothesis development, graph
interconnectivity (Helmholtz graph supercharged) and clever
experimental validation", and (b) "bioinformatics was driven there
earlier by the at-the-time obscene amounts of data leading to
semantic tagging becoming the norm to identify genes". Both
graduated to paper text. The bioinformatics-precedent argument is
anchored on Ashburner et al. 2000 (Gene Ontology, Nature Genetics);
the Helmholtz cross-centre graph reuses `curdt2025hmc`. The
marketing-verb "supercharged" was rephrased to "fully-instrumented"
to fit the DLR voice rules. Two new fair2r:Claim entries
(`bioinformatics-precedent`, `future-research-infrastructure`),
both at `human-confirmed`.
*Artefacts touched:* `paper/sections/pattern.tex`,
`paper/references.bib`, `doc/provenance.ttl`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-research-infrastructure`

### 2026-05-06 --- "ontologies might actually help" --- domain ontologies as schema extension
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* New §3.5 "Extensibility through domain ontologies" in
`paper/sections/pattern.tex`; three new bib entries (`janowicz2019sosa`
for SOSA/SSN, `rijgersberg2013om` for OM-2,
`qudt` for QUDT); new `claim:domain-ontologies-extension` in the
graph at `human-confirmed`. The German fragment "konkrete
standardisierte Methode" carried into the prose as a load-bearing
technical term in the source-author voice.
*Artefacts touched:* `paper/sections/pattern.tex`,
`paper/references.bib`, `doc/provenance.ttl`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-domain-ontologies`

### 2026-05-06 --- "link reviewer-side AI policies + reproducibility-crisis literature"
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* Five new bib entries: `ioannidis2005`,
`pineau2021reproducibility`, `neurips_llm_policy`, `iclr_llm_policy`,
`aclrr_llm_policy`. Citations inserted in `paper/sections/intro.tex`
(reproducibility baseline) and `paper/sections/background.tex`
(reviewer-AI policies). Two new fair2r:Claim entries.
*Artefacts touched:* `paper/sections/intro.tex`,
`paper/sections/background.tex`, `paper/references.bib`,
`doc/provenance.ttl`.
*Provenance IRI:* `fair2r:hc-gap-fill-reproducibility-and-policies`

### 2026-05-06 --- "do we have a list of reading tasks for the researcher?"
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* New `scripts/build_reading_queue.py` that produces
`doc/reading-queue.md` from the graph plus the bib. Entries sorted
by load-bearing weight (number of `fair2r:Claim` entries that
depend on the source via `prov:wasDerivedFrom`). Wired into
`paper/Makefile` (`make provenance` regenerates both
analysis fragments and the queue) and into
`.github/workflows/build-paper.yml`. Surfaced on the public site
nav as "Reading queue".
*Artefacts touched:* `scripts/build_reading_queue.py`,
`doc/reading-queue.md`, `paper/Makefile`,
`.github/workflows/build-paper.yml`,
`scripts/build_provenance_site.py`.
*Provenance IRI:* `fair2r:hc-reading-queue`

### 2026-05-06 --- "Its still a bit hard to read" --- more illustrations
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* Three TikZ figures added on the DLR token palette: the
verification-ladder FSM, the F(AI)\textsuperscript{2}R axes
$4\times 2$ grid, the accelerator-vs-blender coupling-rule partition.
Each replaces a paragraph that was carrying load by prose alone.
*Artefacts touched:* `paper/figures/ladder-fsm.tex`,
`paper/figures/axes.tex`, `paper/figures/coupling-rule.tex`,
`paper/sections/pattern.tex`, `paper/sections/authors-note.tex`,
`doc/provenance.ttl`.
*Provenance IRI:* `fair2r:hc-readability-figures`

### 2026-05-06 --- "yes, also perform another pass on the context data"
*Type:* `content-prompt`
*Leverage:* high
*Triggered:* The accelerator-or-blender observation graduated to
paper text in `paper/sections/authors-note.tex` as the *coupling rule*
extending *What surprised me about the cooperation*; corresponding
`fair2r:MetaContribution` `hc:obs-accelerator-or-blender` flipped from
`promotedToPaper="pending"` to `"yes"`. A third-pass source-research
subagent was dispatched in parallel to (a) verify the existing bib
entries that remain at `lit-retrieved`, (b) build new sources for the
manifold-vs-extrapolation framing, distributed-cognition philosophical
grounding, prompt-engineering literature, and HMC / NFDI4Ing position
papers, and (c) run a context-data pass: orphan
`fair2r:HumanContribution` checks, dangling-cite check across
`paper/sections/*.tex`, section-graph mismatch checks, and
unactioned-`Next:` todos in `doc/logbook.md`.
*Artefacts touched:* `paper/sections/authors-note.tex`,
`doc/provenance.ttl`, `doc/user-contributions.md`,
`paper/references.bib` (via the dispatched subagent),
`doc/sources.md` (via the dispatched subagent).
*Provenance IRI:* `fair2r:hc-third-pass-research`

---

## Aggregate count (back-filled at 2026-05-06)

| Type | Count |
|---|---|
| `structural-decision`     | 5 |
| `corrective-intervention` | 4 |
| `content-prompt`          | 5 |
| `rule-shape`              | 5 |
| `observation`             | (tracked in `user-observations-log.md`) |
| `responsibility-uptake`   | 1 |
| `experience-meta`         | (implicit; carried over from Obscurity-Is-Dead) |

These are reconstructions; the count is a lower bound on the actual
number of contributions, since some sessions made several at once.

### 2026-05-07 --- Add-illustrations pass: hero graphic + two supporting figures
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* Researcher reported the paper "felt a bit hard to read"
and asked for a hero graphic plus two to three supporting
illustrations. The illustration subagent added one hero
(`paper/figures/hero.tex` plus a `hero.standalone.tex` wrapper) wired
into `paper/main.tex` front matter and `slides/pitch-5min.tex` title
slide; one writer/reader dual-loop figure
(`paper/figures/dual-loop.tex`) placed in `paper/sections/intro.tex`;
one failure-mode coverage heat-strip
(`paper/figures/failure-mode-coverage.tex`) placed in
`paper/sections/failure-modes.tex` below Table 1. Each figure ships
with a `.figspec.md` per the illustration agent's output format. No
new TikZ libraries required. Provenance updated:
`act:add-illustrations-pass`, `ai:add-illustrations-pass` (first
`fair2r:AIContribution` recorded in the graph), and matching
`ent:figure-*` entities; rdflib re-parse: 1531 -> 1591 triples (+60).
*Artefacts touched:* `paper/figures/hero.tex`,
`paper/figures/hero.standalone.tex`, `paper/figures/dual-loop.tex`,
`paper/figures/failure-mode-coverage.tex`, the three matching
`.figspec.md` files, `paper/main.tex`, `paper/sections/intro.tex`,
`paper/sections/failure-modes.tex`, `slides/pitch-5min.tex`,
`doc/provenance.ttl`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-add-illustrations-prompt`
(matching AI mirror: `fair2r:ai-add-illustrations-pass`)

### 2026-05-07 --- Verification pass 2: 19 further sources advanced + 4 bib corrections flagged
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* User dispatched a second source-analyzer subagent run
after the first verification pass landed (PR #11). The subagent
walked the 22 remaining `lit-retrieved` entries (skipping the 3
already on the institutional-access list) and advanced **19** of
them to `ai-confirmed`, each with a verbatim quoted snippet in the
new fifth-pass log of `doc/sources.md`: `clarke2009modelchecking`,
`klein2009sel4`, `alemohammad2023mad`, `shumailov2024collapse`,
`chen2023drift`, `luccioni2024power`, `patterson2021carbon`,
`strubell2019energy`, `li2023thirsty`, `birhane2022values`,
`thorp2023chatgpt`, `sadasivan2023reliably`, `reynolds2021prompt`,
`liu2023prompt`, `anderson2024homogenization`,
`kuteeva2024diversity`, `clark1998extended`, `clark2025extending`,
`hutchins1995cognition`. Direct `WebFetch` returned 403 at every
publisher domain in this pass; all retrievals went through the Exa
`web_fetch` MCP tool, with two `web_search_exa` assists for OUP
Analysis and OUP Applied Linguistics. Four bib corrections flagged
for the orchestrator to apply: `clark2025extending` DOI / volume /
pages; `kuteeva2024diversity` volume / number / pages;
`liu2023prompt` article number; `li2023thirsty` final-version
title. Result: rdflib re-parse 1591 → 1607 triples (+16); rung
distribution **51 ai-confirmed**, **3 lit-retrieved** (all on the
institutional-access list), 21 human-confirmed, 10
source-vendored, 2 needs-research.
*Artefacts touched:* `doc/sources.md`, `doc/provenance.ttl`,
`doc/reading-queue.md` (regenerated),
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-verification-pass-2`


### 2026-05-07 --- Scoping prompt: provenance verification programme
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* User dispatched the research-protocol subagent to
author a position-paper-style scoping document at
[`doc/research/provenance-verification.md`](research/provenance-verification.md)
answering the question "how could the F(AI)²R provenance graph
be verified or analyzed?". The doc covers three orthogonal axes
(structural / SHACL, semantic / SPARQL, formal / model checking
and theorem proving), surveys what is in place today
(`scripts/provenance_analysis.py`), proposes a six-item 12-month
verification programme with one-line success criteria, and is
explicit about what verification cannot solve (form vs. truth).
Three runnable SPARQL examples are inlined and were verified
against the live graph before being pasted in. The doc was
registered in the public site nav (one `PAGES` entry plus one
`NAV` entry in `scripts/build_provenance_site.py`).
*Artefacts touched:* `doc/research/provenance-verification.md`
(new), `doc/provenance.ttl` (+30 triples; new
`ent:doc-provenance-verification`,
`act:write-provenance-verification-scoping`,
`hc:provenance-verification-prompt`),
`scripts/build_provenance_site.py`,
`doc/logbook.md`, `doc/user-contributions.md`.
*Provenance IRI:* `hc:provenance-verification-prompt`

### 2026-05-07 --- Illustrations pass 2: ladder-fsm to Mermaid, rung-distribution figure added, dual-loop retired
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* Researcher prompt: "rerun illustrator with new info ---
Mermaid, matplotlib, and other publication-ready tools can also be
used". The illustration subagent re-ran on the full paper, with no
privilege given to the prior TikZ-only pass, and published an audit
verdict: keep the six TikZ figures whose argument is shape (hero,
axes, pipeline, coupling-rule, eight-practices,
failure-mode-coverage); replace the verification-ladder FSM with a
Mermaid `stateDiagram-v2` source
(`paper/figures/ladder-fsm.mmd`, rendered to `.pdf` and `.png` via
`mmdc`) so the manuscript and the Pages site can share one
source-of-truth artefact; retire the dual-loop figure that had
duplicated the hero on the same opening page; add a matplotlib
rung-distribution figure
(`paper/figures/src/rung-distribution.py`, deterministic, DLR
palette, rendered to `.pdf` and `.png`) as a one-glance companion
to the auto-generated rung table in
`paper/sections/provenance-analysis.tex`. Conference deck updated
in two frames (verification-ladder frame; rung-distribution frame)
to use the rendered PDFs. Provenance updated:
`act:add-illustrations-pass-2` (informed by the first illustrations
activity), `ai:add-illustrations-pass-2`,
`hc:rerun-illustrations-prompt`, two new `ent:figure-*` entities
(`rung-distribution`, `ladder-fsm-mermaid` with
`prov:wasDerivedFrom ent:figure-ladder-fsm`), and
`prov:wasInvalidatedBy` triples on the prior `ent:figure-ladder-fsm`
and `ent:figure-dual-loop`. rdflib re-parse: 1607 -> 1686 triples
(+79). Net figure count: 8 (was 8). Tools used: TikZ (6 figures),
Mermaid (1 figure), matplotlib (1 figure).
*Artefacts touched:* `paper/figures/ladder-fsm.mmd`,
`paper/figures/ladder-fsm.pdf`, `paper/figures/ladder-fsm.png`,
`paper/figures/ladder-fsm.tex` (now a thin shim around the rendered
PDF), `paper/figures/ladder-fsm.figspec.md`,
`paper/figures/rung-distribution.pdf`,
`paper/figures/rung-distribution.png`,
`paper/figures/rung-distribution.figspec.md`,
`paper/figures/src/rung-distribution.py`,
`paper/sections/intro.tex` (dual-loop input removed),
`paper/sections/provenance-analysis.tex`,
`slides/conference-30min.tex` (two frames updated),
`paper/figures/dual-loop.tex` (deleted),
`paper/figures/dual-loop.figspec.md` (deleted),
`doc/provenance.ttl`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-rerun-illustrations-prompt`
(matching AI mirror: `fair2r:ai-add-illustrations-pass-2`)

### 2026-05-07 — Rerun illustrator with new toolset (pass 3)
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* Researcher prompt: "run the illustrator again with the
broader toolset now pinned in `agents/illustration.md` --- decide
per-figure whether to refine, replace, or add, capped at 10 total
figures; DLR Corporate Design held binding for every tool". The
illustration subagent re-ran on the full paper. Audit verdict:
keep all eight prior figures (`hero`, `axes`, `pipeline`,
`coupling-rule`, `eight-practices`, `failure-mode-coverage` in
TikZ; `ladder-fsm` in Mermaid; `rung-distribution` in matplotlib)
--- their renderings are already DLR-CD-compliant and no default
theming has leaked through. Add one new figure: a
**provenance-topology preview**
(`paper/figures/provenance-topology.{pdf,png}`, source
`paper/figures/src/provenance-topology.py`), a node-link drawing
of the F(AI)\textsuperscript{2}R provenance schema with five
PROV-O lanes (Agents / Plans / Activities / Entities / Claims)
hand-laid for honest schema-shape but each node's `n=<count>`
badge read at render time from `doc/provenance.ttl` via `rdflib`.
Wired into `paper/sections/provenance-analysis.tex` at the section
opening, so the reader sees the shape of the graph before reading
the audit numbers drawn from it. AI-only nodes carry a `//` hatch
in addition to the soft-blue fill (greyscale-legible). Provenance
updated: `act:add-illustrations-pass-3` (informed by
`act:add-illustrations-pass-2`), `ai:add-illustrations-pass-3`,
`hc:rerun-illustrations-pass-3-prompt`, one new
`ent:figure-provenance-topology`. `rdflib` re-parse: 1703 -> 1736
triples (+33). Net figure count: 9 (was 8; cap is 10). Tools used
(cumulative): TikZ (6 figures), Mermaid (1 figure), matplotlib
(2 figures). `latexmk`/`pdflatex` are not present in the current
environment, so `make -C paper pdf` could not be exercised; the
figure render was verified independently by running the script.
*Artefacts touched:* `paper/figures/src/provenance-topology.py`
(new), `paper/figures/provenance-topology.pdf` (new),
`paper/figures/provenance-topology.png` (new),
`paper/figures/provenance-topology.figspec.md` (new),
`paper/sections/provenance-analysis.tex`, `doc/provenance.ttl`,
`doc/logbook.md`, `doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-rerun-illustrations-pass-3-prompt`
(matching AI mirror: `fair2r:ai-add-illustrations-pass-3`)


### 2026-05-07 --- Rule shape: run provenance-curator repair pass with reasons + WIP topology-page transparency
*Type:* `rule-shape`
*Leverage:* high
*Triggered:* Researcher prompt: dispatch the provenance-curator
subagent to repair the 8 claims missing `prov:wasGeneratedBy` that
the public topology page advertises (Worked verification example,
§2), and *while doing so, capture, for each defect, a one-sentence
reason*: "we can learn for our collaborative process". Plus a
transparency requirement: the topology page must show both states
(BEFORE / AFTER) so a reader sees the audit working, not a
sanitised after-image. The provenance-curator subagent: (a) added
the 8 missing `prov:wasGeneratedBy` edges, attaching three to
existing `act:rev-*` activities and minting five synthetic
`act:meta-cooperation-<date>-<slug>` activities for the claims
whose landing commits had no `act:rev-*` parent; (b) recorded a
per-claim repair activity carrying `fair2r:repairs` (new schema
property, domain `prov:Activity`, range `fair2r:Claim`) plus an
`rdfs:comment` literal explaining why the edge was missing; (c)
rewrote the Worked verification example as an honest two-state
walkthrough (WIP disclaimer, BEFORE table preserved, AFTER table
added, "Why those edges were missing" subsection summarising the
dominant pattern, forward-looking next-likely-defect line); (d)
appended the cooperative-process observation "Why audited defects
are pedagogical, not embarrassing" to
`doc/user-observations-log.md` (hypothesis stage; recommends a
*no claim without a parent activity* refusal rule for
`agents/provenance-curator.md`); (e) appended a logbook entry and
this contribution entry. `rdflib` re-parse: 1736 → 1906 triples
(+170). Conformance query against the post-repair graph: 0 rows.
*Artefacts touched:* `doc/provenance.ttl`,
`doc/provenance-graph.md`, `doc/logbook.md`,
`doc/user-contributions.md`, `doc/user-observations-log.md`.
*Provenance IRI:* `fair2r:hc-prov-curator-repair-pass-2026-05-07`
(matching AI mirror:
`fair2r:ai-prov-curator-repair-pass-2026-05-07`)


### 2026-05-07 --- Content prompt: still waiting for new illustrations
*Type:* `content-prompt`
*Leverage:* medium
*Triggered:* User signalled that PR #31 (one new figure:
`provenance-topology`) had been too modest a return on the
broader illustration toolset and asked the illustration subagent
to deliver substantially more new illustrations under the
10-figure cap. Pass-4 retired `eight-practices` and
`rung-distribution` and added three new figures:
`ladder-populations` (verification ladder FSM with rung counts as
node areas), `ai-squared-grid` (2x2 writer-vs-reader matrix), and
`contribution-histogram` (human-author contributions by type, read
from this file).
*Artefacts touched:* `paper/figures/ai-squared-grid.tex`,
`paper/figures/ai-squared-grid.figspec.md`,
`paper/figures/ladder-populations.{pdf,png}`,
`paper/figures/ladder-populations.figspec.md`,
`paper/figures/src/ladder-populations.py`,
`paper/figures/contribution-histogram.{pdf,png}`,
`paper/figures/contribution-histogram.figspec.md`,
`paper/figures/src/contribution-histogram.py`,
`paper/sections/pattern.tex`,
`paper/sections/provenance-analysis.tex`,
`paper/sections/authors-note.tex`,
`paper/sections/eight-practices.tex` (retired figure include),
`doc/provenance.ttl`, `doc/logbook.md`,
`doc/user-contributions.md`.
*Provenance IRI:* `fair2r:hc-rerun-illustrations-pass-4-prompt`
(matching AI mirror: `fair2r:ai-add-illustrations-pass-4`)


### 2026-05-07 --- "complete the loop": close the one outstanding lit-retrieved source
*Type:* `responsibility-uptake`
*Leverage:* medium
*Triggered:* User dispatched a third source-analyzer subagent run
to close the loop opened by PR #33, which had added a single new
`lit-retrieved` source (`shafer2014xennials`, the GOOD Magazine
piece popularising the Xennial bridge-generation framing). The
"complete the loop" framing is the corrective-loop counterpart to
the larger fifth-pass (verification-pass-2) sweep: rather than
let one new lit-retrieved entry sit on the queue, the user
required it be verified and either advanced or escalated within
the same session it was added. Result: source advanced to
`ai-confirmed`, no new escalations, one bib correction flagged
(author was wrong --- "Stankorb and Oelbaum", not "Shafer" ---
title was wrong; bibkey kept stable for citation continuity).
The contribution is `responsibility-uptake` because the prompt is
about closing an audit gap rather than producing new content; the
human author is putting their name to the discipline of "no
lit-retrieved source sits on the queue past the session that
introduces it".
*Artefacts touched:* `doc/sources.md`, `paper/references.bib`,
`doc/provenance.ttl`, `doc/reading-queue.md` (regenerated),
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:hc-complete-loop-prompt-2026-05-07`
(matching AI mirror: `fair2r:ac-verification-pass-3-2026-05-07`;
parent activity: `fair2r:act-meta-cooperation-2026-05-07-verification-pass-3`)


### 2026-05-07 --- Verification pass 3 (AI mirror): close out shafer2014xennials
*Type:* `corrective-intervention`
*Leverage:* medium
*Triggered:* Source-analyzer subagent run (`claude-opus-4-7[1m]`
under the source-analyzer prompt) executed the complete-the-loop
prompt: walked the one outstanding `lit-retrieved` source
introduced since the fifth pass (`shafer2014xennials`), fetched
the GOOD Magazine article via the Exa `web_fetch` MCP tool
(direct `WebFetch` returned 403 against `good.is`), captured a
verbatim quoted snippet in the new sixth-pass log of
`doc/sources.md`, advanced the source from `lit-retrieved` to
`ai-confirmed`, and flagged a bib correction (the article is by
**Stankorb and Oelbaum**, not "Shafer"; title is *"Reasonable
People Disagree about the Post-Gen X, Pre-Millennial
Generation"*, not *"Generation Xennial"*). Bibkey kept stable
for citation continuity. Re-parsed the graph via rdflib (2014 →
2016 triples, +2 net) and regenerated `doc/reading-queue.md` (51
entries, 3 lit-retrieved on the institutional-access list, 47
ai-confirmed, 1 no-rung). Logged this entry as the AI mirror per
the no-parentless-claim rule: parent activity
`act:meta-cooperation-2026-05-07-verification-pass-3`.
*Artefacts touched:* `doc/sources.md`, `paper/references.bib`,
`doc/provenance.ttl`, `doc/reading-queue.md` (regenerated),
`doc/user-contributions.md`, `doc/logbook.md`.
*Provenance IRI:* `fair2r:ac-verification-pass-3-2026-05-07`
