---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
based_on:
- '[[assumption/Monthly Patient Churn Rate Is Approximately 15 Percent]]'
confidence: medium
created: '2026-02-15'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide infrastructure issue.'
name: Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Rami Khouri]]'
- '[[task/Design Patient Lifecycle Discharge Protocol]]'
- '[[note/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[task/Design Patient Discharge Protocol and Literature Review]]'
relationships:
- confidence: 0.75
  context: Enables capacity for growth target
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Growth Trajectory Targets 7000 Plus Patients.md
  type: supports
- confidence: 0.65
  context: Manages scale-induced complexity
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Operational Complexity Has Reached Hospital-Level Scale.md
  type: related-to
- confidence: 0.85
  context: Aids operational stabilization
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Stabilization Must Precede Growth Expansion.md
  type: supports
- confidence: 0.6
  context: Impacts readiness metrics
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Organizational Health Score Can Quantify Growth Readiness.md
  type: related-to
- confidence: 0.7
  context: Boosts health score threshold
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Organizational Health Score Must Clear Threshold Before Growth.md
  type: supports
- confidence: 0.6
  context: Reduces hiring pressure needs
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Rapid Clinician Hiring Degrades Service Quality and Staff Commitment.md
  type: related-to
- confidence: 0.8
  context: Stabilizes workforce capacity
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Workforce Stabilization Must Precede Aggressive Recruitment.md
  type: supports
- confidence: 0.8
  context: Discharge handles projected intake growth
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  type: related-to
- confidence: 0.75
  context: Current intake informs rebalance need
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  type: related-to
- confidence: 0.85
  context: Rebalance improves low conversion
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  type: supports
- confidence: 0.9
  context: Frees capacity to serve more demand
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  type: supports
- confidence: 0.95
  context: Protocol enables framework capacity free
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Israel Discharge Framework Can Free Case Manager Capacity for
    UK Launch.md
  type: supports
- confidence: 0.7
  context: Rebalance affects intake metrics
  source: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  target: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  type: related-to
source: Rami Khouri proposal in Feb 15 2026 team meeting
source_date: '2026-02-15'
status: active
type: assumption
---

# Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio

## Claim

By implementing structured discharge targets (10% after intake, 30% after each of the first three follow-ups), the clinic can shift from a follow-up-heavy model to an intake-heavy model, freeing capacity for new patients while maintaining quality of care.

## Basis

Rami's proposal is based on the observation that the clinic currently has no patient selection at intake and no structured discharge protocol. Natural churn is ~15%, but the clinic needs to actively manage patient flow to match demand. The targets need to be validated against: psychiatric literature on treatment duration, Telia'z patient data patterns, and the financial model.

## Evidence Trail

- Feb 2026: Current follow-up ratio is much lower than the 4:1 ratio needed
- Natural churn: ~15% (per existing assumption)
- Proposed targets: 10/30/30/30% discharge across stages
- Validation needed: literature review + data analysis + financial modeling

## Impact

If validated, this protocol would fundamentally change the clinic's operational character and significantly increase intake capacity without proportional hiring. If incorrect, could lead to premature patient discharge and quality concerns.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]