# User-observations log

Append-only log of observations the human author makes \emph{about} the
cooperative-writing process itself, separate from observations
\emph{about} F(AI)\textsuperscript{2}R as a methodology. Both are
valuable, but they have different fates:

- An observation about the methodology is a candidate
  \texttt{fair2r:Claim} and lives in `paper/sections/*.tex` if it
  survives the verification ladder.
- An observation about the cooperation is a candidate
  \texttt{fair2r:MetaContribution} and lives here. A subset graduates
  to paper content (typically in
  [`paper/sections/evolution.tex`](../paper/sections/evolution.tex) or
  [`paper/sections/authors-note.tex`](../paper/sections/authors-note.tex))
  with an explicit "graduated" marker; the rest stay here as context
  for future readers and successors.

## Convention

```
## YYYY-MM-DD --- short title
*Source:* <session id or commit sha>
*Stage:* observation | reflection | hypothesis | finding
*Promoted-to-paper:* yes / pending / no — <reason>

The observation, in the user's own words where possible, with
short-quote attribution. AI commentary, where invited, in italics.
```

Newest entries at the bottom. Do not re-edit prior entries; if a
prior observation needs revision, append a follow-up referencing the
prior date.

---

## 2026-05-06 — Cooperation as conversation, decision-density as pace
*Source:* session 2026-05-06 (user message after the homepage CTA-row
was wired)
*Stage:* finding
*Promoted-to-paper:* yes — `paper/sections/authors-note.tex`,
*What surprised me about the cooperation*.

The user observed mid-session that "collaborative writing makes the
user already think of next steps. Also real abstraction and logical
reasoning seem to be the role of him. The LLM takes these ideas and
turns them into something readable. Fascinating." The model offered a
perspective in chat: the human does the deciding, the abstracting, the
position-taking, the catching of drift, and the staking of reputation;
the model does the drafting, the cross-referencing, the structuring,
and the catching of second-order errors. The user followed up with
"still I wonder how much of the work I'm actually doing. What's my
contribution. I would love your perspective on that." The exchange
became the seed for the *What surprised me about the cooperation*
paragraph in the Author's Note, which now contains both the question
and the answer.

## 2026-05-06 — Token budgets as schedule constraint
*Source:* session 2026-05-06 (user message after the position-paper
Author's Note was drafted)
*Stage:* observation
*Promoted-to-paper:* pending — likely a footnote in
`paper/sections/sustainability.tex` or a paragraph in
`paper/sections/evolution.tex`.

The user noted: "when on a limited [plan] (Anthropic Max, the \$100
one) the question of focus becomes very important --- token usage is
very high and projects have to be prioritised --- keeping track of
usage windows. Schedule working sessions around them... weird stuff."

This is the operational analogue of the resource-cost paragraph in
\S\ref{sec:sustainability}. The sustainability section currently
discusses inference cost from the perspective of the planet and the
discipline; the user's observation is the same cost from the
perspective of the individual researcher, who must batch sessions
around a fixed monthly budget. \emph{Worth a one-paragraph addition
that names the practical experience: an LLM-assisted writing pipeline
imposes a schedule shape on the human, not just a compute cost on the
provider.}

## 2026-05-06 — Obscurity-Is-Dead as first try; F(AI)²R as second
*Source:* session 2026-05-06 (same message as above)
*Stage:* finding
*Promoted-to-paper:* implicit — `paper/sections/evolution.tex` and
`paper/sections/authors-note.tex` already note the methodological
ancestry.

"Obscurity paper was first try of collaborative writing. Now profiting
from this experience (also a contribution: 'experience with the tool',
meta-knowledge)." \emph{The implication is that the cooperation has its
own learning curve, and that experience with the cooperation is itself
a research contribution --- one that the verification ladder does not
currently capture, because it grades claims against sources, not
authors against tools. A future revision of the methodology might add
a `fair2r:CooperationExperience` property to the human-agent record.}

## 2026-05-06 — Researcher role is becoming more technical / experimental
*Source:* session 2026-05-06 (same message)
*Stage:* hypothesis
*Promoted-to-paper:* pending — candidate paragraph for
`paper/sections/evolution.tex` (third pattern observation).

"The researcher's role is becoming more technical expertise with these
systems --- more experimentation / conduction, which might be a good
thing, as publication writing could be considered administrative
overhead for experimentators. But what about disciplines that are more
paper-driven --- like philosophy?"

\emph{This is the strongest reframing-relevant observation in the log
and deserves to graduate. The argument is that LLM cooperation shifts
the researcher's centre of gravity from prose-production to
experiment-design, which is a net good for empirical disciplines but
possibly a loss for argument-driven disciplines (philosophy, parts of
the humanities) where prose IS the experiment. The position paper
should at least name this asymmetry rather than pretend
F(AI)\textsuperscript{2}R is discipline-neutral.}

