---
alfred_tags:
- on-call-system/issues
- incident-review
- project/accountability
created: '2025-09-21'
description: Comprehensive list of technical issues found during the first real activation
  of the on-call psychiatrist alert system at Telia'z clinic, with proposed improvements.
janitor_note: LINK001 — Telia'z and Ra'ut wikilinks are valid (YAML single-quote escaping
  false positives; all targets exist). related.base#All embed references _bases/related.base
  which does not exist — vault-wide infrastructure gap, embed preserved.
name: On-Call Alert System First Activation Issues 2025-09-21
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Roy Shur]]'
- '[[person/Shachar]]'
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
relationships:
- confidence: 0.8
  context: Sequential on-call incidents
  source: note/On-Call Alert System First Activation Issues 2025-09-21.md
  target: note/On-Call Case Review Ra'ut Communication Gaps 2025-09-22.md
  type: related-to
- confidence: 0.7
  context: Issues exemplify role gaps
  source: note/On-Call Alert System First Activation Issues 2025-09-21.md
  target: note/On-Call Project Accountability and Role Ownership 2025-09-22.md
  type: supports
- confidence: 0.65
  context: Ongoing on-call system problems
  source: note/On-Call Alert System First Activation Issues 2025-09-21.md
  target: note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09.md
  type: related-to
- confidence: 0.55
  context: Shared verification themes
  source: note/On-Call Alert System First Activation Issues 2025-09-21.md
  target: note/Platform Questionnaire Direct-Send Verification Call 2025-10-09.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# On-Call Alert System First Activation Issues 2025-09-21

## Context

After more than one month of the on-call psychiatrist alert system being live at [[project/Telia'z Clinic Israel]], the first real alert was triggered. [[person/Dekkel Taliaz]] initiated a [[conversation/On-Call Alert System Debriefing 2025-09-21]] to identify issues and improve the process.

The alert was initiated by Ra'ut (case manager/intake coordinator). Atef (on-call psychiatrist) received the alert. Multiple technical and process failures were identified.

## Technical Issues

### 1. Caller ID Shows "Elitaz" Instead of "Telia'z"
The incoming call displayed "Elitaz" via TrueCaller. Atef did not recognize it and almost ignored the call. **Minimum fix**: require every on-call doctor to save the alert phone number in their contacts. **Ideal fix**: change the caller ID display.

### 2. No Automated Voice Message
When Atef answered the call, there was silence — no automated voice message explaining the nature of the alert. [[person/Rami Khouri]] noted this feature was supposed to exist.

### 3. No Acknowledgment Mechanism
There is no "press 1 to confirm" option. The system cannot verify whether the on-call doctor actually received and understood the alert. If the call connects but nobody is listening (bad reception, accidental answer), there is no fallback. This ties into the [[decision/Implement Automated Backup for On-Call Doctors]] for escalation.

### 4. Email Link Auto-Dials Ra'ut From Phone
When Atef clicked the email link on his phone, it automatically dialed Ra'ut's number. The telephony system (originally built by [[person/Shachar]]) was designed to create a conference call from the system's phone number, calling both parties. Needs investigation into whether clicking from a computer vs. phone behaves differently. [[person/Sofian Faris]] previously used the system from a computer for triage.

### 5. SMS Addressed to Wrong Person
The SMS containing the examination link said "Hello Ra'ut" instead of addressing the on-call doctor (Atef). The SMS routing appears to target the referral opener rather than the assigned psychiatrist.

### 6. Examination Link Opens Patient Intake Form
Instead of opening the psychiatric examination form, the link opened a patient intake form asking for patient's name, phone, and email. This is the wrong form entirely.

### 7. Ra'ut Lacks Email Access
The case manager (Ra'ut) who opened the referral reported not having email access, creating a gap in the communication chain.

## Process Issues

### 8. No Formal Training Conducted
On-call doctors received no formal training on the alert system. They were added to a WhatsApp group but not walked through the process. [[person/Dekkel Taliaz]] emphasized that [[person/Rami Khouri]] must verify that training happens, even if someone else conducts it.

### 9. No Practice Drills
No dry runs or practice alerts have been conducted despite the system being live for over a month. Dekkel emphasized that drills serve dual purposes: keeping doctors ready AND identifying system issues before they occur in real emergencies.

## Action Items

- Fix caller ID or mandate contact saving → [[task/Fix On-Call Alert Caller ID Display]]
- Investigate auto-voice message → [[task/Investigate On-Call Alert Auto-Voice Message]]
- Add press-1 acknowledgment → [[task/Add Acknowledgment Button to On-Call Alert Calls]]
- Fix SMS routing to on-call doctor → [[task/Fix On-Call SMS Routing to Psychiatrist]]
- Fix examination link form → [[task/Fix On-Call Examination Link to Show Correct Form]]
- Investigate call mechanism from computer → [[task/Investigate On-Call Call Mechanism From Computer]]
- Conduct formal training → [[task/Conduct On-Call System Training for Psychiatrists]]
- Implement practice drills → [[task/Implement On-Call Practice Drills]]

## Related
![[related.base#All]]