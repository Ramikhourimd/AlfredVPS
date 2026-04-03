---
alfred_tags:
- telepsychiatry/constraints
- remote-onboarding/tech-access
- staff/isolation
authority: Clinic operational structure
created: '2026-02-26'
janitor_note: LINK001 — Telia'z wikilink is valid YAML escaping (false positive).
  No action needed.
location: []
name: New Clinicians Blocked Without Day-One Technology Access
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Adopt Three-Track Onboarding Model for New Employees]]'
- '[[assumption/Fully Remote Telepsychiatry Model Underlies All Structural Decisions]]'
- '[[task/Formalize New Employee Onboarding Process]]'
- '[[asset/HoViD]]'
- '[[process/Clinic Israel New Employee Onboarding]]'
relationships:
- confidence: 0.95
  context: Synonymous day-one tech access issues
  source: constraint/New Clinicians Blocked Without Day-One Technology Access.md
  target: constraint/Technology Access Is Hard Day-One Blocker for New Clinical Staff.md
  type: related-to
- confidence: 0.6
  context: Both constrain clinical staff operations
  source: constraint/New Clinicians Blocked Without Day-One Technology Access.md
  target: constraint/Telepsychiatry Work-From-Home Model Creates Structural Staff
    Isolation.md
  type: related-to
source: Operational reality — fully remote telepsychiatry model
source_date: '2026-02-12'
status: active
type: constraint
---

# New Clinicians Blocked Without Day-One Technology Access

## Constraint

In a fully remote telepsychiatry clinic, a new clinician who does not have working access to Microsoft Teams (for video sessions) and HoViD (clinical platform) on their first day is completely unable to function. They cannot see patients, cannot access clinical records, and cannot communicate with the team. Technology access is an absolute prerequisite — unlike operational or administrative onboarding, it cannot be deferred or worked around.

## Source

This is an inherent constraint of the fully remote telepsychiatry model. Unlike a physical clinic where a new hire could shadow a colleague or do paperwork on day one, the remote model means all clinical work flows through two digital platforms. Rami Khouri emphasized this across multiple onboarding discussions on 2026-02-12, describing the failure mode: "a new clinician arriving and not knowing how to get into Teams."

## Implications

- Technology setup must be completed before or on the new clinician's first day — no exceptions
- The onboarding process must treat technology access as a hard gate, not a nice-to-have
- IT provisioning (Teams accounts, HoViD credentials) must be integrated into the hiring workflow upstream of the start date
- Any delay in technology provisioning directly translates to wasted clinician capacity and delayed patient care

## Expiry / Review

Permanent constraint as long as the clinic operates on a fully remote model. Would only change if the clinic introduced in-person or hybrid delivery options.