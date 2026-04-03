---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: UK MHRA and Home Office controlled substance regulations
created: '2026-03-09'
janitor_note: 'LINK001: Telia''z project wikilink uses YAML quote escaping (false
  positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/ which does not exist (vault-wide infrastructure gap). Embeds preserved.
  ORPHAN001: no inbound links — consider linking from relevant project records.'
name: UK Controlled Substance Prescriptions Require Specialized Regulatory Compliance
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel]]'
- '[[task/Build UK Scheduling and Prescription System]]'
relationships:
- confidence: 0.95
  context: Both controlled substance Rx reqs
  source: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  target: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  type: related-to
- confidence: 0.8
  context: Compliance for prescription issuance
  source: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  target: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  type: related-to
- confidence: 0.85
  context: Compliance req drives system need
  source: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  target: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  type: supports
- confidence: 0.75
  context: Controlled sub part of issuance
  source: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  target: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  type: part-of
source: UK clinical operations planning — controlled substance prescription requirements
status: active
type: constraint
---

# UK Controlled Substance Prescriptions Require Specialized Regulatory Compliance

## Constraint

The UK clinic prescription system must handle controlled substance formats specifically for ADHD medications. This goes beyond general prescription issuance — controlled substances have stricter regulatory requirements including specific prescription formats, authorized prescriber verification, and compliance tracking that differ from standard medication prescriptions.

## Source

Identified during UK clinic launch planning. The task to build the UK scheduling and prescription system explicitly noted "external system integration and UK-specific controlled substance formats (ADHD medications)" as a critical requirement.

## Implications

- The prescription feature cannot be a simple document generator — it must integrate with UK controlled substance regulatory frameworks
- ADHD medications (commonly prescribed in psychiatric practice) fall under controlled substance regulations requiring specific prescription formats
- External system integration is required, adding complexity beyond internal platform development
- This may require specialized regulatory knowledge during implementation

## Expiry / Review

Active as long as the UK clinic operates. Controlled substance regulations are subject to change and should be reviewed annually against current UK MHRA/Home Office guidance.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]