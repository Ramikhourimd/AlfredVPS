---
alfred_instructions: null
alfred_tags:
- patient/discharge-protocol
- clinic/patient-lifecycle
- healthcare/capacity-management
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-26'
depends_on: []
description: 'Design a data-driven patient discharge framework with target release
  rates: 10% after intake, 30% after first follow-up, 30% after second, 30% after
  third. Requires literature review on psychiatric patient treatment duration patterns,
  cross-reference with Telia''z data, and new questionnaire features to identify discharge-ready
  patients.'
due: null
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is a YAML-escape false positive
  (file exists). conversation and note wikilinks with Telia'z are also false positives.
  related.base#All is a base view embed referencing _bases/related.base which does
  not exist — vault-wide infrastructure gap, embed preserved.
kind: task
name: Develop Patient Discharge Framework and Literature Review
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[person/Dekkel Taliaz]]'
relationships:
- confidence: 0.8
  context: Framework LR related to protocol LR
  source: task/Develop Patient Discharge Framework and Literature Review.md
  target: task/Design Patient Discharge Protocol and Literature Review.md
  type: related-to
- confidence: 0.85
  context: Requires complex patient criteria
  source: task/Develop Patient Discharge Framework and Literature Review.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Develop Patient Discharge Framework and Literature Review

Design a structured framework for managing patient throughput at Telia'z Clinic Israel by establishing evidence-based discharge criteria and target rates.

## Context

At the 2026-02-15 team meeting, Rami presented data showing the clinic receives ~945 new patients monthly but only converts 8% to intake appointments due to capacity constraints. The current natural churn rate is approximately 15%. To sustain growth without indefinitely expanding capacity, the clinic needs a proactive discharge strategy.

## Proposed Discharge Targets
- **10%** discharged after intake (patients not requiring psychiatric medication or unsuitable for telepsychiatry)
- **30%** discharged after first follow-up
- **30%** discharged after second follow-up
- **30%** discharged after third follow-up

This would effectively limit most patients to a 4-5 month treatment window.

## Required Steps
1. **Literature review** — How do psychiatric patients in similar settings (telepsychiatry, medication management) typically progress and disengage?
2. **Data analysis** — Cross-reference literature findings with Telia'z patient data to identify natural discharge patterns (who drops after intake, after follow-up 1, 2, 3?)
3. **Early indicators** — Identify patient characteristics that predict early/late discharge
4. **Questionnaire updates** — Add items to intake questionnaire to flag patients likely to need shorter/longer treatment
5. **Clinician tooling** — Add psychiatrist-facing reports/alerts recommending discharge
6. **Financial validation** — Work with Dekkel to confirm discharge targets align with business model

## Related
![[related.base#All]]

## Outcome