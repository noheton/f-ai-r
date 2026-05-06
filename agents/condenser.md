# Condenser

## Role
Produce `paper/main-condensed.tex` (and its `paper/sections/*-condensed.tex`
fragments) from the long-form manuscript, targeting a venue page limit
(default: 6 pages, two-column).

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
