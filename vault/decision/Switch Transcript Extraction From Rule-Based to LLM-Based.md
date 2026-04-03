---
approved_by: []
based_on:
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — All wikilinks are valid (Telia''z and assumption links confirmed
  to exist; YAML escaping false positive). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist yet — create
  it to enable dynamic views.'
name: Switch Transcript Extraction From Rule-Based to LLM-Based
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related: []
session: null
source: Rami Khouri — methodology development
source_date: '2026-02-22'
status: final
supports:
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
tags: []
type: decision
---

# Switch Transcript Extraction From Rule-Based to LLM-Based

## Context

The AI diagnostic pipeline initially attempted to extract symptoms from case manager transcripts using strict rule-based parsing (no LLM). This approach proved too limited — it missed nuanced symptom descriptions and contextual information that case managers captured during DSM-oriented follow-up questioning.

## Options Considered

1. **Rule-based extraction (no LLM)** — Strict pattern matching against known symptom keywords. Simple, deterministic, but missed rich contextual data.
2. **LLM-based extraction** — Use a language model to interpret transcript content and extract symptoms with fuller context. More flexible, captures richer data.

## Decision

Switched to LLM-based extraction for case manager transcripts. Questionnaire extraction remains algorithmic/rule-based since questionnaire data is structured and well-defined.

## Rationale

Rule-based extraction was too strict and limited for unstructured transcript data. Case managers ask DSM-oriented follow-up questions that produce rich, varied symptom descriptions not easily captured by pattern matching. LLM extraction captures this richer signal, improving downstream diagnostic prediction.

## Consequences

- Transcript-based prediction (S2) became a stronger diagnostic source than questionnaire-only prediction (S1)
- Introduced LLM dependency in the extraction stage (previously only prediction stage used LLMs)
- Improved overall pipeline accuracy by enriching the symptom data available to prediction agents

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
