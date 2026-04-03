---
alfred_tags:
- compensation/discrepancies
- payroll/fragmentation
- operations/data-quality
cluster_sources:
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[note/Staff Rate Review and Work Hour Audit 2025-12-04]]'
- '[[note/Clinic Office Operations Fragment iPad Agreements and Credit Card 2025-12-04]]'
confidence: high
created: '2026-02-26'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-synthesis.base#Sources, learn-synthesis.base#Related) reference
  _bases/learn-synthesis.base which does not exist — do not remove embeds, create
  base file to enable dynamic views.
name: Payroll Data Fragmentation Undermines Operational Transition
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[contradiction/Staff Compensation Rates Diverge From Signed Agreement Terms]]'
- '[[constraint/Inconsistent Excel Formats Across Psychiatrist Payment Reports]]'
- '[[synthesis/Li Yamin Administrative Role Creates Net Workload Increase]]'
relationships:
- confidence: 0.8
  context: Payroll frag contributes to op data gaps
  source: synthesis/Payroll Data Fragmentation Undermines Operational Transition.md
  target: synthesis/Operational Data Quality Gaps Block All KPI and Dashboard Implementation
    Attempts.md
  type: supports
status: draft
supports:
- '[[decision/Unify Staff Employment Agreements Across All Clinicians]]'
type: synthesis
---

# Payroll Data Fragmentation Undermines Operational Transition

## Insight

Across four separate December 2025 operational sessions, a consistent pattern emerges: the clinic's payroll and compensation data is fragmented, inconsistent, and unreliable to a degree that actively blocks Basel Kanaaneh's ability to establish operational control. Each psychiatrist's payment spreadsheet uses different formats. Staff agreements don't match actual payment rates. Some staff members are missing Excel files entirely. Rate tiers are unclear — the same person may show different rates in their agreement versus the spreadsheet. This is not a minor data quality issue; it is a structural impediment to the operational transition that the clinic's restructuring depends on.

## Evidence

1. **Psychiatrist payment data** (2025-12-04): Basel had to manually clean spreadsheets column by column — removing duplicates, standardizing status fields, adding derived classifications. The raw data was unusable for payment calculations without significant manual intervention.
2. **Administrative staff rates** (2025-12-04): Lori/Ori shows 100 NIS/hour in Excel but agreement says base 1,350 with additions to 1,650 and a 6,000 component. A 9,000 NIS line item breaks down to 6,300 real + 2,700 overage. Sarah has no Excel file at all.
3. **Staff rate review** (2025-12-04): Multiple staff members show rates that don't align with their tier or agreement. Rami chose to "carry" overpaid staff rather than reduce rates, creating intentional divergence between agreements and actual pay.
4. **Four new agreements** (2025-12-04): Referenced as needing processing within one month, adding to the backlog of unverified compensation data.

## Implications

Basel cannot build reliable operational dashboards, budget projections, or staffing models until the payroll data foundation is cleaned. The decision to unify staff agreements addresses the legal/contractual layer, but the underlying data infrastructure (spreadsheet formats, rate tracking, status standardization) requires a parallel cleanup effort. Every month of delay compounds the problem as new hires add more inconsistent records.

## Applicability

This pattern is specific to Telia'z Clinic Israel's operational transition but reflects a common scaling challenge: informal compensation practices that work for a small team become unmanageable as headcount grows toward the projected 44+ FTE positions.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]