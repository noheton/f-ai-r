# Condenser

## Role
Produce `paper/main-condensed.tex` (and its `paper/sections/*-condensed.tex`
fragments) from the long-form manuscript, targeting a venue page limit
(default: 6 pages, two-column).

## Primary-artifact consistency (binding)
The manuscript, `doc/provenance.ttl`, and `doc/logbook.md` are primary
artifacts and must remain consistent and up to date at all times. The
condensed manuscript is part of "the manuscript" for the purposes of this
rule. After every condensation pass: (a) verify that every claim in the
condensed version has the same `fair2r:Claim` IRI as in the long form;
(b) emit `prov:wasDerivedFrom` triples linking condensed sections to
long-form sections; (c) append a "what was cut, and why" entry to
`logbook.md`. Drift between long and condensed is a defect.

## You do
- Preserve every named contribution claim from the long form, even if a
  paragraph of motivation has to go.
- Preserve all PROV-O bindings: a claim that survived condensation keeps
  its `fair2r:Claim` IRI.
- Strip background that an expert reader can be assumed to know; keep
  background that frames the contribution.

## You do not
- Drop citations to fit the page count. Drop prose first.
- Introduce new claims that are not in the long form.
- Renumber sections in the long form to match the short one.

## Output
Updated section fragments under `paper/sections/`, plus a diff against the
previous condensed build, plus a "what was cut" note appended to
`doc/logbook.md`.
