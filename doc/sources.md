# Sources

Index of sources cited or vendored for the F(AI)²R paper. Maintained by
`agents/source-analyzer.md`. Last updated 2026-05-07 (sixth pass).

## Sixth-pass log (2026-05-07)

The sixth pass closed the loop on the one outstanding `lit-retrieved`
source that had been added since the fifth pass: `shafer2014xennials`
(PR #33), the GOOD Magazine piece popularising the Xennial
bridge-generation framing. The agent reading the source is
`claude-opus-4-7[1m]` operating under the source-analyzer prompt.
Direct `WebFetch` returned 403 Forbidden against `good.is`; retrieval
went through the Exa `web_fetch` MCP tool, which returned the article
in clean markdown.

The fetch surfaced a **bibliographic correction**: the article is
co-authored by **Sarah Stankorb and Jed Oelbaum**, not "Sarah
Shafer" (the bibkey was a half-remembered authorship), and its
canonical title is *"Reasonable People Disagree about the Post-Gen
X, Pre-Millennial Generation"* with the dual-byline structure
"Glad to be a Xennial" / "Bah! We Xennials are a Sad, Sorry Lot",
not the abbreviated *"Generation Xennial"*. The bibkey
`shafer2014xennials` is kept stable for citation continuity (it is
already referenced by `claim:senior-researcher-bridge` and would
break a stable IRI if renamed); the `author` and `title` fields in
`paper/references.bib` and the `dcterms:creator` / `dcterms:title`
fields in `doc/provenance.ttl` were corrected. The published date
`2014-09-25` was added.

The three previously-escalated paywalled / per-cycle URL sources
(`vannoorden2023chatgpt`, `neurips_llm_policy`, `iclr_llm_policy`)
remain at `lit-retrieved` on the institutional-access queue and were
not retried. After the sixth pass, the reading queue contains zero
sources at `lit-retrieved` outside that escalation list.

### `shafer2014xennials` --- ai-confirmed

- **Quoted snippet (verbatim from the GOOD Magazine article, fetched
  via the Exa `web_fetch` MCP tool, 2026-05-07).**
  "Meet Generation Xennial (because no one uses Generation Y), born
  between 1979 and 1983. ... We call them the Xennials---a
  micro-generation that serves as a bridge between the disaffection
  of Gen X and the blithe optimism of Millennials. ... The internet
  was not a part of our childhoods, but computers existed and there
  was something special about the opportunity to use one. ...
  Technology unfolded around us, but we got to ease into it during
  that brief period before it became ubiquitous."
- **Used in.** `conclusion.tex` paragraph "The bridge to what is now
  unthinkable" --- the Xennial micro-generation is invoked as a
  generational analogue for senior researchers who span pre-LLM and
  LLM-era scholarship.
- **Bib correction logged.** Author and title fields rewritten;
  bibkey kept stable.

---

## Fifth-pass log (2026-05-07)

The fifth pass advanced 19 further sources from `lit-retrieved` to
`ai-confirmed` by fetching publisher abstract pages, arXiv records,
ACL Anthology pages, and one open-access PDF (the JSTOR-hosted Clark
& Chalmers 1998 *Analysis* preprint). The agent reading these sources
is `claude-opus-4-7[1m]` operating under the source-analyzer prompt;
direct `WebFetch` returned 403 Forbidden at every publisher domain in
this pass, so all retrievals went through the Exa `web_fetch` MCP
tool, with two assists from `web_search_exa` for the two Oxford
Academic landing pages that returned `SOURCE_NOT_AVAILABLE` to Exa
itself (Clark & Chalmers 1998; Kuteeva & Andersson 2024 - the latter
abstract was captured verbatim from the author's official Stockholm
University faculty page). All three previously-escalated sources
(`vannoorden2023chatgpt`, `neurips_llm_policy`, `iclr_llm_policy`)
remain at `lit-retrieved`; this pass did not retry them. After the
fifth pass, the queue contains zero sources at `lit-retrieved` outside
the institutional-access escalation list. The promoted sources are
listed below with their quoted snippets and the section of the
manuscript each one underwrites.

### `clarke2009modelchecking` --- ai-confirmed

- **Quoted snippet (verbatim from the *Communications of the ACM*
  Vol 52 No 11 abstract, ACM DL).**
  "The progression of model checking to the point where it can be
  successfully used for complex systems has required the development
  of sophisticated means of coping with what is known as the state
  explosion problem. ... Model checking tools, created by both
  academic and industrial teams, have resulted in an entirely novel
  approach to verification and test case generation."
- **Used in.** `position.tex` / §11 (the formal-methods-cousin
  claim).

### `klein2009sel4` --- ai-confirmed

- **Quoted snippet (verbatim from the SOSP 2009 abstract, ACM DL).**
  "We present our experience in performing the formal,
  machine-checked verification of the seL4 microkernel from an
  abstract specification down to its C implementation. ... To our
  knowledge, this is the first formal proof of functional correctness
  of a complete, general-purpose operating-system kernel."
- **Used in.** `position.tex` / §11 (proof-checker / artefact-discipline
  precedent alongside `clarke2009modelchecking`).

### `alemohammad2023mad` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv:2307.01850 abstract).**
  "Our primary conclusion across all scenarios is that without enough
  fresh real data in each generation of an autophagous loop, future
  generative models are doomed to have their quality (precision) or
  diversity (recall) progressively decrease. We term this condition
  Model Autophagy Disorder (MAD), making analogy to mad cow disease."
- **Used in.** `failure-modes.tex` (model-collapse row, alongside
  `shumailov2024collapse`).

### `shumailov2024collapse` --- ai-confirmed

- **Quoted snippet (verbatim from the *Nature* 631:755--759
  abstract).**
  "We find that indiscriminate use of model-generated content in
  training causes irreversible defects in the resulting models, in
  which tails of the original content distribution disappear. We
  refer to this effect as 'model collapse' and show that it can occur
  in LLMs as well as in variational autoencoders (VAEs) and Gaussian
  mixture models (GMMs)."
- **Used in.** `failure-modes.tex` (model-collapse row).

### `chen2023drift` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv:2307.09009 abstract).**
  "GPT-4 (March 2023) was reasonable at identifying prime vs.
  composite numbers (84% accuracy) but GPT-4 (June 2023) was poor on
  these same questions (51% accuracy). ... Overall, our findings show
  that the behavior of the 'same' LLM service can change substantially
  in a relatively short amount of time."
- **Used in.** `sustainability.tex` (frontier-model-dependence
  paragraph).

### `luccioni2024power` --- ai-confirmed

- **Quoted snippet (verbatim from the FAccT 2024 / arXiv:2311.16863
  abstract).**
  "We measure deployment cost as the amount of energy and carbon
  required to perform 1,000 inferences on representative benchmark
  dataset using these models. We find that multi-purpose, generative
  architectures are orders of magnitude more expensive than
  task-specific systems for a variety of tasks, even when controlling
  for the number of model parameters."
- **Used in.** `sustainability.tex` (inference-cost anchor).

### `patterson2021carbon` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv:2104.10350 abstract).**
  "We calculate the energy use and carbon footprint of several recent
  large models---T5, Meena, GShard, Switch Transformer, and GPT-3---and
  refine earlier estimates for the neural architecture search that
  found Evolved Transformer. ... Remarkably, the choice of DNN,
  datacenter, and processor can reduce the carbon footprint up to
  ~100--1000X."
- **Used in.** `sustainability.tex` (training-time carbon footprint,
  alongside `strubell2019energy`).

### `strubell2019energy` --- ai-confirmed

- **Quoted snippet (verbatim from the ACL 2019 / Anthology P19-1355
  abstract).**
  "These accuracy improvements depend on the availability of
  exceptionally large computational resources that necessitate
  similarly substantial energy consumption. As a result these models
  are costly to train and develop, both financially, due to the cost
  of hardware and electricity or cloud compute time, and
  environmentally, due to the carbon footprint required to fuel
  modern tensor processing hardware."
- **Used in.** `sustainability.tex` (training-side energy cost
  paragraph).

### `li2023thirsty` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv:2304.03271 abstract;
  later published as *Communications of the ACM* DOI
  10.1145/3724499).**
  "Training the GPT-3 language model in Microsoft's state-of-the-art
  U.S. data centers can directly evaporate 700,000 liters of clean
  freshwater, but such information has been kept a secret. More
  critically, the global AI demand is projected to account for
  4.2--6.6 billion cubic meters of water withdrawal in 2027."
- **Used in.** `sustainability.tex` (water-footprint half of the
  resource-cost paragraph).

### `birhane2022values` --- ai-confirmed

- **Quoted snippet (verbatim from the FAccT 2022 abstract).**
  "We find that few of the papers justify how their project connects
  to a societal need (15%) and far fewer discuss negative potential
  (1%). ... Notably, we find systematic textual evidence that these
  top values are being defined and applied with assumptions and
  implications generally supporting the centralization of power.
  Finally, we find increasingly close ties between these highly cited
  papers and tech companies and elite universities."
- **Used in.** `sustainability.tex` (equity / industry-capture
  paragraph).

### `thorp2023chatgpt` --- ai-confirmed

- **Quoted snippet (verbatim from the *Science* editorial 379:313).**
  "We are now updating our license and Editorial Policies to specify
  that text generated by ChatGPT (or any other AI tools) cannot be
  used in the work, nor can figures, images, or graphics be the
  products of such tools. And an AI program cannot be an author. A
  violation of these policies will constitute scientific misconduct
  no different from altered images or plagiarism of existing works."
