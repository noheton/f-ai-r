# Logbook

Append-only, newest at the bottom. One entry per working session, dated in
ISO-8601. The logbook is the human-readable shadow of `provenance.ttl`; if
you change the manuscript, add an entry here.

Format:

```
## YYYY-MM-DD — short title
*Author:* <human or agent name>
*Touched:* <files>
*Decision / outcome:* <one paragraph>
*Next:* <bullet list>
```

---

## 2026-05-06 — Repository initialised
*Author:* claude-opus-4-7 (under direction of repo owner)
*Touched:* whole tree (initial commit)
*Decision / outcome:* Bootstrapped F(AI²)R as a paper-plus-pipeline
repository. Adopted the meta-structure distilled from
`noheton/Obscurity-Is-Dead`: separation of `paper/` (artifact), `doc/`
(process), and `agents/` (LLM workforce); machine-readable metadata at the
root (`CITATION.cff`, `codemeta.json`, `.zenodo.json`); a Makefile with
stable targets; a PROV-O graph in Turtle as the spine of provenance; a
verification ladder for claims.
The IoT-security domain content of the source repository was deliberately
excluded — only the meta-practices were transferred.
*Next:*
- Replace placeholder author block in `CITATION.cff`, `codemeta.json`,
  `paper/main.tex`.
- Draft `Section 1: Introduction` via `agents/scientific-writer.md`.
- Run `agents/fair-aligner.md` against the empty manuscript to baseline
  the audit report.

## 2026-05-06 — Primary-artifact consistency rule added
*Author:* claude-opus-4-7 (under direction of repo owner)
*Touched:* `CLAUDE.md`, `doc/methodology.md`, `agents/README.md`,
all ten files under `agents/`.
*Decision / outcome:* Codified an invariant: the manuscript
(`paper/`), the PROV-O graph (`doc/provenance.ttl`), and the logbook
(`doc/logbook.md`) are primary artifacts and must remain consistent and
up to date at all times. Every agent prompt now carries a
"Primary-artifact consistency (binding)" block tailored to its role.
The orchestrator is named ultimate custodian of the invariant; the
provenance-curator is named keystone; `fair-aligner` will surface
desync as a `fail`.
*Next:* When `agents/scientific-writer.md` produces its first
section draft, exercise the rule end-to-end as the test case.
