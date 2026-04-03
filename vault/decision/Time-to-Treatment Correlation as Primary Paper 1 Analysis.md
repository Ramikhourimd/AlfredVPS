---
alfred_tags:
- research/paper-scope
- telepsychiatry/ptsd
approved_by: []
based_on:
- '[[assumption/Early Treatment Seekers Have Higher Recovery Rates]]'
- '[[assumption/Majority of Patients Have PTSD Diagnosis]]'
- '[[note/Research Paper Scope and Data Extraction Plan 2025-11-09]]'
challenged_by: []
confidence: high
created: '2026-03-14'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 false positives: Telia''z wikilinks use valid YAML single-quote
  escaping. Base view embeds (learn-decision.base) reference _bases/ files that do
  not exist yet — vault-wide infrastructure gap, not a per-file issue. Duplicate base
  view embeds after --- separator need manual cleanup. Preserving all embeds per policy.'
name: Time-to-Treatment Correlation as Primary Paper 1 Analysis
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Limit Paper to Four or Five Figures Maximum]]'
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
relationships:
- confidence: 0.85
  context: Defines primary analysis for scope
  source: decision/Time-to-Treatment Correlation as Primary Paper 1 Analysis.md
  target: note/Research Paper Scope and Data Extraction Plan 2025-11-09.md
  type: supports
session: ''
source: Rami Khouri during paper scope planning
source_date: '2025-11-09'
status: final
supports:
- '[[decision/Focus First Paper on System Presentation and PTSD Outcomes]]'
tags: []
type: decision
---

# Time-to-Treatment Correlation as Primary Paper 1 Analysis

## Context

Paper 1 needed a primary analytical contribution beyond descriptive system presentation and demographic reporting. The post-October 7th patient cohort has natural variation in when patients entered treatment relative to the trauma event, creating an opportunity for time-based outcome analysis.

## Options Considered

1. **Time-to-treatment correlation** — Correlate elapsed time from trauma event to first treatment session with per-symptom clinical improvement indicators
2. **AI prediction accuracy as primary finding** — Focus on diagnostic prediction performance (deferred to Paper 2)
3. **Composite outcome scoring** — Create a 0-100 aggregate score with response thresholds (deferred pending literature review)

## Decision

The correlation between elapsed time from trauma event to first treatment session and clinical improvement indicators will serve as Paper 1's primary analytical contribution, forming the third layer of the paper alongside system overview and patient demographics.

## Rationale

This analysis leverages the unique post-October 7th cohort where all patients share a common trauma event date, creating a natural experiment. The time-to-treatment variable is cleanly measurable from structured data, and the per-symptom outcome indicators provide clinical granularity without requiring a composite score methodology.

## Consequences

- Requires validated timing data (time from October 7th to first session) for all included patients
- Outcome measures must be extractable and quantifiable per patient
- Statistical significance of the correlation will determine the paper's impact
- If no significant correlation exists, the paper's analytical contribution is substantially weakened

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]