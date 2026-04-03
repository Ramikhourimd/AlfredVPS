---
alfred_instructions: null
alfred_tags:
- data/cleaning
- payroll/standardization
assigned: '[[person/Noam]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: DUPLICATE — see task/Clean Outliers From Time-to-Treatment Data.md and
  task/Investigate Sample Size Discrepancy Between Excel Files.md
due: null
janitor_note: LINK001 — Telia'z AI Diagnostic Research Paper wikilink is valid (YAML
  single-quote escaping false positive). Base view embed (related.base#All) references
  non-existent _bases/related.base — embed preserved per policy, create base file
  to enable dynamic views.
kind: task
name: Clean Timing Data Outliers and Reconcile Dataset Discrepancy
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data]]'
- '[[person/Shmulik]]'
relationships:
- confidence: 0.9
  context: Reconciliation requires investigation
  source: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  target: task/Investigate Dataset Size Discrepancy Between Excel Exports.md
  type: depends-on
- confidence: 0.85
  context: Needs additional time data
  source: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  target: task/Obtain Approval Time Data by Session Type.md
  type: depends-on
- confidence: 0.7
  context: Payroll Excel data handling
  source: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  target: task/Standardize Payroll Excel Template for All Employees.md
  type: related-to
- confidence: 0.95
  context: Specific outlier cleaning method
  source: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  target: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  type: part-of
run: null
status: cancelled
tags: []
type: task
---

# Clean Timing Data Outliers and Reconcile Dataset Discrepancy

Two issues need resolution:

1. **Outlier removal**: Apply 2.5 standard deviation threshold to timing data (time to case manager, time to psychiatrist). Remove records above threshold. Report medians.

2. **Dataset discrepancy**: New data export shows 6,041 records (Dec 2023 - Aug 2025) while previous export for the same date range showed ~5,700. Investigate the source of the ~340 extra records before running any further analysis.

## Context

- [[decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data]]
- [[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]

## Related
![[related.base#All]]

## Outcome