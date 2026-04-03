---
alfred_tags:
- israel-clinic/constraints
- intake-conversion
- session-attrition
authority: Operational metrics
created: '2026-02-27'
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is valid (YAML escaping false
  positive, target verified at project/Telia'z Clinic Israel.md).
name: 25 Percent Session Scheduling to Attendance Attrition January 2026
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Increase Monthly Session Volume to 100 Target]]'
- '[[task/Address Rising Average Wait Time at Clinic Israel]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
- '[[constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February 2026]]'
relationships:
- confidence: 0.6
  context: Clinic ops constraints Jan-Feb 2026
  source: constraint/25 Percent Session Scheduling to Attendance Attrition January
    2026.md
  target: constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026.md
  type: related-to
- confidence: 0.6
  context: Clinic ops constraints Jan-Feb 2026
  source: constraint/25 Percent Session Scheduling to Attendance Attrition January
    2026.md
  target: constraint/Israel Clinic at 8 Percent Intake Conversion February 2026.md
  type: related-to
- confidence: 0.6
  context: Clinic ops constraints Jan-Feb 2026
  source: constraint/25 Percent Session Scheduling to Attendance Attrition January
    2026.md
  target: constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February
    2026.md
  type: related-to
- confidence: 0.65
  context: Capacity and staffing constraints
  source: constraint/25 Percent Session Scheduling to Attendance Attrition January
    2026.md
  target: constraint/Israel Clinic 8 Percent Intake Conversion Rate Limits Availability
    of Stopgap Staff for UK Launch.md
  type: related-to
source: January 2026 KPI Dashboard operational data
source_date: '2026-01-31'
status: active
type: constraint
---

# 25 Percent Session Scheduling to Attendance Attrition January 2026

## Constraint

In January 2026, 109 sessions were scheduled but only 82 were conducted — a 25% attrition rate between scheduling and attendance. This gap represents both lost revenue and wasted psychiatrist availability slots. The monthly session target is 100, so the 82 conducted sessions fall 18% short of target.

## Source

January 2026 KPI dashboard data analyzed in the session volume task. The funnel shows: 125 inquiries → 109 scheduled (92% conversion) → 82 conducted (~75% conversion). The loss concentrates at the scheduling-to-conducted stage, likely driven by cancellations and no-shows.

## Implications

- Even if inquiry-to-scheduling conversion is optimized to 95%+, the 25% attrition at the attendance stage caps effective throughput
- Each unfilled slot represents approximately 250-350 NIS in lost revenue (follow-up to intake rate)
- The attrition may compound with the rising average wait time (14 days): patients scheduled further out may be more likely to cancel
- Backfilling cancelled slots requires secretarial capacity that is already constrained
- Addressing this gap (reducing attrition from 25% to 15%) could add ~11 sessions/month without any additional psychiatrist capacity

## Expiry / Review

This metric should be tracked monthly on the KPI dashboard. Review whether the 25% rate is seasonal or structural by comparing across Q1 2026.