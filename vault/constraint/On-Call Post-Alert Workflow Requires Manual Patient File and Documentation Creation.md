---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Clinical platform architecture limitation
created: '2026-03-15'
janitor_note: 'LINK001: project/Teliaz Clinic Israel wikilink is valid (YAML apostrophe
  escaping false positive). ORPHAN001: No inbound wikilinks from any other record
  — consider linking from project/Teliaz Clinic Israel or related on-call records.'
location: []
name: On-Call Post-Alert Workflow Requires Manual Patient File and Documentation Creation
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
source: On-call incident review revealing multiple manual steps after alert activation
source_date: '2025-09-22'
status: active
tags:
- on-call
- clinical-platform
- manual-process
type: constraint
---

# On-Call Post-Alert Workflow Requires Manual Patient File and Documentation Creation

## Constraint

After an on-call alert is activated and the psychiatrist completes a patient interaction, the subsequent documentation workflow is entirely manual:
1. The consent form was misdirected to the doctor (Atef) instead of the patient
2. No patient file was automatically created in the system
3. The psychiatrist conducted a phone assessment instead of the standard video workflow
4. Rami had to manually send a summary email to Roy Shur
5. Shachar had to manually open a patient file after the fact
6. Dekkel sent a separate email confirming the file was created

## Source

Discovered during the first real on-call alert activation (September 2025). The incident exposed that the clinical platform was not designed to support the on-call use case — it assumes the standard intake flow (questionnaire → scheduling → video session → documentation).

## Implications

Every on-call case requires manual intervention at multiple points to create a proper clinical record. This creates risk of incomplete documentation, especially if the on-call incident occurs at unusual hours when administrative support is unavailable. If on-call volume increases, this manual workflow will not scale.

## Expiry / Review

Should be reviewed when the clinical platform (Retool/Clickx) is updated to support on-call patient registration flows. Until then, a manual checklist or protocol document is needed for post-alert documentation.