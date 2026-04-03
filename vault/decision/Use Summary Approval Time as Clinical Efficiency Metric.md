---
alfred_tags:
- ai/clinical-summaries
- metrics/approval-time
- clinical-efficiency
approved_by: []
based_on:
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
- '[[assumption/Literature Benchmark of 10 Minutes Per Session for Clinical Paperwork]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z wikilink (project/Telia'z AI Diagnostic Research Paper)
  is valid (YAML escaping false positive). Base view embeds (learn-decision.base#Based
  On, learn-decision.base#Related) reference _bases/ files that do not exist — vault-wide
  infrastructure issue. Embeds preserved per rules.
name: Use Summary Approval Time as Clinical Efficiency Metric
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/Clinical Paperwork Literature Benchmark of 10 Minutes]]'
- '[[decision/Use Median With Outlier Cleaning for Timing Data]]'
session: '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
source: Discussion across multiple task records and meeting notes
source_date: '2026-02-22'
status: final
supports:
- '[[task/Obtain Approval Time Data by Session Type]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
tags: []
type: decision
---

# Use Summary Approval Time as Clinical Efficiency Metric

## Context

The AI diagnostic system generates clinical summaries that require psychiatrist approval before becoming part of the patient record. Two possible timing metrics exist: (1) time from session end to summary **generation**, and (2) time from session end to summary **approval**. The team needed to choose which metric to report in the paper as the measure of clinical efficiency.

## Options Considered

1. **Summary generation time** — Measures how fast the AI produces the summary. Easier to measure but does not reflect actual clinical workflow completion.
2. **Summary approval time** — Measures time from session end to psychiatrist approval. Captures the full clinical loop including human review.

## Decision

Use the delta between session end time and summary **approval** time as the primary clinical efficiency metric. Not generation time.

## Rationale

Approval time captures the complete clinical workflow — from session completion through AI generation to psychiatrist sign-off. This is the metric that matters for patient care (when the summary is actually usable) and for comparison against the literature benchmark of ~10 minutes for clinical paperwork. Generation time alone would miss the human review bottleneck.

## Consequences

- All timing data requests to Shmulik must include approval timestamps, not just generation timestamps
- The 8-category timing segmentation (intake/follow-up × 20/30min × transcript/real-time) measures approval time
- Real-time mode comparison depends on approval time being near-zero or negative (sent before session ends)
- Literature comparison against 10-minute benchmark uses approval time

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]