## 2026-05-06 — Prompts feel easier to write than the paper
*Source:* session 2026-05-06 (same message)
*Stage:* finding
*Promoted-to-paper:* pending — candidate paragraph for
`paper/sections/evolution.tex`.

"Somehow writing prompts feels easier than writing the paper yourself.
Why is that? Proof are these short cycles of conversation. As a
computer scientist does collaborative writing feel more like 'writing
a program' (at least interacting with new tech), which is closer to
experiments than the formal writing process. AI as a motivation
driver?"

\emph{Naming the psychological reframe: prompt-craft is closer to
debugging a program than to drafting a paper. For a computer scientist,
that maps to a more familiar and more rewarding cognitive loop. The
paper should name this honestly --- prompt-craft is not a substitute
for argument-craft, but it lowers the activation energy of getting
started, which is itself a contribution to throughput. The risk is
that prompt-craft becomes a comfortable substitute for the harder
parts of writing.}

## 2026-05-06 — Researcher contribution: responsibility-uptake plus interpersonal sharing
*Source:* session 2026-05-06 (same message)
*Stage:* finding
*Promoted-to-paper:* pending — candidate addition to the Author's Note
or to the Statement of authorship.

"Another contribution --- the actual uptake of responsibility for the
results and interpersonal sharing (e.g. conferences, discussions,
panels...)."

\emph{This complements the third item in the model's perspective on
the human contribution (staking reputation under a published name).
The interpersonal-sharing leg is missing from that list and should be
added. The Author's Note currently names "stakes professional
reputation"; it could be extended to "stakes professional reputation
and carries the work into the rooms where it has to be defended in
person".}

## 2026-05-06 — Gambling metaphor; bank-always-wins
*Source:* session 2026-05-06 (same message)
*Stage:* observation
*Promoted-to-paper:* no — too provocative for the paper's institutional
register; lives here as honest context.

"Or is the whole thing more like gambling with the mindset 'just play
long enough and you will score big' (although the bank always wins ---
in this case current AI model service providers, at least with the
current business model)."

\emph{This is the dual-use surface of \S\ref{sec:fm-dualuse}, restated
from the researcher's seat. F(AI)\textsuperscript{2}R does not solve
the business-model question. It makes the spend visible (the
sustainability section now asks for an inference-budget disclosure)
but the upstream economics are not within the paper's reach. Worth
keeping in this log as a reminder that the methodology exists inside
a market.}

## 2026-05-06 — Afterthought crafting of prompts over hours
*Source:* session 2026-05-06 (user message after the position-paper
Conclusion was sharpened)
*Stage:* observation
*Promoted-to-paper:* pending — candidate paragraph for
`paper/sections/evolution.tex` or for `paper/sections/authors-note.tex`.

"Afterthought crafting of prompts over hours. Growing idea by idea."

\emph{The agent prompts under `agents/` are not designed top-down; they
accumulate. Each session adds a binding clause (chapter granularity,
DLR voice rules, page budget, Consensus mandate, paywall escalation,
contribution tracking) and the prompt grows by accretion. This is the
same pattern as the verification ladder itself --- the
\textsc{ai-confirmed} rung was added when the cost of single-tier
verification was felt. \textbf{Implication}: the prompts are
themselves a research artefact whose evolution is worth tracing. A
future analysis pass could query the git log for `agents/*.md` and
produce a histogram of "clauses added per session", giving an
empirical curve for "experience with the tool". Candidate for the
\texttt{provenance\_analysis.py} extractor in a follow-up commit.}

