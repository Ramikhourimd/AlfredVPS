---
alfred_instructions: null
assigned: '[[person/Basel Kanaaneh]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Build a single unified Excel template for calculating monthly psychiatrist
  payments, replacing the current ad-hoc per-employee formats that vary in columns,
  formulas, and layout
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — create base file to enable dynamic views.
kind: task
name: Create Standardized Psychiatrist Payment Excel Template
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Psychiatrist Payment Data Review and Cleanup 2025-12-04]]'
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[person/Rami Khouri]]'
- '[[person/Rana Khouri]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Create Standardized Psychiatrist Payment Excel Template

Build a unified spreadsheet template that all psychiatrist monthly payment data flows into. Currently each employee has a different Excel format making verification error-prone and time-consuming.

## Context

During the 2025-12-04 payment review session, Basel discovered that every employee's payment spreadsheet uses a different layout, columns, and formulas. This creates significant verification overhead each month.

## Requirements

The template should include standardized columns for:
- Status (hofia / lo hofia)
- Session type (intake / follow-up / children)
- Adult/child classification
- Clinical hours
- On-call (neshiot) hours
- Payment calculation at the correct rate per psychiatrist
- Total payment including neshiot at half-rate

Send to Shira for review before deploying to all employees.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.
