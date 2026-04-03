---
alfred_instructions: null
alfred_tags:
- on-call/training
- on-call/drills
- on-call/incident-management
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2025-09-21'
depends_on: []
description: Implement regular practice drills for the on-call alert system. Since
  real alerts are rare (first one after 1+ month), drills are needed to maintain readiness
  and catch system issues.
due: null
janitor_note: 'LINK001: (1) Telia''''z wikilink is YAML escaping false positive. (2)
  Base view embeds (related.base#All) appear twice — systemic, preserved per policy.
  DUPLICATE BODY: Entire note body content is repeated twice — needs manual cleanup.'
kind: task
name: Implement On-Call Practice Drills
priority: medium
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[person/Dekkel Taliaz]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
- '[[decision/Conduct Practice Drills at Various Hours Including With Partners]]'
- '[[person/Alex Lellouche]]'
relationships:
- confidence: 0.7
  context: On-call practice and incident tasks
  source: task/Implement On-Call Practice Drills.md
  target: task/Rami Call Ra'ut to Close On-Call Incident Loop.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Implement On-Call Practice Drills

The on-call alert system was live for over a month before the first real activation. Regular practice drills are needed to keep doctors ready and to identify system issues proactively.

## Context

Identified during the [[conversation/On-Call Alert System Debriefing 2025-09-21]]. [[person/Dekkel Taliaz]] emphasized that practice drills serve two purposes:
1. **Readiness** — keeping on-call doctors familiar with the process, especially since real alerts may be rare
2. **System validation** — catching technical issues (like the ones found in this debriefing) before they affect real emergency responses

Drills should simulate the full workflow: alert call → acknowledgment → accessing examination link → mock documentation.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.

# Implement On-Call Practice Drills

The on-call alert system was live for over a month before the first real activation. Regular practice drills are needed to keep doctors ready and to identify system issues proactively.

## Context

Identified during the [[conversation/On-Call Alert System Debriefing 2025-09-21]]. [[person/Dekkel Taliaz]] emphasized that practice drills serve two purposes:
1. **Readiness** — keeping on-call doctors familiar with the process, especially since real alerts may be rare
2. **System validation** — catching technical issues (like the ones found in this debriefing) before they affect real emergency responses

Drills should simulate the full workflow: alert call → acknowledgment → accessing examination link → mock documentation.

## Updated Requirements (from [[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]])

[[person/Alex Lellouche]] specified a multi-layered drill approach per [[decision/Conduct Practice Drills at Various Hours Including With Partners]]:

1. **Internal drill first** — Test the full workflow internally with on-call doctors and the technical team
2. **Joint drill with Ra'ut** — Include Ra'ut (the referring therapist) in a subsequent drill. This serves dual purpose: system validation AND rebuilding her confidence after the stressful incident
3. **Off-hours drill** — Test the system at unusual hours (e.g., 2:00 AM) to verify the on-call doctor responds when potentially asleep
4. **Cover all scenarios** — Test different callers (not just Ra'ut), different hours, different on-call doctors

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.