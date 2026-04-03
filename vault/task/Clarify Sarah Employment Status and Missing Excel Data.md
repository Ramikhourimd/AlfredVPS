---
alfred_instructions: null
alfred_tags:
- hr/payroll
- employees/compensation
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Sarah (93 NIS/hr hourly worker) has no Excel file in the batch Shira
  sent. Need to confirm whether Sarah is still actively working clinically, and if
  not, update her agreement accordingly. Send email to Shira after vacation.
due: null
janitor_note: '"LINK001 — base embed \![[related.base#All]] target may not exist (system-level
  base file issue). Project link [[project/Telia''z Clinic Israel]] is valid (scanner
  false positive from YAML quote escaping). ORPHAN001 — no inbound links, consider
  linking from project or conversation records."'
kind: task
name: Clarify Sarah Employment Status and Missing Excel Data
priority: medium
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[person/Shira]]'
- '[[conversation/Psychiatrist Payment Data Review and Cleanup 2025-12-04]]'
relationships:
- confidence: 0.9
  context: Clarification requires status verification
  source: task/Clarify Sarah Employment Status and Missing Excel Data.md
  target: task/Verify Sarah Employment Status at Clinic.md
  type: depends-on
- confidence: 0.6
  context: Employee data and admin tasks
  source: task/Clarify Sarah Employment Status and Missing Excel Data.md
  target: task/Remind Jenny to Log Training Hours.md
  type: related-to
- confidence: 0.6
  context: Both HR/payroll tasks
  source: task/Clarify Sarah Employment Status and Missing Excel Data.md
  target: task/Compensate Rivi February 2026 Overtime Hours.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Clarify Sarah Employment Status and Missing Excel Data

Sarah is an hourly worker at 93 NIS/hour who worked months 11-12 but Shira did not include her Excel file in the payroll batch. Need to determine:

1. Is Sarah still actively working clinically?
2. If not working clinically, her agreement (scan) needs to be re-examined
3. Send email to Shira after her vacation (returns Tuesday) requesting the missing data

## Context

Identified during the 2025-12-04 payroll review session. Sarah's data gap was noticed when reviewing the batch of Excels Shira sent for all staff.

## Related
![[related.base#All]]

## Outcome