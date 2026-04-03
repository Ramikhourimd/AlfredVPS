---
created: '2025-11-10'
description: Clickx EHR retained for diagnoses, medications, and referrals. Five staff
  members have access issues. Transition from shared to individual user accounts directed.
janitor_note: LINK001 — Telia'z wikilinks (project/Telia'z Clinic Israel, org/Telia'z)
  are valid (YAML escaping false positive). Base view embed (related.base#All) references
  _bases/related.base which does not exist — vault-wide infrastructure issue.
name: Clickx EHR System Migration and Access Management 2025-11-10
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Operations and System Management Meeting 2025-11-10]]'
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
- '[[org/Telia''z]]'
- '[[task/Resolve Clickx Access for Staff Members]]'
- '[[task/Transition Clickx to Individual User Accounts]]'
- '[[task/Check ICD Version Compatibility in Clickx]]'
- '[[task/Build Patient Blacklist Feature in Clickx]]'
- '[[decision/Clickx Retained for Diagnoses Medications and Referrals]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Clickx EHR System Migration and Access Management 2025-11-10

## Context

Discussion during the 2025-11-10 operations meeting about the state of the Clickx EHR system, access problems for multiple staff members, and the decision to retain Clickx for specific clinical functions.

## Clickx System Scope

Clickx is retained specifically for:
- **Diagnoses** — clinical diagnosis recording
- **Medications** — prescription management
- **Referrals** — referral letter generation

Other clinical documentation functions have migrated to the internal platform.

## Access Issues

Shira reported that multiple staff members have Clickx access problems:
- **Uriel** — cannot access the system
- **Jenny** — cannot access the system
- **Selina** — cannot access the system
- **Elinor** — cannot access the system
- **Noa** — cannot access the system

These access issues need immediate resolution as they affect clinical operations.

## Individual User Accounts

Rami directed a transition from shared credentials to individual user accounts:
- Currently some staff share login credentials (security and audit concern)
- Each clinician must have their own Clickx account
- This supports proper audit trails and accountability
- Shira to coordinate the account creation process

## ICD Version Query

Rami raised a question about which ICD version Clickx uses:
- Need to confirm with Nirit whether the system uses ICD-10 or an older version
- This affects diagnosis coding accuracy and compliance

## Patient Blacklist Feature

Discussion about the need for a patient blacklist feature in Clickx:
- Currently no mechanism to flag patients who should not be treated
- This is needed for operational safety
- Feature request to be raised with the Clickx vendor or built internally

## Key Takeaways

1. **Clickx retained** for diagnoses, medications, and referrals only
2. **5 staff members** blocked from access — urgent resolution needed
3. **Individual accounts** required — end shared credential usage
4. **ICD version** needs confirmation with Nirit
5. **Blacklist feature** needed for patient safety

## Related
![[related.base#All]]
