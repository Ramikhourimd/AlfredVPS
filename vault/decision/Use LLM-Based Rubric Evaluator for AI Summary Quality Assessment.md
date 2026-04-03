---
alfred_tags:
- ai/clinical-evaluation
- evaluation/methodology
approved_by: []
based_on:
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML apostrophe escaping false
  positive). Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which may not exist — vault-wide issue, embeds preserved. BODY — duplicate base
  view embeds at end of file; delete everything after the first \![[learn-decision.base#Related]]
  line (remove the --- separator and second set of embeds).'
name: Use LLM-Based Rubric Evaluator for AI Summary Quality Assessment
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/One Enhancement Cycle Sufficient to Reach Near-Final Prompt Quality]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
- '[[decision/Start AI Model Evaluation With Independent Scoring Before Pairwise]]'
session: ''
source: Rami Khouri built and demonstrated the evaluation framework
source_date: '2025-01-16'
status: final
supports:
- '[[task/Review AI Summary Clinical Accuracy for Model Comparison]]'
tags: []
type: decision
---

# Use LLM-Based Rubric Evaluator for AI Summary Quality Assessment

## Context

The innovation team needed a scalable way to evaluate quality of AI-generated psychiatric summaries across multiple models and patients. Manual clinical review by psychiatrists does not scale and introduces its own biases.

## Options Considered

1. **Manual psychiatrist review** — Each summary reviewed and scored by a clinician
2. **LLM-based automated evaluator** — An LLM evaluator prompt scores summaries against defined rubric criteria
3. **Hybrid** — Automated scoring with periodic manual spot-checks

## Decision

Option 2 with elements of 3: Rami built a rubric-based evaluation framework where each summary section (Status, Discussion, Recommendations) is scored against defined criteria by an LLM evaluator prompt. Yaron provides manual clinical review as external advisor for validation.

## Rationale

Automated evaluation scales across models and patients without requiring psychiatrist time for every comparison. The rubric makes scoring criteria explicit and reproducible. Yaron's clinical expertise provides a validation layer without being the bottleneck.

## Consequences

- Evaluation can run at scale across all patients and models
- Rubric quality becomes the key variable — poor rubric criteria produce misleading scores
- Dependency on the evaluator LLM's ability to assess clinical quality
- Need periodic calibration between automated scores and clinical judgment

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]