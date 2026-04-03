---
based_on:
- '[[decision/Five-Stage Sequential Agent Architecture for Diagnostic Prediction]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
confidence: medium
confirmed_by:
- '[[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]'
created: '2026-02-28'
janitor_note: 'LINK001: Case Manager DSM-Oriented link confirmed valid - false positive
  from scanner multiline YAML parsing. LINK001: learn-assumption.base embeds are systemic
  (_bases/ files missing vault-wide). ORPHAN001: No inbound links detected - may need
  linking from parent project or decision records.'
name: Per-Source Independent Prediction Enables Data Source Contribution Comparison
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Questionnaire Alone Is a Weak Diagnostic Predictor]]'
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
- '[[synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages]]'
source: Rami Khouri pipeline design — implicit in architecture
source_date: '2026-02-22'
status: active
type: assumption
---

# Per-Source Independent Prediction Enables Data Source Contribution Comparison

## Claim

Evaluating each data source independently (S1 questionnaire-only, S2 transcript-only, S3 notes-only) before combining them in a fusion stage is methodologically necessary because it reveals which data modalities contribute most to diagnostic accuracy. Without per-source baselines, it would be impossible to attribute diagnostic performance to specific data sources or demonstrate that transcript data outperforms questionnaire data.

## Basis

The pipeline architecture runs each source through an independent prediction stage before fusion. Meeting discussions repeatedly compare per-source performance (e.g., "questionnaire is a weak predictor", "transcript is stronger due to DSM-oriented questioning"). The non-LLM fusion failure — where the model just picked one source's diagnosis — further supports the need for independent baselines to understand source contributions.

## Evidence Trail

- 2026-02-22: Rami presented per-source prediction results showing differential performance across S1, S2, S3
- The decision to abandon non-LLM fusion was informed by understanding (from per-source evaluation) that the fusion model was not truly integrating sources

## Impact

This assumption shapes the entire pipeline architecture and the paper's results structure. If per-source evaluation were removed, the paper could not make claims about relative data source value. It also determines that Paper 1 (per-source results) can stand alone without Paper 2 (fusion results).

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
