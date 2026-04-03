---
alfred_tags:
- clinic/israel
- executive/dashboard
- operations/kpi
created: '2026-02-25'
description: Analysis of the Variant B executive dashboard prototype for Telia'z Clinic
  Israel, covering four operational KPIs — intake conversion, attendance, case manager
  wait times, and appointment availability — with demo data insights and operational
  implications
janitor_note: LINK001 — Fixed person/Basel Khouri → person/Basel Kanaaneh in related
  field. Body still references [[person/Basel Khouri]] — needs manual body edit. Base
  view embed (related.base#All) references missing _bases/related.base — vault-wide
  infrastructure gap, embed preserved.
name: Clinic Israel Executive Dashboard KPI Analysis
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[project/Telia''z Clinic Israel]]'
- '[[org/Telia''z]]'
- '[[asset/Clinic Israel Executive Dashboard Variant B]]'
- '[[person/Basel Kanaaneh]]'
- '[[decision/Adopt District Model for Clinic Israel]]'
- '[[task/Basel to Present Clinic Operational Plan]]'
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[note/Clinic Israel Flow Dashboard Design]]'
relationships:
- confidence: 0.9
  context: KPI analysis informs design
  source: note/Clinic Israel Executive Dashboard KPI Analysis.md
  target: note/Clinic Israel Executive Dashboard Design Variant B.md
  type: supports
- confidence: 0.8
  context: KPI analysis supports dashboard design
  source: note/Clinic Israel Executive Dashboard KPI Analysis.md
  target: note/Clinic Executive Dashboard Variant B Design.md
  type: supports
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Israel Executive Dashboard KPI Analysis

## Context

An executive dashboard prototype (Variant B) was created for [[project/Telia'z Clinic Israel]] to track four critical operational KPIs. The dashboard uses hardcoded demo data to illustrate the intended monitoring approach. This note analyzes the KPI framework, the demo data signals, and operational implications.

## KPI Framework

The dashboard defines four metrics that together capture the full patient funnel:

| # | KPI | Measures | Target | Direction |
|---|-----|----------|--------|-----------|
| 1 | **Intake Conversion** | Leads → Scheduled appointments | 80% | Higher is better |
| 2 | **Attendance** | Scheduled → Attended sessions | 85% | Higher is better |
| 3 | **Wait Times (CM)** | Average hours from referral to case manager | 48h | Lower is better |
| 4 | **Availability** | Open appointment slots (forward-looking) | 80/month | Higher is better |

This is a coherent funnel: Intake captures top-of-funnel efficiency, Attendance measures conversion to actual care, Wait Times tracks access bottleneck at the case manager level, and Availability is a leading indicator of future wait times.

## Demo Data Insights

### Intake Conversion
- **7-day:** 83.3% (250 of 300 leads scheduled) — above 80% target
- **30-day:** 74.2% (920 of 1,240 leads scheduled) — below 80% target
- **Delta:** +6.6% improvement week-over-week
- **Implication:** Short-term conversion is healthy, but the 30-day view suggests inconsistency. The gap between 7-day and 30-day performance may indicate a recent process improvement or seasonal variance.

### Attendance
- **7-day:** 88.0% (88 of 100 planned) — above 85% threshold
- **30-day:** 85.9% (361 of 420 planned) — barely above threshold
- **Delta:** -2.4% decline
- **Implication:** Attendance is declining. The weekly rate is still above threshold but the negative trend warrants monitoring. The dashboard note correctly identifies this as a no-show/cancellation metric.

### Wait Times — Case Manager
- **7-day:** 62 hours — 29% above the 48-hour target
- **30-day:** 58 hours — 21% above the 48-hour target
- **Delta:** +4h (worsening)
- **Implication:** This is the most concerning metric. Wait times are significantly above target and trending worse. This connects to the known constraint around [[constraint/Secretarial Capacity Is Critically Low]] and staffing challenges discussed in restructuring meetings. The case manager bottleneck may reflect the broader operational strain.

### Availability
- **14-day:** 47 slots — 41% below the 80-slot target
- **30-day:** 112 slots — above target
- **Delta:** -12 slots
- **Implication:** Near-term availability is critically low while longer-term availability is adequate. This pattern suggests bunching — appointments are booked solid for the next two weeks, with capacity opening up further out. This is consistent with the wait time pressure seen above.

## Operational Observations

1. **Wait times and availability are the pressure points.** The dashboard demo data shows these two metrics in red — they represent the operational bottleneck.
2. **Intake is healthy but fragile.** Good short-term conversion can mask capacity problems downstream — high intake with low availability creates patient experience risk.
3. **The funnel is well-designed.** These four KPIs together provide a complete operational picture: top-of-funnel (intake), utilization (attendance), access (wait times), and forward capacity (availability).
4. **This is a prototype, not production.** Demo data is hardcoded. Connecting to live operational data systems would be the next step.

## Connection to Restructuring

This dashboard directly supports the operational visibility needs discussed in the [[project/Telia'z Organizational Restructuring]] context. [[person/Basel Khouri]] as the operational leader of the clinic would use this to monitor the district's performance against KPI targets. The pod structure decision ([[decision/Implement Pod Structure for Psychiatrist Teams]]) may eventually enable per-pod drill-down views.

## Related
![[related.base#All]]