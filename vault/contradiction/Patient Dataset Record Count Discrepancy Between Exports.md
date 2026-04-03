---
alfred_tags:
- organizational/disputes
- staffing/conflicts
- metrics/discrepancies
claim_a: Previous data export showed approximately 5,700 patient records for Dec 2023
  - Aug 2025 date range
claim_b: New data export from Shmulik shows 6,041 records for the same Dec 2023 -
  Aug 2025 date range
created: '2026-02-25'
janitor_note: LINK001 — Telia'z wikilinks valid (YAML escaping false positive). learn-contradiction.base
  embed references missing _bases/learn-contradiction.base. ORPHAN001 — no inbound
  links.
name: Patient Dataset Record Count Discrepancy Between Exports
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[person/Noam]]'
- '[[person/Shmulik]]'
- '[[task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy]]'
source_a: Previous Excel export from Shmulik
source_b: New Excel export received 2026-02-22
status: unresolved
type: contradiction
---

# Patient Dataset Record Count Discrepancy Between Exports

## Claim A

Previous data export showed approximately 5,700 patient intake records for the inclusion period (December 1, 2023 to August 31, 2025).

## Claim B

New data export received on 2026-02-22 from Shmulik shows 6,041 records for the same date range (first case: December 1, 2023; cutoff: August 31, 2025). Additionally, Rami's AI pipeline analysis was run on only ~3,000 records.

## Analysis

A ~340 record discrepancy between two exports of the same date range suggests either:
1. Different filtering/inclusion criteria between exports
2. Data retroactively added to the system for the covered period
3. A bug in one of the export queries
4. Different definitions of what constitutes a "record" (e.g., unique patients vs. intake events)

Additionally, ~25% of records are missing timing data for case manager, with the percentage increasing for psychiatrist timing — this may relate to the count discrepancy.

This must be resolved before finalizing any analysis, as running statistics on inconsistent datasets undermines the paper's validity.

## Resolution

Pending — Noam to investigate with Shmulik.

![[learn-contradiction.base#Related]]