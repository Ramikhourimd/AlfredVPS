---
alfred_tags:
- payroll/processing
- staff/employment
authority: Organizational structure
created: '2026-02-26'
janitor_note: LINK001 — all Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference nonexistent _bases/learn-constraint.base — vault-wide infrastructure gap,
  embeds preserved. ORPHAN001 — no inbound links, consider linking from a parent record.
location: []
name: Payroll and Agreement Data Bottlenecked Through Single Administrator
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[task/Verify Psychiatrist Agreements Match Actual Payment Rates]]'
- '[[task/Verify Staff Agreements Against Actual Payments]]'
- '[[synthesis/Payroll Data Fragmentation Undermines Operational Transition]]'
source: Organizational structure — Shira as sole payroll data custodian
source_date: '2025-12-04'
status: active
type: constraint
---

# Payroll and Agreement Data Bottlenecked Through Single Administrator

## Constraint

All payroll spreadsheets, staff employment agreements, and fee schedule data flow through a single administrator (Shira). When Shira is unavailable (e.g., on vacation from Thursday through Tuesday as noted in the 2025-12-04 session), Basel and Rami cannot independently verify compensation data, process new agreements, or resolve rate discrepancies. This creates a single point of failure in the operational data chain.

## Source

Observed across multiple December 2025 operational sessions. Basel explicitly noted he would "kick the full salary data back to Shira for verification after vacation." Sarah's missing Excel file could not be resolved without Shira. Agreement scans and fee schedules were sent by Shira and could only be verified by cross-referencing her records.

## Implications

1. **Operational delays**: Any payroll verification or agreement processing stalls when Shira is unavailable
2. **Knowledge concentration risk**: If Shira were to leave the organization, critical institutional knowledge about rate histories, agreement variations, and payment logic would be lost
3. **Transition blocker**: Basel's operational takeover requires access to data that only Shira currently curates
4. **Audit vulnerability**: A single custodian means no independent verification path exists for compensation accuracy

## Expiry / Review

This constraint should be reviewed once Basel has full operational access to payroll systems and agreement repositories. The decision to unify staff agreements ([[decision/Unify Staff Employment Agreements Across All Clinicians]]) may partially address this by standardizing the data format, but the access bottleneck remains until data custody is shared.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]