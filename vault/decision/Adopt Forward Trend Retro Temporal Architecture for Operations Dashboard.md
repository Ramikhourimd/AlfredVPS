---
approved_by: []
based_on:
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[note/Clinic Israel Flow Dashboard Design]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base) reference _bases/ which does not exist —
  create it to enable dynamic views. Body contains duplicate base embed blocks.
name: Adopt Forward Trend Retro Temporal Architecture for Operations Dashboard
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[org/Telia''z]]'
- '[[note/Clinic Israel Operational Dashboard Layer 1 Design]]'
session: null
source: Dashboard iteration v4→v5 design review
source_date: '2026-02-25'
status: final
supports:
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
tags: []
type: decision
---

# Adopt Forward Trend Retro Temporal Architecture for Operations Dashboard

## Context

The v4 Flow Dashboard used a funnel-centric three-panel layout (Availability / Patient Flow / Wait Times) that mixed forward-looking and retrospective metrics in the same panels. This created confusion about whether a metric described the current situation, a prediction, or a historical measurement. The team needed a clearer conceptual framework that separated leading indicators from lagging indicators and made the relationship between them visible.

## Options Considered

1. **Option A — Enhanced funnel layout** — Keep v4 three-panel design, add time-direction labels to individual metrics. Lower redesign effort but doesn't solve the fundamental mixing problem.
2. **Option B — Forward/Trend/Retro temporal separation** — Reorganize all dashboard content by time direction: Forward (what's coming), Trend (how things are moving), Retro (what happened). Requires full redesign but creates clear conceptual model.

## Decision

Adopt Option B: restructure the entire dashboard around temporal direction. All metrics are categorized as Forward (future-looking), Trend (directional over time), or Retro (past measurement). The layout stacks three horizontal sections vertically.

## Rationale

- **Eliminates forward/retro confusion:** Previously, slot availability (forward) and wait times (retro) appeared in adjacent cards with no indication they measured different time directions. Now they live in clearly labeled sections.
- **Predictive insight becomes explicit:** The key operational insight — "if Forward slots are declining but Retro looks fine, you're heading for trouble" — is now visually obvious from the section arrangement.
- **Scalable to Layer 2:** Each of the 6 tiles in Forward and Retro sections can independently expand into Layer 2 drill-downs without disrupting the temporal framework.
- **Trend section bridges both views:** Placing trend charts between Forward and Retro creates a visual bridge that shows how the two time directions relate.

## Consequences

- All 6 tile panels reorganized: 3 Forward (Availability, Earliest Slot, Planned) + 3 Retro (Leads→Scheduled, Planned→Completed, Wait Times)
- New dual trend charts: Retro flows (3 lines) and Forward slots (2 lines)
- Interactive controls separated by time direction: Forward window (14d/30d), Retro window (7d/30d/90d)
- Wait times now include both median and average toggle
- Conversion target raised from 80% to 90% based on refined operational understanding
- Previous v4 Flow Dashboard retained as reference; v5 becomes the active prototype

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
