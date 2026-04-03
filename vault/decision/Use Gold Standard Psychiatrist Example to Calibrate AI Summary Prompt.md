---
alfred_tags:
- ai/clinical-summaries/quality
approved_by: []
based_on:
- '[[note/Patient Data Research and AI Summary Quality Discussion 2025-11-11]]'
challenged_by: []
confidence: medium
created: '2026-03-09'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 false-positive: project/Teliaz AI Diagnostic Research Paper
  wikilink is valid (YAML single-quote escaping). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist — vault-wide
  infrastructure gap, embeds preserved per policy.'
name: Use Gold Standard Psychiatrist Example to Calibrate AI Summary Prompt
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Obtain Gold Standard AI Session Summary Example]]'
session: ''
source: Rami Khouri directive during 2025-11-11 meeting with Rivi Idelman
source_date: '2025-11-11'
status: draft
supports:
- '[[assumption/AI Summary System Excluded Case Manager Intake Data During Study Period]]'
tags: []
type: decision
---

# Use Gold Standard Psychiatrist Example to Calibrate AI Summary Prompt

## Context

During a 2025-11-11 meeting between Rami Khouri and Rivi Idelman, a critical quality gap was identified: the AI clinical summary system generates post-session summaries that ignore case manager intake data, producing summaries based only on the psychiatrist session. Psychiatrists had been raising complaints about summary quality in the clinical team WhatsApp group.

## Options Considered

1. **Gold standard example approach** — Have a psychiatrist create a single representative (non-real-patient) example showing ideal summary structure and content, then update the AI prompt accordingly
2. **Systematic quality audit** — Review all complaints, categorize issues, and address them individually
3. **Direct prompt engineering** — Modify the AI prompt based on complaint themes without a reference example

## Decision

A psychiatrist will provide a "gold standard" example of what a high-quality summary should look like — not from a real patient but a representative example showing ideal structure and content. Rivi Idelman will collect the example and forward it to the development team (Tav) so the AI prompt can be updated.

## Rationale

A concrete example provides an unambiguous reference for the development team, rather than abstract quality criteria that could be interpreted differently. This approach is also faster to implement than a systematic audit.

## Consequences

- AI summary quality improvement depends on a single example being sufficiently representative
- If the example doesn't capture the full range of quality issues, additional iterations may be needed
- Summary quality during the study period (before this fix) may differ from post-fix quality, creating a potential confound in research data

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]