# Provenance verification: a scoping note

Status: scoping draft (2026-05-07).
Author: research-protocol subagent (Claude Opus 4.7), under direction
of the human author.
Audience: panel discussants and reviewers asking how the F(AI)²R
provenance graph could be checked rather than merely read.

## 1. Why verify provenance at all?

The load-bearing claim of F(AI)²R is that the manuscript ships with
an *auditable* trail, not merely a present one. A graph that no one
can challenge is decoration; the gain over a free-text acknowledgement
section is rhetorical, not epistemic. Verification is the operation
that turns `doc/provenance.ttl` from a narrated artefact into a
checkable one.

The FAIR audit pass already enforced by
[`agents/fair-aligner.md`](../../agents/fair-aligner.md) is the floor:
it confirms that the four primary artefacts (manuscript, graph,
logbook, slides) are mutually consistent, that every section in the
prose has a `fair2r:Section` mirror, and that every claim flagged in
the manuscript has a `fair2r:Claim` IRI. That is structural hygiene.
The present note describes the ceiling: the wider verification
programme that the floor leaves room for, organised along three
orthogonal axes.

Each axis answers a distinct question. *Structural verification*
asks whether the graph is well-formed against its own schema.
*Semantic verification* asks whether the graph, taken as evidence,
suffices to convince a third party that the paper was produced as
claimed. *Formal verification* asks whether the disciplines the
graph encodes — the verification ladder, the handback discipline —
admit the kind of mechanised reasoning model checking and proof
assistants have made routine elsewhere. The three are not in
competition; they form a stack, and the present F(AI)²R repository
sits firmly at the bottom of it.

## 2. Three axes of verification

### 2.1 Structural verification (SHACL)

The schema in `doc/provenance.ttl` declares classes (`fair2r:Claim`,
`fair2r:Source`, `fair2r:Section`, `fair2r:Figure`, `fair2r:Prompt`),
properties (`fair2r:verificationState`, `fair2r:contradicts`), and
the seven verification rungs (`verif:unverified`,
`verif:needs-research`, `verif:lit-retrieved`, `verif:ai-confirmed`,
`verif:human-confirmed`, `verif:source-vendored`, `verif:lit-read`).
None of these declarations carry cardinality constraints; the schema
states what *can* exist, not what *must*.

SHACL closes that gap. A starter shape set of four to six shapes
covers the bulk of the implicit invariants:

- *Claim shape.* Every `fair2r:Claim` has at least one
  `prov:wasGeneratedBy`, at least one `prov:wasAttributedTo`, and
  exactly one `fair2r:verificationState` whose value is one of the
  seven rung individuals.
- *Source shape.* Every `fair2r:Source` has a `dcterms:title`, a
  `dcterms:identifier`, and (after the `w3c2013provo` defect noted
  in §3 is fixed) a `fair2r:verificationState`.
- *Section shape.* Every `fair2r:Section` has at least one
  `prov:wasGeneratedBy` activity and a `prov:hadPrimarySource` to a
  `fair2r:Manuscript`.
- *Figure shape.* Every `fair2r:Figure` has a `dcterms:source`
  pointing at a TikZ file under `paper/figures/` and a
  `prov:wasGeneratedBy` activity.
- *Activity shape.* Every `prov:Activity` has a `prov:startedAtTime`
  and at least one `prov:wasAssociatedWith`. The transcript
  requirement (`dcterms:source` to a logbook entry or a chat
  transcript) is a stretch invariant; see §3 for why.
- *Rung-membership shape.* The object of any `fair2r:verificationState`
  triple is one of the seven `verif:` individuals, not a free literal.

The executor is `pyshacl`, run locally during development and in CI
on every pull request. A SHACL violation is a hard fail, surfaced in
the same PR comment as the `fair-aligner` audit so reviewers see one
report rather than two. The shapes file, kept under
`doc/shapes/fair2r.ttl`, is itself a primary artefact and falls
under the consistency invariant.

### 2.2 Semantic and reproducibility analysis (SPARQL)

Well-formedness is necessary but not sufficient. A reader who wants
to be convinced that the paper came to be in the way the graph
narrates needs to traverse the graph: from a claim in the prose, to
the activity that generated it, to the prompt that drove that
activity, to the agent that ran the prompt, to the source the claim
was derived from. Each hop is a SPARQL traversal. The graph is
already large enough — currently 1607 triples, with 37 claims, 51
sources, 26 activities, 19 sections, and 9 figures — that ad-hoc
inspection is no longer adequate.

Three queries the human author can run today against the live graph
illustrate the register:

```sparql
# Q1: per-claim provenance trail
PREFIX fair2r: <https://noheton.org/f-ai-r/ns#>
PREFIX prov:   <http://www.w3.org/ns/prov#>
SELECT ?claim ?activity ?agent ?rung WHERE {
  ?claim a fair2r:Claim ;
         prov:wasGeneratedBy   ?activity ;
         prov:wasAttributedTo  ?agent ;
         fair2r:verificationState ?rung .
}
```

