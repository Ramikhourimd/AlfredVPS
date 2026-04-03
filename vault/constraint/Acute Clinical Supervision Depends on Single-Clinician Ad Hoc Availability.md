---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Operational reality — no formal on-call rotation exists
created: '2026-02-26'
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is valid (YAML escaping false
  positive). assumption/Case Managers Need Structured Supervision... wikilink is valid
  (target exists). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist — embeds preserved,
  create base file to enable dynamic views.
name: Acute Clinical Supervision Depends on Single-Clinician Ad Hoc Availability
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Case Managers Need Structured Supervision Framework for Acute Risk
  Assessment]]'
- '[[note/Clinical Supervision - Suicidal Risk Assessment and Military Reporting Protocols]]'
- '[[constraint/Rami Cannot Serve as Full-Time Clinic Medical Director]]'
relationships:
- confidence: 0.95
  context: Ad-hoc availability justifies structured need
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  type: supports
- confidence: 0.75
  context: Ad-hoc supervision affects high-risk protocols
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  type: related-to
- confidence: 0.65
  context: Ad-hoc limits comprehensive risk documentation
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  type: related-to
- confidence: 0.85
  context: Availability vulnerable to alert chain failures
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  type: related-to
- confidence: 0.8
  context: Shared psychiatrist on-call constraints
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/CMO Clinical Approval Required Before Psychiatrist Enters On-Call
    Rotation.md
  type: related-to
- confidence: 0.75
  context: EHR access needed for supervision
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/Individual Clickx EHR Account Required Per Psychiatrist With
    OTP Authentication.md
  type: depends-on
- confidence: 0.7
  context: Part of on-call supervision workflow
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/On-Call Post-Alert Workflow Requires Manual Patient File and
    Documentation Creation.md
  type: related-to
- confidence: 0.55
  context: Linked clinical intake processes
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/Patient Discharge Requires Completed Psychiatry Intake Examination.md
  type: related-to
- confidence: 0.85
  context: Auth required for supervision access
  source: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  target: constraint/Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions.md
  type: depends-on
source: Clinical supervision call between Selina and Rami, 2025-12-01
source_date: '2025-12-01'
status: active
type: constraint
---

# Acute Clinical Supervision Depends on Single-Clinician Ad Hoc Availability

## Constraint

When case managers at Telia'z Clinic Israel encounter acute psychiatric risk situations (suicidal ideation, patients with weapon access, mandatory reporting triggers), they call Rami Khouri directly on an ad hoc basis. There is no formal on-call rotation, escalation protocol, or backup clinician designated for clinical supervision emergencies.

## Source

Documented in the 2025-12-01 supervision call where case manager Selina called Rami for urgent guidance on a military-connected patient with prior suicidal ideation and access to a weapon. Rami provided a comprehensive teaching session on risk assessment hierarchies and reporting protocols — indicating this knowledge was not previously formalized or distributed to case managers.

## Implications

- If Rami is unavailable (in session, traveling, off-hours), case managers have no designated clinical authority to consult
- This creates both a patient safety risk and a liability exposure for the clinic
- The constraint compounds with Rami's planned transition away from day-to-day Medical Director duties — once a new Medical Director is hired, supervision continuity must be formally established
- Military/security patients with weapon access represent an elevated risk category requiring immediate clinical response
- The teaching-session nature of the call reveals that acute risk assessment knowledge has not been codified into training materials or protocols

## Expiry / Review

This constraint should be resolved when: (a) a dedicated Medical Director is hired and operational, and (b) a formal clinical supervision and escalation protocol is established. Review upon Medical Director onboarding.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]