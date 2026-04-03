---
alfred_tags:
- clinic/capacity-management
- patient/discharge
- case-management/staffing
approved_by: []
based_on: []
challenged_by: []
confidence: medium
created: '2026-02-25'
decided_by: []
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist; embeds are duplicated
  in body. Telia''z project/org wikilinks are valid (YAML escaping false positive
  from scanner). All base view embeds preserved per policy.'
name: Four Core KPI Targets for Clinic Operations Dashboard
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Israel Executive Dashboard Design Variant B]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[org/Telia''z]]'
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
- '[[decision/Adopt Forward Trend Retro Temporal Dashboard Architecture]]'
- '[[note/Clinic Israel Operational Dashboard Layer 1 Design]]'
- '[[decision/Adopt Forward Trend Retro Temporal Architecture for Operations Dashboard]]'
session: null
source: Dashboard prototype Variant B
source_date: null
status: draft
supports:
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
tags: []
type: decision
---

# Four Core KPI Targets for Clinic Operations Dashboard

## Context

As part of building an executive dashboard for Clinic Israel operations, four core KPIs were selected with specific target thresholds. These targets appear in the Variant B dashboard prototype and define operational performance standards.

## KPI Targets

| KPI | Target | Direction | Rationale |
|-----|--------|-----------|-----------|
| Intake Conversion | 80% | Higher is better | Measures how effectively inquiries convert to scheduled appointments |
| Attendance Rate | 85% | Higher is better | Threshold for no-show/cancellation management |
| Wait Time (CM) | 48 hours | Lower is better | Maximum acceptable average wait for case manager appointment |
| Availability | 80 slots/month | Higher is better | Forward-looking capacity indicator for scheduling headroom |

## Decision

Adopt these four metrics and targets as the primary executive-level operational KPIs for Clinic Israel.

## Rationale

- **Intake Conversion (80%):** Isolates scheduling/UX effectiveness from clinical delivery, allowing targeted process improvement
- **Attendance (85%):** Standard threshold for mental health service attendance; accounts for normal cancellation rates
- **Wait Time 48h:** Balances patient urgency with realistic scheduling capacity for case manager first contact
- **Availability (80 slots):** Leading indicator — provides early warning before wait times degrade

## Consequences

- Dashboard design built around these four metrics
- Operational team performance measured against these thresholds
- Color-coded alerting (green/yellow/red) triggers at 100%, 90%, and below 90% of target
- Future drill-down layers needed for per-appointment-type and per-provider breakdowns

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]


## V5 Update (Layer 1 Dashboard)

The Layer 1 Operational Dashboard (v5) refined these targets:

| KPI | Previous Target | V5 Target | Change |
|-----|----------------|-----------|--------|
| Conversion (leads→scheduled) | 80% | **90%** | Raised 10pp based on operational maturity |
| Attendance (scheduled→completed) | 85% | 85% | Unchanged |
| Wait Time | 48h (CM only) | **Granular per role×type** | Split into 4 distinct targets |
| Availability | 80 slots/month | 80 slots/month | Unchanged |

### Granular Wait Time Targets (V5)

| Category | Target | Unit |
|----------|--------|------|
| Psychiatrist Intake | ≤14 | days |
| Psychiatrist Follow-up | ≤10 | days |
| Case Manager Intake | ≤48 | hours |
| Case Manager Follow-up | ≤48 | hours |

See [[asset/Clinic Israel Operational Dashboard Layer 1]] for the implementing prototype.


## Update: Layer 1 Dashboard (v5) — Refined Targets

The Layer 1 operational dashboard refines these targets:

| KPI | Original Target | Revised Target | Notes |
|-----|----------------|----------------|-------|
| Conversion (leads→scheduled) | 80% | **90%** | Raised to reflect scheduling process maturity |
| Attendance (scheduled→completed) | 85% | 85% | Unchanged |
| Availability | 80 slots/month | 80 slots/month | Unchanged |
| Wait Time CM | 48h (single target) | **4 granular targets** | Split by role and session type |

### Granular Wait Time Targets (v5)

| Category | Target | Unit |
|----------|--------|------|
| Psychiatrist Intake | ≤14 days | days |
| Psychiatrist Follow-up | ≤10 days | days |
| Case Manager Intake | ≤48 hours | hours |
| Case Manager Follow-up | ≤48 hours | hours |

See [[asset/Clinic Israel Operational Dashboard Layer 1]] and [[note/Clinic Israel Operational Dashboard Layer 1 Design]] for full context.