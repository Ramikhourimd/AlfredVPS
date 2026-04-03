---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: UK healthcare regulatory framework
created: '2026-02-15'
janitor_note: 'LINK001 on Telia''z wikilinks: false positives — YAML single-quote
  escaping renders correctly. LINK001 on learn-constraint.base embeds: vault-wide
  infrastructure gap (_bases/ files not yet created). ORPHAN001: legitimate constraint
  with valid outbound links. No per-file fix needed.'
name: UK Prescription Issuance Requires Separate Regulatory Compliance
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
- '[[task/Build UK Scheduling and Prescription Modules]]'
- '[[person/Stav Zamir]]'
relationships:
- confidence: 0.9
  context: Adds issuance compliance needs
  source: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  target: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  type: supports
- confidence: 0.85
  context: Regulatory needs for issuance
  source: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  target: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  type: supports
source: UK healthcare regulation
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Prescription Issuance Requires Separate Regulatory Compliance

## Constraint

UK ADHD prescriptions cannot be issued through the existing Telia'z system. UK prescription regulations differ from Israel, and patients completing ADHD assessments must receive prescriptions through a compliant UK prescribing mechanism. This may require integration with an external UK prescribing platform or a dedicated module.

## Source

Stav Zamir raised this in the team meeting — "the patient in our assessment gets diagnosed and prescribed medication, but we don't issue a prescription, that's very critical." UK prescribing requirements involve specific systems and compliance that Telia'z hasn't yet addressed.

## Implications

- Cannot launch full UK ADHD service without prescribing capability
- Need to research UK electronic prescribing options
- May need partnership with a UK pharmacy or prescribing service
- Adds development scope and timeline risk to March 31 launch target

## Expiry / Review

Active constraint until UK prescription workflow is designed and implemented.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]