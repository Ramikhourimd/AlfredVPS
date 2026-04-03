---
alfred_instructions: null
alfred_tags:
- uk/prescription
- uk/scheduling
assigned: '[[person/Stav Zamir]]'
blocked_by: []
created: '2026-02-15'
depends_on: []
description: Develop scheduling system (patient appointment self-service) and prescription
  issuance module for UK clinic. Critical for patient experience — assessment without
  prescription is incomplete.
due: null
janitor_note: LINK001 — Telia'z wikilinks (project, conversation) are valid (YAML
  escaping false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist.
kind: task
name: Build UK Scheduling and Prescription Modules
priority: urgent
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.95
  context: Similar build task variants
  source: task/Build UK Scheduling and Prescription Modules.md
  target: task/Build UK Scheduling and Prescription System.md
  type: related-to
- confidence: 0.9
  context: Build depends on scoping
  source: task/Build UK Scheduling and Prescription Modules.md
  target: task/Scope UK Scheduling and Prescription Features for Product Backlog.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Build UK Scheduling and Prescription Modules

Two critical UK-specific product features:

1. **Scheduling system:** Patients need to see available appointment slots and book directly. Not yet scoped — was excluded from the assessment scope but is essential for UK operations.

2. **Prescription module:** UK patients completing ADHD assessment need prescription issuance. Currently the system provides diagnosis but no prescription. Need to understand UK prescription regulations and either integrate with an external prescribing platform or build a dedicated UK module.

Stav flagged both as higher complexity than other backlog items and recommended adding to the priority backlog.

## Context

From [[conversation/Telia'z Team Meeting UK Launch and Operations 2026-02-15]]. Stav emphasized this is critical — "the patient in our assessment gets diagnosed but doesn't get a prescription, that's very critical."

## Related
![[related.base#All]]

## Outcome