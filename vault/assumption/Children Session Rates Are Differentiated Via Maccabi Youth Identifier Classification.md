---
based_on:
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-02-26'
invalidated_by: []
janitor_note: 'LINK001 — All non-base wikilinks verified present (Telia''z YAML escaping
  false positive, decision/Centralize... exists). Base view embeds (learn-assumption.base#Depends
  On This, #Related) reference _bases/learn-assumption.base which does not exist —
  vault-wide infrastructure gap, embeds preserved. ORPHAN001 — no inbound links, expected
  for assumption derived from specific notes.'
name: Children Session Rates Are Differentiated Via Maccabi Youth Identifier Classification
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Standardize Payment Data to Binary Attendance Classification]]'
- '[[decision/Centralize Psychiatrist Payment Processing Into Standardized Unified
  Format]]'
source: Rami and Basel payroll review session
source_date: '2025-12-04'
status: active
tags: []
type: assumption
---

# Children Session Rates Are Differentiated Via Maccabi Youth Identifier Classification

## Claim

The clinic payment formula differentiates between adult and child patient sessions using MCY (Maccabi Youth) identifiers in the patient name field. Children sessions trigger a separate, higher payment rate for psychiatrists. This classification is a derived column added during data processing, not a native field in the clinic management system.

## Basis

During the 2025-12-04 payroll review, Basel and Rami documented the payment calculation logic. An adult/child classification column was added to the payment spreadsheet using MCY identifiers to differentiate session types. The classification directly drives payment differentiation for intake and follow-up sessions, triggering the "children session rate" when applicable.

## Evidence Trail

- 2025-12-04: Payment data review session confirmed MCY-based classification drives rate differentiation

## Impact

If MCY identifiers are missing or incorrectly applied, psychiatrists may be underpaid for children sessions or overpaid for adult sessions. Any system migration or automation of payment processing must preserve this classification logic. The accuracy of the children rate depends entirely on correct MCY tagging in source data.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
