---
alfred_tags:
- clinic/staffing
- secretarial/constraints
- personnel/shortages
authority: Capacity and role consolidation requirements
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z Organizational
  Restructuring.'
name: Rami Cannot Serve as Full-Time Clinic Medical Director
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z Organizational Restructuring]]'
related:
- '[[task/Hire Medical Director for Clinic]]'
- '[[task/Define Rami Role for 2026]]'
- '[[decision/CMO Role Required at Company Level]]'
relationships:
- confidence: 0.7
  context: Admin/leadership role constraints
  source: constraint/Rami Cannot Serve as Full-Time Clinic Medical Director.md
  target: constraint/Renee Admin Transition Blocked Until Secretarial Replacements
    Hired.md
  type: related-to
- confidence: 0.6
  context: Staffing affects director role
  source: constraint/Rami Cannot Serve as Full-Time Clinic Medical Director.md
  target: constraint/Secretarial Capacity Is Critically Low.md
  type: related-to
- confidence: 0.55
  context: Role clarity affects directorship
  source: constraint/Rami Cannot Serve as Full-Time Clinic Medical Director.md
  target: constraint/Secretarial Role Boundaries Undocumented Creating Assignment
    Ambiguity.md
  type: related-to
source: Role overload identified in restructuring meeting
source_date: '2026-02-22'
status: active
type: constraint
---

# Rami Cannot Serve as Full-Time Clinic Medical Director

## Constraint

Rami Khouri cannot continue as the day-to-day Medical Director of the Israel clinic due to his other responsibilities (CMO duties, innovation/AI work, and CEO substitute role). A dedicated Medical Director must be hired.

## Source

This is a capacity constraint identified during the Feb 22 restructuring meeting. Rami currently holds four overlapping roles, and the team agreed this is unsustainable. The Hire Medical Director task explicitly states "Rami cannot fill this role full-time given his other responsibilities."

## Implications

- Medical Director hiring becomes a critical-path dependency for the restructuring
- Until a Medical Director is hired, Rami remains stretched across all four roles
- The organizational chart cannot be finalized until this role is filled
- Rami's role consolidation (4 roles to 2) is blocked by this hire

## Expiry / Review

This constraint resolves when a Medical Director is hired. However, the underlying capacity issue (Rami holding too many roles) should be monitored to prevent recurrence.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]