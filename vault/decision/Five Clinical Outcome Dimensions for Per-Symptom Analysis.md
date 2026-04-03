---
approved_by: []
based_on:
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
- '[[note/Research Paper Scope and Data Extraction Plan 2025-11-09]]'
challenged_by: []
confidence: medium
created: '2026-03-14'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z project wikilink is valid (YAML escaping false positive).
  Constraint wikilink may be broken — verify path. Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist — vault-wide
  infrastructure gap. Body has DUPLICATE base view embeds (two sets of Based On +
  Related) — remove one set manually.'
name: Five Clinical Outcome Dimensions for Per-Symptom Analysis
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/Questionnaire Instrument Structurally Limited to PHQ Depression Anxiety
  and PCL-5 PTSD Domains]]'
session: ''
source: Research Paper Scope and Data Extraction Plan 2025-11-09
source_date: '2025-11-09'
status: draft
supports:
- '[[decision/Time-to-Treatment Correlation as Primary Paper 1 Analysis]]'
tags: []
type: decision
---

# Five Clinical Outcome Dimensions for Per-Symptom Analysis

## Context

After deciding to use per-symptom scoring instead of a composite score, the team needed to define which specific clinical outcome dimensions would be measured and reported. These dimensions needed to be extractable from session transcripts via NLP and clinically meaningful for the post-October 7th PTSD-dominant cohort.

## Options Considered

1. **Broad symptom inventory** — Track all DSM symptom criteria across all diagnoses
2. **PTSD-specific PCL-5 dimensions** — Track only standardized PTSD symptom clusters
3. **Functional and clinical hybrid** — Track a mix of functional outcomes and clinical symptoms most relevant to the cohort

## Decision

Five specific outcome dimensions were selected:
1. **Return to work** — Binary: returned / not returned
2. **Return home** (evacuees only) — Binary: returned / not returned
3. **Sleep improvement** — Self-reported reduction in sleep disturbances
4. **Flashback reduction** — Self-reported reduction in flashback frequency
5. **Clinician-reported improvement** — Psychiatrist clinical assessment

## Rationale

These dimensions combine functional outcomes (work, home) with core PTSD symptoms (sleep, flashbacks) and clinical judgment, providing a multi-perspective view of patient improvement. The functional outcomes are particularly relevant to the post-October 7th context where many patients were evacuees and/or unable to work.

## Consequences

- "Return home" only applies to the evacuee subgroup, creating a subgroup-specific analysis requirement
- NLP extraction pipeline must reliably identify these five dimensions in unstructured transcript text
- Binary outcomes (work, home) are straightforward; continuous outcomes (sleep, flashbacks) require threshold definitions
- Clinician-reported improvement depends on psychiatrist documentation consistency

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
