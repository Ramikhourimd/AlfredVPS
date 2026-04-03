---
account: null
acquired: null
alfred_tags:
- clinic-israel/operations
- dashboard/flow
asset_type: software
cost: null
created: '2026-02-25'
description: HTML/CSS/JS prototype for Clinic Israel Layer 1 operational dashboard
  using Forward/Trend/Retro temporal architecture with 6 tile panels, dual trend charts,
  and interactive time window controls
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (asset.base#Related) references _bases/asset.base which does not
  exist — vault-wide structural issue.
location: null
name: Clinic Israel Operational Dashboard Layer 1
owner: '[[person/Rami Khouri]]'
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[decision/Adopt Forward Trend Retro Temporal Dashboard Architecture]]'
- '[[note/Clinic Israel Operational Dashboard Layer 1 Design]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.75
  context: Operational layer in flow dash
  source: asset/Clinic Israel Operational Dashboard Layer 1.md
  target: asset/Clinic Israel Flow Dashboard.md
  type: part-of
- confidence: 0.6
  context: Israel op layer uses general flow v4
  source: asset/Clinic Israel Operational Dashboard Layer 1.md
  target: asset/Clinic Flow Dashboard v4.md
  type: depends-on
- confidence: 0.65
  context: Israel op layer depends on general
  source: asset/Clinic Israel Operational Dashboard Layer 1.md
  target: asset/Clinic Flow Dashboard.md
  type: depends-on
renewal_date: null
status: active
tags: []
type: asset
vendor: '[[org/Telia''z]]'
---

# Clinic Israel Operational Dashboard Layer 1

## Details

Fifth iteration (v5) of the Telia'z Clinic Israel executive operations dashboard. Introduces a fundamental architectural shift from the flow-funnel layout (v4) to a **Forward/Trend/Retro temporal separation** — splitting all metrics by time direction to eliminate confusion between leading and lagging indicators.

- **Format:** Single HTML file with embedded CSS, JavaScript, and Chart.js
- **Source file:** `inbox/processed/final.html`
- **Previous version:** `Clinic Israel Flow Dashboard` (dashboard4.html)
- **Language:** Hebrew (RTL)
- **Status:** Prototype with demo data — pending API integration

### Architecture: Three Temporal Sections

| Section | Purpose | Tiles | Time Direction |
|---------|---------|-------|----------------|
| **Forward** (On-Calendar) | What's coming | 3 tiles: Availability, Earliest Slot, Planned Sessions | Future (14d or 30d window) |
| **Trend** | How things are moving | 2 charts: Retro flows + Forward slot trends | Historical daily series |
| **Retro** | What happened | 3 tiles: Leads→Scheduled, Planned→Completed, Wait Times | Past (7d, 30d, or 90d window) |

### Forward Tiles

1. **Availability (Free Slots)** — Total open slots in forward window vs monthly target (80), with delta from yesterday and progress bar
2. **Earliest Appointment by Category** — 2×2 matrix: Psychiatrist/Case Manager × Intake/Follow-up, showing days-until and date for each
3. **Planned On-Calendar** — Total scheduled sessions in forward window with mix breakdown (Intake/Follow-up × Psych/CM)

### Trend Charts

1. **Retro Flows** (large chart) — Three lines: Leads (questionnaires), Scheduled Created, Completed — daily with optional 7-day moving average
2. **Forward Slots** (small chart) — Two lines: Psychiatrist slots and Case Manager slots in next 14 days — daily snapshot with optional moving average

### Retro Tiles

1. **Leads → Scheduled Created** — Demand vs scheduling conversion with 90% target, delta tracking, and gap analysis
2. **Planned Past → Completed** — Attendance rate (scheduled-to-occur vs actually completed) with 85% target and leakage count
3. **Wait Times** — 2×2 matrix with median/average toggle: Psych Intake (≤14d), Psych Follow-up (≤10d), CM Intake (≤48h), CM Follow-up (≤48h) — color-coded against targets

### Interactive Controls

| Control | Options | Default | Effect |
|---------|---------|---------|--------|
| Forward window | 14d, 30d | 14d | Changes Forward tiles and planned sessions count |
| Retro window | 7d, 30d, 90d | 30d | Changes Retro tiles, trend chart slice |
| Moving average | 7-day MA, None | 7-day MA | Smooths trend chart lines |
| Wait time mode | Median, Average | Median | Switches wait time display metric |

### KPI Targets (embedded in prototype)

| KPI | Target | Unit | Comparison |
|-----|--------|------|------------|
| Monthly slots | 80 | slots/month | Higher is better |
| Conversion (leads→scheduled) | 90% | percentage | Higher is better |
| Attendance (scheduled→completed) | 85% | percentage | Higher is better |
| Psych Intake wait | ≤14 | days | Lower is better |
| Psych Follow-up wait | ≤10 | days | Lower is better |
| CM Intake wait | ≤48 | hours | Lower is better |
| CM Follow-up wait | ≤48 | hours | Lower is better |

### Key Design Insight

The Forward/Retro separation is the core innovation: if Forward slots are declining but Retro metrics look fine, the clinic is heading toward a capacity crunch that hasn't manifested yet. The Trend section bridges both views with overlaid temporal context.

## Related
![[asset.base#Related]]