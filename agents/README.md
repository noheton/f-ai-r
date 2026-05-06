# Agents

Each file in this directory is a versioned **prompt** for one role in the
F(AI²)R writing pipeline. Treat them as source code: edit, diff, review,
commit. Do not improvise new prompts in chat without landing them here first.

## Role catalogue

| File | Role | Pass |
|---|---|---|
| `orchestrator.md`        | Routes tasks across the other agents and the human author. | both |
| `scientific-writer.md`   | Drafts manuscript prose at section granularity.            | author |
| `source-analyzer.md`     | Reads cited material, extracts claims and quotes.          | author |
| `fair-aligner.md`        | Checks artefacts against the FAIR principles.              | auditor |
| `provenance-curator.md`  | Maintains `doc/provenance.ttl`; refuses fabricated triples. | auditor |
| `layout-scrutinizer.md`  | Reviews LaTeX layout, figure placement, typography.        | auditor |
| `readability-reviewer.md`| Reviews prose for clarity, flow, and novelty signal.       | auditor |
| `illustration.md`        | Plans and specifies figures (TikZ / SVG / matplotlib).     | author |
| `condenser.md`           | Page-budget enforcer. Fires when the compiled PDF exceeds the configured budget (default 10 pages of body). | auditor |
| `presentation.md`        | Slide-deck custodian. Owns `slides/pitch-5min.md` and `slides/conference-30min.md`; ensures slide claims are downstream of the paper text. | author |
| `research-protocol.md`   | Defines literature-search and verification protocols.      | both |

## Primary artifacts — consistency invariant (binds every agent)

The **manuscript** (`paper/`), the **PROV-O graph** (`doc/provenance.ttl`),
and the **logbook** (`doc/logbook.md`) are primary artifacts and must be
**consistent and up to date at all times**. No agent may finish a task
that touches one of them without ensuring the other two reflect the
change. Each prompt below restates this rule with a tailored "what *I*
must keep in sync" clause.

## Conventions every prompt follows

1. **Role, scope, non-goals.** Every prompt opens with what the agent *is*
   and what it *will not do*.
2. **Inputs and outputs are explicit.** A prompt names the files it reads
   and the files it is allowed to write.
3. **Primary-artifact consistency.** Every output bundles (a) the
   manuscript edit, (b) the proposed PROV-O triples, and (c) the
   logbook line. If the agent does not produce one of these directly, it
   *names* who must, before the session ends.
4. **Verification ladder.** Claims emerge tagged `unverified`,
   `needs-research`, `ai-confirmed`, `human-confirmed`, or `source-vendored`.
5. **Refusal is fine.** Agents must say "I cannot verify this" rather than
   invent a citation.
6. **Provenance hand-off.** Every output ends with the triples it expects
   `provenance-curator` to add to `doc/provenance.ttl`.
