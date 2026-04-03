---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Maccabi health fund billing process
created: '2026-03-01'
janitor_note: 'LINK001: Telia''z wikilink is YAML single-quote escaping false positive
  (valid). ORPHAN001: No inbound links — consider linking from project/Telia''z AI
  Clinical Platform or related task records.'
name: Commitment Renewal Validation Requires Manual Secretary Check Against Maccabi
  Portal
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build Commitment Renewal Workflow in Retool]]'
- '[[constraint/No Commitment Renewal Workflow Exists in Retool]]'
- '[[constraint/No Renewal Commitment Entry Mechanism Exists in Retool]]'
- '[[task/Add Secretary Tasks for Commitment Renewal Reminders]]'
relationships:
- confidence: 0.9
  context: Parallel manual checks for Maccabi commitments
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
    MADAC.md
  type: related-to
- confidence: 0.7
  context: Maccabi commitment process constraints
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  type: related-to
- confidence: 0.95
  context: No workflow causes need for manual check
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/No Commitment Renewal Workflow Exists in Retool.md
  type: related-to
- confidence: 0.9
  context: No entry mechanism requires manual validation
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/No Renewal Commitment Entry Mechanism Exists in Retool.md
  type: related-to
- confidence: 0.9
  context: Missing entry point for renewal numbers
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/No System Entry Point for Commitment Renewal Numbers.md
  type: related-to
- confidence: 0.95
  context: Lack of system support for renewals
  source: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  target: constraint/No System Support for Maccabi Commitment Renewals in Retool.md
  type: related-to
source: Maccabi billing integration limitations
status: active
type: constraint
---

# Commitment Renewal Validation Requires Manual Secretary Check Against Maccabi Portal

## Constraint

When patients submit renewal commitment numbers, secretaries must manually validate each number against the Maccabi web portal before the commitment can be accepted in the system. There is no API or automated validation pathway between the Retool platform and Maccabi's systems.

## Source

This constraint comes from the Maccabi billing integration architecture. The original commitment numbers auto-populate from the patient questionnaire, but renewal commitments arrive separately through the patient and must be manually cross-checked. At least one patient has already submitted a renewal commitment with no system entry point.

## Implications

- Every renewal commitment creates a manual validation task for secretaries
- Validation throughput is limited by secretary availability
- No automated check means human error risk in commitment number entry
- As patient volumes grow, manual validation becomes a scaling bottleneck
- Combined with the assumption that secretary pre-session calls can absorb renewal reminders, this adds both reminder AND validation responsibilities to the same role

## Expiry / Review

This constraint persists until either: (a) an API integration with Maccabi's portal is built for automated validation, or (b) the new system rebuild includes automated commitment validation. Review when Shachar's platform rebuild reaches billing module design.