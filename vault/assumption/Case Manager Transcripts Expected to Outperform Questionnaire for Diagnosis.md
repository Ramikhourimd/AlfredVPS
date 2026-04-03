---
alfred_tags:
- mental-health/diagnosis
- data-sources/transcripts
- data-sources/questionnaires
based_on:
- '[[assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'LINK001 — Fixed project field: Teliaz → Telia''z AI Diagnostic Research
  Paper (missing apostrophe). Base view embeds (learn-assumption.base#Depends On This,
  #Related) reference _bases/learn-assumption.base which does not exist — systemic
  issue, embeds preserved. Telia''z wikilink in related is valid (YAML escaping false
  positive). ORPHAN001 — no inbound wikilinks from other records.'
name: Case Manager Transcripts Expected to Outperform Questionnaire for Diagnosis
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[project/Telia''z Clinic Israel]]'
relationships:
- confidence: 0.7
  context: Transcripts outperform despite easy questionnaire extraction
  source: assumption/Case Manager Transcripts Expected to Outperform Questionnaire
    for Diagnosis.md
  target: assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured
    Format.md
  type: related-to
source: Rami Khouri — research meeting discussion
source_date: '2026-02-22'
status: active
type: assumption
---

# Case Manager Transcripts Expected to Outperform Questionnaire for Diagnosis

## Claim

The case manager transcript (S2 agent) is expected to produce better diagnostic predictions than the patient questionnaire (S1 agent), because case managers ask DSM-informed follow-up questions that cover a broader diagnostic spectrum.

## Basis

The patient questionnaire has known structural limitations — it covers depression, anxiety, and PTSD well but has limited questions for other diagnoses (sleep disorders, eating disorders, etc.). Case managers, by contrast, conduct open-ended intake sessions informed by DSM criteria, allowing them to probe symptoms across the full diagnostic spectrum. This broader clinical coverage should translate to better predictive input.

## Evidence Trail

- 2026-02-22: Rami stated S2 is "expected to perform better due to DSM-informed questioning by case managers"
- Questionnaire confirmed as weak predictor (see Questionnaire Alone Is Insufficient Predictor)
- Formal comparison results pending — will be included in Paper 1

## Impact

If confirmed, this validates the multi-source pipeline design and justifies the added complexity of transcript processing. If not confirmed, it would challenge the assumption that richer clinical data necessarily improves AI diagnostic accuracy.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]