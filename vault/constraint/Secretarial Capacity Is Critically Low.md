---
alfred_tags:
- clinic/staffing
- secretarial/constraints
- personnel/shortages
authority: Operational reality
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).'
name: Secretarial Capacity Is Critically Low
project:
- '[[project/Telia''z Organizational Restructuring]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Secretarial Team Will Grow to Five Full Time by Year End]]'
- '[[note/Telia''z Leadership Meeting 2026-02-22 Organizational Structure and Roles]]'
- '[[note/Organizational Strategy Meeting 2026-02-22]]'
relationships:
- confidence: 0.95
  context: Low capacity justifies hiring block
  source: constraint/Secretarial Capacity Is Critically Low.md
  target: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  type: supports
- confidence: 0.9
  context: Low capacity necessitates hiring
  source: constraint/Secretarial Capacity Is Critically Low.md
  target: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  type: supports
- confidence: 0.75
  context: Capacity strained by role ambiguity
  source: constraint/Secretarial Capacity Is Critically Low.md
  target: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  type: related-to
source: Current staffing reality at Telia'z clinic
source_date: '2026-02-22'
status: active
type: constraint
---

# Secretarial Capacity Is Critically Low

## Constraint

The medical secretary team is at critically low capacity: Alice is barely working and Amda is going on maternity leave, leaving the clinic with effectively less than one functional full-time secretary. Renee is transitioning out of hands-on secretarial work into management. This creates an immediate operational bottleneck for both patient-facing services (appointment scheduling, phone support) and staff-facing functions.

## Source

Current staffing reality discussed at the 2026-02-22 leadership meeting. This is not a regulatory or policy constraint but an operational one — the clinic physically does not have enough people to handle secretarial workload.

## Implications

- Immediate hiring of 2+ secretaries is required before any restructuring benefits can materialize
- Patient experience is at risk: missed calls, delayed scheduling, poor first impressions
- Renee cannot fully transition to her Administrative Manager role until replacement secretarial capacity is in place
- Onboarding new secretaries takes time, creating a lag between hiring and capacity relief
- This constraint is a prerequisite blocker for the broader organizational restructuring

## Expiry / Review

This constraint is temporary — it resolves once new secretaries are hired and onboarded. Expected resolution: Q2 2026 if hiring proceeds promptly.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]