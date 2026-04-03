---
approved_by: []
based_on:
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — create base file. Duplicate base view embeds at bottom of
  body need manual cleanup. ORPHAN001 — no inbound wikilinks; consider linking from
  project/Telia''z AI Clinical Platform.'
name: KPIs Are Primary Priority for Existing Retool System
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
session: null
source: Rami Khouri, in Retool prioritization meeting with Shachar
source_date: '2025-12-05'
status: final
supports:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[task/Compile Retool Improvement Priority List]]'
tags: []
type: decision
---

# KPIs Are Primary Priority for Existing Retool System

## Context

Within the three-track improvement framework agreed with Shachar, Rami needed to identify the single most critical capability for Track 1 (critical fixes for H1 2026). Multiple candidates existed: KPI dashboards, Teams video integration, login fixes, and secretary workflow needs.

## Options Considered

1. **KPI dashboards** — Operational visibility into clinic performance metrics
2. **Teams video integration** — Fixing patient no-show issues (~10% revenue impact)
3. **Login/authentication fixes** — Resolving psychiatrist lockout issues
4. **Secretary workflow needs** — Admin and scheduling tool improvements

## Decision

KPI dashboards are the primary priority for the existing Retool system. While Teams integration and login fixes are also Track 1 items, KPIs were identified as the #1 need.

## Rationale

KPI dashboards provide operational visibility that drives all other improvement decisions. Without metrics on no-show rates, follow-up rates, and session utilization, it is difficult to prioritize or measure the impact of other fixes. Roy Shur is already working on defining KPIs and mapping them to database metrics.

## Consequences

- Roy Shur assigned to KPI definition and metric mapping
- Rivi Idelman assigned to design the frontend UX for the KPI dashboard
- Shmulik may need to create additional database views when the KPI spec is ready
- Some metrics require composite views joining multiple entities

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
