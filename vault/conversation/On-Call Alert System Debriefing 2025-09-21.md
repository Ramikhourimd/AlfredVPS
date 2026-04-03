---
alfred_instructions: null
channel: phone
created: '2025-09-21'
description: Debriefing call after the first real activation of the on-call psychiatrist
  alert system at Telia'z clinic. Identified multiple technical issues including wrong
  caller ID, missing auto-voice message, no acknowledgment mechanism, and incorrect
  SMS/link routing.
external_id: null
fork_reason: null
forked_from: null
janitor_note: 'LINK001 false positives: Telia''z and Ra''ut wikilinks use YAML single-quote
  escaping (targets exist). Base view embeds (conversation-detail.base#Messages, #Tasks,
  #Related) reference _bases/ infrastructure — preserved per policy.'
last_activity: '2025-09-21'
message_count: 0
opened: '2025-09-21'
org: '[[org/Telia''z]]'
participants:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[person/Roy Shur]]'
- '[[person/Shachar]]'
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
relationships: []
status: resolved
subject: On-Call Alert System Debriefing 2025-09-21
tags: []
type: conversation
---

# On-Call Alert System Debriefing 2025-09-21

## Current State

**Status:** Resolved
**Ball in court of:** [[person/Rami Khouri]] — to coordinate fixes with [[person/Roy Shur]] and [[person/Shachar]]
**Last activity:** 2025-09-21
**Risk/urgency:** High — alert system has multiple defects that could delay psychiatric emergency response
**Next expected action:** Schedule follow-up call with Roy Shur and Shachar to address technical issues

## Activity Log

| Date | Who | Action |
|------|-----|--------|
| 2025-09-21 | [[person/Dekkel Taliaz]] | Initiated debriefing call to learn from first real alert activation |
| 2025-09-21 | Atef (on-call psychiatrist) | Reported issues encountered during the alert: wrong caller ID, no auto-voice, no acknowledgment button |
| 2025-09-21 | [[person/Rami Khouri]] | Documented issues; assigned to coordinate fixes |
| 2025-09-21 | Atef | Reported that SMS with examination link was addressed to Ra'ut, not to him |
| 2025-09-21 | Atef | Reported that the examination link opened a patient intake form instead of the examination form |
| 2025-09-21 | [[person/Rami Khouri]] | Confirmed that telephony was originally built by [[person/Shachar]] |
| 2025-09-21 | [[person/Dekkel Taliaz]] | Emphasized need for formal training and practice drills for on-call doctors |

## Context

This was the **first real activation** of the on-call psychiatrist alert system after more than one month of the system being live. [[person/Dekkel Taliaz]] called the debriefing explicitly to learn from the experience and improve the process, not to assign blame.

### Participants
- [[person/Dekkel Taliaz]] — CEO, initiated the debriefing
- [[person/Rami Khouri]] — Operations, documenting and coordinating fixes
- Atef — On-call psychiatrist who received the alert

### Issues Identified

1. **Wrong caller ID**: Phone displayed "Elitaz" instead of "Telia'z" — Atef did not recognize the number
2. **No auto-voice message**: When Atef answered, there was no automated voice message explaining the alert
3. **No acknowledgment mechanism**: No option to press "1" to confirm receipt of the alert
4. **Email link auto-dialed Ra'ut**: Clicking the email link from phone auto-dialed Ra'ut (the case manager who initiated the referral) instead of connecting properly
5. **SMS addressed to wrong person**: The SMS with the examination link said "Hello Ra'ut" instead of addressing the on-call doctor
6. **Wrong form in examination link**: The link opened a patient intake form instead of the psychiatric examination form
7. **Ra'ut lacked email access**: The case manager (Ra'ut) who opened the referral did not have email access
8. **No training conducted**: On-call doctors had not received formal training on the alert system
9. **No practice drills**: No dry-run exercises had been conducted despite the system being live for over a month

### Key References
- [[person/Roy Shur]] — system owner, needs to be involved in fixes
- [[person/Shachar]] — originally built the telephony component
- [[person/Sofian Faris]] — previously handled triage calls from computer (reference for how call mechanism works)

## Messages
![[conversation-detail.base#Messages]]

## Tasks
![[conversation-detail.base#Tasks]]

## Related
![[conversation-detail.base#Related]]
