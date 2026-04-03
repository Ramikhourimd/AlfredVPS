---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: UK healthcare regulatory framework
created: '2026-02-28'
janitor_note: 'LINK001: Telia''z AI Clinical Platform wikilink is a YAML escaping
  false positive — link resolves correctly. No action needed.'
name: UK Clinic Requires Actual Prescription Issuance Unlike Israel
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build UK Scheduling and Prescription System]]'
relationships:
- confidence: 0.8
  context: Issuance requires controlled format/system
  source: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  target: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  type: depends-on
- confidence: 0.85
  context: Issuance requires reg compliance
  source: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  target: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  type: depends-on
- confidence: 0.85
  context: Issuance needs specialized compliance
  source: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  target: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  type: depends-on
- confidence: 0.9
  context: Issuance req drives system need
  source: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  target: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  type: supports
source: UK healthcare regulations for controlled substances
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Clinic Requires Actual Prescription Issuance Unlike Israel

## Constraint

The UK clinic must issue actual prescriptions to patients, not just treatment recommendations as in the Israeli operation. This involves integration with external prescription systems and compliance with UK-specific controlled substance formats, particularly for ADHD medications.

## Source

UK healthcare regulations require that clinics issue formal prescriptions. The Israeli model where psychiatrists provide treatment recommendations that patients take to their HMO does not apply in the UK context. Stav flagged this as a critical feature requirement during the 2026-02-15 team meeting.

## Implications

- The clinical platform must include a prescription issuance module for UK operations
- External system integration is needed for UK prescription standards
- ADHD medication prescriptions involve controlled substance regulations with additional compliance requirements
- This is a blocking dependency for UK clinic launch — patients cannot be treated without prescription capability
- The platform must support divergent clinical workflows between Israel and UK

## Expiry / Review

Active as long as UK operations are planned. Review when UK regulatory landscape changes.