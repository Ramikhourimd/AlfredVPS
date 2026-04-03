---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Current Retool platform architecture
created: '2026-02-27'
janitor_note: 'LINK001 false positives: Telia''z wikilinks resolve correctly (YAML
  single-quote escaping). Base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist — vault-wide
  infrastructure gap.'
location:
- '[[project/Telia''z Clinic Israel]]'
name: No Commitment Renewal Workflow Exists in Retool
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build Commitment Renewal Workflow in Retool]]'
- '[[task/Add Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
relationships:
- confidence: 0.85
  context: Entry mechanism part of workflow
  source: constraint/No Commitment Renewal Workflow Exists in Retool.md
  target: constraint/No Renewal Commitment Entry Mechanism Exists in Retool.md
  type: part-of
- confidence: 0.95
  context: No workflow necessitates manual check
  source: constraint/No Commitment Renewal Workflow Exists in Retool.md
  target: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  type: supports
source: System design gap — original build only handled initial commitments
source_date: '2025-01-12'
status: active
type: constraint
---

# No Commitment Renewal Workflow Exists in Retool

## Constraint

The Retool platform has no field or workflow for entering renewal commitment numbers from Maccabi. The original system was built to handle only initial patient commitments (auto-populated from the intake questionnaire). When a patient exhausts their initial sessions and obtains a renewal commitment, there is no entry point in the system to record it.

## Source

System design limitation discovered operationally — at least one patient has already submitted a renewal commitment with no place to enter it. Raised during the 2025-01-12 clinic commitment renewals meeting.

## Implications

- Secretaries cannot enter renewal commitment numbers, blocking continued patient treatment tracking
- Session balance counters become inaccurate after initial commitment is exhausted
- Billing and payment request workflows break for renewal patients
- Each renewal commitment must be validated against the Maccabi web portal before approval — no automated validation exists
- Manual workarounds risk data inconsistency between Retool and Maccabi records

## Expiry / Review

Expected to be resolved when the commitment renewal workflow is built in Retool (or superseded by the new platform rebuild). Alice must first clarify exact renewal commitment structure with Maccabi (session count, terms) before implementation can begin.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]