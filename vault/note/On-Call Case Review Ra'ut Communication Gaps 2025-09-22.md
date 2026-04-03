---
alfred_tags:
- on-call-system/issues
- incident-review
- project/accountability
created: '2025-09-22'
description: Follow-up discussion on Ra'ut's experience during the first on-call alert
  activation, clarifying her understanding of the process, communication delays, and
  proposed solutions including a live status dashboard and negative-feedback notification
  system
janitor_note: 'LINK001: project wikilink [[project/Telia''z Clinic Israel]] uses YAML
  apostrophe escaping (Telia''''z) which is valid, not broken. LINK001: org wikilink
  [[org/Telia''z]] same YAML escaping false positive. LINK001: related.base#All embed
  references _bases/ infrastructure not yet created — vault-wide gap, not per-file
  fix.'
name: On-Call Case Review Ra'ut Communication Gaps 2025-09-22
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
- '[[person/Rami Khouri]]'
- '[[person/Alex Taliaz]]'
- '[[person/Shachar]]'
- '[[org/Telia''z]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
- '[[task/Conduct Therapist Webinar on On-Call Service]]'
relationships:
- confidence: 0.85
  context: Gaps underscore ownership needs
  source: note/On-Call Case Review Ra'ut Communication Gaps 2025-09-22.md
  target: note/On-Call Project Accountability and Role Ownership 2025-09-22.md
  type: supports
- confidence: 0.7
  context: Persistent on-call gaps
  source: note/On-Call Case Review Ra'ut Communication Gaps 2025-09-22.md
  target: note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09.md
  type: related-to
- confidence: 0.6
  context: Communication and verification
  source: note/On-Call Case Review Ra'ut Communication Gaps 2025-09-22.md
  target: note/Platform Questionnaire Direct-Send Verification Call 2025-10-09.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# On-Call Case Review Ra'ut Communication Gaps 2025-09-22

## Context

Follow-up discussion on 2025-09-22, the day after the [[conversation/On-Call Alert System Debriefing 2025-09-21]], focusing specifically on Ra'ut's (case manager/intake coordinator) experience during the first real on-call alert activation. Participants included [[person/Rami Khouri]], [[person/Alex Taliaz]], and other Telia'z leadership. The conversation happened shortly before Rosh Hashana.

This discussion supplements the technical issues documented in [[note/On-Call Alert System First Activation Issues 2025-09-21]] by examining the case manager's perspective and communication breakdown.

## Ra'ut's Experience

### What Happened
- Ra'ut opened an on-call ticket as per the process
- She understood that an on-call psychiatrist (konan) existed and would respond
- The psychiatrist was supposed to call her back within 30 minutes (per the agreement), but did not
- Ra'ut tried to reach [[person/Rami Khouri]], who was abroad at the time and could not answer the phone initially
- She sent a message to Rami, who then told her to escalate to another contact
- The stress of Rami being unavailable (abroad with Dekkel) added to her anxiety
- Ultimately, the patient WAS seen by a psychiatrist — the service was delivered, but communication gaps caused unnecessary stress

### Key Clarification
- Ra'ut DID understand that an on-call duty system existed
- Her issue was NOT the absence of an on-call doctor, but the communication breakdown — the psychiatrist didn't call her back within the expected timeframe
- The on-call psychiatrist (Atef) did not realize the phone call he received was from the on-call system (related to caller ID issue documented in the technical debriefing)

## Proposed Solutions

### 1. Live Status Dashboard (Shachar)
[[person/Shachar]] built a mobile-friendly dashboard where Rami can monitor on-call status updates in real time, seeing when the psychiatrist clicks the link and engages with the case.

### 2. Negative-Feedback Notification System
Rather than receiving a notification for every action (positive feedback), the team agreed to implement a **negative-feedback alert**: Rami receives a notification ONLY when the psychiatrist fails to click the alert link within 10 minutes. This prevents notification overload while ensuring critical gaps are caught.

### 3. Follow-Up Protocol With Ra'ut
Alex directed that Ra'ut must receive follow-up communication before the following Sunday at the latest:
- Rami will call Ra'ut after the on-call meeting summary is sent
- The message: Rami is back from abroad and available; the case was handled; lessons were learned; improvements are being implemented
- Emphasis on forward-looking reassurance, not dwelling on the incident details
- Goal: Ra'ut should feel the organization is responsive and the system is improving

### 4. Therapist Webinar (Thursday)
A webinar for case managers/therapists was planned for Thursday, providing an opportunity to:
- Meet the therapists face-to-face
- Explain what the on-call service provides and when to use it
- Set expectations for response times and escalation paths
- Learn from Ra'ut's experience without singling her out

## Key Insight

The on-call service itself was delivered — the patient was seen by a psychiatrist and received appropriate recommendations. The clinical summary was delayed, but the recommendations were straightforward and not time-critical. The core issue was communication and expectation management with the case manager, not clinical care delivery.

## Related
![[related.base#All]]