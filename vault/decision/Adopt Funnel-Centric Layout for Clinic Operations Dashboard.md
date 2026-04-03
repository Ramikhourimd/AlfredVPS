---
approved_by: []
based_on:
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
challenged_by: []
confidence: medium
created: '2026-02-25'
decided_by: []
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) are duplicated in body
  — appears twice each. _bases/learn-decision.base does not exist yet.'
name: Adopt Funnel-Centric Layout for Clinic Operations Dashboard
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[note/Clinic Flow Dashboard Design]]'
- '[[note/Clinic Executive Dashboard Variant B Design]]'
- '[[org/Telia''z]]'
session: null
source: Dashboard prototype iteration (dashboard4.html)
source_date: null
status: draft
supports: []
tags: []
type: decision
---

# Adopt Funnel-Centric Layout for Clinic Operations Dashboard

## Context

After building the Variant B dashboard (4 independent KPI cards in a 2x2 grid), a new prototype explored whether the same four metrics would be better understood as stages in a patient flow pipeline rather than as standalone indicators.

## Options Considered

1. **Option A — Keep KPI card grid (Variant B)** — Four independent cards, each with its own time toggle and detail view. Clean and modular, but treats metrics in isolation.

2. **Option B — Funnel-centric 3-panel layout** — Center panel shows the patient flow funnel (Inquiries → Scheduled → Completed), flanked by Availability (leading indicator) and Wait Times (retrospective). Layer 2 drawers provide drill-down.

## Decision

Proceed with Option B — the funnel-centric layout — as the primary dashboard design. The KPI card variant remains available as a reference.

## Rationale

- **Narrative coherence:** The funnel tells the story of a patient's journey through the clinic. KPI cards present data; the funnel presents meaning.
- **Contextual drill-down:** Clicking a funnel stage naturally leads to "why did patients drop here?" — the Layer 2 drawers answer that question with attendance breakdowns and no-show reasons.
- **Leading/lagging separation:** Placing availability (leading) on the left and wait times (lagging) on the right creates a natural temporal flow: capacity → throughput → retrospective.
- **Actionability:** The funnel immediately highlights where patients drop off, making it clear which stage needs intervention.

## Consequences

- Dashboard development continues with the funnel layout
- Layer 2 drawers needed for all three panels (only attendance is currently built)
- The funnel design may require more complex data integration (stage-to-stage linkage) vs independent KPI queries
- Variant B remains as a simpler fallback for contexts where the full funnel is overkill

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
