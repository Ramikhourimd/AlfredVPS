---
alfred_tags:
- psychiatry/on-call
- system-gaps
based_on:
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
confidence: high
created: '2025-09-22'
janitor_note: 'Previous janitor_note was incorrect: _bases/ directory EXISTS and learn-assumption.base
  embeds are valid. LINK001 flags are false positives. Cleared by vault-janitor 2026-03-14.
  ORPHAN001: No inbound links detected — this is expected for assumption records derived
  from specific notes. Not an error. Observed by vault-janitor 2026-03-16.'
name: On-Call Alert Failure Caused by Caller ID Anonymization Not Process Ignorance
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
- '[[decision/Conduct Practice Drills at Various Hours Including With Partners]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
relationships:
- confidence: 0.7
  context: On-call process failure assumptions
  source: assumption/On-Call Alert Failure Caused by Caller ID Anonymization Not Process
    Ignorance.md
  target: assumption/On-Call Schedule Distribution Relies on Individual Doctor Manual
    Forwarding.md
  type: related-to
- confidence: 0.8
  context: Visibility gaps in on-call alerts
  source: assumption/On-Call Alert Failure Caused by Caller ID Anonymization Not Process
    Ignorance.md
  target: assumption/On-Call Staff Anxiety Driven by Status Visibility Gaps Not Process
    Misunderstanding.md
  type: related-to
source: Ra'ut case review and on-call debriefing
source_date: '2025-09-22'
status: confirmed
type: assumption
---

# On-Call Alert Failure Caused by Caller ID Anonymization Not Process Ignorance

## Claim

The first real on-call alert failure (September 2025) was caused by a technology gap — caller ID anonymization — not by staff ignorance of the on-call process. Ra'ut (case manager) correctly followed every step of the on-call protocol. The on-call psychiatrist (Atef) did not realize the incoming phone call was from the on-call system because the caller ID did not identify it as such.

## Basis

The 2025-09-22 case review revealed a critical distinction: Ra'ut opened the on-call ticket correctly, understood the process, and expected a callback within 30 minutes per the agreement. The failure point was Atef not recognizing the call as an on-call alert. This reframes the problem from "staff need more training" to "the technology must make on-call calls identifiable."

Key evidence:
- Ra'ut DID understand that an on-call duty system existed
- Ra'ut's issue was NOT the absence of an on-call doctor, but the communication breakdown
- Atef did not realize the phone call he received was from the on-call system (caller ID issue)
- The patient WAS ultimately seen — the service was delivered, but with unnecessary delay and stress

## Evidence Trail

- 2025-09-21: First real on-call alert activation revealed multiple gaps (technical debriefing)
- 2025-09-22: Ra'ut case review confirmed process knowledge was present; technology was the failure point
- Shachar built a real-time status dashboard as a technology-based solution (confirming the technology framing)

## Impact

- On-call system improvements should prioritize caller ID identification and technology fixes over process retraining
- Practice drills (already decided) serve to verify technology works, not just to teach process
- Future on-call system design must ensure the alerting mechanism is unmistakably identifiable to the receiving psychiatrist