```sparql
# Q2: rung distribution at submission time
PREFIX fair2r: <https://noheton.org/f-ai-r/ns#>
SELECT ?rung (COUNT(?c) AS ?n) WHERE {
  ?c a fair2r:Claim ; fair2r:verificationState ?rung .
} GROUP BY ?rung ORDER BY DESC(?n)
```

```sparql
# Q3: ghost citations (sources never invoked by a claim)
PREFIX fair2r: <https://noheton.org/f-ai-r/ns#>
PREFIX prov:   <http://www.w3.org/ns/prov#>
SELECT (COUNT(?s) AS ?n) WHERE {
  ?s a fair2r:Source .
  FILTER NOT EXISTS { ?c a fair2r:Claim ; prov:wasDerivedFrom ?s }
}
```

Each was executed against the present graph with `rdflib`. Q1
returns 37 rows, one per claim. Q2 reports 51 `ai-confirmed`, 21
`human-confirmed`, 10 `source-vendored`, 3 `lit-retrieved`, 2
`needs-research` — the same distribution that
`scripts/provenance_analysis.py` writes into the auto-generated
table consumed by `paper/sections/provenance-analysis.tex`. Q3
returns 27, which is the count of bibliography entries that the prose
discusses but that no claim formally invokes via `prov:wasDerivedFrom`
— a real gap, and a useful one to surface, since it names the work
the next curation pass should do.

These three queries cover only the easy diagnostics. A more
ambitious query library would add: per-section coverage (every
section has at least one claim at `ai-confirmed` or above);
prompt-to-claim traceability (every claim's generating activity has
a `prov:hadPlan` to a `fair2r:Prompt`, and the prompt is vendored
in `agents/`); transcript reachability (every activity points at a
session transcript or logbook entry the reader can read); and
contradiction graphs (the transitive closure of `fair2r:contradicts`
should be acyclic, and any cycle is a curation defect). The natural
host for these is Apache Jena's `arq` (server-side) or `rdflib`
(scripted, as the existing analysis script already does); both
parse the current Turtle file without ceremony.

### 2.3 Formal-methods analogy (model checking and theorem proving)

The verification ladder is, structurally, a finite state machine.
Its rungs are states; its allowed transitions (`unverified` →
`needs-research` → `lit-retrieved` → `ai-confirmed` → `lit-read`
or `source-vendored`, plus the lateral move to `human-confirmed`)
are edges; its disallowed transitions — a claim cannot fall back
from `source-vendored` to `unverified` without an explicit
`prov:Invalidation` — are the safety properties. The handback
discipline (author proposes, audit pass disposes) is the
prover/checker separation that model checking and
certified-software efforts treat as load-bearing: the author need
not be sound, the checker must be.

Three families of formal tooling are candidates. *Temporal-logic
model checkers* (SPIN, NuSMV) would encode the ladder as a Promela
or SMV transition system and LTL-check invariants such as "every
load-bearing claim eventually reaches `lit-read` or
`source-vendored` before submission". *TLA+* would express the
same invariants more declaratively and is the natural fit for the
multi-agent-handback structure; TLC would explore reachable rung
configurations across the full claim set. *Coq* or *Isabelle/HOL*
would support a typed encoding in which a `Claim` whose rung type
is `LitRead` is a different type from one whose rung is
`Unverified`, making rung promotion a property of the type system
rather than of an auxiliary check.

Honesty about the analogy is load-bearing. The FSM and
prover/checker analogies are tight: the rung set is finite, named
transitions encode the methodology, and the audit-pass agents in
`agents/fair-aligner.md` and `agents/provenance-curator.md` are by
construction distinct from the authoring-pass agents whose output
they check. The analogy that is loose is the one between a
manuscript and a transition system: prose is not a program, claims
are not statefully composable in the way SMV variables are, and the
truth of an underlying claim is not a property a model checker can
decide. The related-work paragraph at the end of
[`paper/sections/related.tex`](../../paper/sections/related.tex)
treats this looseness explicitly and is the seed of the present
note rather than its conclusion.

## 3. What is in place today

The closest thing F(AI)²R currently ships to verification is
[`scripts/provenance_analysis.py`](../../scripts/provenance_analysis.py),
which parses `doc/provenance.ttl` with `rdflib` and emits four
LaTeX fragments under `paper/sections/_generated/`: a rung
histogram, section-to-claim coverage, source-invocation strength
(including the ghost-citation count), and a recent-activities
timeline. The auto-generated tables in
`paper/sections/provenance-analysis.tex` read those fragments at
build time, so the manuscript reports the state of the graph at
PDF-compile time rather than a transcribed snapshot.

Two limits matter. First, the script is *descriptive*, not
*prescriptive*: it counts what is in the graph, but it does not
flag what is missing or what would violate an invariant. A graph
in which every claim's rung had silently been demoted to
`unverified` overnight would still produce a clean run; the
output table would simply show 100 % at the bottom rung. Second,
the script does not validate against a schema. Every observation
about graph well-formedness in the present F(AI)²R repository is
either a manual audit (the FAIR aligner) or implicit in the
script's iteration patterns; nothing is mechanically enforced.

