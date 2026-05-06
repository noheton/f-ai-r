# Methodology

This file is the contract between the human author(s) and the LLM agents
defined in `agents/`. It describes *how* the paper is built, not *what* it
says.

## Primary artifacts (invariant)

Three artifacts are primary and must be **consistent and up to date at all
times**:

1. The **manuscript** (`paper/main.tex`, `paper/main-condensed.tex`,
   `paper/sections/*.tex`).
2. The **PROV-O graph** (`doc/provenance.ttl`).
3. The **logbook** (`doc/logbook.md`).

A working session is not complete until all three are in sync. A commit
that updates one of them and leaves the others lagging is a defect, even
if the build passes. This invariant supersedes any per-agent style rule
elsewhere in this repository.

## Pipeline overview

```
       human goal
            │
            ▼
   ┌────────────────┐
   │  orchestrator  │
   └───────┬────────┘
           │
   ┌───────┴────────┬──────────────┬────────────────┐
   ▼                ▼              ▼                ▼
scientific-    source-       illustration       condenser
 writer        analyzer
   │                │              │                │
   ▼                ▼              ▼                ▼
   ─────────  proposed triples  ──────────  ──────────
                       │
                       ▼
              provenance-curator ──► doc/provenance.ttl
                       │
                       ▼
              (audit pass)
                       │
        ┌──────────────┼─────────────────┐
        ▼              ▼                 ▼
  fair-aligner   layout-scrutinizer  readability-reviewer
        │              │                 │
        ▼              ▼                 ▼
                  human sign-off
                       │
                       ▼
                    git commit
                       │
                       ▼
                    logbook entry
```

## Two passes of AI

1. **Authoring pass.** `scientific-writer`, `source-analyzer`,
   `illustration`, `condenser`. AI proposes; humans dispose.
2. **Audit pass.** `fair-aligner`, `layout-scrutinizer`,
   `readability-reviewer`, `provenance-curator`. AI checks the
   manuscript and the graph against explicit criteria.

## Verification ladder

A `fair2r:Claim` carries one of:

| state | meaning |
|---|---|
| `unverified`        | Asserted but no evidence yet attached. |
| `needs-research`    | Evidence-gap acknowledged, search planned. |
| `ai-confirmed`      | An AI agent verified against a vendored or fetched source. |
| `human-confirmed`   | A human author verified the source and the inference. |
| `source-vendored`   | The source itself is in the repo under `doc/sources/`. |

A claim must reach `human-confirmed` (or `source-vendored`) before it can
appear in `main-condensed.tex`.

## Definition of done for a section

1. Prose compiles in `paper/main.tex` with no `\todo` left.
2. Every claim has a `fair2r:Claim` IRI in `doc/provenance.ttl` at
   `human-confirmed` or `source-vendored`.
3. `fair-aligner` audit reports no `fail`s for the section.
4. Logbook entry committed.
