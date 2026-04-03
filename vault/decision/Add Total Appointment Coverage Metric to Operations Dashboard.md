---
approved_by: []
based_on:
- '[[task/Add Total Appointments Metric to Operations Dashboard]]'
- '[[assumption/Same-Month Intake Conversion Rate Understates Actual Patient Service
  Coverage]]'
challenged_by: []
confidence: medium
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z project link valid (YAML escaping false positive).
  based_on link to assumption/Same-Month Intake Conversion Rate verified — target
  exists, scanner false positive from YAML line wrapping. Body has duplicate base
  view embeds (two sets of learn-decision.base#Based On and #Related after --- separator)
  — human must remove the duplicate set. Base view embeds reference _bases/learn-decision.base
  which does not exist. ORPHAN001 — no inbound wikilinks.'
name: Add Total Appointment Coverage Metric to Operations Dashboard
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
- '[[constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February 2026]]'
session: ''
source: Adiel Levin observation during team meeting
source_date: '2026-02-15'
status: draft
supports:
- '[[decision/Adopt Forward Trend Retro Temporal Dashboard Architecture]]'
tags:
- dashboard
- metrics
- capacity
type: decision
---

# Add Total Appointment Coverage Metric to Operations Dashboard

## Context

The current operations dashboard shows same-month intake conversion rate (8.1% in February 2026) — the percentage of patients who register and receive an intake appointment within the same calendar month. During the 2026-02-15 team meeting, Adiel Levin identified a critical gap: the dashboard does not show how many patients have appointments in future months, making the 92% "unserved" figure potentially misleading.

## Options Considered

1. **Keep same-month metric only** — Simpler, but perpetuates a potentially misleading narrative about patient access
2. **Add total coverage metric alongside same-month** — Shows both immediate conversion and eventual coverage, giving a complete picture

## Decision

Add a total appointment coverage metric showing: (a) total patients with any appointment (current or future months) vs. (b) total patients with no appointment at all. This runs alongside the existing same-month conversion metric, not replacing it.

## Rationale

The same-month metric is useful for measuring operational responsiveness but may significantly overstate the unserved patient population. Leadership decisions about hiring urgency, discharge protocols, and capacity investment need the complete picture. Without this metric, the team cannot distinguish between "patients waiting for a future appointment" and "patients truly falling through the cracks."

## Consequences

Once implemented, the narrative around capacity crisis may shift. If total coverage is significantly higher than 8%, it reframes the problem from "catastrophic access failure" to "scheduling latency issue." This could affect the urgency assigned to hiring, discharge protocols, and restructuring decisions.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
