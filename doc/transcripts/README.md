# Transcripts

This directory carries the conversation transcripts that produced the
manuscript. The first integrated practice
(\S\ref{sec:eight} item 1, in `paper/sections/eight-practices.tex`)
binds every working session to commit its transcript here and link
it to the corresponding `prov:Activity` via `prov:used`.

## What lives here

- One file per session: `YYYY-MM-DD-session.md` (or
  `YYYY-MM-DDThhmm-<slug>.md` if more than one session lands on the
  same day).
- Each file contains the user prompts verbatim and a structured
  summary of the AI-side actions, with cross-references to commits
  and PRs in `git log` so the transcript is auditable against the
  repository state.
- The **canonical interactive transcript** is the Claude Code (or
  equivalent client) session URL — for example
  [`https://claude.ai/code/session_<id>`](https://claude.ai/code/).
  It is gated to session participants but is the authoritative
  record. Embed the URL near the top of every transcript file and
  use it as the trailing reference in commit messages produced by
  the session.
- The raw harness JSONL transcript is the second canonical source,
  exported via the LLM client's session-export tool and stored on
  the human author's machine. When the user authorises it, relevant
  excerpts can be pasted into this directory or the JSONL committed
  directly.
- This directory is the human-readable shadow of those two records,
  living inside the repository and auditable against the merged
  commits.

## Format

```
# Session YYYY-MM-DD — <one-line title>

*Cooperation:* Florian Krebs (human author) ×
                <model identifier, e.g. claude-opus-4-7>
*Pre-compaction summary:* (if applicable) — pointer to the
                 in-context summary the harness produced when
                 token usage forced compaction; the summary is
                 the only record of pre-compaction exchanges.
*Outcomes:* PRs / commits this session produced, by SHA.

## Turn-by-turn

### Turn N — <date or relative timestamp>

**User:**
> verbatim user prompt

**AI:** one-paragraph summary of what was done, plus a list of
artefacts touched and any commit / PR identifiers.

(repeat per turn)

## Provenance binding

`prov:Activity` IRIs and `fair2r:HumanContribution` IRIs that this
session produced, listed for cross-checking against
`doc/provenance.ttl`.
```

## Why bother

Practice 1 (`eight-practices.tex`) names transcript preservation
as a binding methodology rule. Until 2026-05-07 the rule was
prescribed but not practised — the
[evolution chronology](../../paper/sections/appendix-d-evolution-chronology.tex)
calls this *"Pipeline as target, not yet as practice."* The
transcripts kept here close that gap: the cooperation that produced
this paper is no longer reconstructible from the logbook and the
commit history alone, it is exportable from this directory.

## Honest limits

- A transcript may be **partial**: the AI can only commit what was
  in its context at the time of writing, which excludes the
  pre-compaction part of any long session. The pre-compaction
  summary message is captured verbatim in the transcript file
  when it exists, with a note that the underlying exchanges are
  not recoverable from this side.
- A transcript may be **redacted**: the human author may strike
  embargoed or third-party-confidential passages. Redactions are
  marked `[REDACTED — <reason>]`; the redaction itself is
  recorded as a `prov:Activity` so the audit chain stays intact.
- A transcript is **not the methodology**. The methodology lives
  in `doc/methodology.md` and the agent prompts under `agents/`.
  The transcripts are a forensic record, not a prescription.
