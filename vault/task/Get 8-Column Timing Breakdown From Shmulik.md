---
alfred_instructions: null
alfred_tags:
- analytics/session-timing
- data-export/8-column
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: 'Request timing data from Shmulik broken into 8 columns: Intake 30min
  transcript, Intake 30min real-time, Intake 20min transcript, Intake 20min real-time,
  Follow-up 30min transcript, Follow-up 30min real-time, Follow-up 20min transcript,
  Follow-up 20min real-time. This allows before/after comparison and intake vs follow-up
  analysis.'
due: null
janitor_note: LINK001 — _bases/related.base does not exist yet; base view embed non-functional.
  Telia'z project wikilink is valid (YAML single-quote escaping false positive). ORPHAN001
  — no inbound links; review whether parent project or person should reference this
  task.
kind: task
name: Get 8-Column Timing Breakdown From Shmulik
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
- '[[person/Shmulik]]'
relationships:
- confidence: 0.8
  context: Breakdown requires segmented request
  source: task/Get 8-Column Timing Breakdown From Shmulik.md
  target: task/Request Segmented Timing Data From Shmulik.md
  type: depends-on
- confidence: 0.95
  context: Data from Get used in Prepare
  source: task/Get 8-Column Timing Breakdown From Shmulik.md
  target: task/Prepare Eight Column Timing Data Export.md
  type: supports
- confidence: 0.95
  context: Supports session frequency analysis request
  source: task/Get 8-Column Timing Breakdown From Shmulik.md
  target: note/Patient Treatment Duration and Session Frequency Analysis Request 2025-11-13.md
  type: supports
- confidence: 0.85
  context: Data required for session analysis
  source: task/Get 8-Column Timing Breakdown From Shmulik.md
  target: task/Analyze Patient Session Frequency by Treatment Period.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Get 8-Column Timing Breakdown From Shmulik

Request detailed timing data split by session type and mode to enable before/after comparison of the real-time summary feature.

## Context

Discussed at 2026-02-22 meeting. The key metric is time from session end to summary approval. Two operational periods exist (transcript mode vs real-time mode), and sessions vary by type (intake vs follow-up) and duration (20 vs 30 minutes).

## Related
![[related.base#All]]

## Outcome