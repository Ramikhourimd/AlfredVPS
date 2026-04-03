---
account: null
acquired: null
alfred_tags:
- clinic-israel/operations
- dashboard/flow
asset_type: software
cost: null
created: '2026-02-25'
description: HTML/CSS/JS prototype for Clinic Israel operations dashboard using funnel-centric
  3-panel layout (Availability, Patient Flow, Wait Times) with Layer 2 attendance
  drill-down drawer, glass-morphism dark theme, RTL Hebrew, and demo data
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (asset.base#Related) references _bases/asset.base which does not
  exist — create it to enable dynamic views.
location: null
name: Clinic Flow Dashboard
owner: '[[person/Rami Khouri]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[decision/Adopt Funnel-Centric Layout for Clinic Operations Dashboard]]'
- '[[note/Clinic Flow Dashboard Design]]'
relationships:
- confidence: 0.9
  context: Israel version of general flow
  source: asset/Clinic Flow Dashboard.md
  target: asset/Clinic Israel Flow Dashboard.md
  type: related-to
- confidence: 0.55
  context: Related via Israel flow dash
  source: asset/Clinic Flow Dashboard.md
  target: asset/Clinic Israel Operational Dashboard Layer 1.md
  type: related-to
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Flow Dashboard

## Details

Static HTML prototype (single-file, no build dependencies) for the Clinic Israel operations dashboard. Replaces the 4-card KPI layout (Variant B) with a funnel-centric 3-panel design that visualizes patient flow as a pipeline: Inquiries → Scheduled → Completed.

- **Format:** Single HTML file with embedded CSS and JavaScript
- **Source file:** `inbox/processed/dashboard4.html`
- **Design approach:** Flow/funnel visualization (evolution from KPI card grid)
- **Language:** Hebrew (RTL)
- **Key innovation:** Layer 2 drill-down drawers — clicking attendance metrics opens a side panel with breakdown by appointment type and no-show reasons

### Layout

| Panel | Content | Orientation |
|-------|---------|-------------|
| Left (1fr) | Availability — real-time slot count with 14d/30d toggle | Leading indicator |
| Center (2fr) | Patient Flow Funnel — 300 inquiries → 250 scheduled → 220 completed | Core pipeline |
| Right (1fr) | Wait Times — CM avg 62h, Psych avg 19d with sparkline trend | Retrospective |

### Layer 2: Attendance Drawer

Activated by clicking attendance pill in funnel or KPI strip. Contains:
- Breakdown by appointment type: Intake (80%), Follow-up CM (92%), Follow-up Psychiatrist (93%)
- No-show categorization: No-show (8), Patient cancellation (10), Clinic cancellation (2), Rescheduled (5)
- Insight: Most no-shows come from intake appointments; recommends double-confirmation reminders

## Related
![[asset.base#Related]]