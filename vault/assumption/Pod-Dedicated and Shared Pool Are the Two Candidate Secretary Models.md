---
alfred_tags:
- healthcare/staff-restructuring
- administration/dual-roles
based_on:
- '[[task/Finalize Secretary Team Structure and Hiring]]'
- '[[decision/Adopt District Model for Clinic Israel]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-assumption.base#Depends On This,
  #Related) reference _bases/learn-assumption.base which does not exist. Create it
  to enable dynamic views. ORPHAN001 — no inbound wikilinks; consider linking from
  project/Telia''z Clinic Israel.'
name: Pod-Dedicated and Shared Pool Are the Two Candidate Secretary Models
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Secretary Roles Should Be Differentiated Into Patient-Facing and Staff-Facing]]'
relationships:
- confidence: 0.8
  context: Models support split assignment for dual func
  source: assumption/Pod-Dedicated and Shared Pool Are the Two Candidate Secretary
    Models.md
  target: assumption/Secretarial Dual Function May Require Split Assignment Model.md
  type: supports
- confidence: 0.8
  context: Secretary models and dual modes
  source: assumption/Pod-Dedicated and Shared Pool Are the Two Candidate Secretary
    Models.md
  target: assumption/Secretary Dual Function Requires Distinct Operational Modes.md
  type: related-to
- confidence: 0.8
  context: Models relate to role differentiation
  source: assumption/Pod-Dedicated and Shared Pool Are the Two Candidate Secretary
    Models.md
  target: assumption/Secretary Roles Should Be Differentiated Into Patient-Facing
    and Staff-Facing.md
  type: related-to
source: task acceptance criteria
source_date: '2026-02-25'
status: active
type: assumption
---

# Pod-Dedicated and Shared Pool Are the Two Candidate Secretary Models

## Claim

The secretary team restructuring has narrowed to two candidate models: (1) pod-dedicated, where secretaries are assigned to specific clinical pods/districts, and (2) shared pool, where secretaries serve all pods from a central pool. Other models (e.g., per-psychiatrist assignment, shift-based rotation, hybrid) are implicitly excluded from consideration.

## Basis

The acceptance criteria for the secretary hiring task list "Decision on pod-dedicated vs. shared pool model" as a binary choice, suggesting the team has already narrowed the option space to these two architectures. This likely follows from the broader district model adoption decision.

## Evidence Trail

- 2026-02-25: Identified as binary decision framing in [[task/Finalize Secretary Team Structure and Hiring]]

## Impact

This assumption constrains the design space for the secretary team. The pod-dedicated model would align secretaries to districts (consistent with the district model decision) but requires more headcount for coverage. The shared pool model is more flexible but may reduce district cohesion. If a hybrid model proves better, this framing would need revisiting.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]