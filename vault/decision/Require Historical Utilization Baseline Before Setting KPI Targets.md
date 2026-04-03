---
approved_by: []
based_on:
- '[[task/Calculate Historical Clinic Utilization Baseline]]'
- '[[conversation/Clinic Manager KPIs and Bonus Structure Meeting 2025-03-27]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Alex Taliaz]]'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist. ORPHAN001 — no inbound wikilinks from other records.'
name: Require Historical Utilization Baseline Before Setting KPI Targets
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Measure Clinic Efficiency by Monetary Utilization Gap]]'
session: null
source: Alex Taliaz
source_date: '2025-03-27'
status: final
supports:
- '[[decision/Measure Clinic Efficiency by Monetary Utilization Gap]]'
- '[[decision/Quarterly KPI-Based Bonus for Clinic Manager]]'
- '[[decision/Clinical Compensation Target 35 to 50 Percent of Revenue]]'
tags: []
type: decision
---

# Require Historical Utilization Baseline Before Setting KPI Targets

## Context

During the 2025-03-27 management meeting on clinic manager KPIs and bonus structure, the team needed to set specific quarterly targets for Shira's performance evaluation. Rami had per-clinician utilization spreadsheets available, but no aggregated historical baseline.

## Options Considered

1. **Set targets based on industry benchmarks** — Use external telepsychiatry utilization data as reference
2. **Set targets based on historical clinic data** — Calculate what the utilization percentage has actually been over the past year, then set targets relative to that baseline
3. **Set targets based on leadership judgment** — Pick round-number targets without data backing

## Decision

Alex Taliaz explicitly required that historical utilization data be calculated first before any specific KPI targets are set. His exact direction: "let's first calculate what this percentage has been historically in the last year, so we have a reference."

## Rationale

Setting targets without knowing the baseline risks either:
- Targets too aggressive (demoralizing, perceived as unfair)
- Targets too lenient (no improvement incentive, wasted bonus budget)

Historical data provides a defensible foundation for target-setting and makes quarterly progress measurable against a real starting point rather than an arbitrary number.

## Consequences

- The bonus structure for Shira's clinic manager role cannot be finalized until the historical baseline is calculated
- Rami needs to aggregate existing per-clinician utilization spreadsheets into a clinic-level monthly time series (past 12 months)
- Once calculated, the baseline range will anchor the 35-50% clinical compensation target from the separate compensation decision

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
