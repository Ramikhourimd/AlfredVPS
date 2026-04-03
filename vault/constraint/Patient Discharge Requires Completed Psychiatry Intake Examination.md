---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Clinical governance protocol
created: '2026-02-26'
janitor_note: 'LINK001: Telia''z project wikilinks are valid (scanner false positive
  from YAML quote escaping). ORPHAN001: Record has valid related links to tasks/decisions
  — not truly orphaned. No action needed.'
location: []
name: Patient Discharge Requires Completed Psychiatry Intake Examination
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Define Complex Patient Protocol Criteria]]'
- '[[decision/Require Protocol Definition Before Feature Development]]'
- '[[decision/Implement Active Patient Discharge Protocol]]'
- '[[assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio]]'
source: Clinical/regulatory requirement
source_date: '2026-02-12'
status: active
type: constraint
---

# Patient Discharge Requires Completed Psychiatry Intake Examination

## Constraint

A patient cannot be formally discharged from the clinic until they have completed a psychiatry intake appointment (medical examination). Earlier stages in the patient journey — questionnaire completion, case manager assessment — can flag a patient as complex or potentially unsuitable, and can recommend against continuing, but they cannot initiate a formal discharge.

## Source

Rami Khouri articulated this during the 2026-02-12 product development meeting when discussing the complex patient protocol design. The constraint reflects clinical governance: only a licensed physician who has conducted a medical examination can make a discharge determination. Pre-intake stages lack the clinical authority to discharge.

## Implications

- The multi-stage patient flow (questionnaire -> case manager -> psychiatrist) must be designed so that flagging and discharge are distinct actions
- Product features for "complex patient alerts" must not include automated discharge at pre-intake stages
- Patients flagged as unsuitable before intake still consume intake appointment capacity (they must be seen before they can be discharged)
- The active discharge protocol (10-30-30-30 targets) only applies to patients who have completed their intake
- This creates a floor on how much the intake appointment bottleneck can be relieved — even patients who will be discharged must first get an intake slot

## Expiry / Review

Permanent clinical constraint. Would only change with regulatory changes to the scope of non-physician clinical staff authority.