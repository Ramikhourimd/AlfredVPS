---
alfred_tags:
- psychiatry/ai-evaluation
- constraints/ground-truth
authority: Methodological limitation (circular reference in evaluation design)
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive:
  double single-quote is YAML escape for literal single quote). Base view embeds (learn-constraint.base#Affected
  Projects, learn-constraint.base#Related) reference _bases/learn-constraint.base
  which does not exist — vault-wide infrastructure gap, embeds preserved per policy.'
location: []
name: Psychiatrist Edits Biased by AI Model Received
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[task/Review AI Summary Clinical Accuracy for Model Comparison]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
relationships:
- confidence: 0.95
  context: Similar AI-induced bias in psychiatrist edits
  source: constraint/Psychiatrist Edits Biased by AI Model Received.md
  target: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  type: related-to
- confidence: 0.9
  context: Evidence of human GT contamination
  source: constraint/Psychiatrist Edits Biased by AI Model Received.md
  target: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  type: supports
- confidence: 0.9
  context: Evidence of human GT contamination
  source: constraint/Psychiatrist Edits Biased by AI Model Received.md
  target: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  type: supports
source: Yaron Goren methodological observation during sprint meeting
source_date: '2025-01-16'
status: active
type: constraint
---

# Psychiatrist Edits Biased by AI Model Received

## Constraint

The psychiatrist's final edited summary — used as the closest "gold standard" for evaluating AI model quality — is itself influenced by whichever AI model generated the initial draft. This creates a circular reference: the benchmark is contaminated by the thing being measured.

## Source

Yaron Goren raised this methodological concern during the innovation sprint meeting on 2025-01-16. When psychiatrists edit an AI-generated summary, their edits are shaped by what the AI produced. A psychiatrist reviewing an O1 output may make different edits than the same psychiatrist reviewing a Gemini output for the same patient session.

## Implications

- Direct model-to-edited-output comparison is methodologically compromised
- Each patient effectively has a different "gold standard" depending on which model was in production when their session was processed
- Pairwise model comparison (head-to-head) may partially mitigate this by revealing relative differences
- A truly independent gold standard would require psychiatrists to write summaries from scratch without seeing any AI output first — which is expensive and may not reflect realistic workflow conditions

## Expiry / Review

This constraint persists as long as the evaluation methodology relies on psychiatrist-edited AI outputs as the reference standard. Should be reviewed if an independent gold standard creation process is established.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]