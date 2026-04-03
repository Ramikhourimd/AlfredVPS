---
alfred_tags:
- on-call-system/issues
- incident-review
- project/accountability
created: '2025-10-09'
description: Phone call about on-call emergency where Ahmad forgot to send duty schedule
  to Shachar, causing missed alert. Rami verifies patient Roei Shalev details in system
  for questionnaire direct-send.
janitor_note: 'LINK001 false positive: Telia''z wikilinks are YAML escaping artifacts
  — targets exist with single apostrophe. Base view embed (related.base) references
  _bases/ file that does not exist — vault-wide structural gap.'
name: On-Call Schedule Failure and Patient Intake Verification 2025-10-09
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
- '[[person/Ahmed Masalha]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[note/Platform Questionnaire Direct-Send Verification Call 2025-10-09]]'
- '[[note/Nova Survivor Patient Intake Platform Coordination 2025-10-09]]'
relationships:
- confidence: 0.85
  context: Same-day verification incidents
  source: note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09.md
  target: note/Platform Questionnaire Direct-Send Verification Call 2025-10-09.md
  type: related-to
session: null
status: active
subtype: reference
tags: []
type: note
---

# On-Call Schedule Failure and Patient Intake Verification 2025-10-09

## Context

Voice memo captured on 2025-10-09. An unidentified caller (Speaker 4) phones Rami Khouri about an on-call emergency at Telia'z Clinic Israel. The call covers two issues: a process failure in the on-call schedule distribution, and verification of patient data in the platform.

## On-Call Schedule Failure

An on-call alert (כוננות) was triggered, but the process broke down:

1. **Ahmad (Ahmed Masalha) was the designated on-call psychiatrist** but forgot to send the on-call duty schedule to Shachar (Segev).
2. **Shachar did not receive the alert** because he was not on the schedule.
3. **The caller could not reach Shachar** (no phone reception in his location).
4. **The caller spoke directly with Ahmad**, who then contacted Shachar.
5. **Shachar needs to update his phone number** in the system and will then handle the on-call call and receive the email notification.

The caller asked Rami to step in as a background monitor for this situation.

## Patient Intake Verification

The caller also asked Rami to verify that the initial questionnaire form had the required patient details filled in, specifically the phone number — necessary for the second questionnaire to be sent directly to the patient.

Rami checked the system and confirmed:
- **Patient name:** Roei Shalev
- **Phone number:** Filled in correctly
- **Consent form:** Not yet filled (Ahmad had not yet called the patient)

The caller confirmed Ahmad had not yet made the call, so the missing consent form was expected.

## Operational Observations

- The on-call scheduling process relies on manual schedule distribution, which is fragile — a single forgotten email caused the entire on-call chain to fail.
- Shachar being away from his computer and out of phone reception created an additional delay.
- The questionnaire direct-send feature (verified in a separate call the same day) depends on intake staff entering patient phone numbers, which worked correctly in this case.

## Related
![[related.base#All]]