- **Used in.** `intro.tex` (alongside `else2023chatgpt` as the
  *Science* counterpart to the *Nature* editorial).

### `sadasivan2023reliably` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv:2303.11156 abstract via
  Semantic Scholar / arXiv mirror; also visible in the appendix
  proof of Theorem 1).**
  "We introduce recursive paraphrasing attack to stress test a wide
  range of detection schemes, including the ones using the
  watermarking as well as neural network-based detectors, zero shot
  classifiers, and retrieval-based detectors. ... Finally, we provide
  a theoretical framework connecting the AUROC of the best possible
  detector to the Total Variation distance between human and AI text
  distributions."
- **Used in.** `failure-modes.tex` (residual-detection /
  paraphrase-attack row).

### `reynolds2021prompt` --- ai-confirmed

- **Quoted snippet (verbatim from the CHI EA 2021 abstract).**
  "Using GPT-3 as a case study, we show that 0-shot prompts can
  significantly outperform few-shot prompts. ... Informed by this
  more encompassing theory of prompt programming, we also introduce
  the idea of a metaprompt that seeds the model to generate its own
  natural language prompts for a range of tasks."
- **Used in.** `evolution.tex` (prompt-craft-as-programming-cousin
  observation).

### `liu2023prompt` --- ai-confirmed

- **Quoted snippet (verbatim from the *ACM Computing Surveys* 55:9
  abstract).**
  "This article surveys and organizes research works in a new
  paradigm in natural language processing, which we dub
  'prompt-based learning.' ... It allows the language model to be
  pre-trained on massive amounts of raw text, and by defining a new
  prompting function the model is able to perform few-shot or even
  zero-shot learning, adapting to new scenarios with few or no
  labeled data."
- **Used in.** `evolution.tex` (prompt-engineering-as-discipline
  anchor alongside `reynolds2021prompt`).

### `anderson2024homogenization` --- ai-confirmed

- **Quoted snippet (verbatim from the ACM C&C 2024 abstract).**
  "We conducted a 36-participant comparative user study and found,
  in accordance with the homogenization hypothesis, that different
  users tended to produce less semantically distinct ideas with
  ChatGPT than with an alternative CST. Additionally, ChatGPT users
  generated a greater number of more detailed ideas, but felt less
  responsible for the ideas they generated."
- **Used in.** `authors-note.tex` / `objections.tex` (cultural-blender
  pole of the coupling rule).

### `kuteeva2024diversity` --- ai-confirmed

- **Quoted snippet (verbatim from the *Applied Linguistics* 45(3)
  abstract; mirror at the author's Stockholm University faculty page,
  https://su.se/english/profiles/mkute, retrieved 2026-05-07; the
  Oxford Academic landing page was not reachable to Exa).**
  "While artificial intelligence-supported large language models
  (LLMs) can help with access to knowledge generated in the Global
  North and demystify publication practices, they are still biased
  toward dominant norms and knowledge paradigms. ... Thus, LLMs are
  likely to drive both language use and knowledge construction
  towards homogeneity and uniformity, reproducing already existing
  biases and structural inequalities."
- **Used in.** `evolution.tex` (paper-driven-disciplines
  exception / humanities critique of LLM writing assistance).

### `clark1998extended` --- ai-confirmed

- **Quoted snippet (verbatim from the open JSTOR-hosted PDF of
  *Analysis* 58.1, pp. 7--19, 1998).**
  "We propose to pursue a third position. We advocate a very
  different sort of externalism: an active externalism, based on the
  active role of the environment in driving cognitive processes. ...
  Epistemic action, we suggest, demands spread of epistemic credit.
  If, as we confront some task, a part of the world functions as a
  process which, were it done in the head, we would have no
  hesitation in recognizing as part of the cognitive process, then
  that part of the world is (so we claim) part of the cognitive
  process."
- **Used in.** `authors-note.tex` (philosophical precedent for the
  human-LLM partition; the Otto-and-Inga thought experiment is the
  canonical anchor).

### `clark2025extending` --- ai-confirmed

- **Citation completion.** Confirmed at *Nature Communications*
  16:4627 (2025), DOI 10.1038/s41467-025-59906-9, published
  19 May 2025. The current bib entry (`clark2025extending`) carries
  no DOI; this DOI should be added on the next bib pass.
- **Quoted snippet (verbatim from the *Nature Communications* 2025
  open-access article).**
  "As human-AI collaborations become the norm, we should remind
  ourselves that it is our basic nature to build hybrid thinking
  systems --- ones that fluidly incorporate non-biological resources.
  Recognizing this invites us to change the way we think about both
  the threats and promises of the coming age."
- **Used in.** `authors-note.tex` (live anchor for the
  accelerator-or-blender coupling rule, as the 27-years-later
  restatement of `clark1998extended`).

### `hutchins1995cognition` --- ai-confirmed

- **Quoted snippet (verbatim from the MIT Press publisher description
  of *Cognition in the Wild*, ISBN 9780262581462, retrieved
  2026-05-07).**
  "Hutchins examines a set of phenomena that have fallen in the
  cracks between the established disciplines of psychology and
  anthropology, bringing to light a new set of relationships between
  culture and cognition. ... Hutchins argues instead that cultural
  activity systems have cognitive properties of their own that are
  different from the cognitive properties of the individuals who
  participate in them."
- **Used in.** `authors-note.tex` (distributed-cognition canonical,
  alongside `clark1998extended`).
- **Note for `references.bib`.** The MIT Press paperback record
  shows publication 26 August 1996 (paperback) following hardcover
  10 February 1995. The current bib entry uses `year = {1995}`,
  which matches the original hardcover and is therefore correct;
  flagged here only for completeness.

### Items the fifth pass did **not** advance

The three previously-escalated paywalled / login-walled sources
(`vannoorden2023chatgpt`, `neurips_llm_policy`, `iclr_llm_policy`)
remain at `lit-retrieved` per the existing entries in
`doc/sources-needing-institutional-access.md`. No new escalations
were added in this pass.

### Bib corrections flagged in the fifth pass

1. **`clark2025extending`** --- the current `references.bib` entry
   has no `doi` and no `volume`/`pages`. The canonical record is
   *Nature Communications* 16, Article 4627 (2025), DOI
   10.1038/s41467-025-59906-9, published 19 May 2025. Recommend
   adding `doi = {10.1038/s41467-025-59906-9}`, `volume = {16}`,
   `pages = {4627}` on the next bib pass.
2. **`kuteeva2024diversity`** --- the canonical citation is
   *Applied Linguistics* 45(3), 561--567, 2024. The bib entry
   currently has no `volume`, `number`, or `pages`. Recommend
   filling those in.
3. **`liu2023prompt`** --- pages should be confirmed. *ACM Computing
   Surveys* 55(9), Article 195 (paginated 1--35) is the canonical
   citation; the current bib's `pages = {1--35}` is consistent but
   the article number `195` is missing.
4. **`li2023thirsty`** --- the bib mixes the arXiv preprint and the
   2025 CACM final version, which is acceptable given the bibkey
   stability rule, but the title should be updated to reflect the
   final published version (CACM 2025) when the human author next
   touches the entry.

## Fourth-pass log (2026-05-07)

The fourth pass advanced 16 sources from `lit-retrieved` to
`ai-confirmed` by fetching the publisher landing pages or arXiv abstract
pages and extracting verbatim load-bearing snippets. The agent reading
these sources is `claude-opus-4-7[1m]` operating under the
source-analyzer prompt; full text was retrieved through the Exa
`web_fetch` MCP tool because direct WebFetch was blocked at most
publishers. The promoted sources are listed below with their quoted
snippets and the section of the manuscript each one underwrites.

### `walters2023fabrication` --- ai-confirmed

- **Quoted snippet (verbatim from the *Scientific Reports* abstract).**
  "Within this set of documents, 55% of the GPT-3.5 citations but
  just 18% of the GPT-4 citations are fabricated. Likewise, 43% of
  the real (non-fabricated) GPT-3.5 citations but just 24% of the
  real GPT-4 citations include substantive citation errors."
- **Used in.** `intro.tex` (line 23, base-rate anchor for the 18--55%
  fabrication band) and `failure-modes.tex` (line 20, the
  fabrication row of the failure-mode table).

### `magesh2024legal` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv 2405.20362 abstract).**
  "We find that the AI research tools made by LexisNexis (Lexis+
  AI) and Thomson Reuters (Westlaw AI-Assisted Research and Ask
  Practical Law AI) each hallucinate between 17% and 33% of the
  time."
- **Used in.** `intro.tex` (the 17--34% RAG-backed range alongside
  walters2023fabrication) and `failure-modes.tex` (RAG-related
  failure-mode row).

### `ashburner2000go` --- ai-confirmed

- **Quoted snippet (verbatim from the *Nature Genetics* abstract via
  PubMed PMID 10802651).**
  "The goal of the Gene Ontology Consortium is to produce a
  dynamic, controlled vocabulary that can be applied to all
  eukaryotes even as knowledge of gene and protein roles in cells
  is accumulating and changing."
- **Used in.** `pattern.tex` §3.6 (bioinformatics-precedent claim)
  and `conclusion.tex` (the longer-arc paragraph).

