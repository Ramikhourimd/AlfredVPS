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
description: 'Develop evidence-based patient discharge framework: literature review
  of psychiatric patient treatment duration, cross-reference with Telia''z data, identify
  early discharge indicators, and build decision support for psychiatrists. Target:
  10% post-intake, 30% post-FU1, 30% post-FU2, 30% post-FU3.'
due: null
janitor_note: 'LINK001 — Telia''z Clinic Israel wikilink valid (YAML escaping). Conversation
  link [[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]
  VERIFIED VALID — target exists (status: resolved). Base view embed (related.base#All)
  references missing _bases/ — vault-wide infrastructure issue, embed preserved.'
kind: task
name: Develop Patient Discharge Framework and Analysis
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
- '[[person/Dekkel Taliaz]]'
relationships:
- confidence: 0.7
  context: Framework analysis supports protocol design
  source: task/Develop Patient Discharge Framework and Analysis.md
  target: task/Design Patient Discharge Protocol and Literature Review.md
  type: supports
- confidence: 0.85
  context: Requires complex patient criteria
  source: task/Develop Patient Discharge Framework and Analysis.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Develop Patient Discharge Framework and Analysis

Rami proposed a structured approach to managing patient flow through active discharge, addressing the capacity crisis (945 new patients/month, only 8% getting intakes).

## Approach

1. **Literature review** — How psychiatric patients behave in treatment (duration, dropout patterns)
2. **Data analysis** — Cross-reference with Telia'z patient data to identify churn patterns, timing, and patient characteristics
3. **Indicator identification** — Find early signals of patients who can be safely discharged
4. **System integration** — Build into questionnaire screening + psychiatrist decision support (reports flagging recommended discharges)

## Discharge Targets

- 10% after intake (patients who don't need pharmacological treatment or are too complex for telehealth)
- 30% after 1st follow-up
- 30% after 2nd follow-up
- 30% after 3rd follow-up

Also need to address patient selection/screening to filter out cases unsuitable for the telehealth model (suicidality, personality disorders, non-pharmacological needs).

## Next Step

Rami and Dekkel (and possibly Basel) to meet for a detailed planning session to align discharge framework with business/financial model.

## Context

From [[conversation/Telia'z Team Meeting UK Launch and Operations 2026-02-15]].

## Related
![[related.base#All]]

## Outcome