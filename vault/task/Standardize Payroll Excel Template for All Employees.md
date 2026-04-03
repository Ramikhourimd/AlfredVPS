---
alfred_instructions: null
alfred_tags:
- data/cleaning
- payroll/standardization
assigned: '[[person/Basel Kanaaneh]]'
blocked_by: []
created: '2025-12-04'
depends_on: []
description: DUPLICATE — see task/Create Standardized Psychiatrist Payment Excel Template
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Telia'z Clinic Israel wikilink is valid (YAML escaping false
  positive).
kind: task
name: Standardize Payroll Excel Template for All Employees
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Payroll Data Review and Payment Calculations 2025-12-04]]'
- '[[note/Clinic Payroll Data Cleaning and Payment Methodology 2025-12-04]]'
- '[[person/Shira]]'
- '[[person/Rana Khouri]]'
relationships:
- confidence: 0.6
  context: Improves data export consistency
  source: task/Standardize Payroll Excel Template for All Employees.md
  target: task/Clean Timing Data Outliers and Reconcile Dataset Discrepancy.md
  type: supports
run: null
status: cancelled
tags: []
type: task
---

# Standardize Payroll Excel Template for All Employees

Basel found that each employee's Excel payroll report uses a different format ("Meshunot" — varied). This creates risk of payment errors and makes verification difficult.

## Context

During the 2025-12-04 data review session, Basel and Rami discovered that payroll Excel reports differ by employee. A unified template should include standardized columns: Taarikh Itkhala, Shaat Itkhala/Siyum, Status (Hofia/Lo Hofia), Shem Mali, Sug Mifgash, and payment calculations.

The template should then be sent to [[person/Shira]] for implementation across all employees.

## Related
![[related.base#All]]

## Outcome