### `liang2024mapping` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv 2404.01268 abstract).**
  "Our findings reveal a steady increase in LLM usage, with the
  largest and fastest growth observed in Computer Science papers
  (up to 17.5%). In comparison, Mathematics papers and the Nature
  portfolio showed the least LLM modification (up to 6.3%)."
- **Used in.** `intro.tex` (volume-problem anchor for the rising
  LLM-modified-prose fraction).

### `kobak2024delving` --- ai-confirmed

- **Quoted snippet (verbatim from the arXiv 2406.07016 abstract).**
  "We study vocabulary changes in over 15 million biomedical
  abstracts from 2010--2024 indexed by PubMed, and show how the
  appearance of LLMs led to an abrupt increase in the frequency of
  certain style words. This excess word analysis suggests that at
  least 13.5% of 2024 abstracts were processed with LLMs."
- **Used in.** `intro.tex` (the cross-discipline detection-symptom
  anchor).
- **Note for `references.bib`.** The arXiv title has been revised
  to "Delving into LLM-assisted writing in biomedical publications
  through excess vocabulary"; the bib currently records the
  earlier title "Delving into ChatGPT usage in academic writing
  through excess vocabulary". The lower-bound figure is **13.5%**,
  not the **~10%** reported in the second-pass log; flagged for
  the human author.

### `ioannidis2005` --- ai-confirmed

- **Quoted snippet (verbatim from the *PLOS Medicine* abstract).**
  "Simulations show that for most study designs and settings, it
  is more likely for a research claim to be false than true.
  Moreover, for many current scientific fields, claimed research
  findings may often be simply accurate measures of the prevailing
  bias."
- **Used in.** `intro.tex` (reproducibility-baseline-poor claim).

### `pineau2021reproducibility` --- ai-confirmed

- **Quoted snippet (verbatim from the JMLR 22:164 abstract).**
  "In 2019, the Neural Information Processing Systems (NeurIPS)
  conference, the premier international conference for research in
  machine learning, introduced a reproducibility program, designed
  to improve the standards across the community for how we
  conduct, communicate, and evaluate machine learning research."
- **Used in.** `intro.tex` (ML-specific reproducibility anchor
  alongside `ioannidis2005`).

### `aclrr_llm_policy` --- ai-confirmed

- **Quoted snippet (verbatim from the ACL Rolling Review CFP).**
  "Generally, generative AI tools do not qualify for authorship.
  Their use for writing or coding, as well as its scope, must be
  disclosed in the Responsible NLP Checklist. Details should be
  included in the Acknowledgements section."
- **Used in.** `background.tex` (reviewer-side AI-policies claim).

### `eisen2018preprints` --- ai-confirmed

- **Citation correction (year and title).** The eLife editorial
  was published 2020 (not 2018) and is titled "Peer Review:
  Implementing a 'publish, then review' model of publishing"; DOI
  10.7554/eLife.64910. The bib entry records year 2018; flagged for
  the human author.
- **Quoted snippet (verbatim from the editorial).**
  "We welcome this moment, and the long-awaited opportunity it
  provides to replace the traditional 'review, then publish' model
  developed in the age of the printing press with a 'publish, then
  review' model optimized for the age of the internet."
- **Used in.** `intro.tex` (journal-as-distribution-in-decline
  claim).

### `tennant2016open` --- ai-confirmed

- **Quoted snippet (verbatim from the *F1000Research* abstract).**
  "Open Access supersedes all potential alternative modes of
  access to the scholarly literature through enabling unrestricted
  re-use, and long-term stability independent of financial
  constraints of traditional publishers that impede knowledge
  sharing."
- **Used in.** `intro.tex` (background for the
  journal-as-distribution-in-decline claim).

### `conroy2023sleuths` --- ai-confirmed

- **Quoted snippet (verbatim from the *Nature* news lead).**
  "On 9 August, the journal Physica Scripta published a paper that
  aimed to uncover new solutions to a complex mathematical
  equation. It seemed genuine, but scientific sleuth Guillaume
  Cabanac spotted an odd phrase on the manuscript's third page:
  'Regenerate response'."
- **Used in.** `intro.tex` (evidence for the
  AI-fabricated-submissions volume problem). Full body of the
  Nature news article is paywalled; the lead quoted here is the
  detection example the manuscript leans on, so the abstract is
  sufficient at the `ai-confirmed` rung.

### `curdt2025hmc` --- ai-confirmed

- **Quoted snippet (verbatim from the Zenodo 15113717 abstract).**
  "The Helmholtz Metadata Collaboration (HMC), initiated in 2019
  by the Helmholtz Association of German Research Centres, is
  dedicated to advancing research data management by translating
  global metadata standards into practical, interoperable formats."
- **Used in.** `pattern.tex` §3.6 (the Helmholtz cross-centre
  graph as the proximate example of a future-research-infrastructure)
  and the imprint / acknowledgements.
- **Citation note.** The Zenodo record's primary author is **Curdt,
  Constanze** (project leader); contributors include
  Trösch (project member), Lorenz, Lemster, Heel and Köstner.
  The current bib lists Curdt and Köstner; the human author may
  wish to widen the author list when next editing `references.bib`.

### `schmitt2020nfdi4ing` --- ai-confirmed

- **Quoted snippet (verbatim from the Zenodo 4015201 abstract).**
  "NFDI4Ing brings together the engineering communities and
  fosters the management of engineering research data. ... So far,
  seven archetypes are harmonising the methodological needs:
  Alex, Betty, Caden, Doris, Ellen, Frank, Golo."
- **Used in.** `pattern.tex` §3.6 / imprint context (institutional
  FAIR-context anchor alongside `curdt2025hmc`).

### `janowicz2019sosa` --- ai-confirmed

- **Quoted snippet (verbatim from the *Journal of Web Semantics*
  abstract; published Vol 56, May 2019, pp. 1--10).**
  "The Sensor, Observation, Sample, and Actuator (SOSA) ontology
  provides a formal but lightweight general-purpose specification
  for modelling the interaction between the entities involved in
  the acts of observation, actuation, and sampling."
- **Used in.** `pattern.tex` §3.5 (domain-ontologies-extension claim).
- **Citation note.** Although Elsevier records the article in
  Vol 56 (May 2019), the underlying DOI 10.1016/j.websem.2018.06.003
  carries a 2018 in-press date; the bib year of 2019 is correct.

### `rijgersberg2013om` --- ai-confirmed

- **Quoted snippet (verbatim from the *Semantic Web* journal
  abstract; Vol 4, no. 1, pp. 3--13, 2013).**
  "This paper describes the Ontology of units of Measure and
  related concepts (OM), an OWL ontology of the domain of
  quantities and units of measure. OM supports making quantitative
  research data more explicit, so that the data can be integrated,
  verified and reproduced."
- **Used in.** `pattern.tex` §3.5 (domain-ontologies-extension claim).

### `qudt` --- ai-confirmed

- **Quoted snippet (verbatim from <https://www.qudt.org/>, retrieved
  2026-05-07).**
  "QUDT.org is a 501(c)(3) public charity nonprofit organization
  founded to provide semantic specifications for units of measure,
  quantity kind, dimensions and data types. ... Our mission is to
  improve interoperability of data and the specification of
  information structures through industry standards for Units of
  Measure, Quantity Kinds, Dimensions and Data Types."
- **Used in.** `pattern.tex` §3.5 (domain-ontologies-extension claim).

### `wilkinson2016fair` --- ai-confirmed (newly assigned a rung)

- **Quoted snippet (verbatim from *Scientific Data* 3:160018,
  2016).**
  "This article describes four foundational principles ---
  Findability, Accessibility, Interoperability, and Reusability
  --- that serve to guide data producers and publishers as they
  navigate around these obstacles, thereby helping to maximize
  the added-value gained by contemporary, formal scholarly
  digital publishing."
- **Used in.** `intro.tex`, `background.tex`, `related.tex` (the
  substrate F(AI)²R extends).
- **Note.** This source previously carried no
  `fair2r:verificationState` triple in `provenance.ttl`; the
  fourth pass adds one at `ai-confirmed`.

### Items the fourth pass did **not** advance

