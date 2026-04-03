---
alfred_instructions: null
alfred_tags:
- data/cleaning
- payroll/standardization
assigned: '[[person/Noam]]'
blocked_by: []
created: '2026-02-22'
depends_on: []
description: DUPLICATE — canonical record is task/Investigate Sample Size Discrepancy
  Between Excel Files.md
due: null
janitor_note: LINK001 wikilinks with Telia'z are YAML-escape false positives (Telia''z
  → Telia'z). Base embed targets (related.base) do not exist — vault-wide infrastructure
  gap. Swept 2026-02-27.
kind: task
name: Investigate Dataset Size Discrepancy Between Excel Exports
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Shmulik]]'
relationships:
- confidence: 0.9
  context: Reconciles dataset size issues
  source: task/Investigate Dataset Size Discrepancy Between Excel Exports.md
  target: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  type: part-of
- confidence: 0.75
  context: Both address timing dataset issues
  source: task/Investigate Dataset Size Discrepancy Between Excel Exports.md
  target: task/Clean Timing Data Outliers at 2.5 SD Threshold.md
  type: related-to
run: null
status: cancelled
tags: []
type: task
---

# Investigate Dataset Size Discrepancy Between Excel Exports

Two data exports from Shmulik for the same inclusion period (Dec 1 2023 to Aug 31 2025) show different record counts: 6041 vs ~5700. This discrepancy must be understood before running final analyses.

## Context

Noam flagged that the newer export has more records despite covering the same date range. Rami noted he analyzed only ~3000 records for his part. Need to confirm all analyses are aligned on the same dataset.

## Related
![[related.base#All]]

## Outcome