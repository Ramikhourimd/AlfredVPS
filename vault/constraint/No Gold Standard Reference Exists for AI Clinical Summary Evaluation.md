---
alfred_tags:
- psychiatry/ai-evaluation
- constraints/ground-truth
authority: Inherent limitation of current evaluation process
created: '2026-02-27'
janitor_note: LINK001 — Telia'z Innovation Program wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist yet — vault-wide infrastructure
  gap. ORPHAN001 — No inbound links; human review needed to connect this constraint
  to relevant projects.
location: []
name: No Gold Standard Reference Exists for AI Clinical Summary Evaluation
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[decision/Start AI Evaluation With Independent Scoring Before Pairwise Comparison]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
relationships:
- confidence: 0.85
  context: No gold std depends on biased edits
  source: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  target: constraint/Psychiatrist Edits Biased by AI Model Received.md
  type: depends-on
- confidence: 0.85
  context: No gold std depends on biased edits
  source: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  target: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  type: depends-on
- confidence: 0.75
  context: Informal channel hinders gold std
  source: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  target: constraint/Psychiatrist AI Feedback Collected Through Informal WhatsApp
    Channel.md
  type: related-to
source: Methodological limitation identified during sprint meeting
source_date: '2025-01-16'
status: active
tags:
- ai-evaluation
- methodology
- ground-truth
type: constraint
---

# No Gold Standard Reference Exists for AI Clinical Summary Evaluation

## Constraint

There is no independent ground truth or gold standard example for evaluating AI-generated psychiatric summaries. The closest reference is the psychiatrist's final edited version, but this is biased — the psychiatrist edits are influenced by whichever AI model output they received, creating a circular dependency.

## Source

Identified during the 2025-01-16 innovation sprint meeting. Yaron Goren raised the caveat that psychiatrist edits are contaminated by the AI output they saw. Each patient needs a "ground truth" ideal output for scoring, but none currently exists.

## Implications

- All evaluation scores are relative, not absolute — there is no objective "correct" summary to score against
- The evaluation rubric must compensate for the lack of ground truth by defining quality criteria independently
- Creating a true gold standard would require psychiatrists to write summaries from scratch without seeing any AI output, which is resource-intensive
- The related assumption that "one gold standard example will fix AI summary quality" may be harder to fulfill than expected

## Expiry / Review

This constraint persists until a gold standard creation process is established. Review when the AI evaluation methodology is formalized.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]