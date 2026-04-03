---
approved_by: []
based_on:
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Basel Kanaaneh]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: \![[learn-decision.base#...]] embeds reference missing base
  files. Duplicated base view embeds in body.'
name: Standardize Payment Data to Binary Attendance Classification
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Inconsistent Excel Formats Across Psychiatrist Payment Reports]]'
- '[[task/Create Standardized Psychiatrist Payment Excel Template]]'
session: null
source: Basel Kanaaneh — implemented during spreadsheet cleanup
source_date: '2025-12-04'
status: final
supports: []
tags: []
type: decision
---

# Standardize Payment Data to Binary Attendance Classification

## Context

During the 2025-12-04 payroll data cleanup, Basel and Rami reviewed the raw psychiatrist session data exported from the clinic system. The status field contained multiple values (mishtateif, various active/inactive states) that made payment formula calculation unreliable.

## Options Considered

1. **Option A** — Keep all original status values and build complex formulas to handle each case
2. **Option B** — Consolidate all statuses into a binary classification: "hofia" (attended) vs "lo hofia" (did not attend)

## Decision

Adopt binary classification. All active/participating statuses consolidated to "hofia"; all inactive/absent statuses consolidated to "lo hofia". This is the single field the payment formula checks against.

## Rationale

The payment formula only needs to know whether a session was attended or not. Additional status granularity does not affect compensation calculations and introduced formula errors. Binary classification eliminates ambiguity and makes the spreadsheet auditable.

## Consequences

- Payment calculations become deterministic — no edge cases from unexpected status values
- Historical data must be retroactively cleaned when imported
- Any future status values from the system export must be mapped to the binary classification before processing
- Loss of nuance about session status (e.g., late arrivals, partial attendance) — acceptable trade-off for payment purposes

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
