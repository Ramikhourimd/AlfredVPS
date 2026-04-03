---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: UK regulatory bodies
created: '2026-02-15'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist. Create it to enable
  dynamic views. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  UK Expansion.'
name: UK Controlled Substance Prescriptions Require Specific Format and System
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Stav Zamir]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
relationships:
- confidence: 0.75
  context: Both constrain prescription issuance rules
  source: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  target: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  type: related-to
- confidence: 0.9
  context: Details required system features
  source: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  target: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  type: supports
- confidence: 0.85
  context: Enables actual prescription issuance
  source: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  target: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  type: supports
source: UK pharmaceutical regulation
status: active
type: constraint
---

# UK Controlled Substance Prescriptions Require Specific Format and System

## Constraint

UK clinic must issue actual prescriptions (not just treatment recommendations like in Israel). ADHD medications are controlled substances requiring specific prescription formats and potentially integration with an external prescribing system.

## Source

UK pharmaceutical and controlled substances regulations.

## Implications

- Product team must build prescription issuance feature (not in current system)
- External system integration likely required
- Different from Israel where patients receive treatment recommendations but not prescriptions directly
- Critical path item for UK launch — patients cannot be treated without prescriptions

## Expiry / Review

Permanent regulatory requirement for UK operations.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]