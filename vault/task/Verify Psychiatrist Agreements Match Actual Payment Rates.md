---
alfred_instructions: null
alfred_tags:
- payroll/verification
- psychiatrist/payments
- staff/contracts
assigned: '[[person/Basel Kanaaneh]]'
blocked_by: []
created: '2025-12-04'
depends_on: []
description: Cross-reference each psychiatrist agreement (iskon/heskem) against actual
  payment rates in the Excel spreadsheet. Where discrepancies exist, coordinate with
  Shira to update. Special attention to Atef (should be 250 NIS follow-up, currently
  200) and Clalit-related changes (share with Shiran).
due: null
janitor_note: '"2026-02-27: LINK001 flags are false positives — Telia''z link is YAML
  escaping (target exists), \![[task.base#Blocked]] is a standard base view embed."'
kind: task
name: Verify Psychiatrist Agreements Match Actual Payment Rates
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Office Fee Schedules Agreements and KPI Review 2025-12-04]]'
- '[[note/Clinic Office Discussion Fee Schedules Surveys and KPIs 2025-12-04]]'
- '[[task/Raise Atef Clinical Rate to Match Scale]]'
- '[[task/Obtain Psychiatrist Fee Schedules From Shira]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.85
  context: Psychiatrists subset of staff checks
  source: task/Verify Psychiatrist Agreements Match Actual Payment Rates.md
  target: task/Verify Staff Agreements Against Actual Payments.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Verify Psychiatrist Agreements Match Actual Payment Rates

Cross-reference every psychiatrist's signed agreement (heskemim) against their actual payment rates in the Excel data. Shira sent updated fee schedules and 4 unified agreement templates. Basel must verify alignment between:

1. The agreement text (what the contract says they earn)
2. The actual payment rates (what they are receiving per the Excel)

## Specific Actions

- **Atef**: Agreement says 200 NIS follow-up, should be raised to 250 NIS. Update the agreement (iskon) accordingly.
- **Ahmed**: Verify his agreement matches his 400/200 intake/follow-up rates.
- **Clalit-related changes**: Any rate changes must be shared with Shiran.
- **All other psychiatrists**: Spot-check agreements Shira sent (6 agreements: Rana, Sara, Shira, Amada, Abitan, Elias) against actual rates.

## Context

Identified during 2025-12-04 office discussion. Shira had sent a Google Drive link to updated clinical agreements for the psychiatry team. Rami directed Basel to verify these against actual rates before confirming back to Shira.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.