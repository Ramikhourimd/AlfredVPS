---
alfred_tags:
- psychiatry/ai-evaluation
- constraints/ground-truth
authority: Evaluation methodology limitation
created: '2026-02-27'
janitor_note: LINK001 — Telia'z Innovation Program wikilink is valid (YAML single-quote
  escaping false positive).
location: []
name: Psychiatrist Edits Biased by AI Output They Received
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[assumption/LLM-Based Evaluator Can Reliably Score Clinical Summary Quality]]'
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
- '[[task/Review AI Summary Clinical Accuracy for Model Comparison]]'
relationships:
- confidence: 0.9
  context: Evidence of human GT contamination
  source: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  target: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  type: supports
- confidence: 0.9
  context: Evidence of human GT contamination
  source: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  target: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  type: supports
source: Yaron Goren methodological observation
source_date: '2025-01-16'
status: active
tags:
- ai-evaluation
- methodology
- bias
type: constraint
---

# Psychiatrist Edits Biased by AI Output They Received

## Constraint

The psychiatrist's final edited summary — used as the closest approximation to a "gold standard" for evaluating AI model quality — is inherently biased by whichever AI model generated the initial draft. Psychiatrists edit what they receive, meaning their corrections are anchored to the AI output rather than being independent clinical judgments.

## Source

Yaron Goren raised this as a methodological caveat during the 2025-01-16 innovation sprint meeting. When evaluating AI models by comparing their output to the psychiatrist's edited version, the evaluation is circular: the "ideal" output was shaped by the AI input.

## Implications

- No truly independent gold standard exists for per-patient AI summary evaluation
- Model comparison results may be systematically biased toward whichever model was deployed in production at the time
- To obtain unbiased reference summaries, psychiatrists would need to write summaries from scratch without seeing any AI output — a significantly more expensive process
- This constraint directly challenges the [[assumption/Gold Standard Example Will Fix AI Summary Quality]] assumption

## Expiry / Review

This constraint persists as long as the evaluation methodology relies on psychiatrist-edited AI outputs as ground truth. It would be resolved by implementing a blinded evaluation protocol where clinicians produce summaries independently of AI output.