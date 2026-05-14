# Publication consent

This file gates **explicit publication** of the F(AI)²R artefact set
(paper, slides, poster, provenance graph) to external repositories
that issue durable identifiers and announce the work to a wider
audience.

## Status

**NOT YET AUTHORISED.**

`paper/main.pdf` and the slide / poster artefacts in
[`releases/latest-draft`](https://github.com/noheton/f-ai-r/releases/tag/latest-draft)
and
[`releases/latest-draft-slides`](https://github.com/noheton/f-ai-r/releases/tag/latest-draft-slides)
are **drafts**. Each PDF carries a *"DRAFT — not yet peer-reviewed"*
watermark via `\faiarDraft=true` in `paper/style/fair2r.sty`.

The submission scaffolds in `.zenodo.json` and `arxiv/` exist; they
do **not** fire until the human author flips this consent.

## What "authorised" looks like

To authorise publication, the human author edits this file:

1. Sets the **Authorised** field below to today's date.
2. Sets `\faiarDraft=false` in `paper/main.tex` so the watermark
   stops appearing.
3. Reviews and commits the final `arxiv/abstract.txt`, the final
   `.zenodo.json` (including the version bump), and the final
   `paper/references.bib`.

Once committed, the **publication workflow** (separate from
`build-paper.yml`, which only builds drafts) takes the
`paper/main.pdf` and submits it to:

- **arXiv** — the abstract category is `cs.DL` (Digital Libraries)
  with `cs.AI` cross-listing.
- **Zenodo** — issues a permanent DOI; the version, license, and
  related-identifiers are read from `.zenodo.json`.

## Authorisation field

**Authorised:** _(unset)_
**Authorised by:** _(unset)_
**Authorised on:** _(unset)_
**Version:** _(unset)_
**arXiv ID:** _(unset)_
**Zenodo DOI:** _(unset)_

## Why this gate exists

The seventh integrated practice (legal honesty about authorship,
§ Eight Integrated Practices) requires that the AI cannot consent
to publication on the human's behalf. This file is the
machine-checkable form of that rule: every release script and CI
job reads it before doing anything irreversible. The repository's
agent prompts under `agents/` are bound by the rule.
