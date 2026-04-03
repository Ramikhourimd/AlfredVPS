---
alfred_instructions: null
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-09-21'
depends_on: []
description: Fix the examination link in the on-call alert so it opens the psychiatric
  examination form instead of the patient intake form.
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide infrastructure issue.
kind: task
name: Fix On-Call Examination Link to Show Correct Form
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[person/Roy Shur]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Fix On-Call Examination Link to Show Correct Form

When the on-call psychiatrist clicks the examination link from the SMS, it opens a patient intake form instead of the psychiatric examination form. The intake form asks for patient name, phone, and email — which is the wrong workflow entirely.

## Context

Identified during the [[conversation/On-Call Alert System Debriefing 2025-09-21]]. The link should open the examination form that the psychiatrist fills out, not the patient self-service intake form. Coordinate with [[person/Roy Shur]] to fix the link target.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.
