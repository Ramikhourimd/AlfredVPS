---
alfred_tags:
- mental-health/diagnosis
- data-sources/transcripts
- data-sources/questionnaires
based_on:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-02-26'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide infrastructure gap. Embeds preserved.'
name: Questionnaire Extraction Is Purely Algorithmic Due to Structured Format
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage]]'
relationships:
- confidence: 0.8
  context: Algo limits questionnaire vs transcripts
  source: assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured
    Format.md
  target: assumption/Case Manager Transcripts Expected to Outperform Questionnaire
    for Diagnosis.md
  type: supports
source: Rami Khouri — pipeline architecture presentation
source_date: '2026-02-22'
status: active
tags:
- methodology
- extraction
type: assumption
---

# Questionnaire Extraction Is Purely Algorithmic Due to Structured Format

## Claim

The patient intake questionnaire has a sufficiently structured and rule-based format that symptom extraction can be performed algorithmically without requiring an LLM. This contrasts with the case manager transcript and notes, which require LLM-based extraction.

## Basis

Stated consistently across all three meeting note records from the 2026-02-22 research session. Rami described the questionnaire extraction as using "a simple algorithm (no LLM needed) due to clear, rule-based structure." The questionnaire covers depression, anxiety, and PTSD with structured response fields that map directly to symptom presence.

## Evidence Trail

- 2026-02-22: Confirmed in pipeline presentation — questionnaire uses algorithmic extraction while transcript required upgrade from rule-based to LLM-based due to unstructured nature.
- Contrast case: Case manager transcript initially attempted rule-based extraction but failed ("too strict"), necessitating LLM-based extraction. This strengthens the claim that the questionnaire's structure is qualitatively different.

## Impact

- Determines pipeline architecture: S1 (questionnaire agent) uses no LLM, reducing cost and latency for that branch.
- If the questionnaire format changes to include free-text fields, this assumption would be invalidated and S1 would need LLM extraction.
- The algorithmic nature makes S1 results fully deterministic and reproducible, unlike LLM-based agents.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]