---
alfred_tags:
- healthcare/clinic-dashboard
- ui/flow-design
created: '2026-02-25'
description: Design specification for the funnel-centric Clinic Israel operations
  dashboard with 3-panel layout (Availability, Patient Flow, Wait Times), Layer 2
  attendance drill-down drawer, and interactive data exploration pattern
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Create it to enable dynamic views. All Telia'z wikilinks are
  valid (YAML escaping false positive).
name: Clinic Flow Dashboard Design
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[note/Clinic Executive Dashboard Variant B Design]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[decision/Adopt Funnel-Centric Layout for Clinic Operations Dashboard]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.9
  context: Base design for v4 analysis
  source: note/Clinic Flow Dashboard Design.md
  target: note/Clinic Flow Dashboard v4 Design Analysis.md
  type: supports
- confidence: 0.85
  context: General design supports Israel variant
  source: note/Clinic Flow Dashboard Design.md
  target: note/Clinic Israel Flow Dashboard Design.md
  type: supports
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Flow Dashboard — Design Specification

## Overview

A fundamentally different approach to the Clinic Israel executive dashboard. While the previous Variant B used four independent KPI cards in a 2x2 grid, this design centers on the **patient flow funnel** — visualizing the clinic's core pipeline as a progression from inquiries through scheduling to completed appointments. Supporting metrics (availability, wait times) flank the funnel in dedicated side panels.

## Design Philosophy

The shift from KPI cards to a funnel layout reflects a key insight: clinic operations are best understood as a **flow**, not as isolated metrics. Intake conversion, attendance, and wait times are stages in a single pipeline. When a patient drops out, the relevant question is *where in the flow* they dropped — not just *which KPI* is below target.

## Architecture: Layer 1 + Layer 2

### Layer 1 — Overview (Always Visible)

**KPI Strip (top):** Four summary tiles — Intake Conversion (83.3%), Attendance (88.0%), Wait CM Avg (62h), Slots 14d (47). The Attendance tile is clickable, opening the Layer 2 drawer.

**3-Panel Layout:**

| Panel | Width | Role | Contents |
|-------|-------|------|----------|
| Left | 1fr | Leading indicator | Real-time availability: 47 open slots vs 80 target. Nearest slot date. Delta from yesterday (-12). 14d/30d toggle. |
| Center | 2fr | Core pipeline | Funnel: 300 inquiries → 83.3% conversion → 250 scheduled → 88% attendance → 220 completed. Each stage has a progress bar with target line. Connector pills between stages show conversion/attendance rates. |
| Right | 1fr | Retrospective | Wait times: CM avg 62h (target 48h), Psych avg 19d (target 14d). Sparkline trend chart. 7d/30d toggle. |

### Layer 2 — Attendance Drill-Down (Drawer)

Triggered by clicking: attendance KPI tile, funnel connector pill, or completed-appointments step.

**Contents:**
1. **Breakdown by appointment type** (target 85% each):
   - Intake: 48/60 = 80% (below target — yellow)
   - Follow-up CM: 23/25 = 92% (above target — green)
   - Follow-up Psychiatrist: 14/15 = 93% (above target — green)

2. **No-show reason categorization:**
   - No-show: 8
   - Patient cancellation: 10
   - Clinic cancellation: 2
   - Rescheduled: 5

3. **Insight:** Most non-attendance comes from intake no-shows. Recommended action: strengthen reminder/double-confirmation the day before.

### Planned Layer 2 Extensions (Not Yet Built)

- Availability panel: Breakdown by CM/Psychiatrist and by appointment type
- Wait Times panel: Median/tail distribution split and per-provider breakdown

## Demo Data

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Inquiries (questionnaires) | 300 | — | Baseline |
| Intake Conversion | 83.3% | 80% | Green |
| Scheduled appointments | 250 | — | Derived |
| Attendance rate | 88.0% | 85% | Green |
| Completed appointments | 220 | — | Derived |
| Available slots (14d) | 47 | 80/month | Yellow |
| Nearest available slot | 14/01 | — | — |
| Slot delta vs yesterday | -12 | — | Red |
| Wait time CM (avg) | 62h | 48h | Red |
| Wait time Psych (avg) | 19d | 14d | Red |
| NPS | 42 | — | Yellow |

## Technical Implementation

- **Stack:** Pure HTML/CSS/JS — no framework dependencies
- **RTL:** `lang="he" dir="rtl"` with CSS grid layout
- **Theme:** Dark glass-morphism (#070d1a), consistent with Variant B aesthetic
- **Grid:** `grid-template-columns: 1fr 2fr 1fr` — responsive to single-column below 1100px
- **Drawer:** CSS transform slide-in with overlay, ESC-to-close, click-outside-to-close
- **Interaction model:** Multiple entry points to same drill-down (KPI tile, connector pill, funnel step)

## Comparison With Variant B

| Aspect | Variant B (KPI Cards) | Flow Dashboard |
|--------|----------------------|----------------|
| Layout | 2x2 card grid | 3-panel with central funnel |
| Mental model | Four independent metrics | Single patient flow pipeline |
| Drill-down | None | Layer 2 drawer (attendance) |
| Time context | Tab toggles per card | Tab toggles per panel |
| Availability | Standalone card | Dedicated left panel |
| Wait times | Standalone card | Dedicated right panel with sparkline |
| Funnel visualization | None | Central element |
| No-show analysis | None | Categorized in Layer 2 |

## Design Insights

1. **Intake is the weak link:** At 80% attendance, intake appointments are the only appointment type below the 85% threshold. Follow-up appointments (CM 92%, Psych 93%) are performing well.
2. **No-shows drive non-attendance more than cancellations:** 8 no-shows + 10 patient cancellations vs only 2 clinic cancellations suggests the problem is patient-side, not operational.
3. **Availability is the canary:** At 47 slots vs 80 target with a -12 daily delta, the availability panel serves as an early warning that wait times will likely worsen.
4. **Wait times exceed targets:** CM at 62h vs 48h target and Psych at 19d vs 14d target indicate capacity pressure.

## Related
![[related.base#All]]