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
description: 'Design and implement active patient discharge protocol to manage intake-to-follow-up
  ratio. Targets: 10% discharged after intake, 30% after 1st follow-up, 30% after
  2nd, 30% after 3rd. Requires literature review, data analysis, questionnaire modifications,
  and psychiatrist dashboard alerts.'
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Link to conversation/Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15
  is valid (target exists). Base view embed (related.base#All) references _bases/related.base
  which does not exist.
kind: task
name: Design Patient Lifecycle Discharge Protocol
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Dekkel Taliaz]]'
- '[[assumption/Monthly Patient Churn Rate Is Approximately 15 Percent]]'
relationships:
- confidence: 0.85
  context: Requires complex patient criteria
  source: task/Design Patient Lifecycle Discharge Protocol.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Design Patient Lifecycle Discharge Protocol

Design a structured patient discharge protocol to actively manage the ratio between intakes and follow-ups. Currently the clinic cannot handle the volume of both new patients and ongoing follow-ups.

## Approach (Rami's proposal)
1. Literature review on psychiatric patient treatment duration norms
2. Cross-reference with Telia'z patient data (churn patterns, timing, characteristics)
3. Identify early signals for appropriate discharge
4. Modify intake questionnaire to better identify patient fit
5. Build psychiatrist dashboard feature flagging recommended discharges
6. Implement discharge targets: 10% post-intake, 30% post-FU1, 30% post-FU2, 30% post-FU3

## Context

From [[conversation/Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15]]. Dekkel wants a dedicated session with Rami to review, then validate against financial model.

## Related
![[related.base#All]]

## Outcome