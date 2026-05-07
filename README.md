# F(AI)²R

> **FAIR research, with AI in the loop — twice.**
> A short-form working paper and a reproducible writing pipeline.

## Read on the web

**[https://noheton.github.io/f-ai-r/](https://noheton.github.io/f-ai-r/)**

## Download the artefacts

| Artefact | Latest draft (auto-built on every push to `main`) |
|---|---|
| **Paper PDF** (DRAFT watermark) | [`releases/download/latest-draft/main.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft/main.pdf) |
| **Pitch deck** (5 min) | [`releases/download/latest-draft-slides/pitch-5min.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/pitch-5min.pdf) |
| **Conference deck** (25 + 5 min) | [`releases/download/latest-draft-slides/conference-30min.pdf`](https://github.com/noheton/f-ai-r/releases/download/latest-draft-slides/conference-30min.pdf) |

Both decks are Beamer-rendered from versioned `.tex` sources under
[`slides/`](slides/) using the DLR Corporate Design Beamer style
([`slides/style/fair2r-beamer.sty`](slides/style/fair2r-beamer.sty)),
which mirrors `paper/style/fair2r.sty`. They are **primary
artefacts** under the consistency invariant, alongside the
manuscript, the PROV-O graph, and the logbook.

The full site renders the methodology, the agent prompts, the logbook,
the PROV-O graph (as grouped tables and as a Mermaid topology), and the
submission plan, all under the DLR Corporate Design.

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
├── paper/        LaTeX sources, bibliography, Makefile  → the artifact
│   └── style/    paper/style/fair2r.sty (DLR Corporate Design)
├── doc/          methodology, FAIR notes, logbook, PROV-O graph → the process
├── slides/       Beamer slide decks: pitch-5min.tex + conference-30min.tex
│   └── style/    fair2r-beamer.sty (DLR Corporate Design, mirrors paper/style/)
├── agents/       LLM agent prompts (one role per file)  → the workforce
├── site/         GitHub Pages source (DLR-aligned static site)
│   └── static/dlr/  vendored DLR design tokens (colors_and_type.css,
│                    Frutiger fonts, logo)
├── scripts/      build_provenance_site.py + requirements.txt
├── CITATION.cff  machine-readable citation
├── codemeta.json software metadata (CodeMeta 2.0)
└── .zenodo.json  archival metadata for Zenodo DOI minting
```

## Build

```sh
make -C paper pdf            # build the short-form paper
make -C slides all           # build both slide decks (PDF + PPTX + HTML)
python scripts/build_provenance_site.py    # build the public site to _site/
```

The paper targets **~10 pages of body, plus references and appendices**.
A single manuscript (`paper/main.tex`); no long/condensed split.

## Provenance

The full creation graph lives in [`doc/provenance.ttl`](doc/provenance.ttl)
as [PROV-O](https://www.w3.org/TR/prov-o/) over Turtle, extended with
DCTERMS and project-local subclasses (`fair2r:AIAgent`,
`fair2r:HumanResearcher`, `fair2r:Claim`, `fair2r:VerificationState`).
Every commit that touches the manuscript adds or refines a triple.

A human-readable mirror of the topology is at
[`doc/provenance-graph.md`](doc/provenance-graph.md). The same graph
renders as grouped tables on the public site under
`/provenance.html`.

## Logbook

Day-by-day notes go to [`doc/logbook.md`](doc/logbook.md), append-only,
newest last. The logbook is the human-readable shadow of the PROV-O
graph.

## Design

The site, the paper PDF, and (forthcoming) the slide deck follow the
**DLR Corporate Design** (CD-Handbuch §10.1, §4 Printmedien):

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
