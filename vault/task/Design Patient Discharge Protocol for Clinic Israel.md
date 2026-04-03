---
alfred_instructions: null
alfred_tags:
- patient/discharge-protocol
- clinic/patient-lifecycle
- healthcare/capacity-management
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-15'
depends_on: []
description: 'Design structured patient discharge protocol with targets: 10% after
  intake, 30% after 1st follow-up, 30% after 2nd, 30% after 3rd. Requires literature
  review, data cross-reference, intake questionnaire modifications, and financial
  model validation with Dekkel.'
due: null
janitor_note: LINK001 — Telia'z wikilinks (project, conversation, note paths) use
  YAML-escaped apostrophes; all resolve correctly — false positives. LINK001 — [[related.base#All]]
  references non-existent _bases/related.base file; embed preserved per rules, base
  file needs separate creation.
kind: task
name: Design Patient Discharge Protocol for Clinic Israel
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[person/Dekkel Taliaz]]'
relationships:
- confidence: 0.85
  context: Requires complex patient criteria
  source: task/Design Patient Discharge Protocol for Clinic Israel.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Design Patient Discharge Protocol for Clinic Israel

Design an active patient lifecycle management system with structured discharge targets to increase intake throughput.

## Proposed Targets
- **10%** discharged after intake (not appropriate for service)
- **30%** discharged after 1st follow-up
- **30%** discharged after 2nd follow-up
- **30%** discharged after 3rd follow-up

## Required Steps
1. Literature review on psychiatric patient treatment duration
2. Cross-reference with Telia'z patient data on natural churn patterns
3. Identify early discharge signals by patient characteristics
4. Modify intake questionnaire for better patient screening
5. Build psychiatrist-facing discharge recommendation features
6. Validate against business/financial model with Dekkel

## Context

From [[conversation/Telia'z Team Meeting UK Launch Operations and Capacity 2026-02-15]]. Only 8% of 945 monthly new patients getting intake appointments. Active lifecycle management needed.

## Related
![[related.base#All]]

## Outcome