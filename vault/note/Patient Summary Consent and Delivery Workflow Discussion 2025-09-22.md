---
alfred_tags:
- healthcare/patient-summary-delivery
- clinic/contractual-obligations
- workflow/consent
created: '2025-09-22'
description: Discussion on patient summary delivery and consent workflow for the on-call
  psychiatry service. Clarified legal requirements under Israeli patient rights law,
  the standard platform flow, and why the current incident bypassed the normal process.
janitor_note: LINK001 — Telia'z wikilinks (project/Telia'z Clinic Israel, org/Telia'z)
  are valid names with YAML single-quote escaping false positives. Base view embed
  (related.base#All) references nonexistent _bases/ directory — vault-wide systemic
  issue, embed preserved.
name: Patient Summary Consent and Delivery Workflow Discussion 2025-09-22
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Oren Taliaz]]'
- '[[person/Dekkel Taliaz]]'
- '[[org/Telia''z]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
relationships:
- confidence: 0.85
  context: Workflow discussion supports contractual delivery
  source: note/Patient Summary Consent and Delivery Workflow Discussion 2025-09-22.md
  target: assumption/Immediate Patient Summary Delivery Is Contractual and Defines
    Case Closure.md
  type: supports
- confidence: 0.8
  context: Both discuss patient summary delivery aspects
  source: note/Patient Summary Consent and Delivery Workflow Discussion 2025-09-22.md
  target: note/Patient Summary Immediate Delivery Expectation Discussion 2025-09-22.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Patient Summary Consent and Delivery Workflow Discussion 2025-09-22

## Context

During the [[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]], the team discussed the patient summary and consent workflow in detail, prompted by the current on-call case where the summary had not been delivered to the referring therapist (Ra'ut).

## Standard Flow (When System Works)

1. **Referral received** — Therapist/case manager opens a ticket through the platform
2. **Patient consent** — Before the psychiatrist can see the patient, the patient must sign a consent form that includes permission to share clinical data with the referring therapist/organization
3. **Patient file created** — System automatically creates a patient record
4. **Teams session** — Psychiatrist conducts the assessment via Microsoft Teams
5. **Auto-transcription** — The session is automatically transcribed
6. **Summary generation** — The AI system generates a clinical summary from the transcription
7. **Psychiatrist approval** — The psychiatrist reviews and approves the summary (this step is mandatory — the summary does not advance without approval)
8. **Summary delivery** — Once approved, the summary is automatically sent to the patient and the referring therapist

## Why This Case Deviated

In the current on-call incident:
- The consent form was sent to Atef (the psychiatrist) instead of the patient due to a technical bug
- No patient file was automatically created in the system
- No Teams session was scheduled — Atef conducted the assessment by regular phone call
- Therefore: no transcription, no auto-generated summary, no automated delivery
- Atef wrote the summary manually; Rami emailed it to [[person/Roy Shur]]
- [[person/Shachar]] manually created a patient file to allow the normal flow to resume

## Legal Framework

Under Israeli patient rights law (Rami's explanation):
- Two practitioners at **different institutions** require **explicit patient consent** to share clinical information
- The consent should preferably be signed (written), though there is legal debate about phone-based consent
- The standard Telia'z flow handles this automatically — consent is obtained before the psychiatrist sees the patient
- If a psychiatrist recommends emergency referral (e.g., ER visit), they can give the recommendation directly to the patient; they do not need the therapist's involvement for that
- For ongoing care coordination, the consent enables sharing the summary with the referring therapist

## Key Lesson

When the system works as designed, summary delivery is automatic and immediate. The on-call case exposed that any deviation from the standard flow (e.g., phone-only assessment without Teams) breaks the automated chain and requires manual intervention.

[[person/Dekkel Taliaz]] confirmed this is already part of the platform design — the issue was process execution, not system capability. For Maccabi patients specifically, summaries still need to be manually entered into Clickx (their EHR system).

## Related
![[related.base#All]]