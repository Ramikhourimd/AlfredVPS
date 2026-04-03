---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — learn-decision.base embeds reference missing _bases/learn-decision.base
  (vault infrastructure gap, embeds preserved). Telia''z wikilinks are valid (YAML
  escaping). ACTION NEEDED: Remove duplicate base embed block at end of file (second
  set of Based On/Related after --- separator).'
name: Implement Read-Only Shadow DB for Analytics
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[project/Telia''z Clinic Israel]]'
session: null
source: Product meeting architecture recommendation
source_date: '2026-02-25'
status: draft
supports: []
tags: []
type: decision
---

# Implement Read-Only Shadow DB for Analytics

## Context

Large analytical queries against the production database risk performance degradation during peak clinical hours. Monthly report pulls, research data extractions, and ad-hoc analytics all compete with real-time clinical operations.

## Options Considered

1. **Option A** — Query production DB directly with time-window scheduling
2. **Option B** — Create a Read-Only/Shadow DB replica synchronized from production

## Decision

Option B: Establish a Read-Only/Shadow DB layer specifically for non-real-time analytical queries. Production DB handles only clinical operations.

## Rationale

Separating read workloads protects clinical operations from analytics-induced slowdowns. The shadow DB supports pagination, complex joins, and large extractions without risking production stability. Scheduling becomes less critical when queries run against the replica.

## Consequences

- Requires DBA/Architecture team to set up replication and sync monitoring
- Data freshness depends on sync frequency (near-real-time vs daily)
- All reporting and research APIs should target the shadow DB
- BigQuery/DWH integration for pricing data remains separate

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
