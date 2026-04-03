---
approved_by: []
based_on:
- '[[task/Add Total Appointments Metric to Operations Dashboard]]'
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — preserved, create base file to enable views. Body has DUPLICATE
  base view embeds (two sets of Based On + Related) — remove one set manually. ORPHAN001
  — no inbound wikilinks.'
name: Add Cross-Month Total Appointment Metric to Operations Dashboard
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Adopt Forward Trend Retro Temporal Dashboard Architecture]]'
- '[[constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February 2026]]'
- '[[assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10 Percent]]'
session: null
source: Adiel Levin during team meeting
source_date: '2026-02-15'
status: draft
supports: []
tags: []
type: decision
---

# Add Cross-Month Total Appointment Metric to Operations Dashboard

## Context

The operations dashboard currently shows same-month conversion rate (8.1% in February 2026), meaning only 8% of new patients who register in a given month receive an intake appointment that same month. Adiel Levin identified that this metric is misleading because it does not account for patients who have appointments scheduled in future months.

## Options Considered

1. **Add cross-month total** — Show total patients with any appointment (current or future month) alongside the same-month conversion rate
2. **Replace same-month metric** — Show only the cumulative appointment rate
3. **Keep current metric only** — Continue showing only same-month conversion

## Decision

Add a new metric showing total patients who have any appointment scheduled (including future months) versus patients with no appointment at all. This runs alongside the existing same-month conversion metric.

## Rationale

The 92% "no appointment" figure is alarming but potentially overstates the problem. Many patients registered in February may have March or April appointments. Without showing the cross-month picture, the dashboard creates a narrative of near-total capacity failure when reality may be more nuanced. The metric is needed for accurate operational assessment and leadership reporting.

## Consequences

- Requires querying future appointment data, not just current-month
- Changes the operational narrative from "92% failure" to a more accurate funnel view
- May reveal that the true unserved rate is lower (or confirm it is as bad as it appears)
- Complements the existing Forward Trend Retro temporal architecture

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
