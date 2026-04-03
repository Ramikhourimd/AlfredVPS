---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — FIXED project/Teliaz → project/Telia'z AI Diagnostic Research
  Paper (missing apostrophe). LINK001 — base view embeds (learn-decision.base) reference
  missing _bases/ files — vault-wide infrastructure gap. Body contains duplicate base
  embed section at bottom — human should remove the duplicate block. ORPHAN001 — no
  inbound wikilinks.
name: Abandon Non-LLM Fusion in Favor of LLM-Based Fusion
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[project/Telia''z Clinic Israel]]'
relationships:
- confidence: 0.7
  context: Part of same agent system architecture
  source: decision/Abandon Non-LLM Fusion in Favor of LLM-Based Fusion.md
  target: decision/Design APIs as Low-Level Entity Endpoints with Sub-Resources.md
  type: related-to
- confidence: 0.85
  context: Fusion supports LLM pipeline design
  source: decision/Abandon Non-LLM Fusion in Favor of LLM-Based Fusion.md
  target: decision/Five-Agent Sequential Pipeline for Clinical AI Summaries.md
  type: supports
- confidence: 0.9
  context: Fusion supports diagnostic pipeline
  source: decision/Abandon Non-LLM Fusion in Favor of LLM-Based Fusion.md
  target: decision/Five-Stage Sequential Agent Architecture for Diagnostic Prediction.md
  type: supports
- confidence: 0.7
  context: Shared multi-agent system design
  source: decision/Abandon Non-LLM Fusion in Favor of LLM-Based Fusion.md
  target: decision/Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints.md
  type: related-to
session: null
source: Research meeting discussion — Rami Khouri described pipeline evolution
source_date: '2026-02-22'
status: final
supports:
- '[[decision/Split AI Diagnostic Research Into Two Papers]]'
tags: []
type: decision
---

# Abandon Non-LLM Fusion in Favor of LLM-Based Fusion

## Context

The multi-agent diagnostic pipeline combines predictions from three sources (questionnaire S1, transcript S2, notes S3). A fusion step is needed to reconcile potentially different diagnoses from each source into a single prediction.

## Options Considered

1. **Non-LLM fusion (algorithmic)** — Combine S1+S2+S3 outputs using rule-based or statistical methods. Tested and abandoned — the model tended to just pick one source's diagnosis rather than truly synthesizing inputs.
2. **LLM-based fusion** — Use an LLM to see all source outputs and synthesize a combined diagnosis. Selected — produced significant improvement over non-LLM fusion.

## Decision

Abandon the non-LLM fusion approach and use LLM-based fusion exclusively. The LLM fusion agent receives outputs from all three prediction agents and produces a synthesized diagnosis.

## Rationale

The non-LLM fusion failed to meaningfully integrate multiple sources — it defaulted to selecting one source's output rather than weighing and combining evidence. The LLM-based approach demonstrated genuine synthesis capability, producing diagnoses that considered all inputs.

## Consequences

- The fusion stage requires LLM inference, adding cost and latency to the pipeline
- This design choice is documented in the methodology for Paper 2 (fusion and expert agent analysis)
- Validates the multi-agent LLM architecture as necessary — simpler approaches were insufficient

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]