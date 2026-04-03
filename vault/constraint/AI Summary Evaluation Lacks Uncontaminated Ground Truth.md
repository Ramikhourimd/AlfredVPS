---
alfred_tags:
- psychiatry/ai-evaluation
- constraints/ground-truth
authority: Methodological limitation — anchoring bias in evaluation design
created: '2026-02-27'
janitor_note: 'Previous janitor_note was incorrect: Telia''z links are YAML apostrophe-escaping
  false positives — all link targets exist. Cleared by vault-janitor 2026-03-14.'
location: []
name: AI Summary Evaluation Lacks Uncontaminated Ground Truth
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
- '[[task/Review AI Summary Clinical Accuracy for Model Comparison]]'
relationships:
- confidence: 0.95
  context: Both lack reliable AI summary eval standards
  source: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  target: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  type: related-to
- confidence: 0.85
  context: GT lack depends on biased psychiatrist edits
  source: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  target: constraint/Psychiatrist Edits Biased by AI Model Received.md
  type: depends-on
- confidence: 0.85
  context: GT lack depends on biased psychiatrist edits
  source: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  target: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  type: depends-on
- confidence: 0.8
  context: Lack of GT justifies approval req
  source: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  target: constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval
    Before Patient Record Entry.md
  type: supports
- confidence: 0.7
  context: Informal feedback impacts GT quality
  source: constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth.md
  target: constraint/Psychiatrist AI Feedback Collected Through Informal WhatsApp
    Channel.md
  type: related-to
source: Yaron Goren methodological review during AI sprint meeting
source_date: '2025-01-16'
status: active
tags:
- ai-evaluation
- methodology
- bias
type: constraint
---

# AI Summary Evaluation Lacks Uncontaminated Ground Truth

## Constraint

The AI model evaluation framework for psychiatric summaries has no uncontaminated ground truth. The psychiatrist's final edited summary — the closest available reference standard — is biased by anchoring: psychiatrists edit based on whichever AI model output they received, not from an independent assessment.

## Source

Raised by external advisor Yaron Goren during the innovation sprint meeting on 2025-01-16. Yaron pointed out that a model that looks like a "7" in standalone scoring might look better or worse when directly compared to alternatives, and that the psychiatrist's edits are influenced by the AI output they started with.

## Implications

- All model comparison scores using psychiatrist-edited summaries as ground truth carry systematic bias
- Models that produce output closer to a psychiatrist's editing style may score higher regardless of clinical accuracy
- Pairwise comparison between models (head-to-head) may partially mitigate this by revealing relative quality differences
- A truly independent gold standard would require psychiatrists to write summaries from scratch without seeing any AI output — which is expensive and time-consuming
- This constraint may limit the validity of the entire AI model evaluation workstream unless addressed

## Expiry / Review

Active until either: (a) an independent gold standard methodology is established, or (b) the team explicitly accepts this limitation and adjusts interpretation of results accordingly.