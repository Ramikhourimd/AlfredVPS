---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
based_on:
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
confidence: high
created: '2026-02-15'
janitor_note: 'LINK001 — all Telia''z, note, and conversation wikilinks are valid
  (YAML escaping false positive, targets verified). Base view embeds (learn-assumption.base#Depends
  On This, #Related) reference _bases/learn-assumption.base which does not exist —
  systemic issue, no base files in vault. Embeds preserved.'
name: Clinic Israel Serving Only 8 Percent of Monthly Patient Demand
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.9
  context: Coverage tied to conv metric limits
  source: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  target: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  type: related-to
- confidence: 0.98
  context: Low coverage justifies hires
  source: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  target: assumption/Scaling Requires Approximately 176 Individual Quarter-Position
    Hires.md
  type: supports
- confidence: 0.8
  context: Coverage derived from intake
  source: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  target: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  type: depends-on
- confidence: 0.9
  context: Coverage derived from conversion
  source: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  target: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  type: depends-on
- confidence: 0.9
  context: Low coverage needs discharge help
  source: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  target: assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio.md
  type: supports
source: Dashboard data presented by Rami Khouri in Feb 15 2026 team meeting
source_date: '2026-02-15'
status: active
type: assumption
---

# Clinic Israel Serving Only 8 Percent of Monthly Patient Demand

## Claim

As of February 2026, Clinic Israel is converting only approximately 8% of incoming patient demand into intake appointments within the same month. Of 945 new patients who completed questionnaires in February, only 77 received intake appointments that month.

## Basis

Dashboard data presented by Rami Khouri during the Feb 15, 2026 team meeting. The month opened at near-full capacity, leaving almost no slots for new intakes. Approximately 600 patients were scheduled for future months, and ~300+ had no appointment at all.

## Evidence Trail

- Feb 2026: 945 new patients, 77 intakes (8.1%)
- Additional ~80 case manager hours expected to come online
- 2 new psychiatrists and 2 new case managers pending onboarding

## Impact

This extreme capacity gap means demand is growing far faster than service capacity. It drives the urgency for: faster onboarding, the patient discharge protocol, additional hiring, and potentially the call-center/vendor stopgap idea.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]