The first item on the verification programme below addresses both
limits.

## 4. A 12-month verification programme

A prioritised list of six work items, each with a one-line success
criterion. Effort estimates assume the human author plus one AI
subagent and exclude review cycles.

1. **SHACL shape file** (≈1 week). Write `doc/shapes/fair2r.ttl`
   with the four to six shapes named in §2.1; add a Make target
   `make -C paper validate` that runs `pyshacl`. *Success:* a
   deliberately broken claim (rung literal removed, attribution
   missing) fails validation and prints a `sh:result` row naming
   the offending IRI.
2. **CI hook** (≈2 days). Add a job to `.github/workflows/` that
   runs `pyshacl` on every PR touching `doc/provenance.ttl` or
   any agent prompt. *Success:* a PR that introduces a SHACL
   violation cannot be merged without an override, surfaced in the
   same status check block as the existing build.
3. **SPARQL query library** (≈1 week). Vendor the three queries
   above plus four more (per-section coverage, prompt traceability,
   transcript reachability, contradiction acyclicity) under
   `doc/queries/*.rq`; add a `make queries` target that runs them
   all and prints a one-line pass/warn/fail per query. *Success:*
   a single command produces the same diagnostics as the current
   `provenance_analysis.py`, without re-implementing them in
   Python.
4. **TLA+ specification of the rung ladder** (≈3 weeks). Encode
   the verification ladder as a TLA+ specification in
   `doc/formal/Ladder.tla`, with the rung-promotion transitions
   as actions and the no-silent-demotion property as a safety
   invariant; run TLC against a finite claim set. *Success:* TLC
   reports zero invariant violations on the spec; an injected
   bug (a `source-vendored` → `unverified` edge) is caught with a
   counter-example trace.
5. **Counter-example witnesses** (≈1 week). Implement the
   "counter-example witness" idea named at the end of the
   related-work section: when a claim is invalidated, attach a
   `fair2r:counterExample` triple pointing at the source whose
   reading caused the invalidation. *Success:* every
   `prov:Invalidation` activity in the graph has at least one
   `fair2r:counterExample` pointer, and the public site
   surfaces the witness alongside the retracted claim.
6. **LLM-checker on rung confidence** (stretch, ≈4 weeks). For each
   `fair2r:Claim`, dispatch a fresh LLM with the claim text and
   the cited source's vendored snippet, and ask it to return a
   confidence band on the recorded rung. *Success:* the
   distribution of LLM-returned bands tracks the distribution of
   recorded rungs to within a documented tolerance; outliers are
   flagged for human review rather than overwriting the rung.

Items 1–3 are the minimum viable verification programme and would
move F(AI)²R from descriptive to prescriptive. Items 4–6 are
research contributions in their own right and would justify a
follow-up paper.

## 5. What this would not solve

Verification of the kind described here certifies the *form* of the
provenance, not the *truth* of the underlying claims. SHACL can
guarantee that every claim has an attached source at
`source-vendored`. SPARQL can guarantee that every section's claims
trace back to vendored prompts and agents. TLC can guarantee that
no claim silently regressed down the ladder. None of those
operations can guarantee that the source actually supports the
claim, that the prompt actually elicited the inference recorded,
or that the human reader who signed off on the rung promotion read
the source carefully rather than skimming the abstract. Those
remain irreducibly human responsibilities, and the F(AI)²R
methodology is explicit about them: the responsibility-uptake
contribution type in `doc/user-contributions.md` is the leg of the
process that the AI cannot share.

A second, narrower limit: verification cannot replace peer review.
A graph that passes every check above can still be wrong about the
world. The verification programme makes the manuscript *legible*
to a sceptical reader; it does not make it *correct*.

## 6. Open questions

The following are pointers for future researchers (or for a
successor paper) to pick up. None has a settled answer in the
current methodology.

- Should the verification ladder be encoded in OWL with
  `owl:disjointWith` between rungs, so that a claim carrying two
  rungs surfaces as a reasoner-flagged inconsistency?
- What is the right transcript granularity? All 26 `prov:Activity`
  nodes currently lack a `dcterms:source` to a session transcript;
  the schema does not yet mandate one.
- How should claim-to-claim *support* be expressed? The graph has
  `fair2r:contradicts` but no `fair2r:dependsOn`, which makes
  downstream invalidation hard to propagate.
- Is the ladder paper-specific, or should successor F(AI)²R papers
  share one ladder vocabulary so that cross-paper claim citations
  carry their rung with them?
- How should LLM-internal reasoning be recorded? Chain-of-thought
  tokens are not captured; some classes of audit (was the
  inference well-formed?) are therefore structurally impossible.
- Could the ladder itself be registered (Zenodo concept DOI,
  W3C-style namespace) so successor papers cite a versioned
  ladder rather than redefining the rungs ad hoc?
