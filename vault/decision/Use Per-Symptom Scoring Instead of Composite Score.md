---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2025-11-09'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
description: Clinical outcomes will be reported as individual per-symptom indicators
  rather than a single composite response score.
janitor_note: 'LINK001: Telia''z project wikilink uses YAML quote escaping (false
  positive). Base view embeds (learn-decision.base#Based On, #Related) reference _bases/
  which does not exist (vault-wide infrastructure gap). Embeds preserved. Related
  field contains duplicate entry for Find NLP Outcome Scoring Literature task.'
name: Use Per-Symptom Scoring Instead of Composite Score
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
session: null
source: conversation/Research Paper Scope and Methodology Planning Meeting 2025-11-09
source_date: '2025-11-09'
status: final
supports: []
tags: []
type: decision
---

# Use Per-Symptom Scoring Instead of Composite Score

## Decision

Clinical outcomes will be presented as individual per-symptom indicators rather than aggregated into a single composite score. Each symptom dimension (sleep improvement, flashback reduction, return to work, return home for evacuees, clinician-reported improvement) will be reported separately.

## Rationale

Dekkel argued that presenting per-symptom results is methodologically more defensible than declaring a single response/no-response threshold. It avoids the criticism that the composite scoring method lacks validation. The team may later develop a composite score as a secondary analysis, but the primary presentation will be per-symptom.

Rami had previously used a per-symptom approach for media reporting and proposed extending it with defined thresholds (e.g., 0-100 scale divided into no response, partial response, good response, full response). This secondary scoring approach was discussed but deferred pending Noam's literature review.

## Context

Rami's existing NLP pipeline already extracts per-symptom indicators from transcripts. The question was whether to also combine them.

## Made By

[[person/Dekkel Taliaz]] and [[person/Rami Khouri]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
