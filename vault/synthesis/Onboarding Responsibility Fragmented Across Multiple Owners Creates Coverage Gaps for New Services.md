---
cluster_sources:
- '[[note/On-Call Project Accountability and Role Ownership 2025-09-22]]'
- '[[note/New Employee Onboarding Structure Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Structure and Technology Requirements 2026-02-12]]'
- '[[note/Clinic Staffing and Psychiatrist Availability Update 2025-11-10]]'
confidence: high
created: '2026-03-08'
janitor_note: 'LINK001: (1) project/Telia''z Clinic Israel link flagged as broken
  but file exists — YAML escaping false positive. (2) learn-synthesis.base# embeds
  are broken — systemic issue, base files do not exist vault-wide. ORPHAN001: No inbound
  links — synthesis is newly created (2026-03-08), may gain links as vault evolves.
  No per-file action needed.'
name: Onboarding Responsibility Fragmented Across Multiple Owners Creates Coverage
  Gaps for New Services
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[synthesis/Manual Single-Person Dependencies Create Cascading Failure Points Across
  Clinic Operations]]'
- '[[constraint/New Clinicians Blocked Without Day-One Technology Access]]'
- '[[assumption/Existing Staff Can Absorb Onboarding Delivery Without Additional Resources]]'
status: active
supports:
- '[[decision/Adopt Three-Track Onboarding Model for New Employees]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
type: synthesis
---

# Onboarding Responsibility Fragmented Across Multiple Owners Creates Coverage Gaps for New Services

## Insight

The clinic's operational onboarding and service setup responsibilities are split across multiple individuals — Shira (clinical training), Roy Shur (system accounts), Shachar (telephony/platform), and others — with no single coordinator ensuring comprehensive coverage. When a new service or function is introduced that does not fit neatly into any existing owner's scope, critical setup tasks fall through the cracks.

## Evidence

1. **On-call service incident (September 2025):** On-call psychiatrists Atef and Ahmad were added to a WhatsApp group but never formally trained on the alert system. Training was supposed to happen but got missed when Rami traveled. The on-call service had no designated operational lead other than Rami, and when he was abroad, no one else picked up the training task. Dekkel Taliaz explicitly stated the project was Rami's end-to-end responsibility.

2. **Three-track onboarding model (February 2026):** Rami and Elias identified that onboarding splits into operational, administrative, and technology tracks — but noted that delivery responsibility was unclear. Rami suggested Stav or Shira should handle the combined operational and technology walkthrough, acknowledging that currently no single person owns the full onboarding experience.

3. **Staffing update (November 2025):** Eliezer's onboarding required coordinating Maccabi forms, platform access, and clinical orientation across multiple people. Shira would handle onboarding process while Roy handled system access — but the coordination between them was ad hoc.

4. **Existing constraint:** The "New Clinicians Blocked Without Day-One Technology Access" constraint demonstrates the real cost of fragmented onboarding — a new hire arriving without Teams or HoViD access is completely blocked.

## Implications

- New services (like on-call, new HMO partnerships, or new clinical programs) require explicit operational owner assignment before launch — not just clinical oversight
- The three-track onboarding model is a step toward addressing this, but still needs a single coordinator to ensure all tracks are covered
- As the clinic scales to 176+ individual hires, the fragmented onboarding model will produce increasingly frequent gaps
- The "closed project" accountability model (Dekkel's position) only works if the responsible person can delegate reliably — which requires clear sub-owners for each track

## Applicability

Applies to all new operational services and new employee onboarding at Telia'z Clinic Israel. The pattern will intensify as the clinic adds Clalit partnerships, additional HMO agreements, and new clinical programs alongside continued Maccabi operations.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]
