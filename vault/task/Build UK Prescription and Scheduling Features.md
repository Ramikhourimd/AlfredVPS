---
alfred_instructions: null
alfred_tags:
- uk/prescription
- uk/scheduling
assigned: '[[person/Stav Zamir]]'
blocked_by: []
created: '2026-02-15'
depends_on: []
description: Develop prescription issuance system and scheduling/appointment booking
  feature for UK clinic. Prescription system involves external system integration
  and UK-specific controlled substance formats. Scheduling feature not yet scoped.
  Must be ready by end of March 2026.
due: '2026-03-31'
janitor_note: LINK001 — Base view embed (related.base#All) references non-existent
  _bases/related.base — systemic issue, embed preserved. Telia'z wikilinks are valid
  (YAML escaping false positive). Broken links to [[conversation/Telia'z Team Meeting
  UK Launch and Clinic Operations 2026-02-15]] and [[project/Telia'z AI Clinical Platform]]
  — targets may not exist, needs human verification.
kind: task
name: Build UK Prescription and Scheduling Features
priority: high
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Shachar]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.95
  context: Similar build task variants
  source: task/Build UK Prescription and Scheduling Features.md
  target: task/Build UK Scheduling and Prescription Modules.md
  type: related-to
- confidence: 0.95
  context: Similar build task variants
  source: task/Build UK Prescription and Scheduling Features.md
  target: task/Build UK Scheduling and Prescription System.md
  type: related-to
- confidence: 0.9
  context: Build depends on scoping
  source: task/Build UK Prescription and Scheduling Features.md
  target: task/Scope UK Scheduling and Prescription Features for Product Backlog.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Build UK Prescription and Scheduling Features

Two critical product features needed for UK clinic launch:

1. **Prescription System**: UK patients must receive actual prescriptions (not just treatment recommendations like in Israel). Involves integration with external prescription system, UK-specific formats for controlled substances (e.g., ADHD medications).

2. **Scheduling/Appointment Booking**: Patients need visibility into available appointment slots. Feature not yet scoped but flagged as critical for patient experience.

## Context

Stav flagged these in [[conversation/Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15]]. Shachar targeting March 31 for full system launch. These features need to be added to the backlog sprint.

## Related
![[related.base#All]]

## Outcome