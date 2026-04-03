---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2026-03-01'
date: '2025-11-09'
depends_on: []
description: Investigate and resolve the critical workflow gap where Maccabi patients
  lose their files when psychiatrists fail to redirect them to case managers, causing
  loss of continuity of care
due: null
janitor_note: 'FM001 — fixed YAML parse error: unescaped single quote in related field
  (Telia''z). LINK001 — related.base#All embed references missing _bases/ infrastructure
  (vault-wide issue). Telia''z wikilinks are valid.'
kind: task
name: Investigate Maccabi Patient File Closure Issue With Psychiatrist Scheduling
priority: high
project: null
related:
- '[[conversation/Operational Processes and Office Planning Discussion 2025-11-09]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[person/Shira]]'
- '[[org/Maccabi Healthcare Services]]'
relationships: []
run: null
status: todo
tags:
- maccabi
- patient-scheduling
- workflow-gap
- urgent
- clinical-operations
type: task
---

## Task Description

Investigate the critical patient file closure issue affecting Maccabi patients at [[project/Telia'z Clinic Israel]].

## Problem

When a Maccabi patient completes an appointment with a psychiatrist:
1. The psychiatrist is supposed to redirect the patient to a case manager for ongoing scheduling
2. Some psychiatrists fail to make this referral
3. Without the case manager referral, the Maccabi system closes the patient file
4. The patient falls through the cracks and loses continuity of care

## Impact

- Patients lose access to ongoing treatment
- Revenue loss from discontinued treatment relationships
- Clinical risk from interrupted care
- Potential compliance issues with Maccabi service agreements

## Investigation Steps

- [ ] Quantify how many patients have been affected (review closed files)
- [ ] Identify which psychiatrists are not making case manager referrals
- [ ] Determine if this is a training issue, a system issue, or both
- [ ] Review the Maccabi system rules for file closure triggers
- [ ] Propose a fix (automated referral, checklist, system alert)

## Urgency

This was flagged as a **critical issue** in the meeting. Patients are actively losing care continuity.

## Resolution Options

1. **Training**: Remind all psychiatrists of the referral requirement
2. **System Alert**: Build an automated alert when a psychiatrist appointment ends without a case manager referral
3. **Default Referral**: Make case manager referral automatic after every psychiatrist appointment
4. **Secretary Catch**: Have secretarial team flag patients without case manager follow-up

---
## Related
![[related.base#All]]
