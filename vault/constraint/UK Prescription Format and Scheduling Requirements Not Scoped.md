---
alfred_tags:
- uk/scheduling
- uk/prescriptions
authority: UK healthcare regulations
created: '2026-03-14'
janitor_note: 'LINK001: Telia''z wikilink is a YAML escaping false positive — link
  resolves correctly. ORPHAN001: No inbound wikilinks — consider linking from project/Telia''z
  UK Expansion.'
name: UK Prescription Format and Scheduling Requirements Not Scoped
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[decision/Launch UK Clinic Through Leon GP Partnership Using His CQC Registration]]'
relationships:
- confidence: 0.8
  context: Unscoped reqs compete for UK backlog
  source: constraint/UK Prescription Format and Scheduling Requirements Not Scoped.md
  target: constraint/UK Product Features Compete for Shared Engineering Backlog With
    Israel.md
  type: related-to
- confidence: 0.95
  context: Overlapping UK sched/prescrip scoping
  source: constraint/UK Prescription Format and Scheduling Requirements Not Scoped.md
  target: constraint/UK Scheduling and Prescription Features Not Yet Scoped.md
  type: related-to
source: Product backlog gap identified at team meeting
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Prescription Format and Scheduling Requirements Not Scoped

## Constraint

Two critical product features for UK operations — prescription formats and patient scheduling — have not been scoped in the product backlog as of February 2026. UK prescription formats differ from Israel, and the scheduling system (critical since UK patients need appointment visibility) has not been designed.

## Source

Identified during the 2026-02-15 team meeting. Rami and Stav were tasked with defining UK prescription format requirements. Scheduling was added to the backlog but remains unscoped.

## Implications

- UK clinical operations cannot function without proper prescription output
- Patient experience degraded without appointment scheduling visibility
- Both features require product development time that competes with the mid-March campaign target
- Questionnaire UI also needs visual fixes (functionality works but presentation needs fixing)

## Expiry / Review

Must be resolved before UK system launch target of March 31, 2026.