---
alfred_tags:
- mental-health/diagnostics
- questionnaire-limitations
- dsm-coverage
confidence: high
confirmed_by:
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-assumption.base#Depends On This,
  #Related) reference _bases/learn-assumption.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).'
name: Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[project/Telia''z Clinic Israel]]'
source: Rami Khouri — known from questionnaire structure analysis
source_date: '2026-02-22'
status: active
type: assumption
---

# Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses

## Claim

The patient intake questionnaire primarily covers depression, anxiety, and PTSD symptoms. It lacks sufficient criteria to diagnose the full range of DSM conditions. The questionnaire correlates with PHQ (depression scale) but not with PCL (PTSD scale), confirming its limited diagnostic scope.

## Basis

- Structural analysis of the questionnaire content — limited to depression, anxiety, PTSD, and some sleep/eating questions
- Rami's earlier statistical analysis showing correlation with PHQ but not PCL
- Known upfront before the AI pipeline was built

## Evidence Trail

- 2026-02-22: Confirmed in meeting. Rami noted this was "known from the structure" before analysis began. Per-source prediction using questionnaire alone produced very low match rates.

## Impact

- Paper 1 will show questionnaire-only prediction is weak (expected result)
- Justifies the need for case manager transcript data as a richer source
- Supports the narrative that multiple data sources are necessary for accurate AI diagnosis

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]