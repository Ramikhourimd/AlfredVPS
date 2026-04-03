---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: UK healthcare regulations
created: '2026-02-26'
janitor_note: LINK001 for Telia'z wikilinks are YAML escaping false positives — all
  targets verified to exist. LINK001 for note/Telia'z Team Meeting UK Launch verified
  valid — file exists. LINK001 for base view embeds is systemic — _bases/ files do
  not exist but embeds must be preserved.
name: UK Clinic Launch Requires Prescription System Not Yet Built
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[note/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Stav Zamir]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
- '[[assumption/UK Launch Can Operate Under Partner CQC Without Own Registration]]'
relationships:
- confidence: 0.9
  context: System must handle controlled substance formats
  source: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  target: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  type: depends-on
- confidence: 0.85
  context: System needs regulatory compliance for issuance
  source: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  target: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  type: depends-on
- confidence: 0.9
  context: Launch requires issuance unlike Israel
  source: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  target: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  type: depends-on
- confidence: 0.9
  context: Requires controlled substance compliance
  source: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  target: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  type: depends-on
source: Product/regulatory requirement
source_date: '2026-02-15'
status: active
type: constraint
---

# UK Clinic Launch Requires Prescription System Not Yet Built

## Constraint

UK patients who complete psychiatric assessment and receive a diagnosis with treatment plan cannot receive medication without a prescription being issued. The Telia'z platform currently does not have e-prescribing capability for the UK market. This system must integrate with UK-specific prescription formats and potentially external prescription networks.

## Source

UK healthcare regulations require prescriptions to be properly issued for controlled and scheduled medications. Stav Zamir flagged this in the 2026-02-15 team meeting as a critical gap not included in the original UK assessment scope.

## Implications

- Patients can be assessed but cannot begin treatment until prescriptions are available
- This creates a gap between diagnosis and medication delivery
- The scheduling feature (appointment booking for patients) is also missing and related
- Both features need to be scoped, designed, and built — Shachar (CTO) will not start without formal specifications
- This may delay the March 31 system launch target or create a degraded-capability launch

## Expiry / Review

Active until the prescription and scheduling modules are built and deployed. Review weekly during UK launch sprint.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]