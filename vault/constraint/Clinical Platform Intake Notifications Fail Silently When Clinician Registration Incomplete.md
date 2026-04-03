---
authority: Telia'z AI Clinical Platform architecture
created: '2026-03-13'
janitor_note: LINK001 — Telia'z project wikilinks are valid (YAML apostrophe escaping
  false positive). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist — vault-wide infrastructure
  gap. ORPHAN001 — no inbound links; consider linking from project/Telia'z Clinic
  Israel or project/Telia'z AI Clinical Platform.
location: []
name: Clinical Platform Intake Notifications Fail Silently When Clinician Registration
  Incomplete
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[constraint/New Clinicians Blocked Without Day-One Technology Access]]'
- '[[constraint/Technology Access Is Hard Day-One Blocker for New Clinical Staff]]'
source: Platform troubleshooting call revealed silent failure mode
source_date: '2025-10-09'
status: active
tags: []
type: constraint
---

# Clinical Platform Intake Notifications Fail Silently When Clinician Registration Incomplete

## Constraint

The clinical platform's intake notification system (the three-link email workflow: phone call, summary form, video session) fails silently when a clinician's phone number or email address is not correctly registered in the system by the VP R&D (Shachar). Neither the clinician nor the operations team receives any error notification — the intake event triggers in the system, but the phone ring and email simply never arrive.

## Source

During a troubleshooting call on 2025-10-09, Rami Khouri investigated why a clinician never received an intake notification despite the system showing that an intake event ("kria") was triggered. The root cause was that the clinician's contact details had not been properly registered in the platform. The system provided no indication of delivery failure.

## Implications

- Intake events can be triggered and "consumed" by the system without any clinician actually being notified, creating invisible patient service gaps
- There is no feedback loop to detect that a notification was not delivered — discovery only happens when someone manually checks
- The registration dependency on a single person (VP R&D) creates a silent single point of failure
- Patient experience is affected: the patient may be waiting for a call that will never come
- This failure mode is distinct from the day-one tech access blocker — it can occur at any time if registration data becomes stale or was never completed

## Expiry / Review

This constraint persists until the platform implements delivery confirmation, retry logic, or dead-letter alerting for undelivered intake notifications.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
