---
alfred_tags:
- healthcare/clinic-dashboard
- ui/flow-design
created: '2026-02-25'
description: Design analysis of the Clinic Israel Flow Dashboard (v4), documenting
  the three-panel funnel architecture, Layer 2 attendance drawer pattern, and evolution
  from KPI-card layout to flow-centric operations visibility.
janitor_note: LINK001 — Telia'z wikilinks (project, org) are valid (YAML escaping
  false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist — embed preserved per policy.
name: Clinic Israel Flow Dashboard Design
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[asset/Clinic Israel Executive Dashboard]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[note/Clinic Executive Dashboard Variant B Design]]'
- '[[note/Clinic Israel KPI Dashboard January 2026]]'
- '[[org/Telia''z]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
relationships:
- confidence: 0.85
  context: Israel design based on general flow
  source: note/Clinic Israel Flow Dashboard Design.md
  target: note/Clinic Flow Dashboard Design.md
  type: depends-on
- confidence: 0.7
  context: Shared clinic flow dashboard theme
  source: note/Clinic Israel Flow Dashboard Design.md
  target: note/Clinic Flow Dashboard v4 Design Analysis.md
  type: related-to
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Israel Flow Dashboard — Design Analysis

## Overview

This is the fourth iteration of the Clinic Israel executive operations dashboard. It represents a fundamental shift in information architecture: moving from a symmetric KPI-card grid (v3) to a flow-centric funnel view with layered drill-down. The design treats the new-patient journey as the primary narrative, with supporting metrics arranged around it.

## Design Philosophy

The v3 dashboard treated all four KPIs as equal peers in a grid. The v4 Flow Dashboard instead tells a story: inquiries arrive (left), flow through a funnel (center), and the time dimension is shown on the right. This spatial arrangement mirrors the patient journey and makes bottlenecks visually obvious.

## Three-Panel Layout

### Left Panel: Availability (Real-Time)
- **Big number:** 47 open slots (14-day window)
- **Monthly target:** 80 slots
- **Progress bar:** 59% fill (yellow — below target)
- **Mini cards:** Nearest appointment date (14/01), delta from yesterday (-12)
- **Interpretation:** Leading indicator. When slots drop, wait times will rise. The -12 delta is an operational warning.

### Center Panel: New Patient Flow (Funnel)
- **Step 1 — Inquiries (questionnaires):** 300
- **Connector — Conversion:** 83.3% (target 80%, green)
- **Step 2 — Scheduled appointments:** 250
- **Connector — Attendance:** 88.0% (target 85%, green, clickable)
- **Step 3 — Completed sessions:** 220 (clickable)
- **Progress bars:** Each step shows absolute volume as bar fill with target markers
- **Key insight:** The funnel shows 300 → 250 → 220, meaning 80 patients (26.7%) are lost between inquiry and completed session. Of the 80 lost: 50 failed to convert to scheduling, 30 were no-shows/cancellations.

### Right Panel: Wait Times (Retrospective)
- **Case Manager:** 62 hours average (target 48h, red — exceeds target)
- **Psychiatrist:** 19 days average (target 14d, red — exceeds target)
- **Trend sparkline:** Downward trend line with target reference
- **Interpretation:** Both wait time metrics exceed targets. The CM wait (62h vs 48h target) and psychiatrist wait (19d vs 14d target) confirm the constraint already captured: rising wait times.

## Layer 2: Attendance Drill-Down Drawer

The most significant new feature is the **slide-out drawer** pattern for Layer 2 detail. Three entry points trigger it:
1. Clicking the Attendance KPI tile in the top strip
2. Clicking the Attendance connector pill in the funnel
3. Clicking the Completed Sessions step

### Drawer Content

**By Appointment Type (target 85%):**
| Type | Attended | Total | Rate | Status |
|------|----------|-------|------|--------|
| Intake | 48 | 60 | 80% | Below target (yellow) |
| Follow-up CM | 23 | 25 | 92% | Above target (green) |
| Follow-up Psychiatrist | 14 | 15 | 93% | Above target (green) |

**No-Show Reasons:**
- No-show (unannounced): 8
- Patient cancellation: 10
- Clinic cancellation: 2
- Rescheduled: 5

**Key Finding:** Intake appointments have the lowest attendance rate (80%), while follow-ups are strong (92-93%). This is consistent with the general pattern that first-time patients are more likely to not show. The dashboard recommends double-confirmation reminders before intake sessions.

## Technical Implementation

- **Drawer pattern:** CSS overlay + translateX animation, ESC-to-close, click-outside-to-close
- **Responsive:** Below 1100px, switches to single-column layout and drawer expands to 92vw
- **Same tech stack as v3:** Pure HTML/CSS/JS, no frameworks, CSS custom properties for theming
- **Theme:** Dark glass-morphism consistent with previous iterations

## Operational Implications

1. **Intake no-show is the primary attendance bottleneck** — the 80% intake rate pulls the overall 88% down. Targeted intervention (SMS/call confirmation) could improve this significantly.
2. **Wait times remain above target** — both CM (62h vs 48h) and psychiatrist (19d vs 14d) are red. This reinforces the rising wait time constraint from the January 2026 data.
3. **Slot availability critically low** — 47 of 80 target slots (59%) with a -12 daily delta indicates accelerating capacity pressure.
4. **End-to-end conversion is 73.3%** (220/300) — meaning roughly 1 in 4 inquiries does not result in a completed session.

## Evolution Path

The design includes placeholder text for future Layer 2 panels:
- **Availability Layer 2:** CM/Psych breakdown + appointment type split
- **Wait Times Layer 2:** Median/tail distribution + per-provider breakdown
- **Flow Layer 2:** Intake vs follow-up breakdown within completed sessions + detailed no-show reasons

## Related
![[related.base#All]]