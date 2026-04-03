---
approved_by: []
based_on:
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
challenged_by: []
confidence: medium
created: '2026-02-25'
decided_by: []
janitor_note: 'LINK001: Telia''z and org/Telia''z wikilinks are valid (YAML escaping
  false positive). Base view embeds (learn-decision.base#Based On, learn-decision.base#Related)
  reference _bases/ which does not exist (vault-wide infrastructure gap). Embeds preserved.
  Duplicate base embed block removed.'
name: Adopt Flow Funnel Layout With Layer 2 Drill-Down Drawers
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[note/Clinic Flow Dashboard v4 Design Analysis]]'
- '[[org/Telia''z]]'
session: null
source: Dashboard v4 prototype (dashboard4.html)
source_date: null
status: draft
supports:
- '[[asset/Clinic Flow Dashboard v4]]'
tags: []
type: decision
---

# Adopt Flow Funnel Layout With Layer 2 Drill-Down Drawers

## Context

The Clinic Israel executive dashboard needed to evolve beyond flat KPI cards (Variant B) to show the causal relationship between metrics — how capacity feeds into patient flow which determines outcomes. Additionally, stakeholders needed the ability to drill into aggregate numbers without leaving the dashboard.

## Options Considered

1. **Option A — Enhanced KPI cards** — Keep the 2-column card grid but add expandable sections within each card. Lower development effort, but doesn't convey the pipeline narrative.
2. **Option B — Three-column flow layout with slide-in drawers** — Restructure into Availability / Flow Funnel / Wait Times panels with Layer 2 drill-down drawers for detailed breakdowns.

## Decision

Adopt Option B: three-column flow layout with slide-in drawer pattern for Layer 2 drill-downs. First Layer 2 implementation is the Attendance breakdown.

## Rationale

- The funnel visualization makes drop-off points between pipeline stages immediately visible, which flat KPI cards cannot convey
- The slide-in drawer pattern provides progressive disclosure — overview stays clean while detail is one click away
- Multiple entry points (KPI tile, connector pill, funnel step) accommodate different user mental models
- The pattern is extensible — same drawer mechanism can be reused for Availability and Wait Times drill-downs

## Consequences

- Dashboard layout is now structurally different from Variant B — not a simple evolution but a redesign
- Remaining Layer 2 drawers (Availability, Wait Times) need to be built following the same pattern
- Time window toggle interaction needs to be wired to actual data switching
- API integration required before production deployment

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]
