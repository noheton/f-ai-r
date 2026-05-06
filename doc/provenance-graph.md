# Provenance graph — human-readable view

Authoritative source: [`provenance.ttl`](provenance.ttl). This file is a
diagrammatic mirror only.

## Diagram (Mermaid)

```mermaid
flowchart TD
  subgraph Agents
    H[fair2r:HumanResearcher<br/>agent:human-author]
    M[fair2r:AIAgent<br/>agent:claude-opus-4-7]
    SW[Scientific Writer]
    SA[Source Analyzer]
    FA[FAIR Aligner]
    PC[Provenance Curator]
    LS[Layout Scrutinizer]
    RR[Readability Reviewer]
    IL[Illustration]
    CO[Condenser]
  end

  subgraph Plans (prompts)
    P_SW[agents/scientific-writer.md]
    P_SA[agents/source-analyzer.md]
    P_FA[agents/fair-aligner.md]
    P_PC[agents/provenance-curator.md]
  end

  subgraph Activities
    A_BOOT[act:bootstrap]
    A_AUTH[fair2r:AuthoringPass<br/>act:author-*]
    A_FAIR[fair2r:AuditPass<br/>act:audit-fair]
    A_LAY[fair2r:AuditPass<br/>act:audit-layout]
    A_READ[fair2r:AuditPass<br/>act:audit-readability]
    A_CUR[act:curate-provenance]
    A_BLD[fair2r:Build<br/>act:build-pdf]
  end

  subgraph Entities
    SRC[fair2r:Source]
    MAN[fair2r:Manuscript<br/>paper/main.tex]
    SEC[fair2r:Section]
    CLM[fair2r:Claim]
    PDF[Compiled PDF]
    GRAPH[doc/provenance.ttl]
  end

  H -- prov:actedOnBehalfOf --> SW
  H -- prov:actedOnBehalfOf --> SA
  H -- prov:actedOnBehalfOf --> FA
  H -- prov:actedOnBehalfOf --> PC

  SW -- hadPlan --> P_SW
  SA -- hadPlan --> P_SA
  FA -- hadPlan --> P_FA
  PC -- hadPlan --> P_PC

  A_BOOT -- prov:wasAssociatedWith --> M
  A_BOOT -- prov:wasAssociatedWith --> H
  A_BOOT -- prov:used --> SRC
  A_BOOT -- prov:generated --> MAN

  A_AUTH -- prov:wasAssociatedWith --> SW
  A_AUTH -- prov:used --> SRC
  A_AUTH -- prov:generated --> SEC
  A_AUTH -- prov:generated --> CLM

  SEC -- prov:hadPrimarySource --> MAN

  A_FAIR -- prov:wasAssociatedWith --> FA
  A_LAY  -- prov:wasAssociatedWith --> LS
  A_READ -- prov:wasAssociatedWith --> RR

  A_FAIR -- prov:used --> MAN
  A_LAY  -- prov:used --> MAN
  A_READ -- prov:used --> MAN

  A_CUR -- prov:wasAssociatedWith --> PC
  A_CUR -- prov:generated --> GRAPH

  A_BLD -- prov:used --> MAN
  A_BLD -- prov:generated --> PDF
  PDF -- prov:wasDerivedFrom --> MAN

  CLM -- fair2r:verificationState --> V[(verif:needs-research<br/>verif:ai-confirmed<br/>verif:human-confirmed<br/>verif:source-vendored)]
```

## Reading the graph

Three concentric loops:

1. **Authoring loop** (left).
   `Human author → Plan (prompt) → AI Agent → Activity → Section / Claim`.
   Output: prose plus proposed triples.

2. **Audit loop** (right).
   `AI Agent (FAIR / Layout / Readability) → Activity → Audit report`.
   Output: pass/warn/fail records that gate the next commit.

3. **Curation loop** (bottom).
   `Provenance Curator → curate-provenance activity → doc/provenance.ttl`.
   The *only* activity allowed to write the graph itself.

The `Build` activity is independent of all three: it consumes the
manuscript and emits the PDF, and is reproducible from the repository
alone. That reproducibility is the F(AI²)R closure: the audit AI can
replay the build, walk the graph, and verify that every claim in the PDF
traces back to either a human author or a vendored source.
