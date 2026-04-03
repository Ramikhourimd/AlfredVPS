---
alfred_instructions: null
alfred_tags:
- data/cleaning
- payroll/standardization
assigned: '[[person/Noam]]'
blocked_by: []
created: '2026-02-22'
depends_on: []
description: DUPLICATE — canonical record is task/Clean Outliers From Time-to-Treatment
  Data.md
due: null
janitor_note: 'LINK001: related.base embed references _bases/related.base which does
  not exist yet. Create the base file to enable dynamic views. Telia''z wikilink is
  valid YAML escaping false positive. ORPHAN001: no inbound wikilinks detected.'
kind: task
name: Clean Timing Data Outliers at 2.5 SD Threshold
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[decision/Use Median With Outlier Cleaning for Timing Data]]'
relationships:
- confidence: 0.95
  context: Specific outlier cleaning task
  source: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  target: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  type: part-of
- confidence: 0.75
  context: Data quality and size issues
  source: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  target: task/Investigate Dataset Size Discrepancy Between Excel Exports.md
  type: related-to
- confidence: 0.8
  context: Requires approval times
  source: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  target: task/Obtain Approval Time Data by Session Type.md
  type: depends-on
run: null
status: cancelled
tags: []
type: task
---

# Clean Timing Data Outliers at 2.5 SD Threshold

Remove timing data outliers using 2.5 standard deviation threshold. Current data shows extreme outliers (300+ day waits) that are clearly technical errors. Apply to all timing metrics and recalculate medians.

## Context

Data shows high variance with outliers up to 388 hours/300+ days. These are likely unclosed patient records or technical errors. The team agreed to use 2.5 SD as the outlier threshold.

## Related
![[related.base#All]]

## Outcome