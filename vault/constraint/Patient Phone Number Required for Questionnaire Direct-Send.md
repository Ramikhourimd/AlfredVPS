---
authority: System architecture
created: '2025-10-09'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  The double-apostrophe in YAML source is standard escaping for a literal single quote.
name: Patient Phone Number Required for Questionnaire Direct-Send
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Deploy Questionnaire Direct-Send to Patients]]'
- '[[note/Platform Questionnaire Direct-Send Verification Call 2025-10-09]]'
source: Technical system requirement — verified during Rami-Shachar call
source_date: '2025-10-09'
status: active
type: constraint
---

# Patient Phone Number Required for Questionnaire Direct-Send

## Constraint

The questionnaire direct-send feature requires a patient phone number to be present in the record. Without it, the system cannot deliver the questionnaire to the patient.

## Source

Technical system requirement confirmed during a verification call between Rami and Shachar on 2025-10-09. Shachar explained "the patient's phone number needs to be present for the system to work."

## Implications

- Intake staff must enter patient phone numbers as a mandatory step before the direct-send feature can function
- Incomplete intake records will silently fail to trigger questionnaire delivery — there is no fallback mechanism mentioned
- Data validation or mandatory field enforcement at intake may be needed to prevent silent failures

## Expiry / Review

Active as long as the questionnaire direct-send feature is in use. Should be reviewed if delivery channels beyond SMS/phone are added.
