---
account: null
acquired: null
alfred_tags:
- clinic-israel/executive-dashboard
asset_type: software
cost: null
created: '2026-02-25'
description: Interactive HTML/CSS/JS prototype of an executive KPI dashboard for Telia'z
  Clinic Israel, tracking intake conversion, attendance, wait times, and slot availability
  with demo data and glassmorphism UI design
janitor_note: '"LINK001 false positives: Telia''z wikilinks use YAML escaping (double
  single-quotes); org/Telia''z.md and project/Telia''z Clinic Israel.md both exist
  and are valid targets. Base view embed \![[asset.base#Related]] preserved per policy
  (_bases/ directory not present)."'
location: null
name: Clinic Israel Executive Dashboard Variant B
owner: null
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[project/Telia''z Clinic Israel]]'
- '[[org/Telia''z]]'
- '[[note/Clinic Israel Executive Dashboard KPI Analysis]]'
relationships:
- confidence: 0.85
  context: Israel variant adapts general Variant B
  source: asset/Clinic Israel Executive Dashboard Variant B.md
  target: asset/Clinic Executive Dashboard Variant B.md
  type: depends-on
- confidence: 0.7
  context: Israel Variant B related to base dashboard
  source: asset/Clinic Israel Executive Dashboard Variant B.md
  target: asset/Clinic Executive Dashboard.md
  type: related-to
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Israel Executive Dashboard — Variant B

## Overview

A self-contained HTML/CSS/JavaScript prototype of an executive-level operational dashboard for [[project/Telia'z Clinic Israel]]. Uses a dark glassmorphism design with RTL Hebrew layout, 2-column card grid, and interactive time-window toggling.

## Technical Details

- **Format:** Single-file HTML with embedded CSS and JavaScript
- **Layout:** RTL (Hebrew), 2-column responsive grid, 4 KPI cards
- **Styling:** Dark glassmorphism theme (frosted glass cards, radial gradients, pill-shaped controls)
- **Interactivity:** Time window toggles (7/14/30 day views), color-coded battery bars with target markers
- **Data:** Hardcoded demo data — not connected to a live data source
- **Last demo update shown:** 2026-01-12 18:25

## KPI Cards

### 1. Intake Conversion
- **Metric:** Leads → Scheduled appointments
- **Target:** 80%
- **Demo data (7d):** 250/300 = 83.3% (above target, green)
- **Demo data (30d):** 920/1240 = 74.2% (below target, red)

### 2. Attendance
- **Metric:** Planned sessions → Attended sessions
- **Threshold:** 85%
- **Demo data (7d):** 88/100 = 88.0% (above threshold, green)
- **Demo data (30d):** 361/420 = 85.9% (near threshold, yellow)

### 3. Wait Times — Case Manager
- **Metric:** Average wait time in hours (retrospective)
- **Target:** 48 hours (lower is better)
- **Demo data (7d):** 62h (above target — pressure indicator red)
- **Demo data (30d):** 58h (above target — pressure indicator red)

### 4. Availability
- **Metric:** Available appointment slots (forward-looking)
- **Target:** 80 slots/month
- **Demo data (14d):** 47 slots (below target, red)
- **Demo data (30d):** 112 slots (above target, green)
- **Earliest available slot:** Jan 14

## Design Notes

- Each card includes a "battery bar" gauge showing actual vs. target, with color coding (green/yellow/red)
- Delta indicators show period-over-period change with directional triangles
- Global header shows demo NPS score (42, yellow) and last-updated timestamp
- Fully responsive — collapses to single column below 1050px

## Related
![[asset.base#Related]]