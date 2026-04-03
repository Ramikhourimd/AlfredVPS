---
based_on:
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
confidence: high
created: '2026-03-03'
janitor_note: 'LINK001: (1) Telia''z Clinic Israel wikilink is valid — YAML escaping
  false positive. (2) Base view embeds (learn-assumption.base#Depends On This, #Related)
  reference non-existent _bases/learn-assumption.base — vault-wide infrastructure
  issue, embeds preserved. ORPHAN001: No inbound wikilinks — consider linking from
  project/Telia''z Clinic Israel or related decision records.'
name: Project Ownership Requires End-to-End Verification Including Delegated Tasks
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[note/On-Call Project Accountability and Role Ownership 2025-09-22]]'
source: Dekkel Taliaz during on-call incident review meeting
source_date: '2025-09-22'
status: active
type: assumption
---

# Project Ownership at Telia'z Requires End-to-End Verification Including Delegated Tasks

## Claim

When a project is assigned to an individual at Telia'z, ownership means full accountability for completion — including verification that delegated sub-tasks are actually executed. Delegation without follow-up verification is not accepted by leadership as an excuse for gaps.

## Basis

During the 2025-09-22 on-call incident review meeting, Dekkel Taliaz explicitly stated that the on-call project was a "closed project" under Rami — meaning Rami bore end-to-end responsibility. Even when Rami delegated tasks to Roy Shur or Shachar, Rami was expected to verify they were completed. Dekkel's position: "If you believe someone else should own part of the project, flag it proactively to leadership — don't let it fall through."

## Evidence Trail

- 2025-09-22: Dekkel stated this principle during on-call post-mortem. Oren echoed the position.
- 2025-10-09: Principle validated when on-call schedule distribution failed because Ahmad forgot to send the schedule — exactly the delegation-without-verification pattern Dekkel warned about.

## Impact

This principle applies beyond on-call to all project ownership at Telia'z:
- Project leads must build verification checkpoints for delegated work
- "I told someone to do it" is not sufficient — confirmation of completion is required
- When a project lead cannot verify delegated work (e.g., due to travel), they must arrange backup verification or escalate to leadership

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
