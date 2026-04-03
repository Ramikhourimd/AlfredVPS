---
alfred_instructions: null
alfred_tags:
- clinic/operations
- kpi-improvement
assigned: '[[person/Basel Kanaaneh]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Average wait time has reached 14 days with rising trend as of January
  2026. Investigate root cause (psychiatrist capacity, scheduling bottleneck, or secretarial
  throughput) and develop remediation plan.
due: null
janitor_note: 'LINK001 — Fixed: assigned changed from [[person/Basel Khouri]] to [[person/Basel
  Kanaaneh]]. Telia''z wikilinks are valid (YAML escaping false positive). Base view
  embed (related.base#All) references _bases/related.base which does not exist — create
  base file to enable dynamic views.'
kind: task
name: Address Rising Average Wait Time at Clinic Israel
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Israel KPI Dashboard January 2026]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
- '[[constraint/Secretarial Capacity Is Critically Low]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.7
  context: 'Clinic goals: wait time vs volume target'
  source: task/Address Rising Average Wait Time at Clinic Israel.md
  target: task/Increase Monthly Session Volume to 100 Target.md
  type: related-to
- confidence: 0.7
  context: 'Clinic goals: wait time vs volume target'
  source: task/Address Rising Average Wait Time at Clinic Israel.md
  target: task/Increase Monthly Session Volume to Target 100.md
  type: related-to
- confidence: 0.95
  context: Addressing requires prior investigation
  source: task/Address Rising Average Wait Time at Clinic Israel.md
  target: task/Investigate Rising Average Wait Time at Clinic Israel.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Address Rising Average Wait Time at Clinic Israel

Investigate and resolve the rising average wait time trend flagged in the January 2026 KPI dashboard.

## Context

The January 2026 management dashboard shows average patient wait time at 14 days with an upward trend. While the nearest available appointment is 3 days (suggesting some capacity exists for urgent cases), the overall trend is concerning.

Potential root causes to investigate:
- **Psychiatrist capacity:** Are there enough psychiatrists to meet demand?
- **Scheduling efficiency:** Is the secretarial team able to schedule efficiently given known capacity constraints?
- **No-show rate:** The gap between 109 scheduled sessions and 82 conducted sessions suggests ~25% attrition — are cancellations being backfilled?
- **Demand growth:** Is inquiry volume outpacing capacity growth?

This connects to the known [[constraint/Secretarial Capacity Is Critically Low]] and the ongoing hiring discussions.

## Related
![[related.base#All]]

## Outcome

To be filled on completion.