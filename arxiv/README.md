# arXiv submission scaffold

This directory holds the **arXiv-ready bundle** of the paper, gated
by `paper/publication-consent.md`. Nothing in here is uploaded
automatically; the bundle is a static artefact for a human to drag
into arXiv's submission UI once consent is recorded.

## Contents

| File | Role |
|---|---|
| `README.md` | This file. |
| `abstract.txt` | The arXiv-style abstract (≤ 1920 characters, plain ASCII with light LaTeX). Mirrored from `paper/sections/abstract.tex` at consent time. |
| `categories.txt` | Primary + cross-list categories. |
| `bundle.sh` | One-shot script that builds an arXiv-style tarball from the repo, ready for upload. Runs `make -C paper pdf`, then assembles `paper/main.tex`, every `paper/sections/*.tex`, `paper/figures/*` (only the active set), `paper/style/fair2r.sty`, and `paper/references.bib` into `arxiv/f-ai-r-<version>.tar.gz`. |

## Categories

Primary: `cs.DL` (Digital Libraries).
Cross-list: `cs.AI`, `cs.CY` (Computers and Society).

## License

Submitted under **CC-BY-4.0** for the prose (matching `LICENSE`).

## Sanity checklist before upload

- [ ] `paper/publication-consent.md` Authorised field is set.
- [ ] `\faiarDraft=false` in `paper/main.tex`.
- [ ] `paper/references.bib` has no `TODO-VERIFY` notes on
      load-bearing entries; the rung distribution shows zero
      `verif:needs-research` claims.
- [ ] The submission abstract in `arxiv/abstract.txt` matches
      `paper/sections/abstract.tex` (modulo arXiv's 1920-char
      limit).
- [ ] `arxiv/bundle.sh` produces a tarball that compiles cleanly
      with `latexmk -pdf` from a fresh extraction.
- [ ] The conference poster and slide decks are NOT in the bundle
      (arXiv preprint = paper only; supplementary artefacts live
      on Zenodo via the `related_identifiers` block in `.zenodo.json`).
