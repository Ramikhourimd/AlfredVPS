---
alfred_tags:
- constraints/cmo-capacity
- uk/clinical-design
authority: Internal capacity
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilinks (project, task) are YAML single-quote
  escaping false positives. Base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/ infrastructure that may not exist — vault-wide issue.
  ORPHAN001 — legitimate constraint record, needs inbound links from related project
  or task records.'
location: []
name: CMO Bandwidth Limits UK Clinical Pathway Design Progress
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[task/Design UK ADHD Clinical Pathway With GP Confederation]]'
- '[[task/Define Data Requirements for OMG-to-Telia''z Patient Handoff]]'
- '[[task/Prepare UK Report Formats]]'
- '[[task/Define UK Prescription and Report Formats]]'
relationships:
- confidence: 0.97
  context: Both on CMO capacity limiting UK pathway
  source: constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress.md
  target: constraint/CMO Capacity Bottleneck Limits UK Clinical Pathway Design.md
  type: related-to
- confidence: 0.92
  context: Both on CMO capacity limiting clinical
  source: constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress.md
  target: constraint/CMO at Full Capacity Limiting Clinical Specification Throughput.md
  type: related-to
- confidence: 0.95
  context: Both on CMO capacity limiting UK clinical
  source: constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress.md
  target: constraint/CMO at Full Capacity Limits UK Clinical Design Bandwidth.md
  type: related-to
- confidence: 0.7
  context: Both UK clinical workflow constraints
  source: constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress.md
  target: constraint/UK Clinical Report Formats Require Adaptation From Israel Templates.md
  type: related-to
source: Rami Khouri, UK NHS ADHD Pathway Design meeting 2025-07-03
source_date: '2025-07-03'
status: active
tags:
- uk-launch
- capacity
- clinical-design
type: constraint
---

# CMO Bandwidth Limits UK Clinical Pathway Design Progress

## Constraint

Dr. Rami Khouri (CMO) is at full capacity across Israel clinic operations and UK expansion workstreams. He explicitly flagged this during the OMG pathway design session, requesting "focused, specific deliverables rather than open-ended process management." Multiple UK clinical design tasks require his input: pathway design, report formats, prescription specifications, clinical questionnaire adaptation, and data handoff requirements.

## Source

Rami stated this directly during the UK NHS ADHD Pathway Design meeting with Adiel on 2025-07-03. The constraint was observable across the 2026-02-15 team meeting where UK report formats, prescription specifications, and clinical flow design all required Rami's involvement alongside ongoing Israel clinic responsibilities.

## Implications

- UK clinical pathway design proceeds only as fast as Rami can allocate time
- Multiple tasks are queued for his input: report formats, prescription specs, questionnaire adaptation, OMG data handoff requirements
- No other team member has the clinical authority to make these decisions
- Single point of failure: if Rami is unavailable, UK clinical design stalls entirely
- Weekly Thursday sync established with Adiel to provide structured touchpoints rather than ad-hoc requests

## Expiry / Review

This constraint persists until either Rami's Israel workload decreases, a UK-based Medical Director is appointed who can share clinical design authority, or all UK clinical specifications are finalized.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]