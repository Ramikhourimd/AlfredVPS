---
alfred_instructions: null
alfred_tags:
- clinic/operations
- retool/prioritization
- admin/handover
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: 'Compile a prioritized list of must-have Retool system improvements for
  H1 2026, incorporating feedback from psychiatrists, secretaries, and clinic operations
  staff. Covers three tracks: critical fixes, new system UI, and new functionality.'
due: null
janitor_note: 'LINK001: \![[related.base#All]] embed references missing base file.
  Embed preserved. Teliaz project ref is valid (YAML escaping false positive).'
kind: task
name: Compile Retool Improvement Priority List
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[person/Shachar]]'
- '[[task/Gather Clinic Staff System Requirements]]'
relationships:
- confidence: 0.95
  context: Both create Retool priority lists
  source: task/Compile Retool Improvement Priority List.md
  target: task/Create Retool Priority List for First Six Months.md
  type: related-to
- confidence: 0.85
  context: Needs clinic staff requirements
  source: task/Compile Retool Improvement Priority List.md
  target: task/Gather Clinic Staff System Requirements.md
  type: depends-on
- confidence: 0.85
  context: Needs sec and clinic requirements
  source: task/Compile Retool Improvement Priority List.md
  target: task/Gather Secretary and Clinic Staff System Requirements.md
  type: depends-on
- confidence: 0.75
  context: Requires prior role alignment
  source: task/Compile Retool Improvement Priority List.md
  target: task/Shira and Rana to Align on Role Boundaries and Handover Schedule.md
  type: depends-on
- confidence: 0.8
  context: Needs resp docs for Retool priorities
  source: task/Compile Retool Improvement Priority List.md
  target: task/Document Secretarial Responsibilities and Assignments.md
  type: depends-on
- confidence: 0.8
  context: Needs resp docs for Retool priorities
  source: task/Compile Retool Improvement Priority List.md
  target: task/Document Secretary Responsibilities and Case Threads.md
  type: depends-on
- confidence: 0.6
  context: Secretary ops context for Retool
  source: task/Compile Retool Improvement Priority List.md
  target: task/Hand Over Weekly Secretary Meetings From Shira to Rana.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Compile Retool Improvement Priority List

Rami needs to compile a structured priority list for the Retool system rebuild, organized into three tracks agreed upon with Shachar:

1. **Critical fixes for H1 2026** — KPIs, Teams integration, login issues, secretary workflow needs
2. **New system UI design** — how the rebuilt interface should look and work
3. **New functionality** — additional features beyond current capabilities

Input sources: meetings with Renee and secretaries, clinic staff feedback, Stav's initial list, personal operational experience.

## Context

Emerged from [[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]] where Shachar requested clear requirements to guide development priorities.

## Related
![[related.base#All]]

## Outcome

To be completed — priority list document ready for review discussion with Shachar.