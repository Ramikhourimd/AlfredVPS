---
alfred_tags:
- clinic/staffing
- secretarial/constraints
- personnel/shortages
authority: Operational necessity
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) are backslash-escaped in body (\\![[...]]) and non-functional. _bases/learn-constraint.base
  does not exist in vault. Either create the base file AND remove backslash escaping,
  or remove the embed lines. Telia''z wikilink is valid (YAML escaping false positive,
  target exists).'
name: Immediate Secretary Hiring Required Due to Maternity Leave
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Finalize Secretary Team Structure and Hiring]]'
relationships:
- confidence: 0.9
  context: both require urgent secretary hiring
  source: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  target: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  type: related-to
- confidence: 0.95
  context: maternity leave causes low capacity
  source: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  target: constraint/Secretarial Capacity Is Critically Low.md
  type: part-of
- confidence: 0.7
  context: Shared clinic staffing constraints
  source: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  target: constraint/Rami Cannot Serve as Full-Time Clinic Medical Director.md
  type: related-to
- confidence: 0.7
  context: Secretarial operational issues
  source: constraint/Immediate Secretary Hiring Required Due to Maternity Leave.md
  target: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  type: related-to
source: Current staffing situation
status: active
type: constraint
---

# Immediate Secretary Hiring Required Due to Maternity Leave

## Constraint

One of two current full-time secretaries is going on maternity leave, creating an immediate staffing gap that must be filled through urgent hiring. Combined with Renee's transition to management, the effective secretary workforce drops from 3 to 1 without new hires.

## Source

Current staffing situation — maternity leave timeline is a fixed constraint.

## Implications

- Hiring 2+ secretaries is urgent, not just planned growth
- Must decide on pod-dedicated vs. shared pool model before hiring (to write accurate job descriptions)
- Coverage plan needed for the transition period before new hires are onboarded
- May need temporary staffing solution if hiring takes longer than expected

## Expiry / Review

Acute constraint — driven by maternity leave timeline. Urgency reduces once new secretaries are hired and onboarded.

\![[learn-constraint.base#Affected Projects]]
\![[learn-constraint.base#Related]]