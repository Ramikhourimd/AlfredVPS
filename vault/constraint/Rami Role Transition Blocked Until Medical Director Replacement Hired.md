---
authority: Organizational dependency — clinic requires physician oversight
created: '2026-02-25'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist. Create base file to enable dynamic views. ORPHAN001 — no inbound
  wikilinks; consider linking from project/Telia''z Organizational Restructuring or
  task/Define Rami Role for 2026.'
name: Rami Role Transition Blocked Until Medical Director Replacement Hired
project:
- '[[project/Telia''z Organizational Restructuring]]'
related:
- '[[assumption/Rami Four Roles Can Be Consolidated Into Two Defined Positions]]'
- '[[assumption/Medical Director Is a Part Time Thirty Percent Position]]'
- '[[constraint/Clinical Operations Require Physician Oversight]]'
- '[[task/Define Rami Role for 2026]]'
source: task/Define Rami Role for 2026.md
source_date: '2026-02-22'
status: active
type: constraint
---

# Rami Role Transition Blocked Until Medical Director Replacement Hired

## Constraint

Rami cannot transition from his current 4-role structure (CEO substitute, Clinic Medical Director, Head of Clinical Operations, Innovation Lead) to the consolidated CMO + Innovation Lead structure until a new Medical Director is hired to take over day-to-day clinical oversight at the clinic level. Israeli law requires physician oversight of medical operations, and Rami is currently the only person fulfilling that regulatory requirement.

## Source

Explicitly listed as a dependency in task/Define Rami Role for 2026.md: "Hiring of a Medical Director for the clinic (to take over day-to-day medical oversight)." This is a hard prerequisite — not a preference, but a structural blocker.

## Implications

- No timeline has been set for the Medical Director hire
- The Medical Director role is estimated at 30% position, which limits the candidate pool
- Until hired, Rami remains locked into the 4-role structure regardless of org chart decisions
- This constraint creates a sequencing dependency: org chart finalization → Medical Director job posting → hiring → Rami role transition
- The board presentation and restructuring implementation cannot be fully realized until this hire completes

## Expiry / Review

Expires when a Medical Director is hired and onboarded. Should be reviewed monthly to assess hiring progress.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
