# FAIR notes

How this repository implements each of the four FAIR principles, and where
F(AI²)R adds the second AI pass.

## Findable

- A persistent identifier will be minted via Zenodo on first archival
  release (`.zenodo.json` is the metadata source).
- Repo-internal identifiers: every `fair2r:Claim` gets an IRI under the
  `https://noheton.org/f-ai-r/claim/` namespace.
- Machine-readable surface: `CITATION.cff` (humans + GitHub), `codemeta.json`
  (CodeMeta tooling), `.zenodo.json` (DataCite via Zenodo).

## Accessible

- Source under MIT (`LICENSE`); prose under CC-BY-4.0 (`LICENSE-paper`).
- Public Git repository — `git clone` is the access protocol.
- Sources cited that are themselves open-licensed are vendored under
  `doc/sources/`. Closed sources are referenced by DOI only and flagged in
  the FAIR audit.

## Interoperable

- Provenance in [PROV-O](https://www.w3.org/TR/prov-o/) plus DCTERMS plus
  FOAF, serialised as Turtle (`doc/provenance.ttl`).
- Manuscript in LaTeX (`paper/`); a portable PDF is the build output.
- Bibliography in BibTeX with DOIs whenever available.

## Reusable

- All artefacts versioned in Git with a clean commit history.
- Each agent prompt is a versioned file in `agents/`, so the *process* is
  reusable, not just the output.
- The Makefile is the canonical build entry point; CI (when added) calls
  the same targets.

## The F(AI²)R extension

| Principle | Author pass (AI₁) | Auditor pass (AI₂) |
|---|---|---|
| Findable      | Drafts metadata, suggests keywords. | Verifies metadata is consistent across CFF / CodeMeta / Zenodo. |
| Accessible    | Vendors sources, generates README. | Verifies licences, broken links, missing files. |
| Interoperable | Emits PROV-O triples for new claims. | Validates Turtle, runs SHACL shapes if defined. |
| Reusable      | Documents prompts, decisions.       | Replays the pipeline on a clean clone and reports drift. |
