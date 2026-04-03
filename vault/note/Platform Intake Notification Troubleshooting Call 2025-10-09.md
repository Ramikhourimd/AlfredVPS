---
created: '2026-03-02'
description: Rami walks an unidentified clinician through the 3-link patient intake
  email workflow after the system failed to deliver the notification, involving Shachar
  for email resend and system registration
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist. Vault-wide infrastructure gap.
name: Platform Intake Notification Troubleshooting Call 2025-10-09
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
- '[[org/Telia''z]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships: []
session: null
status: active
subtype: reference
tags: []
type: note
---

# Platform Intake Notification Troubleshooting Call 2025-10-09

## Context

Voice memo captured on 2025-10-09. Rami Khouri calls an unidentified clinician (likely a psychiatrist or case manager) after noticing that a patient intake event ("kria") was triggered in the system but the clinician never received the expected notification. The conversation is in Arabic and covers both the immediate troubleshooting and a full walkthrough of the platform's 3-link intake workflow.

## Issue

The clinical platform triggered an intake event that should have resulted in:
1. An automated phone ring to the clinician's device
2. An email with three operational links

Neither the phone call nor the email reached the clinician. Rami suspects Shachar (VP R&D) may not have registered the clinician's phone number and email correctly in the system.

## Three-Link Intake Email Workflow

Rami explains the three links ("kishurim") contained in the intake email:

### Link 1: Phone Call With Patient (Sihat Telefon)
- Activates a phone conversation with the patient (metabal)
- The clinician listens to the patient's story and conducts an initial assessment
- Duration: approximately 15 minutes
- Purpose: preliminary screening to determine whether to proceed with a full examination
- The clinician should collect as much detail as possible, noting that the administrative staff who open the cases do not always have complete patient information

### Link 2: Summary Form (Sikum)
- A summary/form generated based on the phone call
- Sent to the patient for agreement/signature on the treatment schema
- The clinician edits the summary based on what was discussed in the phone call and sends it to the patient via email

### Link 3: Video Session Form (Tofes)
- A form sent to the patient that triggers a Teams video session
- Once the patient signs/confirms, a Teams video link opens within approximately 30 minutes
- The clinician then conducts the full examination via Teams video
- A standard sikum (summary) is completed at the end of the session, as with regular appointments

## Resolution

Rami instructs the clinician to:
1. Call Shachar directly (not just message)
2. Ask Shachar to resend the email with the three links
3. Ensure Shachar registers the clinician's phone number in the system (not just email -- the system needs the phone number for the callback feature)

Rami notes he is driving and cannot handle the system details himself at that moment. The clinician confirms the phone call portion should happen within about 15 minutes and agrees to contact Shachar immediately.

## Key Technical Detail

Shachar recently changed the system workflow. Previously, the system would send a notification to the administrative staff to manually enter the clinician's phone number. Now the system may send a direct link (shirat), but the clinician's profile must have their phone number pre-populated for the callback to work.

## Related
![[related.base#All]]
