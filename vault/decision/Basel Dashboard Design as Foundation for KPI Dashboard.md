---
approved_by: []
based_on:
- '[[task/Share Basel Dashboard Design Docs With Rivi]]'
challenged_by: []
confidence: medium
created: '2026-03-01'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: base view embeds (\![[learn-decision.base#...]]) reference
  _bases/ infrastructure files — vault-wide pattern, not a per-file issue. ORPHAN001:
  valid decision record, may gain inbound links as KPI dashboard project progresses.
  No fix needed.'
name: Basel Dashboard Design as Foundation for KPI Dashboard
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Rivi Idelman]]'
- '[[person/Basel Kanaaneh]]'
session: '[[conversation/Product Development Update Meeting 2026-02-12]]'
source: Rami Khouri during Product Development Update Meeting
source_date: '2026-02-12'
status: draft
supports:
- '[[decision/KPIs Are Primary Priority for Existing Retool System]]'
- '[[decision/KPI Dashboard Development Split Across Three Functional Roles]]'
tags: []
type: decision
---

# Basel Dashboard Design as Foundation for KPI Dashboard

## Context

The clinic needs operational KPI dashboards. Rami had previously built a prototype financial dashboard for Basel, producing three design documents (to-do list, implementation plan, tasks) using AI agents. Rivi was assigned to lead the broader KPI dashboard UX design.

## Options Considered

1. **Design KPI dashboard from scratch** — clean slate, potentially better architecture but slower
2. **Use Basel's financial dashboard design docs as starting template** — leverages existing work, faster iteration

## Decision

Rami chose to share the three Basel dashboard design documents with Rivi as the starting foundation for the broader KPI dashboard design. This reuses proven design patterns and AI-generated documentation rather than starting from zero.

## Rationale

The Basel dashboard was already built and validated. Its design documents capture structural decisions (layout, data presentation, task breakdown) that apply to other KPI domains. Starting from a working reference accelerates Rivi's design work.

## Consequences

- KPI dashboard design inherits Basel dashboard's structural patterns
- Rivi has concrete examples rather than abstract requirements to work from
- Risk: Basel's financial dashboard patterns may not suit all KPI domains (clinical, operational)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
