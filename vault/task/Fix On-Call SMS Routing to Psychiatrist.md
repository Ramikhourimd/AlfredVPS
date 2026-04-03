---
alfred_instructions: null
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-09-21'
depends_on: []
description: Fix the on-call alert SMS so it addresses the assigned psychiatrist instead
  of the case manager who opened the referral.
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide infrastructure gap.
kind: task
name: Fix On-Call SMS Routing to Psychiatrist
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

# Fix On-Call SMS Routing to Psychiatrist

The SMS containing the examination link was addressed to Ra'ut (the case manager who opened the referral) instead of to Atef (the on-call psychiatrist). The SMS read "Hello Ra'ut" and contained the examination link.

## Context

Identified during the [[conversation/On-Call Alert System Debriefing 2025-09-21]]. The SMS routing logic appears to use the referral opener's name instead of the assigned on-call doctor's name. This needs to be fixed in the alert system's notification logic. Coordinate with [[person/Roy Shur]].

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.
