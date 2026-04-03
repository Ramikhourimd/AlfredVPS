---
alfred_tags:
- payroll/processing
- staff/employment
authority: Internal employment practice
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML single-quote escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist. Embeds preserved per
  policy. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  Clinic Israel.
name: Mixed Employment Classification Models Create Payroll Reconciliation Ambiguity
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[constraint/Inconsistent Excel Formats Across Psychiatrist Payment Reports]]'
- '[[synthesis/Compensation Data Discrepancies Are Systemic Across All Staff Tiers]]'
relationships:
- confidence: 0.75
  context: Both payroll reconciliation ambiguities
  source: constraint/Mixed Employment Classification Models Create Payroll Reconciliation
    Ambiguity.md
  target: constraint/No Systematic Verification of Staff Active Employment Before
    Payroll Processing.md
  type: related-to
- confidence: 0.7
  context: Payroll data processing constraints
  source: constraint/Mixed Employment Classification Models Create Payroll Reconciliation
    Ambiguity.md
  target: constraint/Payroll and Agreement Data Bottlenecked Through Single Administrator.md
  type: related-to
source: Payroll review session between Rami Khouri and Basel Kanaaneh
source_date: '2025-12-04'
status: active
type: constraint
---

# Mixed Employment Classification Models Create Payroll Reconciliation Ambiguity

## Constraint

Some clinic staff simultaneously hold position-percentage agreements (e.g., 75% position with a fixed monthly salary) and submit hourly timesheet reports (e.g., 100 NIS/hour). When both models coexist for the same employee, the clinic has no policy or system to determine which governs actual payment, making payroll verification impossible.

## Source

Discovered during the December 4, 2025 administrative staff rate review by Rami Khouri and Basel Kanaaneh. Specific example: Lori/Ori's agreement specifies a 75% position with fixed salary components (base 1,350 + additions to 1,650 + 6,000 component), yet she submits hourly Excel reports at 100 NIS/hour. The reviewers could not reconcile the two models — "if she's at 75% position, why would she submit hourly Excel reports?"

## Implications

- Payroll audits cannot determine correct compensation without first resolving which employment model applies to each staff member
- Overpayment or underpayment may persist undetected because there is no single source of truth
- The unified agreement rollout (already decided) must explicitly assign each staff member to ONE employment model
- Automated payroll systems cannot be built while dual classification persists

## Expiry / Review

This constraint should be resolved by the unified staff employment agreement rollout. Review after agreements are standardized.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]