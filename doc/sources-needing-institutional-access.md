# Sources needing institutional access

Append-only list of papers an agent has identified as **necessary**
for a load-bearing claim in the F(AI)²R manuscript but whose **full
text cannot be read** from open sources. The human author (Florian
Krebs) has institutional access through DLR (TIB / ZB MED / Helmholtz
e-journals / direct publisher subscriptions) and can retrieve the
PDFs that this list names.

## Why this file exists

A claim cannot leave the `lit-retrieved` rung of the verification
ladder until somebody has read the source. If the abstract is
sufficient, an AI agent can promote the claim to `ai-confirmed`. If
the claim depends on a figure, a numeric result, a methodological
detail, or wording that the abstract does not contain, the source
must be read in full --- and a paywalled source cannot be read in
full from open access.

The previous behaviour --- silently downgrading the rung, or
fabricating a quotation --- was a failure mode named in
`§\ref{sec:failure-modes}` of the paper. This file is the explicit,
auditable channel through which paywalled-but-necessary papers reach
the human author for retrieval.

## Schema

Append a fenced entry per paper, with these mandatory fields. Do
not edit prior entries; the file is append-only.

```
date-requested:   YYYY-MM-DD
bibkey:           <key in paper/references.bib>
title:            <full title>
authors:          <Authors>
identifier:       <DOI or arXiv id or stable URL>
journal/venue:    <venue, year, vol, pp.>
why-needed:       <which claim in which section the paper backs>
abstract-ok?:     yes | no
                  -- yes if the abstract alone supports the claim
                     (in which case do NOT request; promote to
                     ai-confirmed and remove this entry).
                  -- no if the body of the paper is needed.
specifically-need: <which figure / table / section / quotation>
open-version?:    <yes/no; preprint URL if yes; checked at request
                   time>
status:           pending | supplied | superseded | abandoned
date-supplied:    YYYY-MM-DD (when human author supplies the PDF)
where-vendored:   doc/sources/<bibkey>/ (after supply)
```

A `pending` request older than 30 days is surfaced as a soft `warn`
by the FAIR Aligner (\S\ref{sec:eight}, item 8). A claim that has
gone unverified for more than 90 days must either be hedged in the
prose or removed; the agent that drafts the hedge cites this file
as evidence of the gap.

A `supplied` entry is closed by adding a `source-vendored` directory
under `doc/sources/<bibkey>/` containing the PDF (where licence
permits the redaction policy) plus a `quotes.md` file with the
extracted snippets the manuscript relies on.

## Pending requests

(none yet — agents add entries here as paywalls are encountered.
Each entry should also be cross-referenced from `doc/sources.md` with
the marker `lit-retrieved (paywalled; institutional access requested)`.)

## Supplied / vendored

(none yet — entries move down here when the human author lands the
PDF and `doc/sources/<bibkey>/` is populated.)
