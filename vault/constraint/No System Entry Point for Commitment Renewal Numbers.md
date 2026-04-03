---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Maccabi HMO commitment structure
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML single-quote
  escaping false positive). Base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist — vault-wide
  infrastructure gap, embeds preserved per policy. ORPHAN001 — no inbound wikilinks;
  consider linking from project/Telia''z AI Clinical Platform or billing-related conversation
  records.'
name: No System Entry Point for Commitment Renewal Numbers
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[task/Build Commitment Renewal Workflow in Retool]]'
- '[[task/Add Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
relationships:
- confidence: 0.9
  context: No entry point forces manual validation
  source: constraint/No System Entry Point for Commitment Renewal Numbers.md
  target: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  type: supports
source: Maccabi commitment workflow, Retool system gap
source_date: '2025-01-12'
status: active
type: constraint
---

# No System Entry Point for Commitment Renewal Numbers

## Constraint

When a patient's initial Maccabi commitment is exhausted (intake + 16 CM follow-ups + 4 psychiatric follow-ups), there is no field or workflow in Retool to enter renewal commitment numbers. Original commitments auto-populate from the patient questionnaire, but renewals arrive separately with no system entry point.

## Source

Identified during the 2025-01-12 clinic feature updates meeting. At least one patient has already submitted a renewal commitment number with no place to record it. The gap is in the Retool system design — renewals were not accounted for in the original workflow.

## Implications

- Secretaries cannot validate renewal commitments against the Maccabi web portal through the system
- Session balance counters do not update when new commitments arrive
- Billing/payment request workflows break without renewal tracking
- Manual workarounds create risk of missed renewals and billing errors
- Alice must first clarify exact renewal commitment structure with Maccabi before implementation

## Expiry / Review

Active until commitment renewal workflow is built in Retool or the rebuilt platform. Review when the new system design includes billing workflows.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]