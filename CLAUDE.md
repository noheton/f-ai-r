# Working notes for Claude Code in this repository

This repository is **a paper plus its writing pipeline**. The artifact lives in
`paper/`, the process in `doc/`, the LLM workforce in `agents/`. Treat all
three as load-bearing.

## Primary artifacts (invariant)

The following four artifacts are **primary** and must be **consistent
and up to date at all times**. No commit may be made if any one of
them lags the others.

1. **The manuscript** — `paper/main.tex` plus any included
   `paper/sections/*.tex`.
2. **The PROV-O graph** — `doc/provenance.ttl`.
3. **The logbook** — `doc/logbook.md`.
4. **The slide decks** — `slides/pitch-5min.tex` and
   `slides/conference-30min.tex` (Beamer; DLR Corporate Design via
   `slides/style/fair2r-beamer.sty`). Rendered PDFs are derived; the
   `.tex` sources are the primary artefact.

Concretely, any change that touches one must, in the same commit (or a
clearly linked follow-up commit before the working session ends), produce
the corresponding updates in the others. Examples:

- Add a claim to `main.tex` ⇒ add a `fair2r:Claim` triple to
  `provenance.ttl` ⇒ note the addition in `logbook.md` ⇒ if the
  claim is load-bearing, surface it on the appropriate slide deck.
- Retire a section ⇒ add a `prov:Invalidation` activity in
  `provenance.ttl` ⇒ note the retirement and reason in `logbook.md`
  ⇒ remove or revise the corresponding slide.
- Swap an agent prompt ⇒ update the `fair2r:Prompt` entity referenced by
  `provenance.ttl` ⇒ note the prompt change in `logbook.md`.
- Restructure a deck ⇒ keep its claims aligned with the manuscript;
  log the change as a `fair2r:Contribution` of type
  `content-prompt`.

Every agent in `agents/` is bound by this invariant. The
`agents/presentation.md` agent owns the slide decks; the slides do
not get to argue ahead of the paper.

## Contribution tracking (binding)

Every material contribution to the manuscript or its scaffolding is
logged in [`doc/user-contributions.md`](doc/user-contributions.md)
and (for observations about the cooperation itself) in
[`doc/user-observations-log.md`](doc/user-observations-log.md). Both
are mirrored as `fair2r:HumanContribution`, `fair2r:AIContribution`,
or `fair2r:MetaContribution` entities in `doc/provenance.ttl` per
the `Contribution` extension to the schema.

A "material contribution" is any one of:

- A structural decision (e.g. chapter-per-file rule, position-paper
  reframing).
- A corrective intervention (e.g. catching a wrong DOI, a stale
  cache, a CI failure).
- A content prompt (e.g. "add a section on X").
- A rule-shape addition to an agent prompt or the methodology.
- A meta-observation about the cooperation that may or may not
  graduate to paper content.
- A responsibility-uptake event (the human author signing the
  artefact, defending it in person, or carrying it into a venue).

Format and types are documented at the top of
`doc/user-contributions.md`. Every entry there has a corresponding
`hc:<slug>` IRI in `doc/provenance.ttl`.

This rule applies to AI agents the same way: a session that produces
a material change appends both an entry in
`doc/user-contributions.md` (or, for AI authorship, the AI mirror
file when it exists) and the corresponding triples. The partition the
Author's Note describes
([`paper/sections/authors-note.tex`](paper/sections/authors-note.tex),
*What surprised me about the cooperation*) is auditable only if both
sides log their contributions.

## Ground rules

1. **Never edit `paper/` without also updating `doc/logbook.md`.** Append a
   dated entry. Newest entry goes at the bottom.
2. **Every non-trivial claim added to the manuscript needs a triple in
   `doc/provenance.ttl`.** At minimum: a `fair2r:Claim`, a
   `prov:wasGeneratedBy` activity, a `prov:wasAttributedTo` agent (human or
   AI), and a `fair2r:verificationState`.
3. **Prompts are source code.** When you change how an agent behaves, edit
   the corresponding file in `agents/` and commit it. Do not silently improvise
   new prompts in chat.
4. **Don't fabricate citations.** If a source cannot be verified, mark the
   claim with `fair2r:VerificationState fair2r:NeedsResearch` and leave a
   `\todo{}` in the LaTeX rather than inventing a reference.
5. **One commit, one concern.** Manuscript edits, prompt edits, and
   provenance edits land in separate commits when feasible.

## Build / verify

```sh
make -C paper pdf
make -C paper condensed
```

If `latexmk` is not available, say so explicitly — do not pretend the build
succeeded.

## Branch policy

`main` is the default branch. Development happens on feature branches
off `main`; PRs target `main`. Direct pushes to `main` require explicit
human-author instruction --- everything else lands via pull request.

The legacy long-lived working branch
`claude/init-fair-paper-repo-2d64T` is the current de-facto feature
branch and continues to receive in-flight work between PRs; new
sessions may either stay on it or open a fresh branch off `main`.
Either path is acceptable as long as the PR-into-`main` invariant
holds.

## Pages source

GitHub Pages is configured with **Source = GitHub Actions**, not
"Deploy from a branch". The site deploys exclusively via
[`.github/workflows/pages.yml`](.github/workflows/pages.yml), which
uploads `_site/` as a Pages artefact and runs `actions/deploy-pages`
on the merge commit. No legacy `gh-pages` branch exists or is
required.
