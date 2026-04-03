---
alfred_tags:
- mental-health/diagnosis
- data-sources/transcripts
- data-sources/questionnaires
based_on:
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'ORPHAN001: No inbound wikilinks found. LINK001 Teliaz refs are false
  positives (YAML escaping). Review whether this assumption is referenced elsewhere
  or should be linked from a note/decision.'
name: Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Questionnaire Alone Is Insufficient Predictor for Full DSM Coverage]]'
- '[[assumption/Questionnaire Alone Is a Weak Diagnostic Predictor]]'
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
relationships:
- confidence: 0.9
  context: DSM questioning strengthens transcripts vs questionnaire
  source: assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger
    Diagnostic Source.md
  target: assumption/Case Manager Transcripts Expected to Outperform Questionnaire
    for Diagnosis.md
  type: supports
- confidence: 0.6
  context: Contrasting transcript vs questionnaire strengths
  source: assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger
    Diagnostic Source.md
  target: assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured
    Format.md
  type: related-to
source: Rami Khouri — pipeline design rationale
source_date: '2026-02-22'
status: active
type: assumption
---

# Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic Source

## Claim

Case manager transcripts contain richer diagnostic signal than patient questionnaires because case managers ask DSM-oriented follow-up questions during intake interviews. This structured clinical probing captures symptoms across a broader diagnostic spectrum than the self-report questionnaire, which is limited to depression, anxiety, and PTSD screening instruments.

## Basis

Rami described across multiple meetings that transcript-based prediction (S2) outperforms questionnaire-based prediction (S1). The stated reason is that case managers are trained to ask follow-up questions aligned with DSM diagnostic criteria, producing transcripts that cover more diagnostic categories than the fixed questionnaire. This was the rationale for investing in LLM-based transcript extraction despite the simpler rule-based extraction being sufficient for questionnaires.

## Evidence Trail

- 2026-02-22: Rami presented pipeline results showing transcript agent outperforms questionnaire agent. Attributed to DSM-oriented questioning by case managers.
- Multiple meeting notes consistently describe case managers as asking "DSM-style follow-up questions" — this phrase appears in at least three separate records.

## Impact

This assumption underpins the entire pipeline hierarchy: questionnaire is acknowledged as a weak predictor, while transcript is treated as the strongest single-source predictor. If case managers are not actually asking DSM-oriented questions consistently, transcript prediction quality would degrade. The assumption also justifies the decision to use LLM-based extraction for transcripts (richer, more varied data requires more flexible extraction).