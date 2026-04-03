---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[task/Compile Retool Improvement Priority List]]'
- '[[task/Gather Secretary and Clinic Staff System Requirements]]'
- '[[task/Gather Clinic Staff System Requirements]]'
- '[[task/Create Retool Priority List for First Six Months]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
confidence: medium
created: '2026-03-08'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML double-quote escaping false
  positive). ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  AI Clinical Platform or related platform rebuild tasks.
name: Platform Rebuild Requirements Distributed Across Stakeholders With No Central
  Repository
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[synthesis/Cross-Team R&D Dependencies Are a Systemic Bottleneck]]'
- '[[synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams]]'
status: draft
supports:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
type: synthesis
---

# Platform Rebuild Requirements Distributed Across Stakeholders With No Central Repository

## Insight

The requirements for the platform rebuild are scattered across multiple people and roles — secretaries (Stav's partial list), clinic staff (Renee), psychiatrists (Ori, Alice), operations, and the CTO (Shachar). No single document or repository consolidates all requirements. Multiple parallel tasks exist to gather these fragments, all feeding into a compilation task that Rami owns.

## Evidence

- Task "Compile Retool Improvement Priority List" depends on input from meetings not yet held
- Task "Gather Secretary and Clinic Staff System Requirements" and duplicate "Gather Clinic Staff System Requirements" both reference the same need from different angles
- Task "Finalize Case Manager vs Psychiatrist Screen Responsibility Split" and duplicate "Finalize Case Manager vs Psychiatrist Screen Content Split" show the screen design requirements are also fragmented
- Stav has partial secretary requirements; Renee has operational knowledge; Ori/Alice hold clinical responsibility split decisions
- The CRM module state is itself unverified, meaning even the technical baseline is incomplete

## Implications

- Rami is the single funnel point for all requirement streams — creates a bottleneck
- Without centralization, Track 1/2/3 prioritization risks being based on incomplete information
- Shachar is building the new system and needs clear requirements, but the requirements pipeline has multiple unresolved dependencies
- Risk of the rebuild proceeding with gaps that only surface during implementation

## Applicability

Directly relevant to the Telia'z platform rebuild. Also reflects a broader pattern: when rebuilding systems, distributed organizational knowledge is often the real bottleneck, not technical capability.