---
alfred_tags:
- healthcare/clinic-dashboard
- ui/flow-design
created: '2026-02-25'
description: Comprehensive design analysis of the Flow Dashboard v4 prototype for
  Clinic Israel, covering the three-column panel architecture, patient flow funnel,
  Layer 2 attendance drill-down, and planned future drill-downs.
janitor_note: '"LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  \![[related.base#All]] embed requires _bases/ infrastructure setup — not a content
  issue."'
name: Clinic Flow Dashboard v4 Design Analysis
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Flow Dashboard v4]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[org/Telia''z]]'
- '[[note/Clinic Israel Executive Dashboard KPI Analysis]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
relationships:
- confidence: 0.7
  context: v4 analysis relates to Israel design
  source: note/Clinic Flow Dashboard v4 Design Analysis.md
  target: note/Clinic Israel Flow Dashboard Design.md
  type: related-to
- confidence: 0.9
  context: v4 analysis depends on base design
  source: note/Clinic Flow Dashboard v4 Design Analysis.md
  target: note/Clinic Flow Dashboard Design.md
  type: depends-on
session: null
status: active
subtype: reference
tags: []
type: note
---

# Clinic Flow Dashboard v4 Design Analysis

## Context

Dashboard v4 represents a significant architectural shift from the previous KPI card grid (Variant B / dashboard3.html) to a **flow-oriented layout** that tells the story of patient acquisition and retention. Instead of four independent KPI cards, the dashboard now organizes metrics into three functional panels that reflect the operational pipeline: capacity → patient flow → retrospective performance.

This is the first iteration to include a working **Layer 2 drill-down** (attendance breakdown), establishing the interaction pattern for future drill-downs across all panels.

## Architectural Evolution

### From Cards to Flow

The v3 dashboard presented four KPIs as equal-weight cards in a 2-column grid. While effective for at-a-glance status, it didn't reveal the **causal relationships** between metrics. v4 restructures the layout into three columns that tell a story:

1. **Left panel — Availability (leading indicator):** How much capacity do we have? 47 open slots against a target of 80. This is the input side of the pipeline.
2. **Center panel — Patient Flow (operational pipeline):** The funnel from 300 inquiries → 250 scheduled → 220 completed. This is where conversion and attendance interact. The funnel makes drop-off points visible.
3. **Right panel — Wait Times (lagging indicator):** How long are patients waiting? CM average 62h (target 48h), Psychiatrist average 19d (target 14d). This is the output quality metric.

Reading left-to-right: **capacity → flow → outcome**. A manager can see at a glance where the bottleneck is.

### Layer 2: The Drill-Down Pattern

v4 introduces the Layer 2 interaction model: clicking on a KPI or funnel element opens a **slide-in drawer** from the left with detailed breakdown data. The first implementation is for **Attendance**:

- **Entry points:** Attendance KPI tile, funnel connector pill, or completed-appointments step — all trigger the same drawer
- **Content:** Per-appointment-type breakdown (Intake at 80%, Follow-up CM at 92%, Follow-up Psychiatrist at 93%), no-show reason chips, and an insight callout
- **UX:** Overlay with backdrop blur, ESC to close, click-outside to close

This establishes the pattern for future Layer 2 panels noted in the prototype:
- Availability → CM/Psychiatrist slot split + appointment type breakdown
- Wait Times → Median vs tail distribution + per-provider analysis
- Funnel → Intake vs follow-up split at each stage

## Key Insights from Demo Data

### Intake Is the Weak Link

The attendance drill-down reveals that **intake appointments are the primary source of non-attendance** (80% rate, below the 85% target), while follow-up appointments perform well (92-93%). This suggests the problem is not patient retention but **initial engagement** — patients who have never been seen are more likely to not show up.

The dashboard's insight correctly recommends strengthening pre-appointment reminders and adding double-confirmation the day before intake sessions.

### Wait Times Remain Elevated

Both CM wait time (62h vs 48h target) and psychiatrist wait time (19d vs 14d target) are above target. Combined with the availability panel showing only 47 of 80 target slots available, this paints a picture of **capacity pressure** — the clinic needs more scheduling headroom.

### Funnel Math

- 300 inquiries → 250 scheduled = 83.3% conversion (above 80% target)
- 250 scheduled → 220 completed = 88.0% attendance (above 85% threshold)
- 300 inquiries → 220 completed = 73.3% end-to-end yield

The 26.7% end-to-end loss breaks down as: 16.7% at scheduling conversion + 12% at attendance. Both stages contribute meaningfully to patient loss.

## Design and UX Observations

### Strengths
- **Narrative layout:** The three-column design tells a story rather than just presenting numbers
- **Multiple drill-down entry points:** Users can click the KPI tile, the funnel connector, or the funnel step — all lead to the same detail. This accommodates different user mental models.
- **Progressive disclosure:** Layer 1 is clean and scannable; Layer 2 adds depth without cluttering the overview
- **Consistent visual language:** Target markers (white lines), color coding (green/yellow/red), glass morphism theme carried over from v3

### Areas for Future Development
- **Remaining Layer 2 drawers:** Availability and Wait Times panels have placeholder text but no working drill-downs yet
- **Time window interaction:** Tab buttons (7/14/30 day) are visual only — not wired to switch data
- **Data integration:** All data is hardcoded; requires API connection for production use
- **NPS chip:** Still shows static "NPS: 42" in header — relationship to rest of dashboard unclear

## Relationship to Existing Dashboard Assets

| Asset | Status | Relationship to v4 |
|-------|--------|-------------------|
| Clinic Israel Executive Dashboard | Retired | Original dashboard, superseded |
| Clinic Israel Executive Dashboard Variant B | Active | Design exploration, KPI card layout |
| Clinic Executive Dashboard | Active | Generalized version of the dashboard concept |
| Clinic Executive Dashboard Variant B | Active | Direct predecessor (dashboard3.html) — v4 replaces this layout |
| **Clinic Flow Dashboard v4** | **Active** | **Current iteration** |

## Related
![[related.base#All]]