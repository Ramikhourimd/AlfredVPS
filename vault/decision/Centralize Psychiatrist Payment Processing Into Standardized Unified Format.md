---
approved_by: []
based_on:
- '[[constraint/Inconsistent Excel Formats Across Psychiatrist Payment Reports]]'
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Basel Kanaaneh]]'
janitor_note: 'LINK001 false positives: Telia''z wikilinks are valid (YAML escaping).
  Base view embeds (learn-decision.base) reference missing _bases/ file. ORPHAN001
  — no inbound links. BODY DUPLICATION: entire body content (Context, Options Considered,
  Decision, Rationale, Consequences sections + base view embeds) is duplicated after
  a horizontal rule — needs manual cleanup to remove the duplicate block.'
name: Centralize Psychiatrist Payment Processing Into Standardized Unified Format
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[note/Staff Rate Review and Work Hour Audit 2025-12-04]]'
session: null
source: Basel and Rami payroll review session
source_date: '2025-12-04'
status: final
supports:
- '[[decision/Standardize Payment Data to Binary Attendance Classification]]'
tags: []
type: decision
---

# Centralize Psychiatrist Payment Processing Into Standardized Unified Format

## Context

Each psychiatrist's monthly payment data was arriving in a different Excel format with inconsistent columns, formulas, and layouts. Basel's onboarding as Operations Manager exposed the impossibility of efficient payroll processing without standardization.

## Options Considered

1. **Continue per-psychiatrist formats** — Each psychiatrist keeps their existing spreadsheet format; Shira reconciles manually each month
2. **Standardize to unified format** — Create a single template with standardized columns, status values, and calculation formulas; all psychiatrists use the same format

## Decision

Adopt a unified spreadsheet format with standardized columns. Specific changes implemented during the 2025-12-04 session:
- Remove duplicate date fields (keep creation date, drop end date)
- Consolidate all attendance status values to binary "hofia"/"lo hofia" (attended/did not attend)
- Add derived adult/child classification column using MCY identifiers
- Remove confusing "soug mifgash" (meeting type) field
- Standardize clinical hour rate, session type counting, and on-call hour calculations

## Rationale

The inconsistent formats created a systemic bottleneck: every monthly payroll cycle required manual reconciliation across different spreadsheet structures. With ~176 individual clinicians projected at target scale, this manual approach is unsustainable.

## Consequences

- Basel can process all psychiatrist payments using a single workflow
- Discrepancies between agreements and actual rates become visible through uniform data
- Future automation of payroll calculations becomes feasible
- Requires one-time migration of all existing psychiatrist data to the new format

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]

# Centralize Psychiatrist Payment Processing Into Standardized Unified Format

## Context

Each psychiatrist's monthly payment data was arriving in a different Excel format with inconsistent columns, formulas, and layouts. Basel's onboarding as Operations Manager exposed the impossibility of efficient payroll processing without standardization.

## Options Considered

1. **Continue per-psychiatrist formats** — Each psychiatrist keeps their existing spreadsheet format; Shira reconciles manually each month
2. **Standardize to unified format** — Create a single template with standardized columns, status values, and calculation formulas; all psychiatrists use the same format

## Decision

Adopt a unified spreadsheet format with standardized columns. Specific changes implemented during the 2025-12-04 session:
- Remove duplicate date fields (keep creation date, drop end date)
- Consolidate all attendance status values to binary "hofia"/"lo hofia" (attended/did not attend)
- Add derived adult/child classification column using MCY identifiers
- Remove confusing "soug mifgash" (meeting type) field
- Standardize clinical hour rate, session type counting, and on-call hour calculations

## Rationale

The inconsistent formats created a systemic bottleneck: every monthly payroll cycle required manual reconciliation across different spreadsheet structures. With ~176 individual clinicians projected at target scale, this manual approach is unsustainable.

## Consequences

- Basel can process all psychiatrist payments using a single workflow
- Discrepancies between agreements and actual rates become visible through uniform data
- Future automation of payroll calculations becomes feasible
- Requires one-time migration of all existing psychiatrist data to the new format

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]
