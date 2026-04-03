---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
based_on:
- '[[task/Add Total Appointments Metric to Operations Dashboard]]'
- '[[constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February 2026]]'
challenged_by: []
confidence: low
confirmed_by: []
created: '2026-02-26'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z project wikilink is valid (YAML single-quote escaping
  false positive). Base view embeds (learn-assumption.base#Depends On This, #Related)
  reference _bases/learn-assumption.base which does not exist — vault-wide infrastructure
  gap, embeds preserved per policy. ORPHAN001 — no inbound wikilinks; consider linking
  from project/Telia''z Clinic Israel or dashboard-related records.'
name: Same-Month Intake Conversion Rate Understates Actual Patient Service Coverage
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10 Percent]]'
- '[[assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month]]'
relationships:
- confidence: 0.65
  context: Coverage nuance affects scaling
  source: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  target: assumption/Scaling Requires Approximately 176 Individual Quarter-Position
    Hires.md
  type: related-to
- confidence: 0.8
  context: Better metric than same-month rate
  source: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  target: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  type: supersedes
- confidence: 0.9
  context: Actual coverage > conversion implies
  source: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  target: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  type: contradicts
source: Adiel Levin, team meeting 2026-02-15
source_date: '2026-02-15'
status: active
tags:
- capacity
- metrics
- dashboard
type: assumption
---

# Same-Month Intake Conversion Rate Understates Actual Patient Service Coverage

## Claim

The widely cited 8% same-month intake conversion rate (77 of 945 patients in February 2026) significantly understates the actual proportion of patients who eventually receive clinical appointments. Patients registered in a given month may receive intake appointments in subsequent months, meaning the true service rate across all months is meaningfully higher than 8%.

## Basis

During the 2026-02-15 team meeting, Adiel Levin observed that the dashboard shows 92% of patients don't get appointments in the registration month, but does not show how many of those patients have appointments scheduled in future months. Rami agreed this metric was missing and should be added. The current dashboard architecture only measures same-month conversion, creating a potentially misleading picture of overall patient access.

## Evidence Trail

- 2026-02-15: Adiel raises the gap during team meeting review of operations dashboard
- 2026-02-15: Rami agrees the total-appointments metric should be added (task created)
- Pending: Actual data on cross-month appointment coverage not yet available

## Impact

If the true total conversion rate is substantially higher than 8% (e.g., 25-40%), the capacity crisis narrative changes significantly. Decisions about discharge protocols, aggressive hiring, and operational restructuring are currently calibrated to an 8% figure that may overstate the severity of the problem. Conversely, if the total rate is only marginally higher (e.g., 12%), it confirms the crisis is as severe as presented.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]