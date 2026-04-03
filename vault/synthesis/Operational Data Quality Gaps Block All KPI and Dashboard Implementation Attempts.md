---
alfred_tags:
- compensation/discrepancies
- payroll/fragmentation
- operations/data-quality
cluster_sources:
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[note/Telia''z Strategic Goals and Clinical Sustainability Meeting 2025-12-04]]'
- '[[note/Clinic Protocol Framework and Scaling Strategy 2025-12-04]]'
- '[[note/Clinic Features Protocols and KPIs Brainstorm 2025-12-04]]'
- '[[task/Prepare Protocol Framework Document for Board]]'
confidence: high
created: '2026-02-26'
janitor_note: 'LINK001: Telia''z wikilinks are YAML escaping false positives (targets
  exist). Contradiction and decision links verified as valid — scanner false positives.
  Base view embeds (learn-synthesis.base#Sources, #Related) reference _bases/learn-synthesis.base
  which does not exist yet — preserve per policy. ORPHAN001: No inbound links — human
  review needed.'
name: Operational Data Quality Gaps Block All KPI and Dashboard Implementation Attempts
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[synthesis/Payroll Data Fragmentation Undermines Operational Transition]]'
- '[[synthesis/Compensation Data Discrepancies Are Systemic Across All Staff Tiers]]'
- '[[contradiction/Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical
  Norms]]'
relationships:
- confidence: 0.88
  context: Payroll fragmentation as op data quality gap
  source: synthesis/Operational Data Quality Gaps Block All KPI and Dashboard Implementation
    Attempts.md
  target: synthesis/Payroll Data Fragmentation Undermines Operational Transition.md
  type: related-to
status: draft
supports:
- '[[decision/Centralize Psychiatrist Payment Processing Into Standardized Unified
  Format]]'
- '[[decision/Standardize Payment Data to Binary Attendance Classification]]'
tags: []
type: synthesis
---

# Operational Data Quality Gaps Block All KPI and Dashboard Implementation Attempts

## Insight

Every attempt to implement meaningful operational metrics at Telia'z Clinic Israel is blocked by the same prerequisite: the underlying data must first be cleaned, standardized, and validated. The protocol framework brainstorm identified KPIs the clinic needs to track. The strategic goals meeting projected patient growth and staffing needs. The dashboard initiative requires reliable attendance, wait time, and throughput data. Yet in each case, the team discovered that the raw data is inconsistent, fragmented, or formatted differently per source — requiring manual cleanup before any analysis can begin.

## Evidence

1. **Payment data** (2025-12-04): Psychiatrist payment spreadsheets arrived in inconsistent Excel formats. Basel spent the session cleaning columns, standardizing status values, and fixing formulas before any compensation analysis could happen.
2. **Staff rate data** (2025-12-04): Administrative staff rates showed discrepancies between agreements and actuals. Some staff submitted individual Excel files; others were tracked in a master spreadsheet. No unified source of truth existed.
3. **Session-to-patient ratios** (2025-12-04 strategic meeting): Psychiatrist ratios exceeded >1.0 sessions per patient per month — flagged as anomalous. The team couldn't determine if this was a real clinical pattern or a calculation artifact from how "active patients" are defined in the system.
4. **Protocol framework** (2025-12-04 brainstorm): Rami identified that "the important things we are not tracking" — but before tracking them, the existing data infrastructure needs standardization.

## Implications

The clinic cannot implement the dashboard, KPI system, or protocol framework until data infrastructure is addressed. This creates a sequencing constraint: data standardization must precede KPI definition, which must precede dashboard development, which must precede evidence-based board presentations. Skipping data cleanup produces misleading metrics that could drive wrong decisions.

## Applicability

Applies across all clinic operational domains: clinical outcomes tracking, financial reporting, staffing analytics, and patient flow metrics. Any future data system or automation project must account for the current data quality baseline.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]