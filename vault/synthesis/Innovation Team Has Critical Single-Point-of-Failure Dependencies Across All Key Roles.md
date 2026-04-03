---
cluster_sources:
- '[[note/Stav Zamir Comprehensive Role and Operational Manual]]'
- '[[note/Ohad Edri Complete Work Manual]]'
- '[[note/Rivi Idelman Complete AI Skills Toolkit]]'
- '[[constraint/Clinical AI Prompt Engineering Pipeline Knowledge Concentrated in
  Single Person]]'
- '[[constraint/Ohad Edri C-Level Shadowing Consumes Two Days Per Week]]'
confidence: high
created: '2026-04-01'
name: Innovation Team Has Critical Single-Point-of-Failure Dependencies Across All
  Key Roles
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[constraint/OPTICA Framework Governance Concentrated in Ohad Edri]]'
- '[[constraint/Clinical Viability Validation Authority Concentrated in Stav Zamir]]'
- '[[assumption/Single Person Bridge Between Clinical and Innovation Is Sustainable]]'
- '[[synthesis/Innovation Team Operates Research-Strategy-Rigor Triad Division of
  Labor]]'
status: draft
supports:
- '[[assumption/Half-Time FTE Sufficient for Innovation Team Lead Scope]]'
type: synthesis
---

# Innovation Team Has Critical Single-Point-of-Failure Dependencies Across All Key Roles

## Insight

Across three independent role documentation efforts (Stav's manual, Ohad's manual, Rivi's toolkit), a systemic pattern emerges: every critical function in the Innovation Program is owned by exactly one person with no documented backup, creating a team-wide bus factor of 1.

| Person | Sole-Owner Functions |
|--------|---------------------|
| **Stav Zamir** | Clinical viability validation (all projects), prompt engineering pipeline, clinical needs analysis, implementation coordination |
| **Ohad Edri** | OPTICA framework governance (4/13 steps owned, 8 contributed), AI platform architecture, BigQuery data engineering, N8N agent development |
| **Rivi Idelman** | Problem definition and concept design, staff experience research, stakeholder feedback collection, training content creation |
| **Rami Khouri** | Strategic direction, CEO/board interface, publication pipeline, external partnerships |

No function has a documented secondary owner. The "Research-Strategy-Rigor Triad" division of labor (already documented) is efficient but fragile — it optimizes for throughput at the cost of resilience.

## Evidence

- **Stav**: Role manual explicitly names her "primary authority for validating clinical soundness and safety of ALL new and proposed technological solutions" — no backup validator documented
- **Ohad**: Work manual shows ownership of 4/13 OPTICA steps plus primary contribution to 8 more — further constrained by 2 days/week C-Level shadowing
- **Rivi**: AI toolkit enforces a boundary agreement (Feb 24, 2026) redirecting execution requests away from her — meaning her research/concept design function cannot be temporarily absorbed by others
- **Rami**: The only person with strategic authority, external partnership relationships, and publication oversight

## Implications

- Any single absence (illness, leave, departure) creates a complete blockage in that person's function domain
- The team cannot surge capacity on any workstream because functions don't overlap
- Onboarding a replacement for any role requires months of domain knowledge transfer
- The 3-project WIP limit partially mitigates this by constraining total concurrent load, but doesn't address the fragility of each active project's dependency chain
- This pattern is particularly acute because Ohad's availability is already structurally reduced (C-Level shadowing) and Rivi's is half-time

## Applicability

This applies to all current and future Innovation Program projects. Any project planning should account for key-person availability as a hard scheduling constraint, not a soft risk.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]
