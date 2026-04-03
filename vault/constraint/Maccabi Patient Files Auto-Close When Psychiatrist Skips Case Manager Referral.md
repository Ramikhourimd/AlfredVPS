---
authority: Maccabi Healthcare Services system rules
created: '2026-03-13'
janitor_note: LINK001 — Telia'z wikilink (project/Telia'z Clinic Israel) is valid
  (YAML escaping false positive). ORPHAN001 — no inbound wikilinks from other records.
name: Maccabi Patient Files Auto-Close When Psychiatrist Skips Case Manager Referral
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Investigate Maccabi Patient File Closure Issue With Psychiatrist Scheduling]]'
- '[[constraint/No Commitment Renewal Workflow Exists in Retool]]'
- '[[org/Maccabi Healthcare Services]]'
source: Operational processes discussion — Shira flagged as critical
source_date: '2025-11-09'
status: active
type: constraint
---

# Maccabi Patient Files Auto-Close When Psychiatrist Skips Case Manager Referral

## Constraint

When a Maccabi patient completes a psychiatrist appointment, the psychiatrist must redirect the patient to a case manager for ongoing scheduling. If this referral step is missed, the Maccabi system automatically closes the patient's file. The patient loses continuity of care with no automated safety net to catch the gap.

## Source

Flagged as a critical operational issue during the 2025-11-09 operational processes discussion. Shira and the operations team identified patients actively falling through the cracks.

## Implications

- Patients lose access to ongoing treatment without notification
- Revenue loss from discontinued treatment relationships
- Clinical risk from interrupted care pathways
- Potential compliance violation with Maccabi service agreements
- No automated detection exists — the gap is only discovered when a patient or secretary notices

## Expiry / Review

Active until either: (1) an automated case manager referral is implemented post-psychiatrist appointment, (2) the Maccabi system rules are changed, or (3) the platform rebuild includes a mandatory referral step.
