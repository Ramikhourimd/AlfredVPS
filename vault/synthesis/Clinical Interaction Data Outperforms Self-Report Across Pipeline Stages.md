---
alfred_tags:
- multi-agent/diagnostic-pipeline
- insights/patterns
cluster_sources:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
- '[[assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage]]'
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001: Telia''z wikilinks are YAML escaping false positives (targets
  exist). Assumption link (Case Manager DSM-Oriented Questioning...) verified as valid
  — scanner false positive from line wrapping. Base view embeds (learn-synthesis.base#Sources,
  #Related) reference _bases/learn-synthesis.base which does not exist yet — preserve
  per policy. ORPHAN001: No inbound links — human review needed.'
name: Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Questionnaire Alone Is a Weak Diagnostic Predictor]]'
- '[[assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured Format]]'
relationships:
- confidence: 0.75
  context: Both on LLM clinical performance
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLM.md
  type: related-to
- confidence: 0.75
  context: Both on LLM clinical performance
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in
    LLMs.md
  type: related-to
- confidence: 0.75
  context: Both on LLM clinical performance
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM
    Priming.md
  type: related-to
- confidence: 0.85
  context: Shared data processing across pipeline
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/Data Structure Level Dictates Processing Methodology Across Pipeline.md
  type: related-to
- confidence: 0.8
  context: Trends across pipeline stages
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/LLM Approaches Progressively Replace Rule-Based Methods Across
    Pipeline Stages.md
  type: related-to
- confidence: 0.75
  context: Data success from iterations
  source: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  target: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  type: supports
status: draft
supports:
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
tags:
- pipeline-performance
- data-sources
- diagnostic-accuracy
type: synthesis
---

# Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages

## Insight

Across the multi-agent diagnostic pipeline, data sources involving clinical interaction (case manager transcripts, case manager notes) consistently provide stronger diagnostic signal than patient self-report (questionnaire). This pattern holds at every stage: extraction richness, diagnostic prediction accuracy, and contribution to fusion. The gradient is: questionnaire (weakest) → transcript (stronger) → notes (additional signal) → integrated fusion (strongest).

## Evidence

- **Questionnaire (S1):** Described as a "weak predictive tool" across all three meeting notes. Structurally limited to depression, anxiety, and PTSD — does not cover the full DSM spectrum. Extraction is simple (algorithmic), reflecting the data's shallow diagnostic depth.
- **Transcript (S2):** Expected to perform better because case managers ask DSM-informed follow-up questions. Required LLM-based extraction (rule-based was insufficient), indicating richer, less structured diagnostic content. The investment in LLM extraction was justified by the data's diagnostic value.
- **Notes (S3):** Treated as a distinct additional data source, providing clinical observations beyond what's captured in the conversation transcript.
- **Fusion:** Combining all three sources via LLM produces better results than any single source, but the improvement is primarily driven by the clinical interaction sources rather than the questionnaire.
- **Expert Agent:** Adding clinical reasoning persona further improves accuracy, suggesting the clinical interaction data contains enough signal to support sophisticated diagnostic reasoning.

## Implications

- The pipeline architecture correctly allocates more computational investment (LLM extraction, multi-stage reasoning) to clinical interaction sources.
- Future clinic systems should prioritize enriching clinical interaction data (e.g., training case managers in DSM-oriented questioning) over expanding questionnaire coverage.
- For Paper 1, this gradient should be highlighted as a key finding — it validates the multi-source approach and identifies where diagnostic value concentrates.
- The questionnaire's primary value may be as a screening and routing tool rather than a diagnostic predictor.

## Applicability

- Applies to the Telia'z AI diagnostic pipeline specifically, but likely generalizes to other AI-assisted psychiatric diagnosis contexts.
- Relevant to any clinic considering which data sources to invest in for AI-assisted diagnosis.
- Does NOT apply to contexts where questionnaires are specifically designed for full DSM coverage (e.g., structured clinical interviews).

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]