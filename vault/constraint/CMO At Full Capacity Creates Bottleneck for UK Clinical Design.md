---
alfred_tags:
- constraints/cmo-capacity
- uk/clinical-design
authority: Resource capacity — single person dependency
created: '2026-02-27'
janitor_note: LINK001 — project/Teliaz UK Expansion wikilink is YAML single-quote
  escaping false positive. ORPHAN001 — no inbound wikilinks detected; this constraint
  is referenced in related field of task/Define Data Requirements for OMG-to-Teliaz
  Patient Handoff but may need explicit linking from project/Teliaz UK Expansion.
name: CMO At Full Capacity Creates Bottleneck for UK Clinical Design
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[task/Design UK ADHD Clinical Pathway With GP Confederation]]'
- '[[task/Define Data Requirements for OMG-to-Telia''z Patient Handoff]]'
- '[[task/Prepare UK Report Formats]]'
- '[[task/Define UK Prescription and Report Formats]]'
- '[[synthesis/UK Launch Has Multiple Converging Dependencies Creating Schedule Risk]]'
relationships:
- confidence: 0.95
  context: Both on CMO capacity limiting UK clinical
  source: constraint/CMO At Full Capacity Creates Bottleneck for UK Clinical Design.md
  target: constraint/CMO Bandwidth Limits UK Clinical Pathway Design Progress.md
  type: related-to
- confidence: 0.95
  context: Both on CMO capacity limiting UK clinical
  source: constraint/CMO At Full Capacity Creates Bottleneck for UK Clinical Design.md
  target: constraint/CMO Capacity Bottleneck Limits UK Clinical Pathway Design.md
  type: related-to
- confidence: 0.92
  context: Both on CMO capacity limiting clinical work
  source: constraint/CMO At Full Capacity Creates Bottleneck for UK Clinical Design.md
  target: constraint/CMO at Full Capacity Limiting Clinical Specification Throughput.md
  type: related-to
- confidence: 0.95
  context: Both on CMO capacity limiting UK clinical
  source: constraint/CMO At Full Capacity Creates Bottleneck for UK Clinical Design.md
  target: constraint/CMO at Full Capacity Limits UK Clinical Design Bandwidth.md
  type: related-to
- confidence: 0.7
  context: Both UK clinical workflow constraints
  source: constraint/CMO At Full Capacity Creates Bottleneck for UK Clinical Design.md
  target: constraint/UK Clinical Report Formats Require Adaptation From Israel Templates.md
  type: related-to
source: Explicitly stated by Rami Khouri in OMG pathway design session
source_date: '2025-07-03'
status: active
type: constraint
---

# CMO At Full Capacity Creates Bottleneck for UK Clinical Design

## Constraint

Dr. Rami Khouri (CMO) is at full capacity and has explicitly stated he needs focused, specific deliverables rather than open-ended process management. Since Rami is the sole clinical authority defining the UK ADHD assessment pathway, report formats, prescription requirements, and clinical governance specifications, his availability is a hard constraint on the pace of UK clinical design work.

## Source

Rami stated this directly during the OMG pathway design session (2025-07-03): he is at full capacity and needs focused deliverables. Multiple UK tasks depend on his clinical input — report formats, prescription specifications, clinical pathway design, and data handoff requirements.

## Implications

- UK clinical pathway design cannot proceed faster than Rami's available time allows
- Tasks requiring clinical specification (report formats, prescription module, questionnaire adaptation) compete for the same limited resource
- The weekly Thursday sync (~10:15) established with Adiel is the primary channel for advancing UK clinical work
- Other team members (Stav, Adiel) must prepare focused, specific questions rather than expecting open-ended clinical review sessions
- If Rami's Israel clinic responsibilities increase, UK clinical design work will slow further

## Expiry / Review

This constraint persists until either: (a) Rami's Israel workload decreases, (b) a UK-based Clinical Director is appointed who can take over clinical specification work, or (c) the core UK clinical requirements are fully specified and no longer need CMO input.