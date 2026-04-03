---
cluster_sources:
- '[[task/Implement Automated Patient Reminder Call System]]'
- '[[task/Increase Monthly Session Volume to 100 Target]]'
- '[[task/Address Rising Average Wait Time at Clinic Israel]]'
- '[[task/Add Dashboard Metric for Total Patients Scheduled Across All Months]]'
- '[[constraint/Immediate Secretary Hiring Required Due to Maternity Leave]]'
- '[[constraint/25 Percent Session Scheduling to Attendance Attrition January 2026]]'
confidence: medium
created: '2026-02-27'
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is YAML apostrophe-escaping
  false positive. Patient Demand synthesis wikilink target exists (scanner confused
  by YAML line wrap). ORPHAN001 — no inbound wikilinks; human should verify linkage.
name: Secretary Capacity Is Compounding Bottleneck Across Multiple Operational Workflows
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Automated Patient Reminders Can Halve Secretary Call Workload]]'
- '[[assumption/Renee Transitioning from Secretary to Pure Management]]'
- '[[assumption/Pod-Dedicated and Shared Pool Are the Two Candidate Secretary Models]]'
- '[[contradiction/Secretary Team Baseline Headcount Discrepancy]]'
- '[[synthesis/Patient Demand Outpacing Capacity by 12x Creates Existential Operational
  Risk]]'
status: draft
supports:
- '[[assumption/Minimum Two Additional Secretaries Required Immediately]]'
- '[[assumption/Secretary Roles Should Be Differentiated Into Patient-Facing and Staff-Facing]]'
type: synthesis
---

# Secretary Capacity Is Compounding Bottleneck Across Multiple Operational Workflows

## Insight

Secretary capacity constraints are not an isolated staffing problem — they compound across at least four distinct operational workflows, each amplifying the others. The pattern emerges clearly when task records from different time periods and contexts are viewed together:

1. **Reminder calls** (~50% of secretary time): Manual patient reminder calls consume roughly half of secretary capacity. Each unanswered call triggers repeated attempts.
2. **Scheduling throughput**: Only 92% of inquiries convert to scheduled sessions — the gap is partly limited by secretary availability to process bookings.
3. **Cancellation backfilling**: The 25% scheduling-to-attendance attrition (109 scheduled → 82 conducted in January 2026) cannot be recovered without secretary capacity to backfill cancelled slots in real-time.
4. **Wait time management**: Average wait time reached 14 days and is trending upward — secretaries are the operational layer between available psychiatrist slots and patient scheduling.

The compounding effect: reminder calls consume capacity that could backfill cancellations, which inflates wait times, which increases cancellation likelihood, which requires more backfilling effort.

## Evidence

- [[task/Implement Automated Patient Reminder Call System]]: Shira estimated ~50% of secretary time spent on manual reminder calls (2025-07-14)
- [[task/Increase Monthly Session Volume to 100 Target]]: 109 scheduled but only 82 conducted, 25% attrition (January 2026)
- [[task/Address Rising Average Wait Time at Clinic Israel]]: Average wait time at 14 days, trending upward (January 2026)
- [[constraint/Immediate Secretary Hiring Required Due to Maternity Leave]]: One of two FT secretaries going on maternity leave
- Renee transitioning from secretary to management removes another effective secretary from frontline

## Implications

- Hiring additional secretaries addresses symptoms but not the compounding cycle
- Automated patient reminders could break the cycle by freeing ~50% capacity for higher-value tasks (backfilling, scheduling optimization)
- The bottleneck will worsen as patient volume grows (945+/month) without either automation or significant headcount increase
- Secretary capacity should be treated as a system constraint (Theory of Constraints), not just a staffing metric

## Applicability

This pattern applies specifically to Telia'z Clinic Israel's current scale (945 patients/month, 2 FTE secretaries). The compounding dynamic would be relevant to any telepsychiatry clinic where secretaries handle both administrative scheduling and patient communication functions.
