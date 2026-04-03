---
based_on:
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-15'
invalidated_by: []
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  [[assumption/On-Call Alert Failure Caused by Caller ID Anonymization Not Process
  Ignorance]] EXISTS — scanner confused by long filename wrapping. ORPHAN001 — no
  inbound links; consider linking from project/Telia'z Clinic Israel or decision/Implement
  Automated Backup for On-Call Doctors.
name: Backup On-Call Doctor Provides Acceptable Degraded Coverage for Rare Emergencies
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
- '[[assumption/On-Call Alert Failure Caused by Caller ID Anonymization Not Process
  Ignorance]]'
source: On-call backup system discussion 2025-09-21
source_date: '2025-09-21'
status: active
tags:
- on-call
- clinical-safety
type: assumption
---

# Backup On-Call Doctor Provides Acceptable Degraded Coverage for Rare Emergencies

## Claim

The team explicitly acknowledged that a backup on-call doctor will inherently be "less on-call" than the primary — meaning response probability degrades when the system escalates to backup. The group accepted this trade-off because: (1) the primary on-call doctor is in an active readiness state, (2) backup is only triggered in genuinely rare force majeure situations (sick, ER, accident), and (3) some coverage is better than none.

## Basis

- On-call backup discussion (2025-09-21): One participant raised the concern about degraded readiness; the group deliberately accepted it
- The definitional point was made: "if a doctor is on-call, they are on-call — they cannot simultaneously be in the ER." Backup addresses situations outside normal expectations.

## Evidence Trail

- 2025-09-21: Team agreed backup provides acceptable degraded coverage (note/On-Call Backup System Discussion 2025-09-21)

## Impact

If the backup system is ever activated in a real emergency and the backup doctor also fails to respond, there is no third-tier fallback. This is an accepted risk. Any future on-call incident involving backup failure should prompt re-evaluation of this assumption.
