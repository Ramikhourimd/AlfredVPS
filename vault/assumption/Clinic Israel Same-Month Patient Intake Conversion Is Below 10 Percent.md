---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
confidence: high
confirmed_by:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
created: '2026-02-15'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide issue, embeds preserved.'
name: Clinic Israel Same-Month Patient Intake Conversion Is Below 10 Percent
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.95
  context: Low conversion implies low coverage
  source: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  target: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  type: supports
- confidence: 0.95
  context: Qualifies same-month conversion rate
  source: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  target: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  type: related-to
- confidence: 0.8
  context: Low conv necessitates scaling
  source: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  target: assumption/Scaling Requires Approximately 176 Individual Quarter-Position
    Hires.md
  type: supports
- confidence: 0.85
  context: Conversion depends on intake volume
  source: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  target: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  type: depends-on
- confidence: 0.85
  context: Low conversion justifies protocol
  source: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  target: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  type: supports
source: Rami Khouri dashboard presentation, 2026-02-15
source_date: '2026-02-15'
status: confirmed
type: assumption
---

# Clinic Israel Same-Month Patient Intake Conversion Is Below 10 Percent

## Claim

Only ~8% of new patients who complete the questionnaire in a given month receive an intake appointment in that same month. The remaining 92% are placed on a waiting list for future months.

## Basis

Rami's operations dashboard for February 2026: 945 new patients completed questionnaires, only 77 received intake appointments (8.1%). The month started with near-full capacity, leaving almost no slots for new intakes.

## Evidence Trail

- 2026-02-15: Dashboard data presented at team meeting. ~300 patients have no appointment at all; ~600 scheduled for March+.

## Impact

This confirms a severe capacity bottleneck. The clinic is effectively turning away 92% of monthly demand. Drives urgency for: new clinician recruitment, onboarding acceleration, patient discharge framework, and capacity planning.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]