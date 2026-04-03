---
alfred_instructions: null
alfred_tags:
- patient-sessions/data-analysis
- timing-frequency/metrics
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-11-13'
depends_on: []
description: Build analysis table showing patient treatment duration vs session count
  with interval-based comparison of meeting frequency between early and late treatment
  periods
due: null
janitor_note: LINK001 — Telia'z wikilinks are YAML escaping false positives — targets
  verified to exist. Base view embed (related.base#All) references _bases/related.base
  which does not exist — vault-wide infrastructure issue; embed preserved.
kind: task
name: Analyze Patient Session Frequency by Treatment Period
priority: medium
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[note/Patient Treatment Duration and Session Frequency Analysis Request 2025-11-13]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[project/Telia''z Clinic Israel]]'
relationships:
- confidence: 0.85
  context: Analysis requires timing breakdown
  source: task/Analyze Patient Session Frequency by Treatment Period.md
  target: task/Get 8-Column Timing Breakdown From Shmulik.md
  type: depends-on
- confidence: 0.8
  context: Analysis requires timing export
  source: task/Analyze Patient Session Frequency by Treatment Period.md
  target: task/Prepare Eight Column Timing Data Export.md
  type: depends-on
- confidence: 0.65
  context: Analysis requires requested data
  source: task/Analyze Patient Session Frequency by Treatment Period.md
  target: task/Request Segmented Timing Data From Shmulik.md
  type: depends-on
- confidence: 1.0
  context: Supports session frequency analysis request
  source: task/Analyze Patient Session Frequency by Treatment Period.md
  target: note/Patient Treatment Duration and Session Frequency Analysis Request 2025-11-13.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Analyze Patient Session Frequency by Treatment Period

Build a data analysis table that shows how patient session frequency changes over the course of treatment.

## Requirements

1. Create a table with columns for:
   - Patient identifier (de-identified)
   - Total days in treatment
   - Total number of sessions attended
   - Average session frequency (sessions per time unit)

2. Implement interval-based temporal analysis:
   - Define time intervals across each patient's treatment timeline
   - Use a sliding window (forward-backward range) for each interval
   - Calculate average session frequency within each window

3. Compare early-period vs late-period frequency:
   - Split treatment duration into early and late phases
   - Calculate average meeting frequency for each phase
   - Determine whether there is a statistically meaningful difference

## Context

Requested by Rami via voice memo on 2025-11-13. This analysis informs understanding of patient engagement trajectories and supports discharge protocol design and research paper methodology.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — summary table and key findings on session frequency trends.