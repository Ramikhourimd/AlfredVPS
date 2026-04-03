---
alfred_instructions: null
alfred_tags:
- analytics/session-timing
- data-export/8-column
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: 'Request Shmulik to provide summary approval timing data segmented into
  8 columns: intake 30min transcript, intake 30min real-time, intake 20min transcript,
  intake 20min real-time, follow-up 30min transcript, follow-up 30min real-time, follow-up
  20min transcript, follow-up 20min real-time.'
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Telia'z wikilink is valid (YAML escaping false positive).
kind: task
name: Request Segmented Timing Data From Shmulik
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[person/Shmulik]]'
relationships:
- confidence: 0.9
  context: Request leads to Get
  source: task/Request Segmented Timing Data From Shmulik.md
  target: task/Get 8-Column Timing Breakdown From Shmulik.md
  type: supports
- confidence: 0.85
  context: Request data needed for Prepare
  source: task/Request Segmented Timing Data From Shmulik.md
  target: task/Prepare Eight Column Timing Data Export.md
  type: supports
- confidence: 0.95
  context: Supports session frequency analysis request
  source: task/Request Segmented Timing Data From Shmulik.md
  target: note/Patient Treatment Duration and Session Frequency Analysis Request 2025-11-13.md
  type: supports
- confidence: 0.8
  context: Data request aids analysis
  source: task/Request Segmented Timing Data From Shmulik.md
  target: task/Analyze Patient Session Frequency by Treatment Period.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Request Segmented Timing Data From Shmulik

Request Shmulik to provide summary approval timing data with the following segmentation:

| Session Type | Duration | Mode |
|-------------|----------|------|
| Intake | 30 min | Transcript |
| Intake | 30 min | Real-time |
| Intake | 20 min | Transcript |
| Intake | 20 min | Real-time |
| Follow-up | 30 min | Transcript |
| Follow-up | 30 min | Real-time |
| Follow-up | 20 min | Transcript |
| Follow-up | 20 min | Real-time |

This enables comparison between before/after the real-time mode switch, as well as comparison against literature benchmarks (~10 min for clinical paperwork).

The key metric is: delta between session end time and summary approval time (not generate time).

## Context

- [[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]

## Related
![[related.base#All]]

## Outcome