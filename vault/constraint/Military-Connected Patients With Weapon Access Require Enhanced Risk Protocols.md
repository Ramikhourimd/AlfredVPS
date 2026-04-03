---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Clinical risk management standards
created: '2026-02-26'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z Clinic
  Israel.'
location: []
name: Military-Connected Patients With Weapon Access Require Enhanced Risk Protocols
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Adopt Structured Five-Level Suicidal Risk Assessment Protocol]]'
- '[[constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc Availability]]'
- '[[note/Clinical Supervision - Suicidal Risk Assessment and Military Reporting Protocols]]'
relationships:
- confidence: 0.85
  context: Weapon risks justify supervision framework
  source: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  target: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  type: supports
- confidence: 0.75
  context: Protocols require reliable supervision availability
  source: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  target: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  type: depends-on
- confidence: 0.7
  context: both high-risk protocols
  source: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  target: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  type: related-to
- confidence: 0.7
  context: Alerts critical for weapon-risk responses
  source: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  target: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  type: related-to
source: Clinical risk management standards, military reporting protocols
source_date: '2025-12-01'
status: active
tags: []
type: constraint
---

# Military-Connected Patients With Weapon Access Require Enhanced Risk Protocols

## Constraint

When psychiatric patients are connected to military or security services and have access to a weapon, standard suicidal risk assessment protocols must be elevated. The clinician must assess not only the ideation-intention-plan-act hierarchy but also the patient's access to lethal means (weapon availability), and must follow specific military/security reporting channels when risk is identified.

## Source

During a clinical supervision call on 2025-12-01, case manager Selina contacted Rami Khouri for urgent guidance on a patient with prior suicidal ideation who has military connections and access to a weapon. The case revealed that the clinic's standard risk assessment framework needed to account for weapon access as an aggravating factor and military reporting as an additional documentation requirement.

## Implications

For a telepsychiatry clinic, weapon-access patients represent elevated lethality risk because remote assessment cannot directly verify the patient's physical environment. Case managers must: (1) document weapon access status, (2) escalate to physician supervision immediately rather than at next scheduled contact, and (3) follow military reporting protocols in addition to standard clinical documentation. The clinic's five-level suicidal risk assessment must include weapon access as a risk modifier at each level.

## Expiry / Review

Permanent constraint — applies to all patients with known weapon access regardless of their current risk level. Should be reviewed whenever the clinic's risk assessment protocol is updated.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]