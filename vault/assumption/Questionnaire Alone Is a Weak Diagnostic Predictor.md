---
alfred_tags:
- mental-health/diagnostics
- questionnaire-limitations
- dsm-coverage
confidence: high
confirmed_by:
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
created: '2026-02-22'
janitor_note: LINK001 — learn-assumption.base embeds reference missing _bases/learn-assumption.base
  file. Embeds preserved per janitor rules. Telia'z wikilinks are valid (YAML escaping
  false positive).
name: Questionnaire Alone Is a Weak Diagnostic Predictor
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs]]'
relationships:
- confidence: 0.92
  context: Shared theme of weak questionnaire prediction
  source: assumption/Questionnaire Alone Is a Weak Diagnostic Predictor.md
  target: assumption/Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses.md
  type: related-to
source: Rami Khouri - structural analysis of questionnaire coverage
source_date: '2026-02-22'
status: active
type: assumption
---

# Questionnaire Alone Is a Weak Diagnostic Predictor

## Claim

The patient intake questionnaire used in the Telia'z clinic system is structurally limited as a diagnostic predictor because it only covers a subset of DSM diagnoses — primarily depression (PHQ), anxiety, and PTSD (PCL). It lacks sufficient criteria to predict other diagnoses like psychotic disorders, eating disorders, or specific sleep disorders.

## Basis

- Known a priori from the questionnaire's design — it was not built as a comprehensive diagnostic tool
- Confirmed by prediction accuracy results: questionnaire-only agent (S1) shows very low accuracy outside depression/anxiety/PTSD
- PHQ correlated with AI-extracted symptoms but PCL did not — suggesting even PTSD prediction is weak
- This limitation is precisely why case manager transcripts were added as a second data source

## Evidence Trail

- 2026-02-22: Rami confirmed in meeting that "we know from its structure that it's not a good predictive tool"
- Sample size analysis previously showed no correlation between questionnaire scores and PCL
- PHQ correlation exists, suggesting depression symptoms are captured but trauma symptoms are not

## Impact

- Justifies the multi-source approach (questionnaire + transcript + notes)
- Paper 1 will present questionnaire-only results as a baseline showing limitations
- Supports the argument that AI-extracted transcript symptoms add significant diagnostic value

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]