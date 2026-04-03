---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by: []
based_on:
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z wikilinks valid (YAML escaping false positive). Base
  view embeds (learn-decision.base#Based On, learn-decision.base#Related) reference
  _bases/learn-decision.base which does not exist — infrastructure gap. Embeds preserved
  per rules. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  AI Diagnostic Research Paper.
name: Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related: []
relationships:
- confidence: 0.98
  context: Highly similar fusion abandonment decisions
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Abandon Non-LLM Fusion in Favor of LLM-Based Fusion.md
  type: related-to
- confidence: 0.7
  context: Part of same agent system architecture
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Design APIs as Low-Level Entity Endpoints with Sub-Resources.md
  type: related-to
- confidence: 0.85
  context: Fusion supports LLM pipeline design
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Five-Agent Sequential Pipeline for Clinical AI Summaries.md
  type: supports
- confidence: 0.9
  context: Fusion supports diagnostic pipeline
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Five-Stage Sequential Agent Architecture for Diagnostic Prediction.md
  type: supports
- confidence: 0.7
  context: Shared multi-agent system design
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints.md
  type: related-to
- confidence: 0.85
  context: Fusion supports clinical pipeline
  source: decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion.md
  target: decision/Sequential Multi-Agent Pipeline for Clinical Encounters.md
  type: supports
session: null
source: Rami Khouri — pipeline iteration
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion

## Context

The multi-agent diagnostic pipeline combines predictions from three data sources (questionnaire, transcript, notes). A fusion stage was needed to synthesize these independent predictions into a unified diagnosis.

## Options Considered

1. **Non-LLM fusion** — Algorithmic combination of per-source diagnostic outputs. In practice, the model simply picked one source's diagnosis without truly integrating across sources.
2. **LLM-based fusion** — A language model sees outputs from all three sources and reasons across them to produce an integrated diagnosis.

## Decision

Abandoned non-LLM fusion. Adopted LLM-based fusion where the model receives all three source outputs and synthesizes a unified diagnostic prediction.

## Rationale

The non-LLM fusion approach failed to combine sources meaningfully — it defaulted to selecting one source's diagnosis rather than reasoning across all inputs. LLM-based fusion enables genuine cross-source reasoning, producing diagnoses informed by the full evidence picture.

## Consequences

- Fusion stage now requires LLM inference, adding computational cost
- Diagnostic accuracy improved through genuine multi-source integration
- Enabled the subsequent Expert Agent stage, which further refines the fused diagnosis using DSM persona prompting

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]