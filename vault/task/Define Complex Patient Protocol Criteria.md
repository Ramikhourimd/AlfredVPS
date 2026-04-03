---
alfred_instructions: null
alfred_tags:
- patient/discharge-protocol
- clinic/patient-lifecycle
- healthcare/capacity-management
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-12'
depends_on: []
description: Conduct literature review and internal data analysis to define criteria
  for complex/unsuitable patients, natural dropout patterns, and multi-stage clinical
  checkpoint flow
due: null
janitor_note: 'LINK001 false positives: Telia''z wikilinks use YAML single-quote escaping
  (valid). related.base#All is a standard base view embed. No fix needed.'
kind: task
name: Define Complex Patient Protocol Criteria
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Rivi Idelman]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[conversation/Innovation Team Meeting Clinical Workloads and AI Tools 2026-03-17]]'
relationships:
- confidence: 0.8
  context: Criteria inform discharge protocol design
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Design Patient Discharge Protocol and Literature Review.md
  type: supports
- confidence: 0.75
  context: Criteria inform clinic discharge protocol
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Design Patient Discharge Protocol for Clinic Israel.md
  type: supports
- confidence: 0.7
  context: Criteria support lifecycle discharge design
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Design Patient Lifecycle Discharge Protocol.md
  type: supports
- confidence: 0.75
  context: Criteria aid discharge framework development
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Develop Patient Discharge Framework and Analysis.md
  type: supports
- confidence: 0.7
  context: Criteria relevant to framework lit review
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Develop Patient Discharge Framework and Literature Review.md
  type: supports
- confidence: 0.85
  context: Both define criteria for discharge
  source: task/Define Complex Patient Protocol Criteria.md
  target: task/Develop Patient Discharge Strategy and Criteria.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Define Complex Patient Protocol Criteria

Conduct a literature review and analyze internal patient data to define what constitutes a complex or unsuitable patient, understand natural dropout patterns (when, at which stage, why), and design a multi-stage clinical checkpoint flow with consent mechanisms.

## Context

Emerged from [[conversation/Product Development Update Meeting 2026-02-12]]. Basel requested a feature to alert psychiatrists about complex patients. Rami outlined a protocol-first approach: define criteria, then build features. The protocol spans questionnaire, case manager, and psychiatry stages with different escalation paths at each.

Key design principle: formal discharge can only happen after psychiatry intake (medical examination). Earlier stages can flag and recommend, but cannot discharge.

## Related
![[related.base#All]]

## Outcome