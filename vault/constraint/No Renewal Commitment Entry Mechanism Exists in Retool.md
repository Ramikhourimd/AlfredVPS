---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: System limitation — Retool platform
created: '2026-02-27'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). No base view embeds in this file.
name: No Renewal Commitment Entry Mechanism Exists in Retool
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build Commitment Renewal Workflow in Retool]]'
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
relationships:
- confidence: 0.9
  context: No entry mechanism requires manual
  source: constraint/No Renewal Commitment Entry Mechanism Exists in Retool.md
  target: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  type: supports
source: Operational gap identified during commitment renewal workflow discussion
source_date: '2025-01-12'
status: active
type: constraint
---

# No Renewal Commitment Entry Mechanism Exists in Retool

## Constraint

When a patient exhausts their initial Maccabi commitment (intake + 16 case manager follow-ups + 4 psychiatric follow-ups), there is no field or workflow in Retool to enter a renewal commitment number. Original commitment numbers auto-populate from the patient questionnaire, but renewal commitments arrive through a separate process with no system entry point.

## Source

System design gap — the original Retool implementation only accounted for initial commitment intake, not the renewal lifecycle. At least one patient has already sent a renewal commitment number with nowhere to enter it.

## Implications

- Secretaries cannot validate renewal commitments against the Maccabi portal through the system
- Session balance counters cannot be updated when new commitments are approved
- Billing and payment request workflows break when commitment data is missing
- Manual workarounds are required, increasing error risk and administrative burden

## Expiry / Review

Expires when the renewal commitment workflow is built in Retool (or the new system). Currently blocked on Alice clarifying the exact renewal commitment structure with Maccabi.