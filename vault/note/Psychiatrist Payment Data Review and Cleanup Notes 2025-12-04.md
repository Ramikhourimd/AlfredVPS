---
created: '2026-02-25'
description: Detailed notes from Rami and Basel joint session reviewing monthly psychiatrist
  payment spreadsheets, covering data cleaning methodology, compensation calculation
  logic, staff-specific billing issues, and the need for standardized reporting templates
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — create it to enable dynamic views.
name: Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Psychiatrist Payment Data Review and Cleanup 2025-12-04]]'
- '[[person/Rami Khouri]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Shira]]'
- '[[person/Rana Khouri]]'
- '[[org/Telia''z]]'
- '[[task/Create Standardized Psychiatrist Payment Excel Template]]'
- '[[task/Raise Atef Clinical Rate to Match Scale]]'
- '[[task/Remind Noa About 40-Hour Billing Accuracy]]'
- '[[task/Obtain Psychiatrist Fee Schedules From Shira]]'
- '[[task/Establish Billing Protocol for Extended Intake Sessions]]'
- '[[person/Ahmed Masalha]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04

## Context

Rami and Basel sat together to review the monthly psychiatrist payment spreadsheet for Clinic Israel. The session covered data cleaning procedures, formula logic for compensation calculations, and identified systemic issues with reporting formats. This is part of the ongoing effort to professionalize clinic operations under Basel's management.

## Data Cleaning Methodology

Basel walked through the spreadsheet column by column with Rami:

- **Removed unnecessary columns**: Duplicate date fields (kept "taarikh atkhala" / creation date, removed "taarikh siyum" / end date from the system export), unused meeting type differentiators that don't add analytical value
- **Status field standardization**: Multiple status values in the raw data needed consolidation. Basel changed "mishtateif" and similar active statuses to "hofia" (attended), and all non-active statuses to "lo hofia" (did not attend). This is critical because the payment formula depends on a function that checks specifically for "hofia" vs "lo hofia"
- **Adult/child classification**: Added a derived column using the patient name field to identify adults via MCY (Maccabi Youth) identifiers. The classification drives payment differentiation for intake (antek) and follow-up (maakav) sessions, and triggers the children session rate
- **Removed "soug mifgash" (meeting type)**: This field was confusing because it overlapped with other fields and did not contribute meaningful information for payment calculations

## Payment Calculation Logic

The payment formula works as follows for each psychiatrist:

1. **Clinical hour rate**: Each psychiatrist has a per-hour clinical rate (e.g., Atef = 600 NIS/hr)
2. **Session types**: Intake (antek) and follow-up (maakav) sessions are counted separately
3. **Session hours**: The spreadsheet calculates total clinical hours from session counts and average duration
4. **On-call hours (neshiot)**: By law, on-call hours are paid at half the clinical rate. For Atef: 1.3 hours of neshiot at 300 NIS/hr (half of 600) = 390 NIS
5. **Total payment formula**: (intake hours + follow-up hours) * clinical rate + neshiot hours * (clinical rate / 2)

### Two Methods for Neshiot Calculation

Rami explained there are two equivalent calculation approaches:
- **Method A**: Half the clinical rate (300) multiplied by neshiot hours (1.3) = 390
- **Method B**: Full clinical rate (600) multiplied by half the neshiot hours (0.65) = 390

Both yield the same result. The current spreadsheet uses Method A.

## Staff-Specific Issues

### Atef (Psychiatrist)
- Clinical rate: 600 NIS/hour
- Currently below the standard scale (Iskon) — if rate were raised to 225 (per intake), he would be in line with the standard agreement
- Elinor and Noa heard that "experts" (mumhim) get 450 NIS per session and demanded a rate increase. Atef did not make such a demand
- **Action needed**: Consider raising Atef's rate as he is currently paid less than the standard scale while doing more hours

### Noa (Psychiatrist)
- Sometimes requests additional compensation for extended intake sessions, claiming a single intake took the equivalent of two sessions
- No formal protocol exists for handling this — Noa convinces Rami on a case-by-case basis
- Rami flags a 40-hour billing discrepancy worth approximately 500 NIS that needs verification
- **Action needed**: Remind Noa about 40-hour accuracy; establish protocol for extended session claims

### Sachar
- 31 total work hours reviewed
- Rate of 500 NIS confirmed

### Renee (Administrative)
- Handles hour verification from the scheduling system (yoman)
- Basel should verify that Renee's hour tallies match the reporting system data
- Sometimes the scheduling system shows different numbers than the spreadsheet — discrepancies must be reconciled

## Systemic Issues Identified

### Excel Format Inconsistency
Each employee's payment spreadsheet has a **different format**. Basel discovered this while reviewing multiple employees' files. The columns, formulas, and layout vary per person, making verification extremely time-consuming.

**Decision needed**: Create a single unified Excel template that all employees' data flows into, replacing the current ad-hoc per-employee formats.

### Lack of Billing Protocol
There is no formal protocol for handling edge cases like:
- Extended intake sessions (Noa's case)
- What employees self-report vs what the system records
- The fact that payments are partly based on employee-reported hours with minimal verification

Rami noted this is precisely why a formal protocol for the "sal shikum" (rehabilitation basket) is needed — to eliminate ad-hoc billing adjustments.

## Clicks System Integration

Rami mentioned a separate discussion with Ori about Clicks integration:
- Ori called requesting training rights ("tadrikhot") on the Clicks clinical system for onboarding new therapists
- Shira should continue serving as the training coordinator ("madrikha") for new staff onboarding in Clicks
- Key concepts for Clicks onboarding: the system should be open at all times in the background; therapists should enter and check it during sessions, not just before or after
- Rami considers routing this through Shira's existing staff onboarding responsibilities, or alternatively through a "staff stuff" channel from the parent company

## Related
![[related.base#All]]
