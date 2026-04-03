---
created: '2025-12-04'
description: DUPLICATE — canonical version is note/Psychiatrist Payment Data Review
  and Cleanup Notes 2025-12-04. This record retained for reference but the richer
  version should be preferred.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist yet — create it to enable dynamic views.
name: Clinic Payroll Data Cleaning and Payment Methodology 2025-12-04
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Shira]]'
- '[[person/Rana Khouri]]'
- '[[org/Telia''z]]'
- '[[conversation/Clinic Payroll Data Review and Payment Calculations 2025-12-04]]'
- '[[task/Standardize Payroll Excel Template for All Employees]]'
- '[[task/Raise Atef Hourly Rate to Match Standard]]'
relationships: []
session: null
status: review
subtype: meeting-notes
tags: []
type: note
---

# Clinic Payroll Data Cleaning and Payment Methodology 2025-12-04

## Context

Rami and Basel sat together to review clinic payroll data and payment calculations. The session covered three main areas: data column cleanup in the reporting spreadsheet, payment calculation methodology for psychiatrists, and discrepancies in how different employee reports are formatted.

## Data Cleaning Decisions

### Column Cleanup
- **Removed columns:** "Koteret" (header field) — deemed unnecessary; "Taarikh Siyum" (end date from the system) — redundant since "Taarikh Itkhala" (start date) is sufficient; "Maz'hit Shanim" (age display) — duplicates information available via "Shem Mali" (full name); several duplicate status-related fields
- **Kept columns:** "Taarikh Itkhala" (creation date), "Shaat Itkhala" and "Shaat Siyum" (start/end times), "Shem Mali" (full name for psychiatrist name), Status field

### Status Field Standardization
- Changed "Lo Hofia" / "Mishtateif" / "Lo Hofia" variants to a single standardized "Lo Hofia" value
- Changed "Toam Hofia" / "Ishtateif" / "Shiyur" variants to standardized "Hofia" value
- This standardization enables a formula that filters based on two specific status values: Hofia (attended) vs Lo Hofia (did not attend)

### Adult vs Child Classification
- Identifying adults vs children using the MCY (date of birth) field
- Formula logic: extract name separately, then apply age filter
- "Sug Mifgash" (encounter type) field used to determine: (1) whether adult or child, (2) whether intake or follow-up

## Payment Calculation Methodology

### Standard Psychiatrist Payment
- **Clinical hour rate:** 600 NIS (for standard sessions)
- **Nishui (extra hours) rate:** Half the clinical rate = 300 NIS per hour
- **Legal basis:** Israeli labor law requires payment of half the clinical rate for nishui hours

### Atef's Payment Calculation (Example)
- Available hours in November: 21 hours
- Hours actually worked: 19.3 hours
- Nishui hours: 1.3 hours
- Nishui calculation: 300 NIS x 1.3 = 390 NIS
- Two equivalent calculation methods:
  1. Half of 600 NIS = 300 NIS, multiplied by nishui hours
  2. 150 NIS per nishui session (intake or follow-up), multiplied by number of nishui sessions
- Total payment structure: Clinical sessions (intake + follow-up at standard rate) + Nishui supplement = Total compensation before deductions

### Noa's Billing Pattern
- Noa sometimes claims extended intake sessions, requesting payment as if two intakes were conducted instead of one
- No formal protocol exists for this — she convinced Rami on a case-by-case basis
- This highlights the need for a standardized billing protocol for "Sal Shikum" (rehabilitation basket) sessions

## Expert Fee Discrepancy Issue

- Elinor and Noa heard that expert psychiatrists (Mumkhim) at the clinic earn 450 NIS per session
- They demanded their intake rates be raised accordingly
- **Atef's situation:** Currently earns below the standard rate — needs a raise to 225 NIS to align with the standard fee schedule (Iskaham)
- If Atef's rate is raised to 225, it aligns with the standard; he currently does more hours at a lower rate
- Resolution: Issue new fee schedules (Tarifim) and have all clinicians sign updated agreements

## Excel Standardization Problem

- Basel observed that each employee's Excel payroll report has a different format
- Reports are "Meshunot" (varied) depending on who prepared them
- **Decision needed:** Create a single standardized Excel template for all employees
- This will be sent to Shira for implementation
- Currently Basel will verify reports independently and create a "Master" comparison

## Clickx System Integration Discussion

- Ori called about Clickx system integration for clinical sessions
- Concept: Clickx should be open at all times in the background during clinical encounters
- Key workflow points:
  - Open Clickx at session start, not mid-session
  - Leave a few minutes at end of session for data entry
  - Avoid "over" (overload) during sessions
- Shira could guide new clinicians on Clickx usage as part of onboarding
- Alternative: Have staff training handled through "Avir Le-Staff" (staffing support)

## Rana's Role in Payment Verification

- Rana handles hour verification from the calendar/diary system ("Yoman")
- Cross-checking between reported hours and calendar-logged hours is essential
- Discrepancies found: sometimes calendar shows different hours than the report
- Risk: If someone logs 3 hours mid-month but actually worked more, the number is unreliable until month-end reconciliation

## Related
![[related.base#All]]
