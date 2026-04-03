---
alfred_instructions: null
alfred_tags:
- clinic/operations
- kpi-improvement
assigned: '[[person/Basel Kanaaneh]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Average patient wait time has reached 14 days with a rising trend as
  of January 2026. Investigate root causes and propose corrective action.
due: null
janitor_note: 'LINK001 — [[person/Basel Khouri]] does not exist. Nearest match: [[person/Basel
  Kanaaneh]]. Verify if this is the correct person and update assigned field. Telia''z
  wikilinks in project/related are valid (YAML escaping false positive). Base view
  embed (related.base#All) references _bases/related.base which does not exist yet.'
kind: task
name: Investigate Rising Average Wait Time at Clinic Israel
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Israel KPI Dashboard January 2026]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
- '[[constraint/Secretarial Capacity Is Critically Low]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.95
  context: Investigation before addressing
  source: task/Investigate Rising Average Wait Time at Clinic Israel.md
  target: task/Address Rising Average Wait Time at Clinic Israel.md
  type: supports
- confidence: 0.6
  context: investigation may prompt volume increase
  source: task/Investigate Rising Average Wait Time at Clinic Israel.md
  target: task/Increase Monthly Session Volume to 100 Target.md
  type: supports
- confidence: 0.6
  context: investigation may prompt volume increase
  source: task/Investigate Rising Average Wait Time at Clinic Israel.md
  target: task/Increase Monthly Session Volume to Target 100.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Investigate Rising Average Wait Time at Clinic Israel

The January 2026 KPI dashboard flags the average wait time at 14 days with a rising trend. This needs immediate investigation to prevent patient attrition and potential HMO contract compliance issues.

## Context

- Average wait time: 14 days (rising trend, flagged as warning)
- Nearest available appointment: 3 days (normal — suggests the issue is average, not worst-case)
- Monthly sessions at 82% of target (82/100) — capacity may be a factor
- Known constraint: secretarial capacity is critically low, potentially bottlenecking scheduling

## Investigation Areas

1. Is the bottleneck in psychiatrist availability or scheduling administration?
2. Are specific time slots or providers disproportionately driving the average up?
3. What is the trajectory — how quickly is the average rising month-over-month?
4. Does the 3-day nearest availability mean some slots open but patients prefer specific times/providers?

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.