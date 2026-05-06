# Working notes for Claude Code in this repository

This repository is **a paper plus its writing pipeline**. The artifact lives in
`paper/`, the process in `doc/`, the LLM workforce in `agents/`. Treat all
three as load-bearing.

## Primary artifacts (invariant)

The following three artifacts are **primary** and must be **consistent and
up to date at all times**. No commit may be made if any one of them lags
the others.

1. **The manuscript** — `paper/main.tex` (and `paper/main-condensed.tex`,
   plus any included `paper/sections/*.tex`).
2. **The PROV-O graph** — `doc/provenance.ttl`.
3. **The logbook** — `doc/logbook.md`.

Concretely, any change that touches one must, in the same commit (or a
clearly linked follow-up commit before the working session ends), produce
the corresponding updates in the other two. Examples:

- Add a claim to `main.tex` ⇒ add a `fair2r:Claim` triple to
  `provenance.ttl` ⇒ note the addition in `logbook.md`.
- Retire a section ⇒ add a `prov:Invalidation` activity in
  `provenance.ttl` ⇒ note the retirement and reason in `logbook.md`.
- Swap an agent prompt ⇒ update the `fair2r:Prompt` entity referenced by
  `provenance.ttl` ⇒ note the prompt change in `logbook.md`.

Every agent in `agents/` is bound by this invariant.

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

Development happens on `claude/init-fair-paper-repo-2d64T` (and successor
feature branches). Do not push to `main` without explicit instruction.
