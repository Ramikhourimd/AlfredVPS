---
authority: internal process gap
created: '2026-02-25'
janitor_note: '"LINK001 — (1) Telia''z wikilink is YAML escaping false positive (target
  likely exists). (2) Base view embeds (\![[learn-constraint.base#Affected Projects]]
  and \![[learn-constraint.base#Related]]) reference _bases/learn-constraint.base
  which does not exist. Embeds preserved per policy."'
name: Inconsistent Excel Formats Across Psychiatrist Payment Reports
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Psychiatrist Payment Data Review and Cleanup 2025-12-04]]'
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[task/Create Standardized Psychiatrist Payment Excel Template]]'
source: operational gap
source_date: '2025-12-04'
status: active
type: constraint
---

# Inconsistent Excel Formats Across Psychiatrist Payment Reports

## Constraint

Each psychiatrist's monthly payment spreadsheet uses a different format — different columns, formulas, and layout. This makes monthly payment verification extremely time-consuming and error-prone.

## Source

Discovered by Basel Kanaaneh during the 2025-12-04 payment data review session when comparing multiple employees' Excel files side by side.

## Implications

- Monthly payment verification takes significantly longer than necessary
- Higher risk of calculation errors due to inconsistent formulas
- Difficult for new staff (like Basel) to audit payments independently
- Blocking efficient handoff of payment processing responsibilities

## Expiry / Review

Will be resolved when [[task/Create Standardized Psychiatrist Payment Excel Template]] is completed and deployed across all employees.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
