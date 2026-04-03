---
approved_by: []
based_on:
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist. ACTION REQUIRED: Body has DUPLICATE base view embeds after
  horizontal rule (---) at end of file — remove the second set of \![[learn-decision.base#Based
  On]] and \![[learn-decision.base#Related]] plus the --- separator. Cannot fix via
  CLI (no body-replace command).'
name: Adopt Forward Trend Retro Temporal Dashboard Architecture
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[asset/Clinic Israel Flow Dashboard]]'
- '[[asset/Clinic Executive Dashboard Variant B]]'
- '[[note/Clinic Israel Operational Dashboard Layer 1 Design]]'
- '[[org/Telia''z]]'
session: null
source: Dashboard prototype evolution v4 to v5
source_date: '2026-02-25'
status: final
supports:
- '[[asset/Clinic Israel Operational Dashboard Layer 1]]'
tags: []
type: decision
---

# Adopt Forward Trend Retro Temporal Dashboard Architecture

## Context

After four iterations of the Clinic Israel executive dashboard (KPI cards, glass-morphism, generalized, flow-funnel), a recurring UX problem remained: mixing leading indicators (future availability) with lagging indicators (past wait times) in the same view confused operators into false confidence — "wait times look fine" while future capacity was depleting.

## Options Considered

1. **Option A: Enhanced flow-funnel (v4+)** — Keep the three-panel funnel design, add temporal annotations. Less disruptive but doesn't solve the fundamental confusion.
2. **Option B: Forward/Trend/Retro temporal separation** — Reorganize the entire dashboard by time direction: top section for forward-looking metrics, middle for trends, bottom for retrospective metrics.

## Decision

Adopt Option B — full temporal separation into Forward (On-Calendar), Trend (time-series bridge), and Retro (hindsight) sections.

## Rationale

- **Eliminates leading/lagging confusion:** Forward metrics (slots, earliest appointment) are physically separated from retro metrics (conversion, attendance, wait times). Users process one temporal direction at a time.
- **Enables predictive alerting:** The core operational insight — "declining Forward slots predict future Retro degradation" — is made explicit by the layout itself.
- **Supports layered drill-down:** Layer 1 provides the executive overview; Layers 2+ can drill into per-provider, per-pod, and per-type detail within the same temporal framework.
- **Independent time windows:** Forward (14d/30d) and Retro (7/30/90d) have separate time window controls, allowing operators to zoom into different horizons independently.
- **Trend section bridges both views:** Charts showing daily Forward slot trends alongside Retro flow trends let operators correlate capacity changes with demand patterns.

## Consequences

- Dashboard tile count increases from 4 (v3) to 6 plus 2 charts
- More screen real estate needed — single-scroll vertical layout instead of grid
- Interactive controls multiply (forward window, retro window, MA toggle, wait mode toggle)
- API integration will need separate forward and retro data endpoints
- Previous flow-funnel design (v4) is superseded for the primary operational view

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
