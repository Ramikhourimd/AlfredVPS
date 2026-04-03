---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
based_on:
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
confidence: high
created: '2026-02-15'
description: Dashboard data from February 2026 shows approximately 945 new patient
  registrations per month at the Israel clinic, establishing the baseline demand volume.
janitor_note: LINK001 — learn-assumption.base embeds reference missing _bases/learn-assumption.base.
  Create base file to enable dynamic views. Telia'z wikilinks are valid (YAML escaping
  false positive).
name: Clinic Israel Receiving Approximately 1000 New Patients Per Month
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[task/Design Patient Discharge Protocol for Clinic Israel]]'
relationships:
- confidence: 0.95
  context: Intake volume basis for conversion
  source: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  target: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  type: related-to
- confidence: 0.85
  context: Intake informs service coverage
  source: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  target: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  type: related-to
- confidence: 0.65
  context: Intake relevant to coverage metric
  source: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  target: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  type: related-to
- confidence: 0.75
  context: Intake scale drives hiring needs
  source: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  target: assumption/Scaling Requires Approximately 176 Individual Quarter-Position
    Hires.md
  type: related-to
- confidence: 0.85
  context: High intake needs rebalancing
  source: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  target: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  type: supports
source: Dashboard data presented by Rami at team meeting 2026-02-15
source_date: '2026-02-15'
status: active
type: assumption
---

# Clinic Israel Receiving Approximately 1000 New Patients Per Month

## Claim
Clinic Israel is receiving approximately 945-1000 new patient registrations (questionnaire completions) per month as of February 2026, with only 8% conversion to intake appointments in the same month.

## Basis
Dashboard data presented by Rami at the 2026-02-15 team meeting showed 945 new patients in February (mid-month), with only 77 receiving intake appointments. Approximately 600 scheduled for future months, ~300+ unscheduled entirely.

## Evidence Trail
- 2026-02-15: 945 new patients, 77 intakes (8% same-month conversion)
- Prior months showed lower but growing numbers

## Impact
This volume vastly exceeds current capacity. Drives all decisions around discharge protocols, hiring, onboarding acceleration, and service quality. The 30-40 new psychiatrist hiring target for 2026 is derived from these numbers.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]