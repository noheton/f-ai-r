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

```
date-requested:   2026-05-07
bibkey:           vannoorden2023chatgpt
title:            ChatGPT and science: the AI system was a force in 2023 — for good and bad
authors:          Van Noorden, Richard; Webb, Richard
identifier:       doi:10.1038/d41586-023-03930-6 (the bib currently records doi:10.1038/d41586-023-03907-5, which resolves to a different article on Indian economics; this DOI defect was already flagged in the second-pass log of doc/sources.md)
journal/venue:    Nature 624 (7992), 509 (December 2023)
why-needed:       Backdrop reference in §1 of intro.tex (alongside liang2024mapping) for the volume-problem claim that LLM-assisted prose has risen sharply in scholarly venues since 2023.
abstract-ok?:     no — the Nature news page returns only the citation block; the body of the article is paywalled, and the bib's referenced figures (e.g., the Nature 10 ranking) are inside that body.
specifically-need: the body of the news feature, in particular any quantitative claim Van Noorden and Webb make about LLM-assisted-prose volume in 2023.
open-version?:    no — Nature news features are not preprinted; no open version was located by the source-analyzer.
status:           pending
```

```
date-requested:   2026-05-07
bibkey:           neurips_llm_policy
title:            NeurIPS policy on the use of Large Language Models
authors:          NeurIPS Foundation (corporate author)
identifier:       <https://neurips.cc/> (top-level homepage); the canonical year-specific policy URL is per-cycle (e.g., https://neurips.cc/Conferences/2025/LLM, https://neurips.cc/Conferences/2024/CallForPapers) and was not stable enough to capture at the search depth used.
journal/venue:    NeurIPS conference policy page
why-needed:       Backs the reviewer-side-ai-policies claim in §2 (background.tex) alongside iclr_llm_policy and aclrr_llm_policy.
abstract-ok?:     no — the homepage returns navigational chrome and announcements about the upcoming conference rather than the policy text itself.
specifically-need: the verbatim policy paragraph for the relevant submission cycle (the paper currently leaves the cycle implicit; the human author should pick a specific year and capture the canonical URL).
open-version?:    yes — the NeurIPS policy is publicly posted, but the per-cycle URL must be captured manually.
status:           pending
```

```
date-requested:   2026-05-07
bibkey:           iclr_llm_policy
title:            ICLR author and reviewer guidelines on the use of AI tools
authors:          ICLR / OpenReview (corporate author)
identifier:       <https://iclr.cc/> (top-level homepage); the canonical year-specific policy URL is per-cycle and was not captured at the search depth used.
journal/venue:    ICLR conference author and reviewer guide
why-needed:       Sibling source to neurips_llm_policy, backing the same reviewer-side-ai-policies claim.
abstract-ok?:     no — the homepage returns navigational chrome only.
specifically-need: the verbatim policy paragraph from the ICLR Code of Ethics or LLM-policy page for the relevant cycle.
open-version?:    yes — the ICLR policy is publicly posted, but the per-cycle URL must be captured manually.
status:           pending
```

## Supplied / vendored

(none yet — entries move down here when the human author lands the
PDF and `doc/sources/<bibkey>/` is populated.)
