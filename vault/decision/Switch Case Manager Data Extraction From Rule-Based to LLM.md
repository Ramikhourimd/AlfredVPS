---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 FIXED: project field previously corrected. Telia''z wikilinks
  valid (YAML escaping). Base view embeds reference missing _bases/learn-decision.base
  — vault-wide issue, embeds preserved. BODY FIX REQUIRED: Duplicate base embed sections
  after --- separator (learn-decision.base#Based On and #Related appear twice) — remove
  the --- separator and second pair of embeds manually. ORPHAN001: No inbound wikilinks
  — consider linking from project or conversation records. Swept 2026-03-30, re-swept
  2026-04-01.'
name: Switch Case Manager Data Extraction From Rule-Based to LLM
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[project/Telia''z Clinic Israel]]'
session: null
source: Research meeting discussion — Rami Khouri described pipeline evolution
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Switch Case Manager Data Extraction From Rule-Based to LLM

## Context

The diagnostic pipeline requires symptom extraction from case manager transcripts before prediction agents can operate. Two extraction approaches were tested.

## Options Considered

1. **Rule-based extraction (no LLM)** — Strict algorithmic extraction from transcripts. Initially attempted but yielded poor data capture due to the unstructured nature of conversational transcripts.
2. **LLM-based extraction** — Use an LLM to parse transcripts and extract symptoms. Selected for better data capture.

## Decision

Use LLM-based extraction for case manager transcripts. Rule-based extraction is retained only for the patient questionnaire, where the structured format makes algorithmic extraction sufficient.

## Rationale

Unlike the patient questionnaire (which has a clear, rule-based structure), case manager transcripts are conversational and unstructured. Case managers ask DSM-informed follow-up questions, but the responses and clinical observations are embedded in natural language that rule-based parsers cannot reliably extract.

## Consequences

- Two different extraction methods in the pipeline: algorithmic for questionnaires, LLM for transcripts and notes
- Adds LLM inference cost at the extraction stage (not just prediction)
- Must be documented clearly in the methodology section as a design decision with rationale

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
