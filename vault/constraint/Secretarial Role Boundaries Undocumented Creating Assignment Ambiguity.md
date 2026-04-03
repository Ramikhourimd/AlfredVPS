---
alfred_tags:
- clinic/staffing
- secretarial/constraints
- personnel/shortages
authority: Internal organizational gap
created: '2026-03-16'
janitor_note: 'LINK001 — Telia''z Clinic Israel wikilink is valid (YAML single-quote
  escaping false positive). synthesis/Secretary Capacity link verified valid. Base
  view embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — vault-wide infrastructure gap, embeds preserved. ORPHAN001
  — no inbound wikilinks; draft constraint record, may gain links as restructuring
  project progresses.'
location: []
name: Secretarial Role Boundaries Undocumented Creating Assignment Ambiguity
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Document Secretarial Responsibilities and Assignments]]'
- '[[assumption/Secretary Roles Should Be Differentiated Into Patient-Facing and Staff-Facing]]'
- '[[assumption/Pod-Dedicated and Shared Pool Are the Two Candidate Secretary Models]]'
- '[[synthesis/Secretary Capacity Is Compounding Bottleneck Across Multiple Operational
  Workflows]]'
- '[[constraint/Immediate Secretary Hiring Required Due to Maternity Leave]]'
relationships:
- confidence: 0.9
  context: ambiguity contributes to low capacity
  source: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  target: constraint/Secretarial Capacity Is Critically Low.md
  type: supports
- confidence: 0.6
  context: Ambiguity exacerbates hiring need
  source: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  target: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  type: related-to
- confidence: 0.65
  context: Role issues impact replacements
  source: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  target: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  type: related-to
source: Operational gap identified during 2025-12-02 operations call
source_date: '2025-12-02'
status: active
tags: []
type: constraint
---

# Secretarial Role Boundaries Undocumented Creating Assignment Ambiguity

## Constraint

The secretarial team at Telia'z Clinic Israel has no formal documentation of individual responsibilities, work threads (khuyut), or assignment boundaries. Each secretary's scope of work exists only as informal, undocumented knowledge.

## Source

During the 2025-12-02 operations call, Basel Kanaaneh was tasked with documenting each secretary's current responsibilities and administrative movements since they started. The fact that this task was necessary — and assigned to a newly onboarded operations manager — confirms that no such documentation existed.

## Implications

- New staff (including Basel himself) cannot determine who owns which operational thread without asking
- Secretary hiring and onboarding cannot reference a defined role scope
- The ongoing restructuring of secretary roles (patient-facing vs staff-facing differentiation) lacks a documented baseline to restructure from
- Maternity leave coverage planning is ad-hoc because there is no written record of what the departing secretary handles
- Conflicts or gaps in task ownership go undetected until they cause visible failures

## Expiry / Review

This constraint should be resolved when the documentation task (task/Document Secretarial Responsibilities and Assignments) is completed and reviewed by Rami. Review monthly until resolved.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]