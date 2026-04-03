---
alfred_instructions: null
alfred_tags:
- clinic/operations
- retool/prioritization
- admin/handover
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-12-05'
depends_on: []
description: Compile a prioritized list of critical Retool improvements needed for
  the first six months. Include KPI requirements, system fixes, secretary/admin needs,
  and CRM status review. Schedule meetings with Renee, secretaries, and clinic staff
  to gather input.
due: null
janitor_note: '"LINK001 — base embed \![[related.base#All]] target may not exist (system-level
  base file issue). Project link [[project/Telia''z AI Clinical Platform]] is valid
  (scanner false positive from YAML quote escaping)."'
kind: task
name: Create Retool Priority List for First Six Months
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool Improvements and Data Access Planning 2025-12-05]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[person/Shachar]]'
relationships:
- confidence: 0.85
  context: Needs clinic staff requirements
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Gather Clinic Staff System Requirements.md
  type: depends-on
- confidence: 0.85
  context: Needs sec and clinic requirements
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Gather Secretary and Clinic Staff System Requirements.md
  type: depends-on
- confidence: 0.75
  context: Requires prior role alignment
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Shira and Rana to Align on Role Boundaries and Handover Schedule.md
  type: depends-on
- confidence: 0.95
  context: Variant Retool priority list tasks
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Compile Retool Improvement Priority List.md
  type: related-to
- confidence: 0.8
  context: Needs resp docs for priorities
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Document Secretarial Responsibilities and Assignments.md
  type: depends-on
- confidence: 0.8
  context: Needs resp docs for priorities
  source: task/Create Retool Priority List for First Six Months.md
  target: task/Document Secretary Responsibilities and Case Threads.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Create Retool Priority List for First Six Months

Compile a comprehensive prioritized list of what is critical for the Retool system in the first six months. This list should cover:
- KPI dashboard requirements
- System stability fixes (login, Teams)
- Secretary/admin tool needs
- CRM implementation status review

## Context

Emerged from [[conversation/Retool Improvements and Data Access Planning 2025-12-05]] with [[person/Shachar]]. Stav had started documenting secretary requirements — incorporate that work. Schedule meetings with Renee and clinic staff to gather requirements from each group.

## Related
![[related.base#All]]

## Outcome