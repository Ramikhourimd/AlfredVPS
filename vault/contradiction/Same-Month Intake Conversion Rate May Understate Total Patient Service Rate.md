---
alfred_tags:
- psychiatry/discrepancies
- operations/claims-vs-reality
claim_a: The clinic serves only 8% of patient demand — 945 register monthly but only
  77 get intake appointments
claim_b: The 8% figure measures same-month conversion only; many patients may receive
  appointments in subsequent months, making the actual service rate significantly
  higher
created: '2026-02-26'
janitor_note: LINK001 — Teliaz wikilinks are YAML-escape false positives. Synthesis
  link (Patient Demand Outpacing Capacity by 12x) confirmed valid. ORPHAN001 — no
  inbound links; consider linking from project/Teliaz Clinic Israel.
name: Same-Month Intake Conversion Rate May Understate Total Patient Service Rate
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Add Total Appointments Metric to Operations Dashboard]]'
- '[[assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand]]'
- '[[assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10 Percent]]'
- '[[constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February 2026]]'
- '[[constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026]]'
- '[[synthesis/Patient Demand Outpacing Capacity by 12x Creates Existential Operational
  Risk]]'
relationships:
- confidence: 0.65
  context: Service metrics vs workforce priorities
  source: contradiction/Same-Month Intake Conversion Rate May Understate Total Patient
    Service Rate.md
  target: contradiction/Workforce Stabilization Priority Conflicts With Concurrent
    Recruitment Urgency.md
  type: related-to
resolution: ''
source_a: February 2026 operations dashboard data and multiple existing constraint/assumption
  records
source_b: Adiel Levin observation during 2026-02-15 team meeting
status: unresolved
type: contradiction
---

# Same-Month Intake Conversion Rate May Understate Total Patient Service Rate

## Claim A

The clinic serves only ~8% of incoming patient demand. Multiple records frame this as an existential crisis: 945 patients register monthly, only 77 get intake appointments, and the remaining 92% effectively receive no service. This framing drives urgency around capacity expansion, discharge protocols, and organizational restructuring.

## Claim B

During the 2026-02-15 team meeting, Adiel Levin observed that the dashboard shows 92% of patients don't get appointments in the registration month — but doesn't show how many of those patients eventually receive appointments in subsequent months. The 8% is a same-month metric, not a total service metric. The actual proportion of registered patients who eventually receive any appointment could be substantially higher.

## Analysis

The distinction matters enormously for strategic planning. If the true total-service rate is, say, 30-40% (patients getting appointments within 2-3 months), the capacity crisis is real but less extreme than the 8% framing suggests. If it's still below 15%, the crisis framing is accurate. Currently, no one has this data — Rami agreed the metric should be added to the dashboard.

The existing records (assumptions, constraints, syntheses) consistently use the 8% figure without qualifying it as same-month-only, which may be inflating the perceived severity of the capacity gap. The "12x demand-to-capacity mismatch" synthesis is directly built on this potentially understated metric.

## Resolution

Unresolved. Requires adding the total-appointments metric to the operations dashboard to determine what proportion of registered patients eventually receive service across all months, not just the registration month.