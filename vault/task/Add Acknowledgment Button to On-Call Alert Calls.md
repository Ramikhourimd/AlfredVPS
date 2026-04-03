---
alfred_instructions: null
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-09-21'
depends_on: []
description: Add a press-1-to-confirm acknowledgment mechanism to on-call alert calls
  so the system can verify the doctor received the alert.
due: null
janitor_note: 'LINK001: related.base embed references missing _bases/ infrastructure
  — vault-wide gap. Telia''z project link is valid (scanner false positive from YAML
  quote escaping).'
kind: task
name: Add Acknowledgment Button to On-Call Alert Calls
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[person/Roy Shur]]'
- '[[person/Shachar]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Add Acknowledgment Button to On-Call Alert Calls

Currently there is no way to confirm that the on-call doctor received and understood the alert. Add a "press 1 to confirm" mechanism.

## Context

Identified during the [[conversation/On-Call Alert System Debriefing 2025-09-21]]. Without acknowledgment, the system cannot distinguish between a successful alert delivery and a dropped/ignored call. This is a prerequisite for the backup escalation described in [[decision/Implement Automated Backup for On-Call Doctors]] — if no acknowledgment within a defined window, the system should call the backup doctor.

Coordinate with [[person/Roy Shur]] and [[person/Shachar]] for implementation.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.
