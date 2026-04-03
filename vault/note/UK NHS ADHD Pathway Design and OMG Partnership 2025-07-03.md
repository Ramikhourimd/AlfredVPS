---
alfred_tags:
- healthcare/adhd
- partnerships/uk
- systems/case-management
created: '2025-07-03'
description: Working session between Rami and Adiel mapping the UK NHS ADHD patient
  pathway from GP referral through triage, case manager intake, and psychiatrist assessment.
  Covers OMG partnership structure, governance model, data transfer requirements,
  and service economics for the Leeds tender.
janitor_note: LINK001 for [[project/Telia'z UK Expansion]] and [[org/Telia'z]] are
  false positives caused by YAML apostrophe escaping — target files exist. LINK001
  for related.base#All embed references _bases/ file that does not exist yet (vault-wide
  infrastructure gap, not a per-record issue).
name: UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[org/OMG Healthcare]]'
- '[[org/GP Confederation Leeds]]'
- '[[org/Telia''z]]'
- '[[location/Leeds]]'
- '[[conversation/UK NHS ADHD Pathway Design Meeting 2025-07-03]]'
- '[[conversation/GP Confederation ADHD Service Partnership Meeting 2025-01-22]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03

## Context

Rami and Adiel met to work through the detailed clinical pathway for the UK NHS ADHD service that Telia'z will deliver in partnership with OMG Healthcare. Adiel built an Excel spreadsheet mapping each stage of the patient flow, and this session focused on filling in the clinical requirements that Rami needs to define.

Rami flagged upfront that he is at full capacity and needs focused, specific deliverables rather than open-ended process management. They agreed to establish a recurring weekly sync, likely on Thursdays around 10:15.

## OMG Partnership Structure

OMG Healthcare is a UK health services company with two business lines:
1. **Real estate/facilities** — They build and operate NHS clinic premises across England
2. **Clinical services** — They are also a registered healthcare provider with their own CQC license

Key facts about OMG:
- ~100,000 GP patients across their clinic network
- ~400,000 acute care patients annually
- Physical clinic infrastructure in Leeds and elsewhere in England
- They hold the CQC registration and handle clinical governance/safeguarding
- They bid on NHS tenders; Telia'z is their psychiatric service provider

The relationship: OMG handles the regulatory/governance layer and physical infrastructure; Telia'z provides the psychiatric clinical expertise. Both organizations jointly deliver the service.

## NHS ADHD Patient Pathway (as mapped in meeting)

### Stage 1: GP Referral
- Patient is referred by their GP to the combined Telia'z/OMG service
- GP referral enters the service pipeline

### Stage 2: Initial Triage (OMG handles)
- OMG staff perform inclusion/exclusion screening using health inequity and high risk factors
- Conducted by phone or virtual (not in-person at clinic)
- **Outcomes:**
  - Not suitable → returned to GP with explanation
  - Need more info → returned to GP with specific data request
  - Suitable → referred onward to psychiatric assessment pathway

### Stage 3: Data Handoff to Telia'z
- Once patient passes triage, OMG transfers patient to Telia'z
- **Critical gap identified:** Need to define exactly what data OMG must provide at handoff
- Shachar (CTO) asked the right question: how does this data physically arrive? (PDF, API, etc.)

### Stage 4: Self-Administered Clinical Questionnaire
- **Key clinical decision:** Before the case manager intake, patient completes a self-administered questionnaire
- Rami clarified this is NOT a case manager intake — it is a self-report instrument
- Purpose: Sharpen and focus the subsequent case manager assessment
- Any deviation from the standard Telia'z flow needs clinical justification

### Stage 5: Case Manager Intake
- Standard Telia'z case manager interview
- Informed by questionnaire results from Stage 4

### Stage 6: Psychiatrist Intake Assessment
- Full psychiatric evaluation

### NHS vs Private Flow Distinction
- The NHS pathway includes the OMG triage layer (Stage 2) for regulatory compliance
- For private patients, Telia'z would skip the triage and use their standard Israeli flow (more efficient, lower cost)

## Adiel's Excel Framework

Adiel structured the analysis across these dimensions per stage:
- **Stage name and requirements**
- **Who does it** (OMG or Telia'z)
- **How** (virtual, face-to-face, phone)
- **Staff type needed**
- **Data requirements**
- **Time estimate**
- **Cost per hour of staff**
- **Output/outcome of each stage**

## Governance and Compliance

- OMG operates under CQC licensing — clinical governance and safeguarding are their top priorities
- Telia'z operates as a service provider under OMG's governance framework
- This is specifically for the Leeds tender, though the model is designed to be replicable

## Working Arrangement

- Rami acknowledged he cannot manage open-ended processes due to his ADHD and current overload
- Requests focused, specific tasks with advance notice (ideally a week ahead)
- Proposed recurring Thursday sync (~10:15) aligned with OMG Tuesday meetings
- Pattern: OMG meeting Tuesday → Adiel prepares homework → Rami/Adiel sync Thursday

## Related
![[related.base#All]]