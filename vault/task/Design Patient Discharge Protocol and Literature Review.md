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
description: 'Conduct literature review on psychiatric patient treatment patterns
  and design an active patient discharge protocol to manage clinic capacity. Targets:
  10% after intake, 30% after each of first three follow-ups.'
due: null
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is valid (YAML escaping false
  positive). Conversation and note wikilinks (Telia'z Team Meeting UK Launch and Clinic
  Operations 2026-02-15) appear valid — scanner false positive from quote escaping.
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — systemic issue, embed preserved.
kind: task
name: Design Patient Discharge Protocol and Literature Review
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Dekkel Taliaz]]'
relationships:
- confidence: 0.85
  context: General lit review supports clinic design
  source: task/Design Patient Discharge Protocol and Literature Review.md
  target: task/Design Patient Discharge Protocol for Clinic Israel.md
  type: supports
- confidence: 0.8
  context: Both design discharge protocols
  source: task/Design Patient Discharge Protocol and Literature Review.md
  target: task/Design Patient Lifecycle Discharge Protocol.md
  type: related-to
- confidence: 0.8
  context: Protocol design and framework analysis linked
  source: task/Design Patient Discharge Protocol and Literature Review.md
  target: task/Develop Patient Discharge Framework and Analysis.md
  type: related-to
- confidence: 0.9
  context: Shared lit review on discharge frameworks
  source: task/Design Patient Discharge Protocol and Literature Review.md
  target: task/Develop Patient Discharge Framework and Literature Review.md
  type: related-to
- confidence: 0.85
  context: Requires complex patient criteria
  source: task/Design Patient Discharge Protocol and Literature Review.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Design Patient Discharge Protocol and Literature Review

Rami Khouri to design an active patient discharge protocol to transform the clinic from a retention-heavy to intake-heavy operation:

## Steps
1. Literature review on psychiatric patient treatment duration patterns
2. Cross-reference with Telia'z clinical data — identify natural dropout patterns
3. Identify predictive indicators for short-term vs. long-term treatment needs
4. Modify intake questionnaire to flag patients suitable for brief treatment
5. Build psychiatrist-facing recommendation features (automated discharge suggestions)
6. Validate against financial model with Dekkel

## Target Discharge Rates
- 10% released after intake
- 30% released after first follow-up
- 30% released after second follow-up
- 30% released after third follow-up

## Context

Currently 945 new patients/month arrive but only 8% get intake appointments. Existing patients consuming all available follow-up slots. Active discharge is essential to create capacity for new intakes.

## Related
![[related.base#All]]

## Outcome