# F(AI²)R

> **FAIR research, with AI in the loop — twice.**
> A working paper and a reproducible writing pipeline.

`F(AI²)R` re-reads the FAIR principles (**F**indable, **A**ccessible, **I**nteroperable,
**R**eusable) for an era where Large Language Models participate in scholarly
production. The "²" is deliberate: AI appears **twice** in the loop —

1. **AI-Assisted authoring.** LLM agents help draft, structure, illustrate, and
   condense the manuscript under human direction.
2. **AI-Audited provenance.** A machine-readable PROV-O graph records *who*
   (human or model) did *what*, *when*, from *which sources*, so that another
   AI — or another human — can later verify, replay, or contest each claim.

This repository **is** the paper and **is** the process. Everything that
produced the PDF, including prompts, decisions, and dead ends, is committed
alongside the source.

## Layout

```
.
├── paper/        LaTeX sources, bibliography, Makefile  → the artifact
├── doc/          methodology, FAIR notes, logbook, PROV-O graph → the process
├── agents/       LLM agent prompts (one role per file)  → the workforce
├── CITATION.cff  machine-readable citation
├── codemeta.json software metadata (CodeMeta 2.0)
└── .zenodo.json  archival metadata for Zenodo DOI minting
```

## Build

```sh
make -C paper pdf        # build the long form
make -C paper condensed  # build the short / venue version
make -C paper all        # both
make -C paper clean
```

## Provenance

The full creation graph lives in [`doc/provenance.ttl`](doc/provenance.ttl) as
[PROV-O](https://www.w3.org/TR/prov-o/) over Turtle, extended with DCTERMS and
project-local subclasses (`fair2r:AIAgent`, `fair2r:HumanResearcher`,
`fair2r:Claim`, `fair2r:VerificationState`). Every commit that touches the
manuscript should add or refine a triple.

## Logbook

Day-by-day notes go to [`doc/logbook.md`](doc/logbook.md), append-only, newest
last. The logbook is the human-readable shadow of the PROV-O graph.

## Licensing

- **Code, prompts, scripts, RDF**: MIT (`LICENSE`).
- **Manuscript text and figures**: CC-BY-4.0 (`LICENSE-paper`).

## Citation

See [`CITATION.cff`](CITATION.cff). When citing pre-publication snapshots, cite
the Git commit hash and the Zenodo DOI once minted.
