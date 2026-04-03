---
alfred_tags:
- ai/clinical-summaries
- metrics/approval-time
- clinical-efficiency
approved_by: []
based_on:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are YAML escaping false positives. STRUCTURAL
  FIX NEEDED: Body contains DUPLICATE base view embeds after --- separator at end
  of file. Remove the second ---/\![[learn-decision.base#Based On]]/\![[learn-decision.base#Related]]
  block manually. CLI cannot replace body content. Base view embeds reference _bases/learn-decision.base
  which does not exist.'
name: Measure Summary Approval Time Not Generation Time
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
- '[[constraint/Clinical Paperwork Literature Benchmark of 10 Minutes]]'
relationships:
- confidence: 0.85
  context: Both define summary approval time aspects
  source: decision/Measure Summary Approval Time Not Generation Time.md
  target: decision/Measure Summary Approval as Delta From Session End.md
  type: related-to
- confidence: 0.9
  context: Clarifies approval time for metric use
  source: decision/Measure Summary Approval Time Not Generation Time.md
  target: decision/Use Summary Approval Time as Clinical Efficiency Metric.md
  type: supports
- confidence: 0.8
  context: Approval time metrics at measure/segment levels
  source: decision/Measure Summary Approval Time Not Generation Time.md
  target: decision/Segment Summary Approval Time Analysis Into Eight Categories.md
  type: related-to
session: null
source: Rami Khouri - pipeline design decision
source_date: '2026-02-22'
status: final
supports:
- '[[task/Obtain Approval Time Data by Session Type]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
tags: []
type: decision
---

# Measure Summary Approval Time Not Generation Time

## Context

The AI system generates clinical summaries either from transcripts (post-session) or in real-time (during session). Two potential metrics exist for measuring clinical efficiency: (1) time from session end to summary generation, and (2) time from session end to psychiatrist approval of the summary. The team needed to decide which metric to report in the paper.

## Options Considered

1. **Summary generation time** — When the AI produces the summary. Faster to measure but doesn't reflect clinical workflow completion.
2. **Summary approval time** — When the psychiatrist reviews and approves the summary. Reflects actual clinical workflow completion and is the point at which the summary becomes a clinical record.

## Decision

Use the delta between session end time and summary approval time as the key metric for clinical efficiency. Summary generation time is not the meaningful endpoint.

## Rationale

The clinically meaningful moment is when the psychiatrist approves the summary — this is when it enters the patient record and the clinical workflow is complete. In real-time mode, summaries may be generated before the session ends (negative delta), but what matters is when the psychiatrist signs off. This also enables direct comparison against the literature benchmark of ~10 minutes for clinical paperwork.

## Consequences

The 8-column timing data request to Shmulik specifically asks for approval time deltas. Real-time mode should show near-zero or negative approval times (summary ready before session ends), making the comparison with transcript mode more dramatic.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]