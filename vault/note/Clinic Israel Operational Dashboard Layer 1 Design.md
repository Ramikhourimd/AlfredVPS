---
created: '2026-02-25'
description: Architecture analysis of the Layer 1 operational dashboard (v5) for Telia'z
  Clinic Israel, documenting the Forward/Trend/Retro temporal separation, KPI mapping,
  and design evolution from previous dashboard iterations
janitor_note: 'LINK001 false-positive: project/Teliaz Clinic Israel and org/Teliaz
  are valid (YAML escaping). LINK001 base-embeds: _bases/related.base does not exist
  — base view embed preserved but non-functional.'
name: Clinic Israel Operational Dashboard Layer 1 Design
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[decision/Adopt Forward Trend Retro Temporal Dashboard Architecture]]'
- '[[org/Telia''z]]'
- '[[note/Clinic Israel KPI Dashboard January 2026]]'
- '[[person/Rami Khouri]]'
- '[[decision/Adopt Forward Trend Retro Temporal Architecture for Operations Dashboard]]'
relationships: []
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Israel Operational Dashboard Layer 1 Design

## Context

This is the fifth iteration of the Clinic Israel executive dashboard. The evolution path:
1. **v1** — `Clinic Israel Executive Dashboard` (retired) — initial KPI cards
2. **v2** — `Clinic Israel Executive Dashboard Variant B` — glass-morphism redesign
3. **v3** — `Clinic Executive Dashboard Variant B` — generalized version
4. **v4** — `Clinic Israel Flow Dashboard` — three-panel funnel with drill-down drawer
5. **v5** — `Clinic Israel Operational Dashboard Layer 1` (this version) — Forward/Trend/Retro temporal architecture

## Core Architectural Innovation: Temporal Separation

The previous dashboards mixed leading and lagging indicators in the same view — slot availability (forward-looking) sat next to wait times (backward-looking), which could confuse operators into false confidence ("wait times look fine" while "capacity is depleting ahead").

This version enforces strict temporal separation:

- **Forward (On-Calendar):** Only metrics about what's coming — available slots, nearest appointments, planned sessions. These are leading indicators.
- **Trend:** Bridging view showing how forward and retro metrics are moving over time. Two charts: one for retro flows (leads/scheduled/completed), one for forward slot trends.
- **Retro (Hindsight):** Only metrics about what happened — conversion rates, attendance, actual wait times. These are lagging indicators.

**The operational insight:** "If Forward slots are declining but Retro looks fine — you're heading toward trouble that hasn't shown up yet." This is explicitly called out in the dashboard's own tooltip text.

## Forward Section Analysis

### Tile F1: Availability (Free Slots)
- Shows total open appointment slots in the selected forward window (14d or 30d)
- Compared against monthly target of 80 slots via progress bar
- Includes delta from yesterday (Δ) for trend awareness
- The note calls this "predictive" — if it's low today, wait times will rise in 2 weeks

### Tile F2: Earliest Appointment by Category
- 2×2 matrix splitting by role (Psychiatrist/Case Manager) and session type (Intake/Follow-up)
- Each cell shows days-until-earliest and the specific date
- Identifies which service category is the bottleneck
- Aggregated "earliest any" callout at the bottom

### Tile F3: Planned On-Calendar
- Total sessions scheduled in the forward window
- Mix breakdown: Intake vs Follow-up count, Psych vs CM count
- Explicitly notes this is "how much will happen ahead" not "how much was scheduled this week"

## Trend Section Analysis

### Left Chart (Large): Retro Flows
Three daily lines: Leads (questionnaire submissions), Scheduled Created (appointments booked), Completed (sessions that actually occurred). Optional 7-day moving average smoothing.

**Diagnostic tip embedded in UI:** "If 'Scheduled Created' is rising but 'Completed' isn't — the leakage is in Attendance/No-show/Cancellations."

### Right Chart (Small): Forward Slot Trend
Two daily lines showing how available slots (next 14 days) are trending for Psychiatrists vs Case Managers.

**Diagnostic tip:** "If Forward slots are declining over time — you're heading toward a crunch even if Retro looks fine right now."

## Retro Section Analysis

### Tile R1: Leads → Scheduled Created
- Demand (questionnaire submissions) vs scheduling output (appointments created)
- Conversion rate with 90% target (up from 80% in v3)
- Includes period-over-period deltas for leads and scheduling volume
- Gap analysis: "X missing to convert every inquiry into a booking"

### Tile R2: Planned Past → Completed
- Sessions that were supposed to occur vs sessions that actually did
- Attendance rate with 85% target and target line on progress bar
- Leakage count (planned minus completed)
- Split by Intake vs Follow-up completed counts
- References "Layer 2 for no-show breakdown detail"

### Tile R3: Wait Times
- 2×2 matrix matching Forward's earliest-slot matrix
- Toggleable between Median and Average (median is default — aligns with earlier decision to use median for timing data)
- Color-coded against per-category targets:
  - Psych Intake: ≤14 days
  - Psych Follow-up: ≤10 days
  - CM Intake: ≤48 hours
  - CM Follow-up: ≤48 hours

## KPI Target Evolution

Comparing targets across dashboard iterations:

| KPI | v3 (Variant B) | v5 (Layer 1) | Change |
|-----|---------------|--------------|--------|
| Conversion | 80% | **90%** | Raised 10pp |
| Attendance | 85% | 85% | Unchanged |
| Wait Time | 48h (CM only) | **Granular per role×type** | Split into 4 targets |
| Availability | 80 slots/month | 80 slots/month | Unchanged |

The conversion target increase from 80% to 90% represents growing confidence in the scheduling process or a more ambitious operational standard. The wait time granularity (4 targets instead of 1) enables per-service-type bottleneck detection.

## Layer Architecture

The dashboard is explicitly labeled "Layer 1" (שכבה 1), implying:
- **Layer 1:** Executive overview with high-level KPIs (this dashboard)
- **Layer 2:** Drill-down detail (attendance breakdown, no-show analysis — partially built in v4's drawer)
- Potentially more layers for per-provider, per-pod, or per-patient-type views

## Technical Implementation

- Single-file HTML with embedded CSS and Chart.js 4.4.1
- Dark glass-morphism theme with CSS custom properties
- Responsive grid (3-column → 1-column on mobile)
- Hebrew RTL layout
- All data is hardcoded demo data — requires API integration for production
- Chart.js renders both trend charts with interactive tooltips

## Related
![[related.base#All]]
