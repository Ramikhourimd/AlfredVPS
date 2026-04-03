---
alfred_tags:
- ai/clinical-summaries
- metrics/approval-time
- clinical-efficiency
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
janitor_note: 'FIXED: project field corrected project/Teliaz → project/Telia''z AI
  Diagnostic Research Paper (canonical active record). FIXED: decided_by corrected
  person/Dekkel Khouri → person/Dekkel Taliaz (prior sweep). LINK001 — learn-decision.base
  embeds reference missing _bases/learn-decision.base — vault-wide structural gap.
  Body has DUPLICATE base view embeds (two sets) — cannot fix via vault CLI, needs
  manual removal of second set.'
name: Measure Summary Approval as Delta From Session End
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[task/Obtain Approval Time Data by Session Type]]'
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
relationships:
- confidence: 0.9
  context: Defines delta measure for efficiency metric
  source: decision/Measure Summary Approval as Delta From Session End.md
  target: decision/Use Summary Approval Time as Clinical Efficiency Metric.md
  type: supports
- confidence: 0.75
  context: Approval time defs/analysis at diff levels
  source: decision/Measure Summary Approval as Delta From Session End.md
  target: decision/Segment Summary Approval Time Analysis Into Eight Categories.md
  type: related-to
session: null
source: Research meeting 2026-02-22
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Measure Summary Approval as Delta From Session End

## Context

The research paper needs to report how quickly psychiatrists approve AI-generated clinical summaries. Two time periods exist in the data: a pre-change period (summary auto-generated post-session, psychiatrist opens later) and a post-change period (real-time generation during session). Measuring "generation to approval" is misleading because pre-change idle time inflates the metric.

## Options Considered

1. **Delta from summary generation to approval** — Misleading for pre-change period (includes hours/days of idle time before psychiatrist even opens the document)
2. **Delta from session end to approval** — Clinically meaningful: when does the patient's documentation get finalized?
3. **Delta from document open to approval (editing time)** — Possible via Google Drive audit logs but inconsistent quality

## Decision

Use session-end-to-approval as the primary metric. Present as before/after comparison: pre-change period shows significant delays (days), post-change period shows near-zero (approval happens during the session). Separately, compare editing time to literature benchmark of ~10 minutes per session.

## Rationale

Patient-centric metric that tells a clear story. In real-time mode, summaries are often approved before the session even formally ends, making the delta zero or negative. The before/after comparison demonstrates the system's operational impact.

## Consequences

- Rami to request 8-column segmented data from Shmulik: intake vs follow-up x 30min vs 20min x transcript (pre) vs real-time (post)
- Real-time period values near zero are the desired outcome, not an anomaly
- Literature comparison (~10 min paperwork per session) provides external benchmark

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]