---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2025-03-27'
decided_by:
- '[[person/Alex Taliaz]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — All wikilinks are valid (YAML escaping false positive for
  apostrophes). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — vault-wide infrastructure gap.
  Duplicate base view embeds FIXED (removed second set).'
name: Measure Clinic Efficiency by Monetary Utilization Gap
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Manager KPIs and Bonus Structure Meeting 2025-03-27]]'
- '[[note/Clinic Manager KPI Framework and Bonus Structure 2025-03-27]]'
- '[[person/Shira]]'
session: null
source: Alex Taliaz during management meeting 2025-03-27
source_date: '2025-03-27'
status: final
supports:
- '[[decision/Quarterly KPI-Based Bonus for Clinic Manager]]'
tags:
- kpi
- utilization
type: decision
---

# Measure Clinic Efficiency by Monetary Utilization Gap

## Context

Rami tracked clinician utilization using percentage-based metrics (hours utilized vs available hours). The challenge was that percentage comparisons across clinicians with different pay rates and employment models (hourly vs available-hours) were misleading.

## Options Considered

1. **Percentage-based utilization** — Track utilization rate as a percentage per clinician. Simple but misleading: a clinician at 75% utilization costing 170 NIS/hr is less impactful than one at 90% costing 430 NIS/hr.
2. **Monetary gap measurement (NIS)** — For each clinician, calculate the difference between what was paid and what was used, in absolute NIS terms. Sum across all clinicians for a single bottom-line number.

## Decision

Adopt monetary gap measurement. For each clinician: calculate `(actual cost per hour worked - contractual rate) × hours`, then sum to get total NIS loss from underutilization. Set a target to minimize this aggregate number.

## Rationale

Monetary measurement automatically weights by cost — expensive underutilized clinicians surface as bigger problems. It also naturally handles mixed payment models (per-session vs per-available-hour) because the formula captures actual financial impact regardless of model. Alex noted this approach works well in the service industry.

## Consequences

- Shira can optimize at the individual clinician level using the per-person breakdown
- Built-in clinicians (paid only per session) contribute zero to the gap, simplifying tracking
- Historical baseline must be calculated before setting targets

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]
