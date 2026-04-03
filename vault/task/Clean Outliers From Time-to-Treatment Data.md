---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2026-02-22'
depends_on: []
description: Remove statistical outliers from time-to-treatment data using 2.5 standard
  deviation threshold. Affects time-to-case-manager and time-to-psychiatrist columns.
  Report median values after cleaning.
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. All Telia'z wikilinks are valid (YAML escaping false positive).
kind: task
name: Clean Outliers From Time-to-Treatment Data
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[task/Investigate Sample Size Discrepancy Between Excel Files]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Clean Outliers From Time-to-Treatment Data

Remove records with time values exceeding 2.5 standard deviations from the mean. Current data contains extreme outliers (170+ hours, 300+ days) that distort averages — likely data artifacts from patients left in waiting lists or technical recording errors.

After cleaning, report median values (not mean) due to remaining skew.

## Context

Discussed in [[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]. Current unfiltered data:
- Mean time to case manager: ~2 weeks
- Median time to case manager: 8 days
- Mean time to psychiatrist: 25 days
- Median time to psychiatrist: 16 days (8+8)

Assigned to Noam (statistician). Must verify cleaned results align with IRB commitments (originally specified ~3-5 days).

## Related
![[related.base#All]]

## Outcome
