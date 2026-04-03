---
alfred_tags:
- psychiatry/on-call
- system-gaps
based_on:
- '[[note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
challenged_by:
- '[[note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09]]'
confidence: high
confirmed_by: []
created: '2026-03-13'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  synthesis/Manual Single-Person Dependencies link needs manual verification. Base
  view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide infrastructure gap, embeds preserved. ORPHAN001
  — no inbound wikilinks; consider linking from project/Telia''z Clinic Israel.'
name: On-Call Schedule Distribution Relies on Individual Doctor Manual Forwarding
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
- '[[synthesis/Manual Single-Person Dependencies Create Cascading Failure Points Across
  Clinic Operations]]'
relationships:
- confidence: 0.75
  context: Manual processes cause on-call gaps
  source: assumption/On-Call Schedule Distribution Relies on Individual Doctor Manual
    Forwarding.md
  target: assumption/On-Call Staff Anxiety Driven by Status Visibility Gaps Not Process
    Misunderstanding.md
  type: related-to
source: On-Call Schedule Failure 2025-10-09
source_date: '2025-10-09'
status: active
tags: []
type: assumption
---

# On-Call Schedule Distribution Relies on Individual Doctor Manual Forwarding

## Claim

The on-call psychiatrist system depends on the designated on-call doctor to manually forward the on-call duty schedule to the next person in the chain (e.g., Shachar/operations). There is no automated schedule distribution — if the doctor forgets to send the schedule, downstream recipients are never notified they are on the rotation and the entire alert chain breaks.

## Basis

On 2025-10-09, an on-call alert was triggered but the process failed because Ahmad (Ahmed Masalha), the designated on-call psychiatrist, forgot to send the on-call duty schedule to Shachar (Segev). Shachar did not receive the alert because he was not on the schedule. The caller could not reach Shachar (no phone reception), and had to contact Ahmad directly to resolve the situation. This is the second on-call failure in a month — the first real activation on 2025-09-21 also revealed multiple process gaps.

## Evidence Trail

- 2025-09-21: First real on-call activation revealed five distinct technical and process failures
- 2025-09-21: Backup system discussion acknowledged need for automated escalation
- 2025-10-09: Schedule distribution failure confirmed the manual forwarding dependency
- The pattern of repeated failures in the same system within weeks suggests the manual process is structurally unreliable

## Impact

- The on-call system's reliability is bounded by individual doctor compliance with a manual administrative task
- A psychiatrist forgetting one email can render the entire emergency response system non-functional
- This creates liability risk: if a patient emergency occurs during a schedule gap, no one may respond
- The proposed automated backup system (from 2025-09-21 discussion) would partially mitigate this, but does not address the root cause of manual schedule distribution

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]