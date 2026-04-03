---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: ''
created: '2026-03-03'
janitor_note: 'LINK001: Base view embeds reference _bases/ files not yet created (systemic).
  Teliaz wikilink is valid (YAML escaping false positive).'
name: On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[decision/Conduct Practice Drills at Various Hours Including With Partners]]'
- '[[note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09]]'
- '[[note/On-Call Project Accountability and Role Ownership 2025-09-22]]'
relationships:
- confidence: 0.75
  context: Unreliable alerts impact supervision framework
  source: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  target: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  type: supports
- confidence: 0.65
  context: Alert failures risk documentation gaps
  source: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  target: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  type: related-to
- confidence: 0.85
  context: Alert failures contribute to ad hoc availability
  source: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  target: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  type: supports
- confidence: 0.7
  context: Alert chain vital for high-risk military patients
  source: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  target: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  type: related-to
source: On-call schedule failure incident October 2025
source_date: '2025-10-09'
status: active
type: constraint
---

# On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail

## Constraint

The on-call psychiatrist alert system depends entirely on manual steps: the designated on-call doctor must manually send the duty schedule to the coordinator (Shachar), who then receives alert notifications. If any manual step is missed — a forgotten email, an unreachable phone — the entire alert chain breaks with no automated fallback.

## Source

During the 2025-10-09 on-call incident, Ahmad Masalha (designated on-call psychiatrist) forgot to send the duty schedule to Shachar. Shachar therefore did not receive the alert. The caller could not reach Shachar by phone (no reception in his location). The failure cascaded: no schedule sent → no alert received → no on-call coverage → emergency escalation to Rami.

## Implications

- A single forgotten step by one person disables the entire on-call safety net
- There is no automated schedule distribution, no automated backup routing, and no system-level fallback
- Patient safety depends on human memory and phone availability
- The constraint persists even after the decision to implement automated backup was proposed (implementation status unclear)

## Expiry / Review

This constraint should be re-evaluated once the automated backup system (referenced in [[decision/Implement Automated Backup for On-Call Doctors]]) is implemented and operational.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]