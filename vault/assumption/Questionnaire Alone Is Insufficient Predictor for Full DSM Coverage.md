---
alfred_tags:
- mental-health/diagnostics
- questionnaire-limitations
- dsm-coverage
confidence: high
confirmed_by:
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
created: '2026-02-22'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — create base file to enable dynamic views.'
name: Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.95
  context: Similar critiques of questionnaire efficacy
  source: assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage.md
  target: assumption/Questionnaire Alone Is a Weak Diagnostic Predictor.md
  type: related-to
- confidence: 0.95
  context: Overlapping claims on DSM prediction limits
  source: assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage.md
  target: assumption/Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses.md
  type: related-to
source: AI diagnostic pipeline analysis by Rami Khouri
source_date: '2026-02-22'
status: confirmed
type: assumption
---

# Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage

## Claim

The patient self-report questionnaire, while useful for depression, anxiety, and PTSD screening, does not contain sufficient criteria to reliably predict the full range of DSM diagnoses. Its structure inherently limits diagnostic coverage.

## Basis

The questionnaire primarily contains questions targeting depression (PHQ), anxiety, and PTSD. For conditions outside these three areas (sleep disorders, eating disorders, etc.) there are not enough criteria to generate a meaningful diagnostic prediction. This was known from the questionnaire's design before the analysis confirmed it.

## Evidence Trail

- 2026-02-22: Rami confirmed that prediction accuracy using questionnaire alone was very low, as expected from its structural limitations
- PHQ scores correlated with depression measures but not with PCL (PTSD checklist), further confirming the questionnaire's depression-centric coverage

## Impact

This assumption supports the decision to add case manager transcript data as a second input source, and validates the multi-source approach of the diagnostic pipeline.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]