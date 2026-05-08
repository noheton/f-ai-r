---
slug: getting-started
title: Getting started
---

# Getting started with F(AI)²R

This page is for someone who wants to **adopt the F(AI)²R writing
methodology for their own paper**, not just read about it. The page
hands you a single initialization prompt that, pasted into a fresh
Claude Code session in an empty git repository, sets up the scaffold
the rest of this site documents. The rest of the page covers
prerequisites, what the cooperation loop looks like once the scaffold
is up, and how to adapt it to a domain that is not scholarly writing.

This repository ([`noheton/f-ai-r`](https://github.com/noheton/f-ai-r))
is the canonical reference. The initialization prompt below tells
the LLM to clone its agent prompts, schema, and binding rules from
this repo and adapt them to your title and your domain. Updates to
the methodology land on `main` here; the prompt always points at
the live state.

## Prerequisites

You need:

- **Git.** A fresh empty repository on your machine; the
  initialization prompt creates everything inside it.
- **Python 3.10+** with `rdflib` and `markdown` (`pip install rdflib
  markdown`). The provenance graph is RDF; the site builder is
  Markdown.
- **LaTeX** with `latexmk` (TeX Live 2023+ or MiKTeX). Used to
  compile the paper PDF and the Beamer slide decks.
- **An LLM coding client** that can read and write files in the
  repository. Claude Code is the reference client; Claude Desktop or
  any equivalent that exposes a file-edit tool will also work.
- **Optional but recommended.** A GitHub repository with Pages
  enabled (Source = *GitHub Actions*), so the public site
  deploys via the CI workflow rather than from a branch.

## Initialization prompt

Open Claude Code (or your equivalent client) inside an empty git
repository, paste the block below verbatim, and replace the two
angle-bracketed placeholders. The agent will draft a plan; review
it before letting it commit.

```
Bootstrap an F(AI)²R writing pipeline for a paper titled
"<your paper title here>" in the domain "<your domain — e.g.
mechanical engineering, computational biology, software
verification>".

Use https://github.com/noheton/f-ai-r as the canonical reference.
Read its agents/, doc/methodology.md, doc/provenance.ttl schema
block, paper/main.tex, paper/style/, and CLAUDE.md to understand
the conventions before you start. Adapt rather than copy
verbatim: my domain is not scholarly writing about AI, so the
eight integrated practices and the source-analyzer's literature
norms must be re-thought, not transplanted.

Your task — execute one item at a time, propose then commit:

1. Create CLAUDE.md mirroring the binding rules block from
   noheton/f-ai-r/CLAUDE.md, adapted to my domain. The
   primary-artefact consistency invariant, the contribution-
   tracking rule, the no-parentless-claim rule, and the
   chapter-per-file rule all carry over.

2. Create agents/ with the 11 agent prompts from
   noheton/f-ai-r/agents/. Adapt source-analyzer.md to my
   domain's literature retrieval norms; adapt fair-aligner.md
   to whatever standards my venue applies; leave the rest
   essentially intact.

3. Create paper/main.tex as a thin assembler with one
   \section{} per file under paper/sections/. Seed
   paper/style/ from noheton/f-ai-r/paper/style/, replacing
   DLR Corporate Design tokens with whatever institutional
   design system applies to me (or with a bare-bones fallback
   if none).

4. Create doc/provenance.ttl seeded with the schema block from
   noheton/f-ai-r/doc/provenance.ttl: the fair2r: namespace,
   the verification rungs, the Claim / Source / Section /
   Figure / Contribution classes. Add an act:bootstrap
   activity, a fair2r:HumanContribution mirroring this prompt
   (born with that activity as its parent per the
   no-parentless-claim rule), and one act:meta-cooperation-*
   parent for the seed claims you write into the manuscript.

5. Create doc/logbook.md and doc/user-contributions.md with
   the headers from noheton/f-ai-r/doc/. Append a dated
   bootstrap entry to each.

6. Create doc/methodology.md adapted to my domain — keep the
   primary-artefact list, the verification ladder, the
   eight-integrated-practices structure, the design-system
   block. Replace the eight practices with eight that fit my
   domain (or fewer if my domain genuinely needs fewer; the
   number is not load-bearing, the integration is).

7. Create the CI workflows: .github/workflows/build-paper.yml
   (latexmk on every push to main; rolling latest-draft
   release of paper/main.pdf), .github/workflows/pages.yml
   (build the static site from doc/ and publish to GitHub
   Pages with Source = GitHub Actions).

8. Add scripts/build_provenance_site.py and
   scripts/build_reading_queue.py from noheton/f-ai-r/scripts/.
   These are domain-agnostic; copy them as-is, then run both
   to verify they work against the seeded graph.

Rules you are bound by — these are not negotiable:

- Primary-artefact consistency. paper/main.tex (with its
  sections), doc/provenance.ttl, doc/logbook.md, and the slide
  decks must agree at all times. A change that touches one
  must, in the same commit or a clearly linked follow-up,
  produce the corresponding update in the others.

- No-parentless-claim. Every fair2r:Claim must carry
  prov:wasGeneratedBy to a named act:* activity. If no
  obvious parent exists, mint a synthetic
  act:meta-cooperation-<date>-<slug> activity at claim-add
  time. A claim without a parent is a graph defect.

- Chapter-per-file. One \section{} per file under
  paper/sections/. paper/main.tex is a thin assembler.

- Source-research mandate. Never fabricate citations. If a
  source cannot be verified, mark the claim with
  fair2r:verificationState verif:needs-research and leave a
  \todo[inline]{verify} marker in the LaTeX.

- Verification ladder. Sources move through the rungs
  unverified → needs-research → lit-retrieved →
  ai-confirmed → human-confirmed / source-vendored →
  lit-read. The lit-read rung is human-only; the model can
  never grant it.

- Voice. Precise, factual, institutional. No second person
  outside the Author's Note. No emoji. No marketing verbs.
  British English unless the venue's house style says
  otherwise.

After bootstrap is complete:
- Run `python3 -c "from rdflib import Graph; g = Graph();
  g.parse('doc/provenance.ttl', format='turtle');
  print(len(g), 'triples')"` and confirm the graph parses.
- Run `python3 scripts/build_provenance_site.py` and confirm
  it produces a non-empty _site/ directory.
- Open a pull request rather than pushing directly to main.

Confirm before any commit. Do not push to a remote branch I
have not explicitly authorised.
```

## What to expect once the scaffold is up

The cooperation loop has three sides.

1. **You direct.** "Add a section on X." "Fix the wrong DOI on
   `cite:smith2024foo`." "Verify these five sources." Every
   directive is a `fair2r:HumanContribution` with a typed leverage
   level, recorded in `doc/user-contributions.md`.

2. **Agents draft and audit.** The scientific-writer drafts; the
   source-analyzer fetches and grades sources; the FAIR-aligner
   audits primary-artefact consistency; the layout-scrutinizer
   checks typography and DLR-CD compliance (substitute your own
   design system); the readability-reviewer reads the prose;
   the condenser enforces the page budget; the
   provenance-curator is the only agent allowed to write the
   graph.

3. **You decide.** Audit findings come back as punch lists. The
   small fixes you authorise in batch; the taste calls
   (page-budget cuts, paragraph splits, repetition trims) you
   make explicitly. Nothing graduates to paper text without
   you naming the activity that generated it.

The discipline is **handback**: a writer agent proposes, an audit
agent checks, you decide. The handback boundaries are where
hallucinations get caught.

## Adapting to a different domain

F(AI)²R is domain-agnostic. To use it for software engineering,
mechanical engineering, computational biology, or anything where
the truth-claims of a paper need to survive an audit:

- **Keep the schema.** `Claim`, `Source`, `Section`, `Figure`,
  `Contribution`, the verification ladder, the
  primary-artefact invariant — these are domain-neutral.

- **Replace the eight practices.** Our eight are about
  scholarly writing under LLM pressure. Yours might be about
  reproducibility of CFD simulations, or experimental
  protocols in wet-lab biology, or theorem-proving discipline
  in formal verification. The number is not load-bearing; the
  integration is.

- **Adapt the source-analyzer.** Each domain has its own
  literature retrieval norms, its own preprint culture, its
  own authoritative repositories. The agent prompt names
  Consensus and Google Scholar as defaults; replace those
  with whatever your domain trusts.

- **Adapt the FAIR-aligner.** Each venue applies its own
  reproducibility standards: PRISMA, ARRIVE, MIAME, the ACM
  artefact-evaluation badges. The agent prompt audits against
  the standard; tell it which one.

- **Keep the design system honest.** DLR Corporate Design
  is binding for us because the paper is a DLR product. If
  your institution has one, use it; if not, pick a minimal
  set of tokens and stick to them. Default tool theming
  counts as an unfinished figure.

## Staying synced with the process

This page is hand-authored at the prose layer; the binding-rules
block below is **auto-synced** with `CLAUDE.md` on every site
build, so the rules a new user is given match the rules the
canonical repository runs under.

<!-- BEGIN AUTO-SYNCED: ground-rules -->
_Auto-synced from `CLAUDE.md` by `scripts/sync_getting_started.py`. Do not edit in place — edit `CLAUDE.md` and rebuild._

These are the rules the canonical repository runs under. The initialization prompt above hands the same rules to a new adopter; the block below is the source of truth as of the last site build.

### Ground rules (live from CLAUDE.md)

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
   `	odo{}` in the LaTeX rather than inventing a reference.
5. **One commit, one concern.** Manuscript edits, prompt edits, and
   provenance edits land in separate commits when feasible.

<!-- END AUTO-SYNCED: ground-rules -->

## Where to look next

- [Methodology](methodology.html) — the canonical methodology, with
  the table of process evolutions.
- [FAIR](fair.html) — the FAIR axes and the (AI)² factor.
- [Human-AI collaboration](collab.html) — how the cooperation loop
  is structured.
- [Provenance](provenance.html) — the live graph.
- [Provenance topology](provenance-graph.html) — schema diagram
  plus a worked verification example.
- [Logbook](logbook.html) — every session, every decision, dated.
- [Reading queue](reading-queue.html) — sources still to be
  promoted from `ai-confirmed` to `lit-read`.