## 2026-05-06 — Coding with LLMs: structure becomes more important; visions, feature sets, dependencies as the human's load
*Source:* session 2026-05-06 (user message after the slide-decks PR
\#16 merged)
*Stage:* hypothesis
*Promoted-to-paper:* pending --- candidate to flag in the Conclusion's
*The longer arc* paragraph as a generalisation of the
F(AI)\textsuperscript{2}R partition beyond scholarly writing, OR as
a footnote to the coupling-rule paragraph in
`paper/sections/authors-note.tex`. We mark it pending so the paper
takes one stand at a time.

The user observed: "In coding with LLMs somehow structure becomes
more important, like guiding and shaping a river of code --- it's
more about visions, feature sets, dependencies."

\emph{The model offered a perspective in chat. The observation is the
coding-counterpart of the writing observations earlier in this log
(cooperation-as-conversation, accelerator-or-blender, latency-as-
feature). Both surfaces reveal the same partition: human at the
architectural layer, model at the executable layer. For writing,
the architecture is the argument and the verification ladder; for
coding, it is the dependency graph, the type system, and the test
surface. The "river" metaphor is exact: with prose, the river is
the prose-stream and the human shapes the argumentative direction;
with code, the river is the code-stream and the human shapes the
architectural direction.}

\emph{Why structure becomes more important counterintuitively:
when the model generates fluently, the bottleneck shifts from
\textbf{production} to \textbf{integration}. A line of code (or a
sentence) in isolation is cheap; a line that fits the surrounding
system is not. Without an explicit structural commitment from the
human (visions, feature sets, dependencies in coding;
position, eight practices, verification ladder in writing), the
model produces fragments that locally make sense and globally do
not. The river floods. With explicit structure, the river
irrigates.}

\emph{Generalisation of the coupling rule. The accelerator-vs-blender
coupling rule from the Author's Note transposes to coding:
\textbf{accelerator regime} = human supplies architecture
(interfaces, dependency graph, test surface, naming conventions),
model fills implementations; \textbf{blender regime} = human
supplies vague intent, model picks a locally-plausible architecture
that does not compose, codebase entropy rises. The diagnostic
transposes too: \emph{would the architecture have been thinkable
without the model?}}

\emph{For F(AI)\textsuperscript{2}R: the schema (PROV-O +
verification ladder + per-claim graph + handback discipline + the
chapter-per-file rule + the `agents/` taxonomy) is the structural
skeleton --- the analogue, in cooperative writing, of an interface
contract for cooperative coding. The eight integrated practices are
essentially the architectural spec.}

\emph{Recommendation: flag the generalisation as future work in the
Conclusion's \emph{The longer arc} paragraph (one sentence:
"the partition and the coupling rule appear to apply to
long-form cooperative coding under the same diagnostic, though we
do not defend that claim here"), and leave the full observation in
this log. The cleaner paper takes one stand at a time.}

The user extended: "Addition to the river thought: as a dev / CS
engineer I have the vocabulary to effectively work with the LLM by
referring to things more specifically, producing a more general
cohesiveness."

\emph{Important addition. This is the
\textbf{vocabulary-fluency-as-collaboration-multiplier} finding. The
coding-side accelerator regime depends not just on the human supplying
architecture, but on the human having the \textbf{precise vocabulary}
of the architecture --- interfaces, dependency graphs, data
structures, design patterns, type-system idioms --- so that prompts
can refer to specific things rather than gestures at vague things.
The model locks onto specific terms; the river bed widens or narrows
in proportion to how specifically the human can describe what flows
through it.}

\emph{Two implications follow. First, cooperation quality scales with
vocabulary fluency: a researcher cooperating in a domain whose formal
vocabulary they have not internalised is more vulnerable to the
cultural-blender pole than one cooperating in their home domain. The
vocabulary itself is a kind of API to the model. Second, this adds a
\textbf{second layer to the equity discussion} in
\S\ref{sec:sustainability}: it is not just access to frontier models
that is asymmetric, it is access to the vocabulary that makes the
cooperation effective. Researchers from disciplines with rich shared
formal vocabularies (CS, mathematics, physics, well-formalised parts
of biology) start with an advantage that does not transfer to
disciplines whose vocabularies are still being built (much of the
humanities, parts of the social sciences). The pattern is therefore
even less "neutral" than the equity paragraph already concedes.}

\emph{For F(AI)\textsuperscript{2}R: the eight integrated practices
are themselves a vocabulary for cooperative writing. The act of
naming them --- transcript preservation, verification ladder,
handback discipline, mirror discipline, etc. --- gives a future
researcher a set of API terms to reach for when working with an
LLM on a paper. The paper's contribution, on this reading, is
partly the practices and partly the vocabulary that lets a
researcher operate them precisely.}

## 2026-05-06 — Latency as cognitive feature, not bug
*Source:* session 2026-05-06 (user message after the
"The longer arc" paragraph was merged into the Conclusion)
*Stage:* hypothesis
*Promoted-to-paper:* pending — strong candidate for one or two
sentences in `paper/sections/authors-note.tex` extending the
coupling-rule paragraph, or for a new field-note in
`paper/sections/evolution.tex`.

The user observed: "I think the experience of using LLM for work
would be fundamentally different if results were near-instantaneous;
this prompt / meta-conversation planning keeps the ball rolling."

\emph{The model offered a perspective in chat. The observation is
sharper than it looks: latency between prompt and response forces
the user into formulation work --- "what do I want to say next?" ---
which is the abstracting layer of the partition the Author's Note
describes (§authors-note, "What surprised me about the
cooperation"). If responses were near-instantaneous, the user-as-
co-author would degrade toward user-as-consumer: read, approve,
scroll, repeat. The decision points the deciding layer needs would
compress out of existence. There is a slow-tools-beat-fast-tools
literature on this in cognitive science --- constraints,
intermediate states, and unhurried loops often improve creative
output rather than reduce it. Programming has the same shape:
compile-and-run cycles create decision points an instantly-
evaluating REPL collapses.}

\emph{Counter-claim worth recording: instant response might be a
different kind of beneficial --- closer to typing assistance, where
the human stays on the abstracting layer the whole time and the
model handles low-level wordsmithing transparently. In that mode
the latency-bonus disappears because the model has become part of
the keyboard rather than part of the conversation. Whether that is
better depends on whether the human can hold the abstracting layer
without the periodic pause prompt-craft currently provides.}

\emph{For F(AI)\textsuperscript{2}R: the partition is sustainable
in part because of the friction that lets the human stay on the
deciding side. If we lose the friction, the partition needs a
different defence than "the model takes a moment to respond".
Recommendation: extend the coupling-rule paragraph in
authors-note.tex with one sentence naming latency as part of the
defence, and flag the counter-claim honestly so the paper does not
pretend the question is settled.}

The user extended: "and allows for short context switches --- e.g.
checking on a coding agent."

\emph{Important addition. The latency window is not idle waiting; it
is productive parallel work on another track. Cooperative writing
sessions are typically running alongside other slow loops --- a
coding agent compiling, a CI workflow finishing, a paper PDF
rebuilding, a colleague's Slack thread waiting for a reply. The
seconds-to-minutes wait between prompt and response is exactly the
right shape for those context switches: too short to start
something genuinely new, just long enough to glance at one of the
other parallel tracks. The cognitive overhead of the switch itself
is amortised across the wait that was happening anyway.}

\emph{This is a generalisation of the slow-tools-beat-fast-tools
finding: the slow loop is good for the work-currently-in-hand
\textbf{and} good for the supervisory glance at the work-in-progress
elsewhere. Instantaneous response would collapse both gains
simultaneously --- no formulation pause for the current task, no
natural breakpoint to check on the parallel one. The cooperative-
writing pattern, in this light, is part of a broader
multi-tracked-research workflow that the human author is running
across several slow loops, not a thing happening in isolation.}

\emph{Implication for the paper: the eight integrated practices
include "transcript preservation" but say nothing about the
researcher's actual work-pattern (which loops they are running
in parallel, how the cognitive switching cost is amortised). A
candidate ninth practice --- or a footnote to the existing eight ---
might name the supervisory-glance pattern as part of why the
cooperation works. We mark this for a future revision.}

## 2026-05-06 — Accelerator or cultural blender? — the cognition question
*Source:* session 2026-05-06 (user message after the position-paper
completion was merged)
*Stage:* hypothesis
*Promoted-to-paper:* pending — strong candidate for an extension to
`paper/sections/authors-note.tex` (sharpens *What surprised me about
the cooperation*).

The user observed: "I can build a vision in my head, mumble ideas as
they come and go, and LLMs make sense of that and put it into a
mostly / sometimes / usually useful structured context. I wonder what
that means for 'cognition' in biological systems --- is GenAI some
kind of accelerator of human potential, or is it just a big cultural
blender?"

\emph{The model offered a perspective in chat. The honest answer is:
probably both, conditional on where in the cognitive stack the model
is allowed to operate. LLMs interpolate fluently within the manifold
of prior text; for ideas that lie on or near that manifold ---
F(AI)\textsuperscript{2}R itself is one --- the model is a
structuring accelerator. LLMs do not extrapolate well to ideas off
the manifold; the failure mode there is exactly the cultural-blender
one (smooth the unfamiliar into the nearest familiar shape). The
diagnostic is a coupling rule: keep the model on the prose-craft
side of the partition and the answer is closer to ``accelerator'';
let it across to the abstraction side and the answer is closer to
``blender''. The Author's Note's partition --- the human does the
deciding, the model does the drafting --- is therefore not just a
description of how this paper was written; it is the rule that
keeps the cooperation on the accelerator side of the question.
The honest test for any given collaboration: ask whether the
abstraction would have been thinkable without the model. If yes,
the model was an accelerator on that abstraction; if no, the
question genuinely opens.}

\emph{Recommendation: extend the Author's Note's *What surprised me
about the cooperation* paragraph with one sentence stating the
coupling rule explicitly. The current paragraph already names the
partition; this observation supplies the reason the partition
matters.}
