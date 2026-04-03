---
alfred_tags:
- uk/scheduling
- uk/prescriptions
authority: Engineering team capacity
created: '2026-03-07'
janitor_note: LINK001 — Telia'z wikilinks use YAML single-quote escaping (targets
  verified to exist). learn-constraint.base#Affected Projects and learn-constraint.base#Related
  are base view embeds, not broken links. ORPHAN001 — no inbound links; consider linking
  from project/Telia'z UK Expansion or project/Telia'z AI Clinical Platform.
name: UK Product Features Compete for Shared Engineering Backlog With Israel
project:
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
- '[[task/Scope UK Scheduling and Prescription Features for Product Backlog]]'
- '[[task/Prepare UK Report Formats]]'
- '[[synthesis/Single Israeli Team Serves Dual Markets Creating Resource Contention]]'
relationships:
- confidence: 0.8
  context: Backlog impacts unscoped UK features
  source: constraint/UK Product Features Compete for Shared Engineering Backlog With
    Israel.md
  target: constraint/UK Scheduling and Prescription Features Not Yet Scoped.md
  type: related-to
source: Team meeting backlog discussion
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Product Features Compete for Shared Engineering Backlog With Israel

## Constraint

UK-specific product features — questionnaire adaptation, report formats, prescription module, scheduling system — must be prioritized within the same product development backlog and sprint cycle that serves the Israel clinic. There is no dedicated UK engineering team; all development flows through Stav Zamir's team.

## Source

February 15, 2026 team meeting. Stav explicitly discussed adding UK features (prescription, scheduling, report formats) to the existing product backlog. The backlog prioritization meeting at 2:00 PM the same day was to determine sequencing alongside Israel feature development.

## Implications

- UK feature delivery competes directly with Israel clinic improvements and innovation program features
- Sprint capacity is finite — every UK feature displaces an Israel feature (or vice versa)
- Complex UK features (prescription integration, scheduling) were flagged by Stav as "more complex than other backlog items"
- March 31 system launch deadline creates pressure to prioritize UK features, potentially slowing Israel development
- No ability to parallelize UK and Israel development across separate teams

## Expiry / Review

This constraint expires if/when a dedicated UK engineering resource is hired or if the product team is expanded. Should be reviewed if UK patient volume justifies dedicated engineering investment.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]