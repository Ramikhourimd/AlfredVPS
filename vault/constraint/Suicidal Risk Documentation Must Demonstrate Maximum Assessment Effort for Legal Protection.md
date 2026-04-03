---
alfred_tags:
- psychiatry/suicide-risk
- clinical-supervision/acute
- risk-protocols
authority: Ministry of Health regulations, legal precedent
created: '2026-03-06'
janitor_note: LINK001 — [[project/Telia'z Clinic Israel]] is valid (YAML single-quote
  escaping false positive). ORPHAN001 — legitimate constraint record, needs inbound
  links from related project or decision records.
name: Suicidal Risk Documentation Must Demonstrate Maximum Assessment Effort for Legal
  Protection
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Adopt Structured Five-Level Suicidal Risk Assessment Protocol]]'
- '[[decision/Case Manager Role Does Not Include Suicidality Screening]]'
- '[[note/Clinical Supervision Suicidal Risk Assessment Protocols]]'
relationships:
- confidence: 0.85
  context: doc reqs need structured assessment
  source: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  target: assumption/Case Managers Need Structured Supervision Framework for Acute
    Risk Assessment.md
  type: supports
- confidence: 0.8
  context: doc depends on supervision
  source: constraint/Suicidal Risk Documentation Must Demonstrate Maximum Assessment
    Effort for Legal Protection.md
  target: constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc
    Availability.md
  type: depends-on
source: Clinical supervision guidance from Rami Khouri, McKree case precedent (USA)
source_date: '2025-12-01'
status: active
type: constraint
---

# Suicidal Risk Documentation Must Demonstrate Maximum Assessment Effort for Legal Protection

## Constraint

Every assessed risk factor in a suicidal risk evaluation must be documented. If a symptom was not assessed, the clinician must either return to assess it in a follow-up or document why it was not assessed with clinical reasoning. The critical liability scenario is when a symptom is neither assessed nor mentioned — this creates legal exposure.

## Source

Clinical supervision guidance from Rami Khouri (2025-12-01), referencing the McKree case (USA) where clinicians were found liable for inadequate immediate danger assessment. This represents both regulatory requirements (Ministry of Health physician oversight) and legal precedent establishing the standard of care.

## Implications

Clinicians must document their assessment of the full five-level suicidality escalation ladder (ideation → thoughts → intention → plan → act). Immediate danger assessment is only valid as a point-in-time snapshot — no clinical tool reliably predicts future danger. This means documentation must be thorough at each contact, not assumed from prior assessments. Training and protocol enforcement must ensure clinicians understand that omission of assessment is worse than an incorrect assessment.

## Expiry / Review

Ongoing — this is a permanent medico-legal standard. Should be reviewed whenever Ministry of Health updates clinical documentation requirements or when new legal precedents emerge.