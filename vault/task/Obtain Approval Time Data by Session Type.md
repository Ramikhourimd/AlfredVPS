---
alfred_instructions: null
alfred_tags:
- data/cleaning
- payroll/standardization
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-22'
depends_on: []
description: DUPLICATE — canonical record is task/Request Segmented Timing Data From
  Shmulik.md
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. All Telia'z wikilinks are valid (YAML escaping false positive).
  This is a DUPLICATE — canonical record is task/Request Segmented Timing Data From
  Shmulik.md.
kind: task
name: Obtain Approval Time Data by Session Type
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
relationships:
- confidence: 0.7
  context: Provides data for timing cleanup
  source: task/Obtain Approval Time Data by Session Type.md
  target: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  type: supports
- confidence: 0.65
  context: Data source for outlier detection
  source: task/Obtain Approval Time Data by Session Type.md
  target: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  type: supports
run: null
status: cancelled
tags: []
type: task
---

# Obtain Approval Time Data by Session Type

Request from Shmulik (data provider) a detailed breakdown of summary approval times across 8 categories:

| Session Type | Mode |
|-------------|------|
| Intake 30min | Transcript (pre-change) |
| Intake 30min | Real-time (post-change) |
| Intake 20min | Transcript |
| Intake 20min | Real-time |
| Follow-up 30min | Transcript |
| Follow-up 30min | Real-time |
| Follow-up 20min | Transcript |
| Follow-up 20min | Real-time |

Key metric: Delta between session end time and summary approval time. For real-time mode, this should be near zero or negative (sent before session ends).

For Paper 1: Compare pre/post real-time implementation and benchmark against literature (~10 min paperwork standard).

## Context

Rami already communicated this request to Shmulik. Follow up via [[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]].

## Related
![[related.base#All]]

## Outcome