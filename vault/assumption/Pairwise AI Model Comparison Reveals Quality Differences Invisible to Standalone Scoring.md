---
alfred_tags:
- ai-evaluation/clinical-summaries
- llm/scoring-methods
- model-comparison/pairwise
based_on:
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001: Base view embeds reference missing _bases/ files — vault-wide
  infrastructure gap. ORPHAN001: No inbound wikilinks; consider linking from a relevant
  project or decision record.'
name: Pairwise AI Model Comparison Reveals Quality Differences Invisible to Standalone
  Scoring
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[decision/Use Independent Scoring Before Pairwise Comparison for AI Model Evaluation]]'
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
- '[[person/Yaron Goren]]'
relationships:
- confidence: 0.9
  context: Reveals diffs invisible to standalone scoring
  source: assumption/Pairwise AI Model Comparison Reveals Quality Differences Invisible
    to Standalone Scoring.md
  target: assumption/LLM-Based Evaluator Can Reliably Score Clinical Summary Quality.md
  type: contradicts
- confidence: 0.9
  context: Specific mechanism for greater informativeness
  source: assumption/Pairwise AI Model Comparison Reveals Quality Differences Invisible
    to Standalone Scoring.md
  target: assumption/Pairwise Model Comparison More Informative Than Standalone Scoring.md
  type: supports
source: Yaron Goren advisory input
source_date: '2025-01-16'
status: active
type: assumption
---

# Pairwise AI Model Comparison Reveals Quality Differences Invisible to Standalone Scoring

## Claim

When evaluating AI-generated psychiatric summaries across models (O1, O1 Med, Gemini 2.0 Flash), comparing models head-to-head (pairwise/relative comparison) captures quality differences that are lost when each model is scored independently against a rubric. A model scoring "7" in isolation might look clearly better or worse when directly compared to alternatives.

## Basis

Yaron Goren raised this as a methodological concern during the 2025-01-16 innovation sprint meeting. His reasoning: absolute scoring against a rubric may miss subtle quality differences that become apparent only in direct comparison — differences in clinical reasoning depth, language precision, or recommendation specificity that a numerical rubric may not capture.

## Evidence Trail

- 2025-01-16: Yaron's advisory input during sprint meeting, leading to the decision to start with independent scoring but plan for pairwise comparison as enhancement

## Impact

- Current evaluation methodology (independent scoring) may underestimate quality gaps between models
- Pairwise comparison should be added as a second evaluation pass
- Could change which model is selected for production use
- Relevant to the broader AI summary quality gap that has been unresolved since November 2025