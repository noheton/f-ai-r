# F(AI)²R

> **FAIR research, with AI in the loop — twice.**
> A short-form working paper and a reproducible writing pipeline.

## Read on the web

**[https://noheton.github.io/f-ai-r/](https://noheton.github.io/f-ai-r/)**

The site is mobile-friendly: the *Get started* page hands a new
adopter a single initialisation prompt for Claude Code that
bootstraps an F(AI)²R scaffold on a fresh repository.

## Download the artefacts

| Artefact | Latest draft (auto-built on every push to `main`) |
|---|---|
| **Paper PDF** (DRAFT watermark) | [`releases/download/latest-draft/main.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf) |
| **Conference poster** (A0 portrait) | [`releases/download/latest-draft-slides/poster-A0.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/poster-A0.pdf) |
| **Pitch deck** (5 min) | [`releases/download/latest-draft-slides/pitch-5min.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/pitch-5min.pdf) |
| **Conference deck** (25 + 5 min) | [`releases/download/latest-draft-slides/conference-30min.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/conference-30min.pdf) |

The decks are Beamer-rendered from `.tex` sources under
[`slides/`](slides/) using the DLR Corporate Design Beamer style
([`slides/style/fair2r-beamer.sty`](slides/style/fair2r-beamer.sty));
the poster is `tikzposter` with DLR-CD colour overrides on the
`Simple` built-in theme. Together with the manuscript, the PROV-O
graph, and the logbook, they form the **five primary artefacts**
under the consistency invariant
([`CLAUDE.md`](CLAUDE.md)).

The full site renders the methodology, the agent prompts, the
process-evolution chronology, the logbook, the PROV-O graph (as
grouped tables, an interactive explorer, and a Mermaid topology
with a worked verification example), the contribution histogram,
the reading queue, the transcript directory, and the submission
plan, all under the DLR Corporate Design.

---

- **Repository:** <https://github.com/noheton/f-ai-r>
- **Author:** Florian Krebs · ORCID [0000-0001-6033-801X](https://orcid.org/0000-0001-6033-801X) · DLR Zentrum für Leichtbauproduktionstechnologie (ZLP), Augsburg
- **Affiliations:** Helmholtz-Gemeinschaft · NFDI4Ing · HMC (Helmholtz Metadata Collaboration)

`F(AI)²R` re-reads the FAIR principles (**F**indable, **A**ccessible, **I**nteroperable,
**R**eusable) for an era in which Large Language Models participate in scholarly
production. The **(AI)** factor is multiplied through every FAIR axis, **squared**
because each axis demands two passes over every artefact:

1. **Authoring pass.** LLM agents help draft, structure, illustrate, and
   condense the manuscript under human direction.
2. **Audit pass.** A machine-readable PROV-O graph records *who* (human
   or model) did *what*, *when*, from *which sources*, so that another
   AI — or another human — can later verify, replay, or contest each
   claim.

This repository **is** the paper and **is** the process. Everything that
produced the PDF, including prompts, decisions, and dead ends, is committed
alongside the source.

## Layout

```
.
├── paper/             LaTeX sources, bibliography, Makefile  → the artefact
│   ├── sections/      one \section{} per file (chapter-per-file rule)
│   ├── figures/       TikZ + matplotlib + Mermaid; PNG renders for the site
│   └── style/         paper/style/fair2r.sty (DLR Corporate Design)
├── slides/            Beamer decks + tikzposter A0 poster
│   ├── pitch-5min.tex      5-minute pitch
│   ├── conference-30min.tex  25 + 5 conference talk
│   ├── poster-A0.tex       A0 portrait conference poster
│   └── style/         fair2r-beamer.sty (DLR Corporate Design)
├── doc/               methodology, FAIR notes, logbook, PROV-O graph → the process
│   ├── provenance.ttl      PROV-O over Turtle (the audit substrate)
│   ├── logbook.md          dated session record
│   ├── user-contributions.md  human-side typed contributions
│   ├── user-observations-log.md  meta-observations on the cooperation
│   ├── transcripts/        per-session conversation transcripts (practice 1)
│   └── sources.md          per-source verification ladder
├── agents/            11 LLM agent prompts (one role per file)  → the workforce
├── site/              GitHub Pages source (DLR-aligned, mobile-friendly)
│   └── static/        dlr/ tokens + figures/ PNGs + style.css with
│                      responsive breakpoints
├── scripts/           build_provenance_site.py, sync_getting_started.py,
│                      provenance_analysis.py, build_reading_queue.py
├── CLAUDE.md          binding rules: primary-artefact consistency,
│                      no-parentless-claim, chapter-per-file
├── CITATION.cff       machine-readable citation
├── codemeta.json      software metadata (CodeMeta 2.0)
└── .zenodo.json       archival metadata for Zenodo DOI minting
```

## Build

```sh
make -C paper pdf            # build the short-form paper
make -C slides all           # build pitch + conference + poster
python scripts/build_provenance_site.py    # build the public site to _site/
```

The paper targets **~10 pages of body** plus references and
appendices; a single manuscript (`paper/main.tex`), no
long/condensed split. The conference poster carries the
visual heavy-lift (hero figure, populated verification ladder,
provenance topology) so the body need not duplicate.

## Provenance

The full creation graph lives in
[`doc/provenance.ttl`](doc/provenance.ttl) as
[PROV-O](https://www.w3.org/TR/prov-o/) over Turtle, extended
with DCTERMS and project-local subclasses (`fair2r:AIAgent`,
`fair2r:HumanResearcher`, `fair2r:Claim`,
`fair2r:VerificationState`, `fair2r:Slidedeck`,
`fair2r:Poster`, `fair2r:Transcript`,
`fair2r:Contribution`). The graph carries roughly 2 300+
triples; every commit that touches the manuscript or any
primary artefact adds or refines triples. The
**no-parentless-claim** invariant binds: every `fair2r:Claim`
must have a `prov:wasGeneratedBy` edge to a named `act:*`
activity (defect class repaired in the open; see the topology
page's *Worked verification example*).

A human-readable mirror of the topology is at
[`doc/provenance-graph.md`](doc/provenance-graph.md). The
graph renders as grouped tables (`/provenance.html`), as a
schema diagram with a worked SHACL/SPARQL example
(`/provenance-graph.html`), and as an interactive node browser
(`/provenance-explorer.html`) on the public site.

## Logbook + transcripts

Day-by-day notes go to [`doc/logbook.md`](doc/logbook.md),
append-only, newest last; the logbook is the human-readable
shadow of the PROV-O graph. Per-session conversation
transcripts go under
[`doc/transcripts/`](doc/transcripts/), bound to the
manuscript via `prov:used` on the corresponding authoring
activity (the first integrated practice of the eight). The
canonical interactive transcript for any session is the Claude
Code session URL recorded in the transcript file's header.

## Adopting F(AI)²R for your own paper

The *Get started* page on the public site
([`https://noheton.github.io/f-ai-r/getting-started.html`](https://noheton.github.io/f-ai-r/getting-started.html))
hands a new adopter a single initialisation prompt for Claude
Code (or any equivalent LLM coding client). Pasted into a
fresh git repository, it bootstraps an F(AI)²R scaffold —
agent prompts, schema, binding rules, build pipeline — and
adapts it to your title and your domain. The prompt's *Ground
rules* block is auto-synced from this repository's
[`CLAUDE.md`](CLAUDE.md) on every site build, so an adopter
is always handed the live rules rather than a snapshot.

## Design

The site, the paper PDF, the Beamer slide decks, and the A0
conference poster all follow the **DLR Corporate Design**
(CD-Handbuch §10.1, §4 Printmedien):

- **Type:** Frutiger 45 Light for Drucksachen; **Arial** mandated for
  electronic channels (Web, PowerPoint, E-Mail).
- **Colour:** Default **DLR Blue `#00658B`**; chapter variants Green
  (`#82A043`) and Yellow (`#D2AE3D`) available via
  `<html data-variant="b|c">`.
- **Layout:** white backgrounds, generous whitespace, square corners
  (0–2px), hairline `#cfcfcf` borders, no gradients in chrome, no
  shadows on print.
- **Voice:** precise, factual, institutional; no second person, no
  emoji, no marketing verbs.

Tokens vendored under [`site/static/dlr/`](site/static/dlr/);
LaTeX style under [`paper/style/fair2r.sty`](paper/style/fair2r.sty).

## Licensing

- **Code, prompts, scripts, RDF**: MIT (`LICENSE`).
- **Manuscript text and figures**: CC-BY-4.0 (`LICENSE-paper`).
- **DLR design assets** (fonts, logo, token CSS): vendored from the
  upstream DLR design system bundle; redistribution rights are
  inherited from the upstream and are confined to use within this
  project. Per CD-Handbuch §10.1 the public web channel runs on the
  **Arial** fallback (already in the stack) when Frutiger embedding
  rights are not available.

## Citation

See [`CITATION.cff`](CITATION.cff). When citing pre-publication
snapshots, cite the Git commit hash and the Zenodo DOI once minted.
