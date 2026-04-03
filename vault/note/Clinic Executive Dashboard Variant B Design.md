---
alfred_tags:
- clinic/israel
- executive/dashboard
- operations/kpi
created: '2026-02-25'
description: Design specification for Variant B of the Telia'z Clinic Israel executive
  dashboard, featuring four KPI cards (Intake Conversion, Attendance, Wait Times CM,
  Availability) with glass-morphism UI, battery-style progress bars, and time-window
  toggles
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Create it to enable dynamic views. Telia'z wikilinks are valid
  (YAML escaping false positive).
name: Clinic Executive Dashboard Variant B Design
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Telia''z]]'
- '[[asset/Clinic Executive Dashboard]]'
relationships:
- confidence: 0.95
  context: Israel-specific Variant B design
  source: note/Clinic Executive Dashboard Variant B Design.md
  target: note/Clinic Israel Executive Dashboard Design Variant B.md
  type: related-to
- confidence: 0.7
  context: KPI analysis for dashboard design
  source: note/Clinic Executive Dashboard Variant B Design.md
  target: note/Clinic Israel Executive Dashboard KPI Analysis.md
  type: related-to
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Executive Dashboard — Variant B Design

## Overview

HTML/CSS/JS prototype for an executive-level clinic operations dashboard. Dark glass-morphism aesthetic with RTL Hebrew layout. Designed to give leadership an at-a-glance view of the four core operational KPIs for Telia'z Clinic Israel.

## KPI Cards

### 1. Intake Conversion
- **Metric:** Leads → Scheduled appointments (percentage)
- **Target:** 80%
- **Time windows:** 7 days, 30 days
- **Pills:** Total leads count, scheduled appointments count
- **Battery bar:** Fill shows actual conversion vs 80% target marker
- **Interpretation:** Measures coordination/UX effectiveness. Does not include whether sessions actually occurred.

### 2. Attendance
- **Metric:** Planned sessions → Sessions that occurred (percentage)
- **Threshold:** 85%
- **Time windows:** Week, 30 days
- **Pills:** Planned sessions count, attended sessions count
- **Battery bar:** Fill shows actual attendance vs 85% threshold
- **Interpretation:** No-show / cancellation rate. Breakdown by session type is available at a deeper layer.

### 3. Wait Times — Case Manager (CM)
- **Metric:** Average wait time in hours (retrospective)
- **Target:** 48 hours
- **Time windows:** 7 days, 30 days
- **Pills:** Average hours, target hours (48)
- **Battery bar:** Inverted — fuller bar means more pressure (exceeded target). Green when under target, red when over.
- **Interpretation:** Measures operational pressure on case manager scheduling.

### 4. Availability
- **Metric:** Open appointment slots (real-time / forward-looking)
- **Target:** 80 slots per month
- **Time windows:** 14 days, 30 days
- **Pills:** Nearest available slot date, target slot count (80)
- **Battery bar:** Fill shows slots as proportion of target
- **Interpretation:** Leading indicator — when red today, wait times will increase tomorrow.

## Design Details

- **Layout:** 2-column grid (responsive to single column below 1050px)
- **Theme:** Dark glass-morphism (`#070d1a` background, subtle radial gradient glows, glass-border cards)
- **Cards:** 22px border-radius, inner corner glow pseudo-element, min-height 290px
- **Typography:** System UI font stack, KPI numbers at 56px/950 weight
- **Color coding:** Green (`#2ecc71`) = good, Yellow (`#f1c40f`) = warning, Red (`#e74c3c`) = bad
- **Interactivity:** Tab-based time window toggles per card, delta indicators (triangle arrows) showing period-over-period change
- **Header chips:** NPS score indicator (demo: 42, yellow), last-updated timestamp

## Demo Data Structure (JavaScript)

Each KPI card has data keyed by time window. Structure per metric:
- **Intake:** `{ leads, scheduled, prev_leads, prev_scheduled, label }`
- **Attendance:** `{ planned, done, prev_planned, prev_done, label }`
- **Wait CM:** `{ hours, prev_hours, label }`
- **Availability:** `{ slots, prev_slots, earliest, label }`

Delta calculations compare current vs previous period values. Color thresholds use 90% of target as the warning boundary (or 110% for inverted metrics like wait time).

## Technical Notes

- Pure HTML/CSS/JS — no framework dependencies
- All data currently hardcoded; designed for API integration
- RTL layout with `lang="he" dir="rtl"`
- CSS custom properties for theming

## Related
![[related.base#All]]