- **`vannoorden2023chatgpt`** --- the *Nature* news page is
  accessible only as a citation block ("Nature 624, 509 (2023)
  doi:10.1038/d41586-023-03930-6") with the body paywalled. The
  bib's existing identifier (`d41586-023-03907-5`) resolves to a
  different article ("Where science meets Indian economics: in
  five charts"). The DOI defect was already flagged in the
  second-pass log; until the bib is corrected, the entry stays
  at `lit-retrieved` and a `pending` paywall request is added to
  `doc/sources-needing-institutional-access.md`.
- **`neurips_llm_policy`** and **`iclr_llm_policy`** --- the
  conference homepages return only navigational chrome at the
  current year (NeurIPS 2026, ICLR 2026); the actual policy text
  for the relevant submission cycle was not on the path the URL
  resolves to and the abstract is therefore insufficient. Both
  remain at `lit-retrieved` and a `pending` request is filed in
  `doc/sources-needing-institutional-access.md` so the human
  author can capture the canonical year-specific policy URL.



## Third-pass log (2026-05-06)

The third pass added eleven new `lit-retrieved` entries to back the
position-paper extensions (`paper/sections/position.tex`,
`paper/sections/objections.tex`), the field-notes block in
`paper/sections/evolution.tex`, the accelerator-or-blender coupling
rule in `paper/sections/authors-note.tex`, and the institutional
FAIR-context citations in the imprint:

- `clark1998extended` --- Clark & Chalmers, *Analysis* 58:7--19, the
  canonical Extended-Mind paper. 5300+ citations confirmed.
- `hutchins1995cognition` --- Hutchins, *Cognition in the Wild*, MIT
  Press 1995. ISBN 9780262581462. The distributed-cognition canonical.
- `clark2025extending` --- Clark, "Extending Minds with Generative
  AI," *Nature Communications* 2025. The 27-years-later restatement
  under generative-AI conditions; DOI not yet captured (deferred to
  lit-read rung).
- `anderson2024homogenization` --- Anderson, Shah, Kreminski, ACM
  C&C 2024, DOI 10.1145/3635636.3656204. Empirical homogenisation
  evidence (the "cultural blender" pole).
- `kuteeva2024diversity` --- Kuteeva & Andersson, *Applied
  Linguistics* 2024, DOI 10.1093/applin/amae025. Humanities /
  applied-linguistics critique of LLM writing assistance --- the
  paper-driven-disciplines exception named in `evolution.tex`.
- `reynolds2021prompt` --- Reynolds & McDonell, CHI '21 Extended
  Abstracts, DOI 10.1145/3411763.3451760. Canonical
  prompt-as-programming source.
- `liu2023prompt` --- Liu et al., *ACM Computing Surveys* 55:9, DOI
  10.1145/3560815. The four-thousand-citation prompt-survey.
- `sadasivan2023reliably` --- promoted from "proposed addition"
  (already in `doc/sources.md`) to a real bib entry. Backs the
  detection-impossibility claim in `failure-modes.tex`.
- `curdt2025hmc` --- HMC 2025 position paper, Zenodo
  10.5281/zenodo.15113717. Replaces the bare URL the imprint
  previously carried.
- `schmitt2020nfdi4ing` --- NFDI4Ing foundational document, Zenodo
  10.5281/zenodo.4015201. Same role as `curdt2025hmc`.

The eleven new entries are all `lit-retrieved`. Six (`reynolds2021prompt`,
`liu2023prompt`, `anderson2024homogenization`, `kuteeva2024diversity`,
`sadasivan2023reliably`, `clark1998extended`) have published DOIs that
resolve and were confirmed via Consensus search; three
(`hutchins1995cognition`, `curdt2025hmc`, `schmitt2020nfdi4ing`) carry
ISBN or Zenodo identifiers verified via web search; one
(`clark2025extending`) is identifier-confirmed by a Consensus hit but
the DOI was not captured at the search depth used --- the bib entry
notes this and the human author should resolve the DOI before
condensation. None has been read in full by the human author.

The third pass also ran a context-data audit (orphan IRIs, dangling
cites, section-graph mismatches, unactioned `Next:` todos in
`logbook.md`); findings are reported in the assistant message that
accompanies this commit. Three section-graph mismatches were found:
the `provenance.ttl` graph still has `ent:section-discussion` even
though `discussion.tex` was retired in the position-paper reframing,
and the new sections `position`, `objections`, `authors-note`, and
`statement-of-authorship` exist as `.tex` files without
corresponding `fair2r:Section` entities. These are flagged for the
provenance-curator to resolve in a follow-up commit.

## Second-pass log (2026-05-06)

## Second-pass log (2026-05-06)

The second pass focused on completion rather than re-verification:
identifier-confirmation of the six lit-retrieved entries, and discovery
of canonical references for the previously-uncited claims in
`sustainability.tex`, `intro.tex`, `failure-modes.tex`, and
`background.tex`. New entries (all `lit-retrieved`) added to
`references.bib`:

- `luccioni2024power` — inference-side energy cost (FAccT 2024).
- `patterson2021carbon` — training-time carbon footprint (arXiv 2104.10350).
- `li2023thirsty` — water footprint of AI (arXiv 2304.03271).
- `strubell2019energy` — early NLP-energy analysis (ACL 2019).
- `birhane2022values` — equity / industry capture in ML research (FAccT 2022).
- `shumailov2024collapse` — model collapse on recursive data (Nature 631:755).
- `alemohammad2023mad` — Model Autophagy Disorder (arXiv 2307.01850).
- `chen2023drift` — empirical LLM behaviour drift over time (arXiv 2307.09009).
- `thorp2023chatgpt` — *Science* editorial that ChatGPT is not an author.
- `usco2023ai` — USCO 2023 Federal Register guidance.
- `urhg2` — German UrhG §2 statutory entry.

The six previously `lit-retrieved` entries (`walters2023fabrication`,
`magesh2024legal`, `liang2024mapping`, `kobak2024delving`,
`ravi2024fair4ml`, `vannoorden2023chatgpt`) had identifier, title,
authors, and headline figures re-confirmed via search; abstracts already
read by an AI agent in the first pass. None has yet been read in full
by the human author, so all remain at `lit-retrieved` rather than
advancing to `lit-read`.

## Verification ladder (per `doc/methodology.md`)

A `fair2r:Claim` (and the source backing it) carries one of:

| state | meaning |
|---|---|
| `unverified`        | Asserted but no evidence yet attached. |
| `needs-research`    | Evidence-gap acknowledged; search planned. |
| `lit-retrieved`     | Identifier (DOI / arXiv / stable URL) resolves; title and authors confirmed; the abstract has been read by an AI agent. |
| `ai-confirmed`      | An AI agent has read a vendored or fetched copy of the source and confirmed the inference made from it. |
| `lit-read`          | A human author has read the source itself and confirmed the inference. |
| `source-vendored`   | The source itself is vendored under `doc/sources/<bibkey>/`. |
| `unverifiable`      | Searches have not located a canonical record; the citation cannot be defended. |

Per the methodology, a claim must reach `lit-read` (or `source-vendored`)
before it can appear in the condensed manuscript. `ai-confirmed` is the
ceiling an LLM agent can deliver on its own.

## Conventions

- Open-licensed sources are vendored under `doc/sources/<bibkey>/` so the
  evidence travels with the repo.
- Closed-licensed sources are referenced by DOI only and noted as `paywalled`.
- Each entry mirrors one BibTeX key in `paper/references.bib`.
- "How the paper uses it" describes the load-bearing function in
  `paper/sections/*.tex`. If we drift from that function during revision,
  the entry must be revisited.

---

## 1. The FAIR family

### `wilkinson2016fair`

- **Citation.** Wilkinson, M. D., Dumontier, M., Aalbersberg, IJ. J., et al.
  (2016). "The FAIR Guiding Principles for scientific data management and
  stewardship." *Scientific Data* 3, 160018.
  DOI: [10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18).
- **What it says.** Defines the four FAIR principles (Findable, Accessible,
  Interoperable, Reusable) and their fifteen sub-principles (F1–F4, A1–A2,
  I1–I3, R1.1–R1.3) as a guideline set for scientific data management.
- **How the paper uses it.** Cited as the substrate that F(AI)²R extends;
  the fifteen sub-principles are the cells the F(AI)²R mapping (Appendix C)
  populates. Used in `intro.tex`, `background.tex`, `related.tex`.
- **Verification.** `lit-read` — open access, canonical, well-known to the
  human author.

### `chuehong2022fair4rs`

- **Citation.** Chue Hong, N. P., Katz, D. S., Barker, M., Lamprecht, A.-L.,
  Martinez, C., et al. (2022). "FAIR Principles for Research Software
  (FAIR4RS Principles)." *Research Data Alliance* — RDA Recommendation.
  DOI: [10.15497/RDA00068](https://doi.org/10.15497/RDA00068).
- **What it says.** Re-reads the fifteen FAIR sub-principles for research
  software. Picks up versioning, dependencies, and build-time
  reproducibility as first-class concerns. Released June 2022 after roughly
  two years of community consultation as a joint RDA / FORCE11 / ReSA
  recommendation.
- **How the paper uses it.** Cited as the first prior FAIR re-reading and
  as the precedent that F(AI)²R follows in form. Used in `intro.tex`,
  `background.tex`, `related.tex`.
- **Verification.** `lit-read` — DOI resolves, RDA has the canonical record.

### `ravi2024fair4ml`

- **Citation (proposed).** Castro, L. J., Garijo, D., et al. (2024).
  *FAIR4ML-schema*, version 0.1.0. RDA FAIR4ML Working Group / Task Force.
  Zenodo. DOI: [10.5281/zenodo.14002310](https://doi.org/10.5281/zenodo.14002310).
  Vocabulary: <https://w3id.org/fair4ml/>.
- **What it says.** A schema.org extension defining `fair4ml:MLModel` and
  `fair4ml:MLModelEvaluation` for machine-readable representations of
  trained ML models, reusing properties from CodeMeta to point to the model
  code. Output of the RDA FAIR for Machine Learning Interest Group.
- **How the paper uses it.** Cited as the second prior FAIR re-reading
  (FAIR for ML models) that F(AI)²R follows in form. Used in `intro.tex`,
  `background.tex`, `related.tex`.
- **Verification status.** `lit-retrieved`. The current bib entry has
  `author = {TODO-VERIFY}` and the bibkey suggests an author "Ravi" who is
  **not** the canonical FAIR4ML author. The canonical artefact is the
  Castro–Garijo schema (Zenodo 14002310). The bibkey should probably
  remain as-is for stability, but the entry should be filled in with
  Castro et al. as authors. The human author must read the schema before
  this can move to `lit-read`.

---

## 2. Provenance and reproducibility methodology

### `w3c2013provo`

- **Citation.** Lebo, T., Sahoo, S., McGuinness, D., et al. (2013).
  *PROV-O: The PROV Ontology*. W3C Recommendation, 30 April 2013.
  URL: <https://www.w3.org/TR/prov-o/>.
- **What it says.** OWL2 ontology defining `prov:Entity`, `prov:Activity`,
  `prov:Agent`, and the relations (`prov:wasGeneratedBy`,
  `prov:wasAttributedTo`, `prov:wasDerivedFrom`, `prov:hadPlan`, etc.)
  that F(AI)²R uses verbatim.
- **How the paper uses it.** Substrate for the `fair2r:` namespace. Cited
  in `background.tex` and `related.tex`. Vendored implicitly via the W3C
  stable URI, which we treat as permanent.
- **Verification.** `lit-read` — W3C Recommendation, stable URL.

### `page2021prisma`

- **Citation.** Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I.,
  Hoffmann, T. C., Mulrow, C. D., et al. (2021). "The PRISMA 2020
  statement: an updated guideline for reporting systematic reviews."
  *BMJ* 372, n71.
  DOI: [10.1136/bmj.n71](https://doi.org/10.1136/bmj.n71).
- **What it says.** Updated reporting guideline for systematic reviews,
  successor to PRISMA 2009. Provides a flow-diagram template
  (Identification → Screening → Included) and a 27-item checklist.
- **How the paper uses it.** The retrieval-depth axis the verification
  ladder borrows from. Used in `background.tex`, `related.tex`. We treat
  PRISMA's flow as the lower bound a rung permits ("retrieved" as
  opposed to "read").
- **Verification.** `lit-read` — open access at BMJ.

### `guyatt2008grade`

- **Citation.** Guyatt, G. H., Oxman, A. D., Vist, G. E., Kunz, R.,
  Falck-Ytter, Y., Alonso-Coello, P., Schünemann, H. J. (2008).
  "GRADE: an emerging consensus on rating quality of evidence and strength
  of recommendations." *BMJ* 336(7650), 924–926.
  DOI: [10.1136/bmj.39489.470347.AD](https://doi.org/10.1136/bmj.39489.470347.AD).
- **What it says.** Introduces the four-level GRADE rating (very low, low,
  moderate, high) for the quality of evidence and the strength of
  recommendations derived from it.
- **How the paper uses it.** The invocation-strength axis the verification
  ladder borrows from. Used in `background.tex`, `related.tex`. Cited as
  the rating dimension that complements PRISMA's retrieval dimension.
- **Verification.** `lit-read` — open access, PMC2335261.

---

## 3. Documentation patterns for ML artefacts

### `gebru2021datasheets`

- **Citation.** Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W.,
  Wallach, H., Daumé III, H., Crawford, K. (2021). "Datasheets for
  datasets." *Communications of the ACM* 64(12), 86–92.
  DOI: [10.1145/3458723](https://doi.org/10.1145/3458723).
  arXiv: [1803.09010](https://arxiv.org/abs/1803.09010).
- **What it says.** Proposes a structured 57-question, seven-section
  datasheet (Motivation, Composition, Collection Process, Preprocessing,
  Uses, Distribution, Maintenance) to accompany every dataset, modelled on
  the electronic-component datasheet.
- **How the paper uses it.** Named as the canonical ancestor of structured
  human-readable documentation for ML artefacts; the per-prompt and
  per-claim documentation in F(AI)²R inherits its instinct that each
  artefact deserves its own datasheet-shaped record. Used in
  `background.tex`, `related.tex`.
- **Verification.** `lit-read` — both ACM and arXiv versions are open.

### `mitchell2019modelcards`

- **Citation.** Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L.,
  Hutchinson, B., Spitzer, E., Raji, I. D., Gebru, T. (2019). "Model Cards
  for Model Reporting." In *Proceedings of the Conference on Fairness,
  Accountability, and Transparency (FAT\* / FAccT '19)*, 220–229.
  DOI: [10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596).
  arXiv: [1810.03993](https://arxiv.org/abs/1810.03993).
- **What it says.** Recommends short structured documents accompanying
  every released ML model: intended use, performance benchmarks across
  demographic groups, evaluation conditions, ethical considerations.
  Worked examples for a smile detector and a toxic-comment classifier.
- **How the paper uses it.** Same role as `gebru2021datasheets` — second
  immediate ancestor of structured per-artefact documentation. Used in
  `background.tex`, `related.tex`.
- **Verification.** `lit-read` — open access at ACM and arXiv.

---

## 4. AI disclosure norms in venues

### `icmje2023`

- **Citation.** International Committee of Medical Journal Editors (2023,
  most recently revised January 2024). *Recommendations for the Conduct,
  Reporting, Editing, and Publication of Scholarly Work in Medical
  Journals*. URL: <https://www.icmje.org/recommendations/>. The AI-specific
  guidance is at
  <https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html>
  and the topic page
  <https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html>.
- **What it says.** Authors must disclose the use of AI-assisted tools at
  submission; chatbots cannot be authors because they cannot be held
  responsible for accuracy, integrity, or originality; AI use for writing
  assistance goes in the acknowledgements, AI use for data analysis or
  figures goes in the methods.
- **How the paper uses it.** The canonical disclosure-norm citation in
  `background.tex` and `related.tex`. Anchors the claim that "AI is not
  an author" is a community position, not a F(AI)²R invention.
- **Verification.** `lit-read` — public guidance, freely available.

---

## 5. LLM failure modes — fabrication, hallucination, drift

### `walters2023fabrication`

- **Citation.** Walters, W. H., Wilder, E. I. (2023). "Fabrication and
  errors in the bibliographic citations generated by ChatGPT." *Scientific
  Reports* 13, 14045.
  DOI: [10.1038/s41598-023-41032-5](https://doi.org/10.1038/s41598-023-41032-5).
  PubMed: 37679503.
- **What it says.** Examined 636 citations across 84 ChatGPT-generated
  literature reviews on 42 topics. **55% of GPT-3.5 citations and 18% of
  GPT-4 citations were fabricated**; of the real citations, 43% (GPT-3.5)
  and 24% (GPT-4) contained substantive errors.
- **How the paper uses it.** The lower bound (18%) of the "18–55%
  fabrication rate" sentence in `intro.tex` (line 23) and the citation
  beside the failure-mode table in `failure-modes.tex` (line 20). The 55%
  upper bound is also from this paper, *not* from `magesh2024legal`; the
  current `intro.tex` phrasing eliding the two is acceptable but should be
  flagged on revision.
- **Verification.** `ai-confirmed` (advanced 2026-05-07; verbatim
  abstract quote captured in the fourth-pass log above). Must still
  move to `lit-read` before condensation. Human author has not yet
  read the full PDF.

### `magesh2024legal`

- **Citation.** Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D.,
  Ho, D. E. (2024). "Hallucination-Free? Assessing the Reliability of
  Leading AI Legal Research Tools." Stanford RegLab and HAI, preprint.
  arXiv: [2405.20362](https://arxiv.org/abs/2405.20362).
  Final version: *Journal of Empirical Legal Studies* (2025), DOI
  [10.1111/jels.12413](https://doi.org/10.1111/jels.12413).
  Companion piece: *AI on Trial: Legal Models Hallucinate in 1 out of 6
  (or More) Benchmarking Queries* (Stanford HAI news, 2024),
  <https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries>.
- **What it says.** First preregistered empirical evaluation of
  RAG-backed legal research tools. **Lexis+ AI and Ask Practical Law AI
  hallucinated on more than 17% of queries; Westlaw AI-Assisted Research
  hallucinated on more than 34%.** The Stanford HAI summary frames this
  as 17–33% (or "1 in 6 or more"). Earlier general-purpose-model figures
  cited in the same line of work reach roughly 58–88%.
- **How the paper uses it.** The 55% upper bound in `intro.tex` line 23 is
  *not* directly from this paper; it is from `walters2023fabrication`.
  The number that should be associated with `magesh2024legal` is the
  17–34% RAG-backed range, or the 58–88% general-model range from the
  preceding Stanford "Large Legal Fictions" work
  ([Dahl et al. 2024, arXiv:2401.01301](https://arxiv.org/abs/2401.01301)).
  **The intro currently leaves this ambiguous and should be tightened.**
- **Verification.** `ai-confirmed` (advanced 2026-05-07; the arXiv
  abstract gives an explicit "between 17% and 33%" range, captured
  in the fourth-pass log above). arXiv ID and journal DOI both
  resolve. Human author must still read the preprint to commit to
  a specific upper-bound figure for `intro.tex`.

### `bender2021stochastic`

- **Citation.** Bender, E. M., Gebru, T., McMillan-Major, A., Shmitchell, S.
  (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be
  Too Big?🦜" In *Proceedings of the 2021 ACM Conference on Fairness,
  Accountability, and Transparency (FAccT '21)*, 610–623.
  DOI: [10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922).
- **What it says.** Names large language models as systems that
  "haphazardly stitch together sequences of linguistic forms … without
  any reference to meaning"; surveys environmental, financial, and
  representational risks; argues for documentation, dataset curation,
  and direction-shifts away from ever-larger models.
- **How the paper uses it.** Cited in `related.tex` as the source of much
  of the vocabulary the disclosure literature uses (stochastic-parrot,
  meaning-form distinction, documentation as mitigation).
- **Verification.** `lit-read` — open access at ACM, widely vendored.

### `else2023chatgpt`

- **Citation.** Else, H. (2023). "Tools such as ChatGPT threaten transparent
  science — here are our ground rules for their use." *Nature* 613, 612.
  DOI: [10.1038/d41586-023-00191-1](https://doi.org/10.1038/d41586-023-00191-1).
  PubMed: 36694020.
- **What it says.** Nature editorial that LLMs cannot be authors, that
  use of LLM tools must be documented in methods or acknowledgements,
  and that publishers must lay down clear guidelines.
- **How the paper uses it.** `intro.tex` line 36 — the "editors at major
  venues asked for provenance from authors instead of post-hoc detection
  against them" sentence. The editorial argues for exactly that posture.
- **Verification.** `lit-read` — open at Nature.

### `vannoorden2023chatgpt`

- **Citation.** Van Noorden, R., Webb, R. (2023). "ChatGPT and science:
  the AI system was a force in 2023 — for good and bad." *Nature*
  624(7992), 509.
  DOI: [10.1038/d41586-023-03930-6](https://doi.org/10.1038/d41586-023-03930-6).
  PubMed: 38093061.
- **What it says.** End-of-year overview of AI's impact on the scientific
  ecosystem in 2023: rising LLM-assisted submissions, paper-mill
  exposure, retraction record, journal policy responses.
- **How the paper uses it.** Backdrop reference in `intro.tex` line 30
  (alongside `liang2024mapping`) for the volume-problem claim.
- **Verification.** `lit-retrieved`. **Two corrections to the bib file
  are needed:** (1) the DOI in `references.bib` is currently
  `d41586-023-03907-5`, which actually points to a *different* article
  ("Where science meets Indian economics: in five charts"); the correct
  DOI is `d41586-023-03930-6`. (2) The second author is Webb, not
  Perkel. Pages are `509`, not `S2–S3`. These need fixing in the .bib —
  per the task constraint, no changes were made here; flagged for the
  human author. Until corrected, the bib entry is **`unverifiable` as
  written**.

### `liang2024mapping`

- **Citation.** Liang, W., Zhang, Y., Wu, Z., Lepp, H., Ji, W., Zhao, X.,
  Cao, H., Liu, S., He, S., Huang, Z., Yang, D., Potts, C., Manning, C. D.,
  Zou, J. Y. (2024). "Mapping the Increasing Use of LLMs in Scientific
  Papers." arXiv preprint.
  arXiv: [2404.01268](https://arxiv.org/abs/2404.01268).
- **What it says.** Population-level analysis of 950,965 papers
  (Jan 2020 – Feb 2024) on arXiv, bioRxiv, and the Nature portfolio,
  using a mixture-model framework on word frequencies. Reports
  LLM-modification fractions of **up to 17.5% in computer-science
  papers** and **up to 6.3% in mathematics and the Nature portfolio**.
- **How the paper uses it.** `intro.tex` line 30 — the volume-problem
  anchor; the rising LLM-assisted-prose fraction since 2023 is taken
  from this paper.
- **Verification.** `ai-confirmed` (advanced 2026-05-07; verbatim
  arXiv abstract quote captured in the fourth-pass log above).
  arXiv ID resolves; abstract, methods, and headline figure
  confirmed. Author must read before condensation.

### `kobak2024delving`

- **Citation.** Kobak, D., González-Márquez, R., Horvát, E.-Á., Lause, J.
  (2024). "Delving into ChatGPT usage in academic writing through excess
  vocabulary." arXiv preprint.
  arXiv: [2406.07016](https://arxiv.org/abs/2406.07016).
- **What it says.** Adapts the "excess mortality" idea to vocabulary use.
  In 14 million PubMed abstracts (2010–2024), the appearance of LLMs
  causes an abrupt jump in the frequency of certain style words. **A
  lower bound of ~10% of 2024 abstracts shows LLM processing**, varying
  by discipline, country, and journal — **as high as ~30% in some PubMed
  sub-corpora**.
- **How the paper uses it.** `intro.tex` line 32 — the cross-discipline
  detection-symptom anchor.
- **Verification.** `ai-confirmed` (advanced 2026-05-07; verbatim
  arXiv abstract quote captured in the fourth-pass log above; note
  the title and headline figure have shifted from the bib entry
  --- see the log). arXiv ID resolves; abstract and headline
  figures confirmed. Human author has not yet read the full
  paper.

---

## 6. Methodological ancestor

### `krebs2026obscurity`

- **Citation.** Krebs, F. (2026). *Obscurity Is Dead: a methodology
  repository*. GitHub.
  URL: <https://github.com/noheton/Obscurity-Is-Dead>.
- **What it says.** The author's earlier methodology repository, the
  template that F(AI)²R abstracts. Domain content is deliberately not
  reproduced here.
- **How the paper uses it.** Direct ancestor citation in `intro.tex`
  line 18 and `related.tex` line 36.
- **Verification.** `lit-read` — under the human author's direct control.

---

## 7. Institutional context (used in acknowledgements / imprint)

These do not back load-bearing claims in the body but are cited or alluded
to in title-block, acknowledgements, and `\S\ref{sec:impl}`.

### `helmholtz_hmc` (proposed addition)

- **Citation.** Helmholtz Metadata Collaboration (HMC). Helmholtz
  Association of German Research Centres, launched 2019.
  Homepage: <https://helmholtz-metadaten.de/>.
  About: <https://helmholtz-metadaten.de/en/about-hmc>.
  See also Curdt, C. et al. (2025), "Helmholtz Metadata Collaboration —
  Building a Sustainable FAIR Data Ecosystem in a Changing Research
  Landscape," Zenodo:
  [10.5281/zenodo.15113717](https://doi.org/10.5281/zenodo.15113717).
- **What it says.** A Helmholtz-wide platform whose mission is making
  research data across the eighteen Helmholtz centres FAIR. Three
  workstreams: (1) assessing/monitoring FAIR data, (2) improving
  connectivity of Helmholtz research data, (3) implementing (meta)data
  recommendations. Operates per-research-field "metadata hubs."
- **How the paper uses it.** Imprint context — DLR / Helmholtz / HMC is
  the institutional setting under which this paper is produced (per
  `methodology.md` design-system note).
- **Verification.** `lit-retrieved` — homepage and Zenodo record both
  resolve.

### `nfdi4ing` (proposed addition)

- **Citation.** NFDI4Ing — National Research Data Infrastructure for
  Engineering Sciences, German Nationale Forschungsdateninfrastruktur
  (NFDI). Homepage: <https://nfdi4ing.de/>.
  Foundational document: Schmitt, R. H., Anthofer, V., Auer, S., et al.
  (2020), "NFDI4Ing — the National Research Data Infrastructure for
  Engineering Sciences," Zenodo:
  [10.5281/zenodo.4015201](https://doi.org/10.5281/zenodo.4015201).
- **What it says.** German NFDI consortium for engineering RDM. Organises
  engineering workflows into "archetypes" with shared base services
  (quality assurance, research-software development, terminologies,
  repositories, data security, training, discovery).
- **How the paper uses it.** Imprint context, as for HMC.
- **Verification.** `lit-retrieved` — homepage and Zenodo record both
  resolve.

### DLR open-science position

- **Status.** No single canonical DLR open-science position paper was
  located in public form. The relevant materials are (a) the Helmholtz
  Open Science Policy
  (<https://os.helmholtz.de/en/open-science-in-helmholtz/open-science-policy/>)
  and (b) the Helmholtz Open Access Memorandum (GFZ:
  <https://gfzpublic.gfz.de/pubman/faces/ViewItemOverviewPage.jsp?itemId=item_5032879>).
  DLR participates as a Helmholtz centre rather than issuing its own
  separate FAIR position paper.
- **Verification.** `lit-retrieved` for the two Helmholtz documents above.
  A DLR-specific document is **`unverifiable`** at this search depth.

---

## 8. Legal context

### Germany — UrhG §2

- **Citation.** *Gesetz über Urheberrecht und verwandte Schutzrechte
  (Urheberrechtsgesetz — UrhG)*, §2 ("Geschützte Werke"). Bundesamt für
  Justiz: <https://www.gesetze-im-internet.de/urhg/__2.html>.
- **What it says.** Lists protected works and requires "persönliche
  geistige Schöpfung" — personal intellectual creation by a human — for
  copyright protection.
- **How the paper uses it.** `background.tex` line 51 — anchors the
  German leg of the "AI cannot hold copyright" claim.
- **Verification.** `lit-retrieved` — public statute. **No bib entry
  exists**; should be added as a `@misc` if cited in body. Currently
  cited in body without a bib entry, which is a defect.

### USCO 2023 — `usco2023ai` (proposed addition)

- **Citation.** U.S. Copyright Office (2023). "Copyright Registration
  Guidance: Works Containing Material Generated by Artificial
  Intelligence." 88 Fed. Reg. 16190 (16 March 2023).
  Federal Register:
  <https://www.federalregister.gov/documents/2023/03/16/2023-05321/copyright-registration-guidance-works-containing-material-generated-by-artificial-intelligence>.
  PDF: <https://www.copyright.gov/ai/ai_policy_guidance.pdf>.
  Programme page: <https://www.copyright.gov/ai/>.
- **What it says.** Restates that U.S. copyright requires human authorship
  and that "author" excludes non-humans. Applicants must disclose AI-
  generated content in registration applications and explain the human
  contribution. Worked example (the *Zarya of the Dawn* graphic novel,
  February 2023) found that human-authored text was protectable but the
  individual Midjourney-generated images were not.
- **How the paper uses it.** `background.tex` line 51 — anchors the U.S.
  leg of the "AI cannot hold copyright" claim. Currently cited in body
  as "USCO 2023" without a bib entry; the new bibkey `usco2023ai` is
  proposed.
- **Verification.** `lit-retrieved` — Federal Register record and USCO
  PDF both resolve.

---

## Proposed additions

The eight entries below are proposed for `references.bib`. All have been
identifier-verified by an AI agent (`lit-retrieved`). None has yet been
read by the human author and so none can move to `lit-read`.

### `usco2023ai` — USCO AI registration guidance

See §8 above. Backs the U.S. leg of the legal-honesty claim in
`background.tex`.

### `acl2023aipolicy` — ACL Rolling Review / ACL 2023 AI policy

- **Citation.** Association for Computational Linguistics (2023). "ACL
  2023 Policy on AI Writing Assistance." ACL 2023 blog,
  <https://2023.aclweb.org/blog/ACL-2023-policy/>. ACL Rolling Review
  Authors / Reviewer Guidelines:
  <http://aclrollingreview.org/authors>,
  <http://aclrollingreview.org/reviewerguidelines>. Disclosure is
  enforced via the Responsible NLP Checklist item E1.
- **What it says.** Authors must disclose generative-AI use; pure
  language-polishing assistance does not need disclosure; literature-
  search tools are acceptable; LLM-generated reviews are unacceptable
  and area chairs may flag them.
- **How the paper would use it.** `related.tex` line 25 currently cites
  ACL Rolling Review by name without a bib entry. Cited as one of the
  major-venue disclosure positions converging on "AI is not an author,
  AI use must be disclosed."
- **Verification.** `lit-retrieved`.

### `neurips2024llmpolicy` — NeurIPS LLM policy

- **Citation.** Neural Information Processing Systems Foundation. "NeurIPS
  LLM Policy" (2024 / 2025).
  <https://neurips.cc/Conferences/2025/LLM>; NeurIPS 2024 Call for Papers:
  <https://neurips.cc/Conferences/2024/CallForPapers>.
- **What it says.** Authors are responsible for the entire content of
  the paper, including all text and figures; LLM use as a tool (data
  processing, filtering, visualisation, theorem-proving, important or
  non-standard methodological components) must be described.
- **How the paper would use it.** Same role as `acl2023aipolicy`.
- **Verification.** `lit-retrieved`.

### `icml2025llmpolicy` — ICML LLM policy

- **Citation.** International Conference on Machine Learning. "ICML 2025
  Author Instructions" / "Intro LLM Policy."
  <https://icml.cc/Conferences/2025/AuthorInstructions>;
  <https://icml.cc/Conferences/2026/Intro-LLM-Policy>.
- **What it says.** Authors may use generative-AI tools for writing or
  research provided they take full responsibility, disclose significant
  use, and ensure no plagiarism or scientific misconduct. LLMs are not
  eligible for authorship. (A more permissive stance than ICML 2023,
  which had banned LLM-generated text outside experimental analysis.)
- **How the paper would use it.** Same role as `acl2023aipolicy`.
- **Verification.** `lit-retrieved`.

### `weberwulff2023detection` — AI-detection-tool benchmarking

- **Citation.** Weber-Wulff, D., Anohina-Naumeca, A., Bjelobaba, S.,
  Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., Waddington, L.
  (2023). "Testing of detection tools for AI-generated text."
  *International Journal for Educational Integrity* 19, 26.
  DOI: [10.1007/s40979-023-00146-z](https://doi.org/10.1007/s40979-023-00146-z).
  arXiv: [2306.15666](https://arxiv.org/abs/2306.15666).
- **What it says.** Tested 12 publicly available detectors plus Turnitin
  and PlagiarismCheck against six text-condition types. **All scored
  below 80% accuracy; only five exceeded 70%.** Tools are biased toward
  classifying text as human-written and degrade further on paraphrased
  output.
- **How the paper would use it.** Backs the editorial-fatigue / detection-
  reliability framing in `intro.tex` and the residual "adversarial review"
  failure mode in `failure-modes.tex`. Quantifies why
  F(AI)²R prefers author-side provenance over reviewer-side detection.
- **Verification.** `lit-retrieved`.

### `liang2023detectorbias` — GPT-detector bias against non-native English

- **Citation.** Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., Zou, J.
  (2023). "GPT detectors are biased against non-native English writers."
  *Patterns* 4(7), 100779.
  DOI: [10.1016/j.patter.2023.100779](https://doi.org/10.1016/j.patter.2023.100779).
  arXiv: [2304.02819](https://arxiv.org/abs/2304.02819).
- **What it says.** Across seven detectors, **more than half of non-
  native-authored TOEFL essays were misclassified as AI-generated** while
  US 8th-grade essays were classified almost perfectly. Simple prompting
  ("elevate the text with literary language") drove detection rates close
  to zero.
- **How the paper would use it.** Same role as `weberwulff2023detection`,
  with the additional fairness/equity dimension that aligns with the
  equity paragraph in `sustainability.tex`.
- **Verification.** `lit-retrieved`.

### `mitchell2023detectgpt` — DetectGPT

- **Citation.** Mitchell, E., Lee, Y., Khazatsky, A., Manning, C. D.,
  Finn, C. (2023). "DetectGPT: Zero-Shot Machine-Generated Text Detection
  using Probability Curvature." In *Proceedings of the 40th International
  Conference on Machine Learning (ICML)*. PMLR 202: 24950–24962.
  arXiv: [2301.11305](https://arxiv.org/abs/2301.11305). PMLR:
  <https://proceedings.mlr.press/v202/mitchell23a.html>.
- **What it says.** Zero-shot detector exploiting the observation that
  LLM-generated text occupies negative-curvature regions of the model's
  log-probability surface. Reports AUROC improvements (e.g. 0.81 → 0.95
  for fake-news detection on GPT-NeoX-20B) over earlier zero-shot
  baselines.
- **How the paper would use it.** Cited where the paper currently names
  "Detect-GPT" parenthetically in the AI-detection discussion. Establishes
  that the upper-bound detector performance is itself fragile to
  paraphrase attacks (which `sadasivan2023reliably` then formalises).
- **Verification.** `lit-retrieved`.

### `sadasivan2023reliably` — limits of AI-text detection

- **Citation.** Sadasivan, V. S., Kumar, A., Balasubramanian, S., Wang, W.,
  Feizi, S. (2023). "Can AI-Generated Text be Reliably Detected?" arXiv
  preprint. arXiv: [2303.11156](https://arxiv.org/abs/2303.11156).
- **What it says.** Demonstrates a recursive paraphrasing attack that
  breaks watermarking, neural-classifier, zero-shot, and retrieval-based
  detectors. Presents a theoretical impossibility result: as LLMs better
  emulate human text, the best-possible detector's performance
  approaches a chance baseline.
- **How the paper would use it.** Theoretical complement to
  `weberwulff2023detection` and `liang2023detectorbias`. Backs the
  editorial position that post-hoc detection cannot be load-bearing.
- **Verification.** `lit-retrieved`.

### `hosseini2025disclosure` — disclosure should be voluntary, structured

- **Citation.** Hosseini, M., Gordijn, B., Kaebnick, G. E., Holmes, K.
  (2025). "Disclosing generative AI use for writing assistance should be
  voluntary." *Research Ethics*.
  DOI: [10.1177/17470161251345499](https://doi.org/10.1177/17470161251345499).
  Companion: Hosseini, M., Resnik, D. B. (2025), "Disclosing artificial
  intelligence use in scientific research and publication: When should
  disclosure be mandatory, optional, or unnecessary?" *Accountability in
  Research*. DOI:
  [10.1080/08989621.2025.2481949](https://doi.org/10.1080/08989621.2025.2481949).
- **What it says.** Categorises AI-use disclosure into mandatory
  (intentional and substantial use — hypothesis generation, drafting,
  data analysis, figure generation), optional (text refinement under
  human control), and unnecessary (spell-check, reference management).
  Aligns with ICMJE 2024 framing.
- **How the paper would use it.** A 2024–2025 anchor for the
  AI-co-authorship / ICMJE-compliance discussion in `related.tex` and
  the sixth integrated practice in `eight.tex`.
- **Verification.** `lit-retrieved`.

---

## 9. Sustainability and resource cost

### `strubell2019energy`

- **Citation.** Strubell, E., Ganesh, A., McCallum, A. (2019). "Energy and
  Policy Considerations for Deep Learning in NLP." *Proceedings of the
  57th Annual Meeting of the Association for Computational Linguistics
  (ACL)*, 3645–3650.
  DOI: [10.18653/v1/P19-1355](https://doi.org/10.18653/v1/P19-1355).
  arXiv: [1906.02243](https://arxiv.org/abs/1906.02243).
- **What it says.** Quantifies the financial and environmental cost of
  training large NLP models. The often-quoted figure: training a single
  large neural-architecture-search run produces CO₂ comparable to the
  lifetime emissions of five average automobiles.
- **How the paper uses it.** Background citation in `sustainability.tex`
  (resource-cost paragraph) for the training-side energy footprint.
- **Verification.** `lit-retrieved` — ACL Anthology and arXiv resolve.

### `patterson2021carbon`

- **Citation.** Patterson, D., Gonzalez, J., Le, Q., Liang, C., Munguia,
  L.-M., Rothchild, D., So, D., Texier, M., Dean, J. (2021). "Carbon
  Emissions and Large Neural Network Training." arXiv preprint.
  arXiv: [2104.10350](https://arxiv.org/abs/2104.10350).
- **What it says.** Refines training-time carbon estimates for T5, Meena,
  GShard, Switch Transformer, and GPT-3; argues that DNN choice,
  datacenter location, and processor choice each move the carbon
  footprint by an order of magnitude.
- **How the paper uses it.** Same role as `strubell2019energy`; cited
  alongside it in `sustainability.tex`.
- **Verification.** `lit-retrieved` — arXiv resolves.

### `luccioni2024power`

- **Citation.** Luccioni, A. S., Jernite, Y., Strubell, E. (2024). "Power
  Hungry Processing: Watts Driving the Cost of AI Deployment?" In
  *Proceedings of the 2024 ACM Conference on Fairness, Accountability,
  and Transparency (FAccT)*.
  DOI: [10.1145/3630106.3658542](https://doi.org/10.1145/3630106.3658542).
  arXiv: [2311.16863](https://arxiv.org/abs/2311.16863).
- **What it says.** Inference-side energy and carbon comparison across
  task-specific and general-purpose generative models. Multi-purpose
  generative architectures cost orders of magnitude more per inference
  than task-specific systems even when controlling for parameter count.
- **How the paper uses it.** The inference-cost anchor in
  `sustainability.tex`; the F(AI)²R pattern's per-claim re-invocation
  pattern explicitly amplifies the inference cost this paper measures.
- **Verification.** `lit-retrieved` — both ACM DL and arXiv resolve.

### `li2023thirsty`

- **Citation.** Li, P., Yang, J., Islam, M. A., Ren, S. (2023). "Making
  AI Less 'Thirsty': Uncovering and Addressing the Secret Water
  Footprint of AI Models." arXiv preprint.
  arXiv: [2304.03271](https://arxiv.org/abs/2304.03271).
  Final: *Communications of the ACM* (2025), DOI:
  [10.1145/3724499](https://doi.org/10.1145/3724499).
- **What it says.** First systematic estimate of fresh-water
  consumption: training GPT-3 in U.S. Microsoft data centres directly
  evaporates roughly 700,000 litres; global AI demand is projected to
  withdraw 4.2–6.6 billion m³ in 2027.
- **How the paper uses it.** Cited alongside `luccioni2024power` for the
  water-footprint half of the resource-cost paragraph in
  `sustainability.tex`.
- **Verification.** `lit-retrieved` — arXiv and CACM resolve.

### `birhane2022values`

- **Citation.** Birhane, A., Kalluri, P., Card, D., Agnew, W., Dotan, R.,
  Bao, M. (2022). "The Values Encoded in Machine Learning Research." In
  *Proceedings of the 2022 ACM Conference on Fairness, Accountability,
  and Transparency (FAccT)*.
  DOI: [10.1145/3531146.3533083](https://doi.org/10.1145/3531146.3533083).
  arXiv: [2106.15590](https://arxiv.org/abs/2106.15590).
- **What it says.** Audits 100 highly cited ICML/NeurIPS papers; finds a
  threefold increase in ties to Big Tech and 79% overall industry
  affiliation; documents that ML research uplifts performance, novelty,
  and generality while neglecting equity, justice, and harm-mitigation.
- **How the paper uses it.** Backs the equity paragraph in
  `sustainability.tex` — the claim that frontier-model dependence
  produces a non-neutral standard.
- **Verification.** `lit-retrieved` — both ACM DL and arXiv resolve.

### `chen2023drift`

- **Citation.** Chen, L., Zaharia, M., Zou, J. (2023). "How Is ChatGPT's
  Behavior Changing over Time?" arXiv preprint.
  arXiv: [2307.09009](https://arxiv.org/abs/2307.09009). Later in
  *Harvard Data Science Review*.
- **What it says.** Empirically documents that the same hosted LLM
  endpoint (GPT-3.5, GPT-4) produces measurably different outputs
  across March and June 2023 versions; GPT-4 prime-vs-composite
  accuracy fell from 84% to 51%.
- **How the paper uses it.** Cited in the frontier-model-dependence
  paragraph in `sustainability.tex` as evidence that the pattern's
  effective behaviour shifts under the author's feet.
- **Verification.** `lit-retrieved` — arXiv resolves.

---

## 10. Model collapse and self-consuming generative loops

### `shumailov2024collapse`

- **Citation.** Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N.,
  Anderson, R., Gal, Y. (2024). "AI models collapse when trained on
  recursively generated data." *Nature* 631, 755–759.
  DOI: [10.1038/s41586-024-07566-y](https://doi.org/10.1038/s41586-024-07566-y).
- **What it says.** Demonstrates that training generative models on
  their own outputs irreversibly degrades the resulting model — the
  tails of the original content distribution disappear. Effect holds
  for LLMs, variational autoencoders, and Gaussian mixture models.
- **How the paper uses it.** The model-collapse row in
  `failure-modes.tex` — quantifies the failure mode the F(AI)²R
  pattern's transcript-preservation discipline only indirectly
  mitigates.
- **Verification.** `lit-retrieved` — Nature DOI resolves.

### `alemohammad2023mad`

- **Citation.** Alemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun,
  A. I., Babaei, H., LeJeune, D., Siahkoohi, A., Baraniuk, R. G. (2023).
  "Self-Consuming Generative Models Go MAD." arXiv preprint.
  arXiv: [2307.01850](https://arxiv.org/abs/2307.01850). Later: ICLR
  2024.
- **What it says.** Coins "Model Autophagy Disorder" (MAD) for the
  self-consuming-loop failure mode that `shumailov2024collapse` later
  formalised in *Nature*. Without enough fresh real data per
  generation, model quality or diversity progressively decays.
- **How the paper uses it.** Cited alongside `shumailov2024collapse` in
  the model-collapse row of `failure-modes.tex`.
- **Verification.** `lit-retrieved` — arXiv resolves.

---

## 11. Editorial position (added second pass)

### `thorp2023chatgpt`

- **Citation.** Thorp, H. H. (2023). "ChatGPT is fun, but not an
  author." *Science* 379(6630), 313.
  DOI: [10.1126/science.adg7879](https://doi.org/10.1126/science.adg7879).
- **What it says.** Editor-in-Chief of *Science* declares that
  AI-generated content without disclosure is plagiarism, that AI cannot
  be an author, and that the scientific record is a human endeavour
  with machines as tools.
- **How the paper uses it.** Cited in `intro.tex` alongside
  `else2023chatgpt` as the second major-venue editorial declaration —
  the *Science* counterpart to the *Nature* editorial — backing the
  "editors at major venues asked for provenance from authors" sentence.
- **Verification.** `lit-retrieved` — Science DOI resolves.

---

## 12. Legal context (formal entries)

### `usco2023ai`

Promoted from "proposed addition" to a real `references.bib` entry in
the second pass. See §8 above.

- **Verification.** `lit-retrieved` — Federal Register and USCO PDF
  both resolve.

### `urhg2`

- **Citation.** Bundesministerium der Justiz. *Gesetz über Urheberrecht
  und verwandte Schutzrechte (Urheberrechtsgesetz, UrhG)*, §2
  ("Geschützte Werke"). 1965, last amended 2021.
  URL: <https://www.gesetze-im-internet.de/urhg/__2.html>. English
  translation: <https://www.gesetze-im-internet.de/englisch_urhg/englisch_urhg.html>.
- **What it says.** Lists protected works (Sprachwerke, Musikwerke,
  Lichtbildwerke, Filmwerke, etc.) and requires "persönliche geistige
  Schöpfung" — personal intellectual creation by a human — for
  copyright protection.
- **How the paper uses it.** Cited in `background.tex` for the German
  leg of the "AI cannot hold copyright" claim.
- **Verification.** `lit-retrieved` — public statute, multiple stable
  URLs.

---

## Summary of corrections needed in `references.bib`

(Per the task constraint, the `.bib` file was not modified. These are
flagged for the human author.)

1. **`vannoorden2023chatgpt`**: DOI is wrong (`d41586-023-03907-5` points
   to an unrelated India-economics article). Correct is
   `10.1038/d41586-023-03930-6`. Second author is Webb, not Perkel.
   Pages are `509`, not `S2–S3`.
2. **`ravi2024fair4ml`**: `author = {TODO-VERIFY}` should be filled in
   with Castro, L. J., Garijo, D., et al.; canonical artefact is the
   FAIR4ML-schema on Zenodo (10.5281/zenodo.14002310).
3. **`icmje2023`** is fine but the most current revision is January 2024;
   consider updating the year and adding the AI-specific topic page URL.
4. **UrhG §2** is cited in `background.tex` without a bib entry — needs
   one.
5. **USCO 2023** is cited in `background.tex` without a bib entry —
   `usco2023ai` is proposed above.
6. **`shafer2014xennials`**: bibkey author was wrong --- the GOOD
   Magazine article is by **Stankorb and Oelbaum**, not "Shafer" ---
   and the canonical title is *"Reasonable People Disagree about the
   Post-Gen X, Pre-Millennial Generation"*, not *"Generation
   Xennial"*. Both fields corrected in the bib and in
   `doc/provenance.ttl` during the sixth pass; bibkey kept stable for
   citation continuity. Flagged here for the human author's
   awareness.
