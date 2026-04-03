---
alfred_tags:
- multi-agent/diagnostic-pipeline
- insights/patterns
cluster_sources:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001: project/Telia''z AI Diagnostic Research Paper wikilink is
  YAML escaping false positive (file exists). learn-synthesis.base embeds (#Sources,
  #Related) reference missing _bases/learn-synthesis.base — vault-wide gap. ORPHAN001:
  no inbound links — consider linking from AI research project.'
name: Pipeline Architecture Emerged Through Iterative Failure Correction
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs]]'
- '[[synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages]]'
relationships:
- confidence: 0.85
  context: Iterative dev enabled clinical data superiority
  source: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  target: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  type: supports
- confidence: 0.85
  context: Failures led to structure-based processing
  source: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  target: synthesis/Data Structure Level Dictates Processing Methodology Across Pipeline.md
  type: supports
- confidence: 0.9
  context: Iterative correction drove LLM adoption
  source: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  target: synthesis/LLM Approaches Progressively Replace Rule-Based Methods Across
    Pipeline Stages.md
  type: supports
status: draft
supports:
- '[[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]'
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
type: synthesis
---

# Pipeline Architecture Emerged Through Iterative Failure Correction

## Insight

The current five-stage multi-agent diagnostic pipeline was not designed top-down. It evolved through a series of failures where each new stage was added to address a specific limitation of the previous architecture. This iterative-failure pattern is consistent across all five source meeting notes.

## Evidence

The evolution sequence, reconstructed from meeting records:

1. **Rule-based transcript extraction failed** → Switched to LLM-based extraction (richer symptom capture)
2. **Per-source predictions showed limited accuracy** → Added fusion stage to combine sources
3. **Non-LLM fusion just picked one source diagnosis** → Abandoned for LLM-based fusion
4. **LLM fusion improved but lacked clinical reasoning** → Added "Expert Agent" with psychiatrist persona and DSM reasoning
5. **Expert Agent diagnosed differently from real psychiatrists** → Added "Biased Agent" with contextual priming, which replicated human diagnostic patterns

Each stage was a response to a concrete, observed failure — not a theoretical design choice.

## Implications

- The methodology section should present this as iterative refinement, not a pre-planned architecture
- The failure-driven narrative strengthens the paper's contribution: each architectural decision is empirically motivated
- Future pipeline extensions should follow the same pattern: identify a concrete failure, add a targeted stage
- The bias agent's existence is itself evidence that pure DSM reasoning diverges from clinical practice

## Applicability

This iterative-failure pattern applies to:
- Other multi-agent LLM pipeline designs in clinical settings
- Any research where the methodology evolved during the study
- Paper 2 (bias analysis), which builds on understanding why the expert and biased agents diverge

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]