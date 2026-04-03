---
alfred_instructions: null
alfred_tags:
- patient/discharge-protocol
- clinic/patient-lifecycle
- healthcare/capacity-management
assigned: null
blocked_by: []
created: '2026-03-01'
date: '2025-11-10'
depends_on: []
description: null
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML single-quote escaping false
  positive). Base view embed (related.base#All) references _bases/related.base which
  does not exist (vault-wide infrastructure gap). Embed preserved. Non-standard fields
  (owner, related_to, date) detected — consider migrating to standard task schema
  fields (assigned, related).
kind: task
name: Contact Former Hosen Patients for Clalit South Pipeline
owner:
- '[[person/Rami Khouri]]'
priority: medium
project: null
related: []
related_to:
- '[[org/Clalit Health Services]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]'
- '[[assumption/Clalit South Will Generate 200 Patients Per Week Within Three Months]]'
relationships:
- confidence: 0.6
  context: Both prep patient protocols/pipeline
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Define Complex Patient Protocol Criteria.md
  type: related-to
- confidence: 0.7
  context: Patient data informs discharge design
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Design Patient Discharge Protocol and Literature Review.md
  type: supports
- confidence: 0.65
  context: Patient data informs discharge design
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Design Patient Discharge Protocol for Clinic Israel.md
  type: supports
- confidence: 0.7
  context: Patient data informs discharge design
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Design Patient Lifecycle Discharge Protocol.md
  type: supports
- confidence: 0.7
  context: Patient data informs framework dev
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Develop Patient Discharge Framework and Analysis.md
  type: supports
- confidence: 0.7
  context: Patient data informs framework dev
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Develop Patient Discharge Framework and Literature Review.md
  type: supports
- confidence: 0.75
  context: Patient data informs strategy dev
  source: task/Contact Former Hosen Patients for Clalit South Pipeline.md
  target: task/Develop Patient Discharge Strategy and Criteria.md
  type: supports
run: null
status: todo
tags:
- clalit
- hosen
- patient-pipeline
- south
type: task
---

# Contact Former Hosen Patients for Clalit South Pipeline

## Objective

Reach out to patients displaced by the closure of Hosen (a mental health facility in the south) as a potential patient pipeline for the Telia'z–Clalit South psychiatric referral system.

## Context

Discussed during the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]. The closure of Hosen creates an immediate pool of patients who need continued psychiatric care and could be directed through the new Clalit referral pathway.

## Action

1. Identify the patient population affected by Hosen's closure
2. Determine which patients are Clalit members in the South District
3. Coordinate with Tzachi or [[person/Michal Boguz]] on referral pathways for these patients
4. Assess volume impact on the [[assumption/Clalit South Will Generate 200 Patients Per Week Within Three Months|200 patients/week projection]]

---
## Related
![[related.base#All]]