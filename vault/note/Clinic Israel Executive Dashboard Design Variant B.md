---
alfred_tags:
- clinic/israel
- executive/dashboard
- operations/kpi
created: '2026-02-25'
description: 'Design documentation for Variant B of the Clinic Israel executive dashboard,
  tracking four operational KPIs: intake conversion, attendance, wait times, and slot
  availability with glass-morphism UI'
janitor_note: LINK001 — Telia'z project and org links are valid (YAML single-quote
  escaping false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist.
name: Clinic Israel Executive Dashboard Design Variant B
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Telia''z]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
relationships:
- confidence: 0.9
  context: Design depends on KPI analysis
  source: note/Clinic Israel Executive Dashboard Design Variant B.md
  target: note/Clinic Israel Executive Dashboard KPI Analysis.md
  type: depends-on
- confidence: 0.9
  context: Israel variant depends on general design
  source: note/Clinic Israel Executive Dashboard Design Variant B.md
  target: note/Clinic Executive Dashboard Variant B Design.md
  type: depends-on
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Israel Executive Dashboard Design — Variant B

## Overview

HTML/CSS/JS prototype for a clinic operations executive dashboard. Uses a dark glass-morphism aesthetic with RTL Hebrew layout. Contains four KPI cards with time-window toggles and progress battery visualizations. Currently loaded with hardcoded demo data (NPS demo: 42, last updated 12 Jan 2026).

The "Variant B" designation implies comparison against at least one alternative design.

## KPI Cards

### 1. Intake Conversion
- **Metric:** Leads (inquiries) → Scheduled appointments
- **Target:** 80%
- **Time windows:** 7 days, 30 days
- **Demo data (7d):** 300 leads, 250 scheduled = 83.3%
- **Note:** Measures coordination/UX. Does not include whether appointments actually took place.

### 2. Attendance
- **Metric:** Planned appointments → Completed appointments
- **Target (threshold):** 85%
- **Time windows:** Week, 30 days
- **Demo data (week):** 100 planned, 88 completed = 88%
- **Note:** Tracks no-shows and cancellations. Breakdown by appointment type available at drill-down level.

### 3. Wait Times — Case Manager (CM)
- **Metric:** Average wait time in hours (retrospective)
- **Target:** 48 hours
- **Time windows:** 7 days, 30 days
- **Demo data (7d):** 62 hours (above target — red)
- **Note:** Battery fills as pressure increases — fuller = worse. Inverse metric (lower is better).

### 4. Availability
- **Metric:** Open appointment slots (forward-looking)
- **Target:** 80 slots per month
- **Time windows:** 14 days, 30 days
- **Demo data (14d):** 47 slots available, earliest: 14 Jan
- **Note:** Leading indicator — when red today, wait times will increase tomorrow.

## Design Characteristics

- **Visual style:** Dark glass-morphism (frosted glass cards, subtle radial gradients, corner glow effects)
- **Layout:** RTL Hebrew, 2-column responsive grid (collapses to 1 column below 1050px)
- **Color coding:** Green (good) / Yellow (warning at 90% of target) / Amber-Red (bad)
- **Interactions:** Time-window tab toggles per card, delta indicators showing period-over-period change
- **Battery visualization:** Progress bar with target marker line, contextual fill color
- **Typography:** System UI font stack, 56px hero KPI numbers

## Data Structure

Hardcoded JSON `DATA` object with per-metric, per-window structure including current and previous period values for delta calculation. Production version would need API integration.

## Related
![[related.base#All]]