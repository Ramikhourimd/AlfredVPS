---
alfred_instructions: null
alfred_tags:
- analytics/session-timing
- data-export/8-column
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-22'
depends_on: []
description: 'Request from Shmulik a timing data export split into 8 columns: intake
  30min transcript, intake 30min real-time, intake 20min transcript, intake 20min
  real-time, follow-up 30min transcript, follow-up 30min real-time, follow-up 20min
  transcript, follow-up 20min real-time. This enables comparison across session types
  and before/after the real-time change.'
due: null
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — create it to enable dynamic views. ORPHAN001 — no inbound wikilinks; consider
  linking from project/Telia'z AI Diagnostic Research Paper.
kind: task
name: Prepare Eight Column Timing Data Export
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Shmulik]]'
relationships:
- confidence: 0.9
  context: Export prep needs breakdown data
  source: task/Prepare Eight Column Timing Data Export.md
  target: task/Get 8-Column Timing Breakdown From Shmulik.md
  type: depends-on
- confidence: 0.85
  context: Export needs requested segmented data
  source: task/Prepare Eight Column Timing Data Export.md
  target: task/Request Segmented Timing Data From Shmulik.md
  type: depends-on
- confidence: 0.95
  context: Supports session frequency analysis request
  source: task/Prepare Eight Column Timing Data Export.md
  target: note/Patient Treatment Duration and Session Frequency Analysis Request 2025-11-13.md
  type: supports
- confidence: 0.8
  context: Export supports frequency analysis
  source: task/Prepare Eight Column Timing Data Export.md
  target: task/Analyze Patient Session Frequency by Treatment Period.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Prepare Eight Column Timing Data Export

Coordinate with Shmulik to produce a timing data export with 8 columns distinguishing between intake/follow-up, short/long session, and transcript/real-time operational modes. This is needed to compare summary approval times before and after the real-time system change.

## Context

Rami identified that comparing approval times requires separating by session type (intake 30min, intake 20min, follow-up 30min, follow-up 20min) and by operational mode (transcript-first vs real-time). This gives 8 comparison columns that allow the paper to show improvement from the real-time change.

## Related
![[related.base#All]]

## Outcome