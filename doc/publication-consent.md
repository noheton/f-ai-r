# Publication consent

**Status: NOT YET GIVEN.**

This file is the **gate** read by every script and workflow that
publishes the manuscript outside the local working tree (Zenodo
deposition, arXiv submission, conference upload, social-media
announcement). Until a signed entry below records explicit
human-author consent for a specific surface, those workflows must
refuse to publish.

The pattern is borrowed from the methodological ancestor
[`noheton/Obscurity-Is-Dead`](https://github.com/noheton/Obscurity-Is-Dead).
It is the audit-pass control on the **Accessible** axis
(`§3 axes`, A1.2 in Appendix C of the paper): an artefact is not
"accessible" until the human author has authorised that surface.

## How to record consent

Append a fenced entry below, with these mandatory fields. Do not
remove or edit prior entries; consent records, like the logbook,
are append-only.

```
date:           YYYY-MM-DD
granted-by:     <human author name> (ORCID <id>)
channel:        <how consent was conveyed; e.g. "in-person discussion",
                 "signed PDF", "email reply">
surface:        zenodo | arxiv | github-pages-public-deploy |
                 social-media-announcement | conference-upload
branch:         <git ref this consent applies to>
commit:         <git SHA the consent applies to>
scope-covered:  <what the consent authorises>
scope-excluded: <what the consent does NOT authorise>
preconditions:  <list, e.g. "Aligner audit clean", "no live credentials
                 in git history", "co-authors have signed off">
revocation:     <how to revoke this consent if circumstances change>
```

A consent record applies **only to the named surface, the named
branch, and the named commit**. A subsequent commit needs a fresh
record for the same surface. Revocation invalidates the public
surface but does not retract the recorded artefact.

## Recorded consents

(none)

## What is currently authorised

- **GitHub Pages site at `https://noheton.github.io/f-ai-r/`** —
  authorised implicitly by the public nature of the GitHub repository
  and the consolidated `build.yml` workflow (the `site` + `deploy`
  jobs) that deploys on every push to `main`.
  The site carries a watermarked DRAFT note on the linked PDF. It
  does **not** count as a peer-reviewed publication.
- **The DRAFT-watermarked PDF on the `latest-draft` GitHub release** ---
  same status as above. Auto-built; carries the watermark; not a
  publication.

## What is NOT authorised

- **Zenodo deposition.** Even if `.zenodo.json` is fully populated,
  the `submission/zenodo` workflow (when it exists) must refuse to
  upload until a `surface: zenodo` consent record appears below with
  a matching branch and commit.
- **arXiv submission.** Same gate.
- **Conference, journal, or workshop upload.** Same gate.
- **Removal of the DRAFT watermark.** Setting `\faiarDraft` to
  `false` in `paper/main.tex` requires a `surface: publication`
  consent record naming the venue.

This file is a primary artefact under the consistency invariant
(`CLAUDE.md`); a change to it is mirrored in `doc/logbook.md` and in
`doc/provenance.ttl` in the same commit.
