---
account: null
acquired: null
alfred_tags:
- clinic-israel/operations
- dashboard/flow
asset_type: software
cost: null
created: '2026-02-25'
description: 'Flow Dashboard prototype (v4) for Telia''z Clinic Israel with three-column
  layout: Availability panel, New Patient Flow funnel, and Wait Times panel. Introduces
  Layer 2 attendance drill-down drawer with per-appointment-type breakdown and no-show
  reason analysis.'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive,
  all targets exist). Base view embed \![[asset.base#Related]] references _bases/asset.base
  which does not exist yet. Create _bases/asset.base to enable dynamic views.
location: null
name: Clinic Flow Dashboard v4
owner: '[[person/Rami Khouri]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[note/Clinic Israel Executive Dashboard KPI Analysis]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.95
  context: v4 supersedes earlier version
  source: asset/Clinic Flow Dashboard v4.md
  target: asset/Clinic Flow Dashboard.md
  type: supersedes
- confidence: 0.85
  context: Israel variant of general flow
  source: asset/Clinic Flow Dashboard v4.md
  target: asset/Clinic Israel Flow Dashboard.md
  type: related-to
- confidence: 0.6
  context: Shared clinic dashboard theme
  source: asset/Clinic Flow Dashboard v4.md
  target: asset/Clinic Israel Operational Dashboard Layer 1.md
  type: related-to
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Flow Dashboard v4

## Details

Fourth iteration of the Clinic Israel executive operations dashboard. Replaces the 2-column KPI card layout (Variant B) with a 3-column panel architecture: Availability (left), New Patient Flow funnel (center), and Wait Times (right). Adds the first working Layer 2 drill-down: an attendance breakdown drawer.

- **Format:** Single HTML file with embedded CSS and JavaScript
- **Source file:** `inbox/processed/dashboard4.html`
- **Design:** Dark glassmorphism theme, RTL Hebrew layout
- **Data:** Hardcoded demo data — pending API integration
- **Predecessor:** `asset/Clinic Executive Dashboard Variant B` (dashboard3.html)

### Architecture Changes from v3

| Feature | v3 (Variant B) | v4 (Flow Dashboard) |
|---------|----------------|---------------------|
| Layout | 2-column KPI card grid | 3-column panels (Availability / Funnel / Wait Times) |
| Funnel view | None | 3-step funnel: Inquiries → Scheduled → Completed |
| Layer 2 drill-down | None (planned) | Attendance drawer with per-type breakdown |
| Interactive elements | Time window toggles | Clickable KPI tiles, funnel steps, and connector pills opening drawers |

### KPI Strip (Layer 1)

| KPI | Demo Value | Target |
|-----|-----------|--------|
| Intake Conversion | 83.3% | 80% |
| Attendance | 88.0% | 85% |
| Wait CM (Avg) | 62h | 48h |
| Slots (14d) | 47 | 80/month |

### Funnel Flow (Center Panel)

| Step | Count | Metric |
|------|-------|--------|
| Inquiries (questionnaires) | 300 | Baseline |
| Appointments scheduled | 250 | 83.3% conversion |
| Appointments completed | 220 | 88.0% attendance |

### Layer 2: Attendance Drill-Down

Accessed by clicking Attendance KPI tile, funnel connector pill, or completed step.

**By appointment type (target 85%):**
| Type | Attended / Scheduled | Rate | Status |
|------|---------------------|------|--------|
| Intake | 48 / 60 | 80% | Below target (yellow) |
| Follow-up CM | 23 / 25 | 92% | Above target (green) |
| Follow-up Psychiatrist | 14 / 15 | 93% | Above target (green) |

**No-show reasons:**
- No-show: 8
- Patient cancellation: 10
- Clinic cancellation: 2
- Rescheduled: 5

**Insight:** Most non-attendance stems from intake no-shows. Recommended action: strengthen reminder / double-confirmation day before.

### Planned Layer 2 Additions (noted in prototype)

- **Availability panel:** CM/Psychiatrist breakdown + appointment type split
- **Wait Times panel:** Median/tail distribution + per-provider breakdown
- **Funnel:** Intake vs follow-up split + no-show reasons per step

## Related
![[asset.base#Related]]