---
alfred_tags:
- clinic/staffing
- secretarial/constraints
- personnel/shortages
authority: Operational reality — staffing dependency
created: '2026-02-25'
janitor_note: 'LINK001 — all Telia''z wikilinks are valid (YAML escaping false positive:
  double single-quotes resolve to literal apostrophe). Base view embeds (learn-constraint.base#Affected
  Projects, learn-constraint.base#Related) reference _bases/ files that do not exist
  — vault-wide issue, not file-specific. ORPHAN001 — no inbound wikilinks detected;
  consider linking from project/Telia''z Organizational Restructuring or task records.'
location: []
name: Renee Admin Transition Blocked Until Secretarial Replacements Hired
project:
- '[[project/Telia''z Organizational Restructuring]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Secretarial Capacity Is Critically Low]]'
- '[[assumption/Renee Is the Right Fit for Administrative Manager]]'
- '[[assumption/Secretarial Team Will Grow to Five Full Time by Year End]]'
- '[[note/Telia''z Leadership Meeting 2026-02-22 Organizational Structure and Roles]]'
relationships:
- confidence: 0.9
  context: block depends on low secretarial capacity
  source: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  target: constraint/Secretarial Capacity Is Critically Low.md
  type: depends-on
- confidence: 0.95
  context: Blocked until secretaries hired
  source: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  target: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  type: depends-on
- confidence: 0.65
  context: Secretarial issues delay transition
  source: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  target: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  type: related-to
source: Operational dependency from Feb 22 meeting discussion
source_date: '2026-02-22'
status: active
type: constraint
---

# Renee Admin Transition Blocked Until Secretarial Replacements Hired

## Constraint

Renee cannot fully transition from hands-on secretarial/administrative work to her new Administrative Manager role until replacement secretarial staff are hired and onboarded. The meeting note explicitly states Renee is "moving to pure management" and that the clinic needs "to hire 2 more immediately" — but until those hires are in place, Renee must continue covering secretarial functions.

## Source

Operational dependency identified in the Feb 22 leadership meeting. The secretarial team is at critically low capacity (Alice barely working, Amada going on maternity leave, Avital leaving). Renee is currently one of the people covering gaps, so her transition to a management-only role creates additional capacity loss if replacements are not in place first.

## Implications

- The Administrative Manager pillar of the district model cannot be activated until secretarial hiring completes
- This creates a sequential dependency: hire secretaries → onboard → Renee transitions → admin pillar operational
- Estimated timeline: 2-3 months minimum (hiring + onboarding), meaning the three-pillar model cannot be fully operational before Q2 2026 at earliest
- If secretarial hiring is delayed, the entire restructuring timeline shifts

## Expiry / Review

This constraint expires when at least 2 new secretaries are hired and sufficiently onboarded to cover Renee's current operational duties. Review monthly or upon each secretarial hire.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]