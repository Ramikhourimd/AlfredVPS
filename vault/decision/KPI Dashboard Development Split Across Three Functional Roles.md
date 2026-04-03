---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, learn-decision.base#Related) reference
  _bases/learn-decision.base which may not exist yet — vault-wide infrastructure gap,
  not a per-file issue.
name: KPI Dashboard Development Split Across Three Functional Roles
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[person/Roy Shur]]'
- '[[person/Rivi Idelman]]'
session: null
source: Rami Khouri — assigned roles during product sync
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# KPI Dashboard Development Split Across Three Functional Roles

## Context

The clinic needs operational KPI dashboards. Rami had previously built a prototype financial dashboard for Basel, but a proper production dashboard requires coordinated effort across data definition, database engineering, and UX design.

## Options Considered

1. **Single owner builds end-to-end** — One person handles KPI definition, DB views, and frontend
2. **Three-role split** — Separate KPI definition, database engineering, and UX design responsibilities
3. **External vendor/contractor** — Outsource dashboard development entirely

## Decision

Split KPI dashboard development across three roles:
- **Roy Shur** — Define KPIs, map them to database metrics, identify data gaps
- **Shmulik** — Create necessary database views when KPI spec is ready
- **Rivi Idelman** — Design frontend UX based on Roy's KPI definitions (not Rami's prototype)

## Rationale

Each role maps to a distinct competency. Roy understands the operational metrics, Shmulik controls database access and view creation, and Rivi brings proper UX design skills. Rami's earlier prototype was a proof-of-concept only — production quality requires dedicated UX work.

## Consequences

- Sequential dependency: Roy must finish KPI spec before Shmulik can create views, and both must be ready before Rivi designs the frontend
- Rami's prototype dashboard documents serve as starting reference material for Rivi
- Basel's financial dashboard is considered closed and is not part of this effort

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
