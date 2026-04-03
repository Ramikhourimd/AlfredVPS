---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2026-02-22'
depends_on: []
description: The latest Excel file from Shmulik contains 6,041 records for the Dec
  2023 - Aug 2025 period, while the previous file for the same date range had approximately
  5,700. Must determine the cause before running final analyses.
due: null
janitor_note: LINK001 — Telia'z project link valid (YAML escaping false positive).
  related.base embed references missing _bases/related.base. DUP001 — possible duplicate
  of task/Investigate Sample Size Discrepancy Between Excel Exports.md.
kind: task
name: Investigate Sample Size Discrepancy Between Excel Files
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[task/Clean Outliers From Time-to-Treatment Data]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Investigate Sample Size Discrepancy Between Excel Files

Two data exports for the same date range (December 1, 2023 through August 31, 2025) show different record counts:
- Previous Excel: ~5,700 records
- Latest Excel (received 2026-02-22 morning): 6,041 records

This discrepancy must be understood before any analysis can be considered reliable. Possible causes: duplicate records, changed inclusion criteria, data processing differences.

Additionally, Rami's analysis was conducted on ~3,000 records — need to verify all analyses use the same dataset.

Noam flagged this issue. Resolution needed to ensure all analyses (demographic, time-to-treatment, diagnostic prediction) operate on the same verified dataset.

## Context

Raised in [[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]].

## Related
![[related.base#All]]

## Outcome
