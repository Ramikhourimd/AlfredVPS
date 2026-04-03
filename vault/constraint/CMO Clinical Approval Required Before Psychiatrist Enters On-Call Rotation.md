---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: CMO (Rami Khouri)
created: '2026-03-12'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML single-quote escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist — vault-wide systemic
  gap; embeds preserved per policy. ORPHAN001 — no inbound links; consider linking
  from project/Telia''z Clinic Israel or related decisions.'
name: CMO Clinical Approval Required Before Psychiatrist Enters On-Call Rotation
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[decision/Conduct Practice Drills at Various Hours Including With Partners]]'
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
relationships:
- confidence: 0.85
  context: Pre-rotation psychiatrist requirements
  source: constraint/CMO Clinical Approval Required Before Psychiatrist Enters On-Call
    Rotation.md
  target: constraint/Individual Clickx EHR Account Required Per Psychiatrist With
    OTP Authentication.md
  type: related-to
- confidence: 0.6
  context: Rotation serves high-risk patients
  source: constraint/CMO Clinical Approval Required Before Psychiatrist Enters On-Call
    Rotation.md
  target: constraint/Military-Connected Patients With Weapon Access Require Enhanced
    Risk Protocols.md
  type: related-to
- confidence: 0.7
  context: Approved staff use alert chain
  source: constraint/CMO Clinical Approval Required Before Psychiatrist Enters On-Call
    Rotation.md
  target: constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps
    Fail.md
  type: related-to
source: Clinical governance requirement emphasized during on-call system debriefing
source_date: '2025-09-21'
status: active
type: constraint
---

# CMO Clinical Approval Required Before Psychiatrist Enters On-Call Rotation

## Constraint

Each psychiatrist must receive explicit clinical approval from the CMO (Rami Khouri) before they are authorized to receive patients through the on-call alert system. Being added to the on-call WhatsApp group or rotation schedule is not sufficient — the CMO must verify the psychiatrist's clinical readiness to handle emergency cases independently.

## Source

During the [[conversation/On-Call Alert System Debriefing 2025-09-21]], [[person/Dekkel Taliaz]] emphasized strongly that even if Rami does not personally conduct the on-call training, he must verify it happens and must approve each doctor clinically before they can receive on-call patients. This was reinforced after the first real on-call activation exposed that psychiatrists had been added to the system without completing proper training.

## Implications

- On-call onboarding cannot be fully delegated — the CMO retains a clinical gating function
- New psychiatrists joining the on-call rotation face a dependency on CMO availability for approval
- As Rami transitions toward a Global Medical Director role, this approval authority must be formally transferred to the incoming Medical Director
- Creates a single-person bottleneck for expanding on-call coverage

## Expiry / Review

Should be reviewed when the Medical Director role is filled and clinical supervision responsibilities are formally transferred.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]