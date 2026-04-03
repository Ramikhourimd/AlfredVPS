---
account: null
acquired: null
alfred_tags:
- clinic-israel/operations
- dashboard/flow
asset_type: software
cost: null
created: '2026-02-25'
description: 'HTML/CSS/JS prototype for Clinic Israel operations flow dashboard (v4)
  with three-panel layout: availability, new-patient funnel, and wait times. Adds
  Layer 2 attendance drill-down drawer with per-appointment-type breakdown and no-show
  analysis.'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (asset.base#Related) references _bases/asset.base which does not
  exist — do not remove embed, create base file to enable dynamic views.
location: null
name: Clinic Israel Flow Dashboard
owner: '[[person/Rami Khouri]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[asset/Clinic Israel Executive Dashboard]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[note/Clinic Israel Flow Dashboard Design]]'
- '[[org/Telia''z]]'
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
relationships:
- confidence: 0.8
  context: Flow depends on operational layer
  source: asset/Clinic Israel Flow Dashboard.md
  target: asset/Clinic Israel Operational Dashboard Layer 1.md
  type: depends-on
- confidence: 0.8
  context: Israel flow depends on general v4
  source: asset/Clinic Israel Flow Dashboard.md
  target: asset/Clinic Flow Dashboard v4.md
  type: depends-on
- confidence: 0.75
  context: Israel flow depends on original
  source: asset/Clinic Israel Flow Dashboard.md
  target: asset/Clinic Flow Dashboard.md
  type: depends-on
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Israel Flow Dashboard

## Details

Fourth iteration (v4) of the Telia'z Clinic Israel executive operations dashboard. Represents a major architectural shift from the previous KPI-card layout to a three-panel flow-centric design with drill-down layers.

- **Format:** Single HTML file with embedded CSS and JavaScript
- **Source file:** `inbox/processed/dashboard4.html`
- **Previous version:** `Clinic Executive Dashboard Variant B` (dashboard3.html)
- **Language:** Hebrew (RTL)
- **Status:** Prototype with demo data — pending API integration

### Architecture Changes from v3

| Aspect | v3 (Variant B) | v4 (Flow Dashboard) |
|--------|----------------|---------------------|
| Layout | 2-column KPI card grid | 3-panel: left (availability), center (funnel), right (wait times) |
| Primary view | 4 equal KPI cards | Patient flow funnel with conversion/attendance connectors |
| KPI strip | None | Top strip with 4 summary KPIs |
| Drill-down | None | Layer 2 slide-out drawer (attendance breakdown) |
| Interactivity | Tab-based time windows | Clickable funnel stages + connector pills open drawer |

### KPI Summary Strip

| KPI | Demo Value | Target |
|-----|-----------|--------|
| Intake Conversion | 83.3% | 80% |
| Attendance | 88.0% | 85% |
| Wait CM (Avg) | 62h | 48h |
| Slots (14d) | 47 | 80/month |

### Layer 2: Attendance Drill-Down

Slide-out drawer accessible from KPI strip, funnel connector pill, or completed-sessions step. Shows:

- **By appointment type:** Intake (80%), Follow-up CM (92%), Follow-up Psychiatrist (93%)
- **No-show reasons:** No-show (8), Patient cancellation (10), Clinic cancellation (2), Rescheduled (5)
- **Insight:** Most non-attendance comes from intake no-shows; recommends double-confirmation reminders

## Related
![[asset.base#Related]]