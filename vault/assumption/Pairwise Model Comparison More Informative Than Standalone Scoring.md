---
alfred_tags:
- ai-evaluation/clinical-summaries
- llm/scoring-methods
- model-comparison/pairwise
based_on:
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-27'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which may not exist — vault-wide infrastructure issue, embeds preserved. ORPHAN001
  — no inbound links noted but assumption is actively referenced by related assumptions.'
name: Pairwise Model Comparison More Informative Than Standalone Scoring
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[assumption/One Enhancement Cycle Sufficient to Reach Near-Final Prompt Quality]]'
relationships:
- confidence: 0.85
  context: Pairwise more informative than standalone
  source: assumption/Pairwise Model Comparison More Informative Than Standalone Scoring.md
  target: assumption/LLM-Based Evaluator Can Reliably Score Clinical Summary Quality.md
  type: contradicts
source: Yaron Goren, external advisor
source_date: '2025-01-16'
status: active
tags:
- ai-evaluation
- methodology
type: assumption
---

# Pairwise Model Comparison More Informative Than Standalone Scoring

## Claim

Comparing AI-generated psychiatric summaries head-to-head (pairwise) captures quality differences that are lost when each model is scored independently against a rubric. A model scoring "7" in isolation might look clearly better or worse when directly compared to alternatives.

## Basis

Raised by Yaron Goren during the 2025-01-16 sprint meeting as a methodological concern. This is a well-established principle in evaluation methodology (relative comparison often reveals finer distinctions than absolute scoring), but has not been validated specifically for clinical summary evaluation.

## Evidence Trail

- 2025-01-16: Yaron raised the pairwise comparison point during AI model evaluation discussion
- Team decided to start with independent scoring but consider adding pairwise comparison later

## Impact

If true, the current evaluation methodology (standalone rubric scoring) may miss important quality differences between O1, O1 Med, and Gemini 2.0 Flash. This could lead to selecting a suboptimal model. The evaluation framework may need to be expanded to include pairwise comparison rounds.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]