---
alfred_tags:
- telepsychiatry/constraints
- remote-onboarding/tech-access
- staff/isolation
authority: Operational reality — remote telepsychiatry model
created: '2026-02-26'
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is valid (YAML escaping false
  positive).
name: Technology Access Is Hard Day-One Blocker for New Clinical Staff
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Adopt Three-Track Onboarding Model for New Employees]]'
- '[[assumption/Fully Remote Telepsychiatry Model Underlies All Structural Decisions]]'
- '[[note/New Employee Onboarding Structure Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Framework Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Framework and Technology Requirements 2026-02-12]]'
- '[[task/Formalize New Employee Onboarding Process]]'
relationships:
- confidence: 0.6
  context: Shared clinical staff challenges
  source: constraint/Technology Access Is Hard Day-One Blocker for New Clinical Staff.md
  target: constraint/Telepsychiatry Work-From-Home Model Creates Structural Staff
    Isolation.md
  type: related-to
source: Multiple onboarding framework discussions 2026-02-12
source_date: '2026-02-12'
status: active
type: constraint
---

# Technology Access Is Hard Day-One Blocker for New Clinical Staff

## Constraint

New clinical staff at Telia'z Clinic Israel cannot perform any clinical work without access to two systems: Microsoft Teams (video session platform) and HoViD (clinical records platform). Unlike operational or administrative onboarding — which can be deferred or learned gradually — technology access is a binary prerequisite. A clinician without Teams/HoViD credentials on day one is 100% blocked.

## Source

Four separate notes from the 2026-02-12 Rami–Elias onboarding discussion all independently emphasize this as the single non-negotiable element. Rami stated explicitly: without technology access, "the new employee cannot function" — they "literally cannot join Teams sessions or access the clinical system."

## Implications

- Every new hire workflow must prioritize technology provisioning above all other onboarding steps
- Delays in IT credential setup directly translate to delayed revenue (clinician cannot see patients)
- In a fully remote clinic, technology access IS the equivalent of physical workplace access — there is no fallback
- The three-track onboarding model was designed specifically around this constraint, making technology the mandatory first track

## Expiry / Review

Permanent constraint as long as the clinic operates on a fully remote telepsychiatry model. Review if the clinic ever adopts hybrid or in-person sessions.