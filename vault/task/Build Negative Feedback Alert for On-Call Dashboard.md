---
alfred_instructions: null
assigned: '[[person/Shachar]]'
blocked_by: []
created: '2025-09-22'
depends_on: []
description: Implement automated notification that alerts Rami ONLY when the on-call
  psychiatrist fails to click the alert link within 10 minutes, using negative-feedback
  approach to avoid notification overload
due: null
janitor_note: LINK001 — Telia'z and Ra'ut wikilinks are valid (YAML escaping false
  positive). related.base#All embed references _bases/related.base which may not exist
  — preserved per policy. ORPHAN001 — standalone task, no inbound links.
kind: task
name: Build Negative Feedback Alert for On-Call Dashboard
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Build Negative Feedback Alert for On-Call Dashboard

Implement an automated alert mechanism on the on-call status dashboard built by [[person/Shachar]]. The system should send a notification to [[person/Rami Khouri]] ONLY when the on-call psychiatrist does NOT click the alert link within 10 minutes of the on-call ticket being opened.

## Context

During the [[note/On-Call Case Review Ra'ut Communication Gaps 2025-09-22]] discussion, the team agreed that positive notifications (for every action) would cause notification fatigue. Instead, a negative-feedback approach was chosen: alert only on inaction.

The dashboard already supports mobile access and real-time status tracking. This task adds the automated timeout notification layer.

## Acceptance Criteria

- If the on-call psychiatrist does not click the alert link within 10 minutes, Rami receives a notification
- No notification is sent when the psychiatrist responds in time (negative feedback only)
- Works with the existing mobile-friendly dashboard Shachar built

## Related
![[related.base#All]]

## Outcome

Filled in on completion.
