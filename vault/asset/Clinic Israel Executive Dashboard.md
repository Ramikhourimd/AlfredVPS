---
account: null
acquired: null
asset_type: software
cost: null
created: '2026-02-25'
description: DUPLICATE — see asset/Clinic Executive Dashboard Variant B.md for canonical
  record
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (asset.base#Related) references _bases/asset.base which does not
  exist — create base file to enable dynamic views.
location: null
name: Clinic Israel Executive Dashboard
owner: null
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[note/Clinic Israel Executive Dashboard Design Variant B]]'
- '[[asset/Clinic Israel Flow Dashboard]]'
relationships: []
renewal_date: null
status: retired
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Israel Executive Dashboard

## Details

Interactive HTML/CSS/JS prototype dashboard for Telia'z Clinic Israel operations. Variant B design with glassmorphism UI, RTL Hebrew layout, and dark theme.

### KPI Cards
1. **Intake Conversion** — Leads to scheduled appointments (target: 80%)
2. **Attendance** — Planned vs attended sessions (threshold: 85%)
3. **Wait Times – CM** — Case manager average wait time (target: 48 hours)
4. **Availability** — Open appointment slots (monthly target: 80)

### Features
- Time window toggles (7-day, 14-day, 30-day views)
- Delta indicators showing period-over-period change
- Battery/progress bar visualization with color-coded status (green/yellow/red)
- Target markers on progress bars
- Responsive 2-column grid layout

### Technical Stack
- Pure HTML/CSS/JS (no frameworks)
- CSS custom properties for theming
- Hardcoded demo data (not connected to live data source)
- NPS indicator chip (demo value: 42)

## Related
![[asset.base#Related]]
