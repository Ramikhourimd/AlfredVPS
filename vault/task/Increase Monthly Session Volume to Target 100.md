---
alfred_instructions: null
alfred_tags:
- clinic/operations
- kpi-improvement
assigned: '[[person/Basel Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Clinic Israel conducted 82 sessions in January 2026 against a target
  of 100 (82% achievement). Identify bottlenecks in the scheduling and execution pipeline
  to close the 18-session gap.
due: null
janitor_note: LINK001 — Telia'z and org wikilinks valid (YAML escaping false positive).
  person/Basel Khouri does not exist — create person record for Basel Khouri. Base
  view embed (related.base#All) references _bases/related.base which does not exist.
kind: task
name: Increase Monthly Session Volume to Target 100
priority: medium
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Israel KPI Dashboard January 2026]]'
- '[[task/Address Rising Average Wait Time at Clinic Israel]]'
- '[[constraint/Secretarial Capacity Is Critically Low]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.8
  context: Increases capacity to reduce waits
  source: task/Increase Monthly Session Volume to Target 100.md
  target: task/Address Rising Average Wait Time at Clinic Israel.md
  type: supports
- confidence: 0.7
  context: 'Clinic ops: volume & wait time'
  source: task/Increase Monthly Session Volume to Target 100.md
  target: task/Investigate Rising Average Wait Time at Clinic Israel.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Increase Monthly Session Volume to Target 100

Close the gap between current monthly session volume (82) and target (100).

## Context

The January 2026 KPI dashboard shows 125 inquiries yielded 109 scheduled sessions, but only 82 were actually conducted. The conversion funnel has two leak points:

1. **Inquiry to scheduling:** 125 → 109 (87% conversion, target is 95%)
2. **Scheduling to conducted:** 109 → 82 (~75% show rate)

Addressing both leak points could recover the full 18-session deficit. The scheduling-to-conducted gap is the larger issue — a 25% no-show/cancellation rate needs investigation.

Potential actions:
- Implement appointment reminders (SMS/email)
- Analyze no-show patterns by day-of-week and time slot
- Develop cancellation backfill procedures
- Review secretarial scheduling practices for optimization

## Related
![[related.base#All]]

## Outcome

To be filled on completion.