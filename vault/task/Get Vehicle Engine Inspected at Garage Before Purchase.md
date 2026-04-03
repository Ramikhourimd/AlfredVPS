---
alfred_instructions: null
alfred_tags:
- vehicles/pre-purchase-inspection
- diesel-4x4/engine-certification
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Have the diesel engine professionally inspected at a garage to verify
  engine health before completing vehicle purchase. The pre-purchase inspector flagged
  excessive crankcase blowby and oil contamination.
due: null
janitor_note: LINK001 — [[related.base#All]] is a base view embed; preserved per policy.
  ORPHAN001 — no inbound links; consider linking from a parent project or conversation
  record.
kind: task
name: Get Vehicle Engine Inspected at Garage Before Purchase
priority: high
project: null
related:
- '[[note/Vehicle Pre-Purchase Inspection Report 2025-11-03]]'
relationships:
- confidence: 0.9
  context: Task implements cert requirement
  source: task/Get Vehicle Engine Inspected at Garage Before Purchase.md
  target: decision/Require Garage Certification Before Diesel 4x4 Purchase.md
  type: depends-on
- confidence: 0.95
  context: Task implements engine cert req
  source: task/Get Vehicle Engine Inspected at Garage Before Purchase.md
  target: decision/Require Garage Engine Certification Before Vehicle Purchase.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Get Vehicle Engine Inspected at Garage Before Purchase

The pre-purchase vehicle inspector flagged the engine as requiring professional garage verification before completing the purchase. Key concerns:

1. Excessive crankcase blowby (fumes from dipstick opening)
2. Oil contamination across entire engine and undercarriage
3. Signs of prior hood removal and front bumper repair (possible engine swap)
4. Engine number unreadable due to oil

The inspector stated that if the garage confirms the engine is healthy, the garage takes responsibility — not the inspector.

## Context

This task emerged from the vehicle inspection on 2025-11-03. See [[note/Vehicle Pre-Purchase Inspection Report 2025-11-03]] for full findings.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what the garage found, and whether the purchase proceeded.