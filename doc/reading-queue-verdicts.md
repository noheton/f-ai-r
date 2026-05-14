# Reading-queue verdicts

Human-edited companion to [`reading-queue.md`](reading-queue.md).
Each line records the author's verdict on whether a source can advance from
`ai-confirmed` (or `lit-retrieved`) to `lit-read`.

## Format

```
bibkey: <advance|hold|retire|pending> — optional free-text note
```

- `advance` — the source supports every dependent claim as stated; once
  set, also update the rung in `doc/provenance.ttl` to `verif:lit-read`
  and drop the `\todo[inline]{verify}` marker in the manuscript.
- `hold` — the source has been examined but the verdict is not yet
  clear; the note explains what is outstanding.
- `retire` — the source does not support the claims it is attached to;
  remove the `prov:wasDerivedFrom` edges in `doc/provenance.ttl` (the
  bib entry may stay for historical accuracy).
- `pending` — no verdict yet (the default for newly-added sources).

New sources receive a `pending` line automatically on the next build of
`scripts/build_reading_queue.py`; pre-existing lines are preserved.

## Verdicts (one per source, sorted alphabetically)

aclrr_llm_policy: pending
alemohammad2023mad: pending
anderson2024homogenization: pending
ashburner2000go: pending
bender2021stochastic: pending
benjelloun2024croissant: pending
birhane2022values: pending
chen2023drift: pending
chuehong2022fair4rs: pending
clark1998extended: pending
clark2025extending: pending
clarke2009modelchecking: pending
conroy2023sleuths: pending
curdt2025hmc: pending
eisen2018preprints: pending
else2023chatgpt: pending
gebru2021datasheets: pending
guyatt2008grade: pending
hutchins1995cognition: pending
iclr_llm_policy: pending
icmje2023: pending
ioannidis2005: pending
janowicz2019sosa: pending
klein2009sel4: pending
kobak2024delving: pending
kuteeva2024diversity: pending
li2023thirsty: pending
liang2024mapping: pending
liu2023prompt: pending
liu2026ara: pending
luccioni2024power: pending
magesh2024legal: pending
mitchell2019modelcards: pending
neurips_llm_policy: pending
page2021prisma: pending
patterson2021carbon: pending
pineau2021reproducibility: pending
qudt: pending
ravi2024fair4ml: pending
reynolds2021prompt: pending
rijgersberg2013om: pending
sadasivan2023reliably: pending
schmitt2020nfdi4ing: pending
shafer2014xennials: pending
shumailov2024collapse: pending
strubell2019energy: pending
tennant2016open: pending
thorp2023chatgpt: pending
urhg2: pending
usco2023ai: pending
vannoorden2023chatgpt: pending
w3c2013provo: pending
walters2023fabrication: pending
wilkinson2016fair: pending
