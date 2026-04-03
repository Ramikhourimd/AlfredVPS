---
alfred_tags:
- payroll/processing
- staff/employment
authority: Internal process gap — no enforcing authority
created: '2026-02-27'
janitor_note: 'LINK001: Telia''z wikilinks are valid (YAML double-quote escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist yet — create it to enable
  dynamic views. ORPHAN001: no inbound wikilinks; consider linking from project/Telia''z
  Clinic Israel or related payroll records.'
name: No Systematic Verification of Staff Active Employment Before Payroll Processing
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[synthesis/Compensation Data Discrepancies Are Systemic Across All Staff Tiers]]'
- '[[synthesis/Payroll Data Fragmentation Undermines Operational Transition]]'
- '[[constraint/Payroll and Agreement Data Bottlenecked Through Single Administrator]]'
relationships:
- confidence: 0.8
  context: Verification tied to admin bottleneck
  source: constraint/No Systematic Verification of Staff Active Employment Before
    Payroll Processing.md
  target: constraint/Payroll and Agreement Data Bottlenecked Through Single Administrator.md
  type: related-to
source: Observed during December 2025 payroll review session
source_date: '2025-12-04'
status: active
type: constraint
---

# No Systematic Verification of Staff Active Employment Before Payroll Processing

## Constraint

The clinic has no systematic mechanism to verify whether staff members are actively working before processing their payroll. Employment status verification relies on ad-hoc knowledge — someone happens to know (or not know) whether a person is still seeing patients. This creates a risk of paying inactive staff and an inability to maintain accurate headcount data.

## Source

Observed during the 2025-12-04 administrative staff rate review between Rami Khouri and Basel Kanaaneh ([[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]):
- Sarah (93 NIS/hour): "Unclear if she is still actively working clinically — they need to verify whether her agreement should be re-examined"
- If Sarah is not working clinically, the action is to "communicate that via email" — suggesting no prior notification mechanism exists
- Shira "did not send an Excel file for Sarah" — some staff are missing entirely from payroll data batches
- Lori/Ori submitting hourly Excel reports despite being on a percentage-based position — inconsistent reporting formats mask actual activity

The broader payroll review session ([[note/Staff Rate Review and Work Hour Audit 2025-12-04]]) revealed similar ambiguity across multiple staff members, where rate review required manually cross-referencing spreadsheets, agreements, and institutional memory to determine who is actively employed and at what terms.

## Implications

- Payroll may include payments to staff who have stopped clinical work without formal notification
- Headcount planning (critical for the restructuring) relies on unreliable data about who is actually active
- The quarter-position employment model (most staff at ~25%) amplifies this: with ~176 individual positions targeted, tracking active status manually becomes untenable at scale
- Budget forecasting for clinical compensation cannot be accurate without reliable active-status data
- Onboarding and offboarding processes lack a formal state transition that updates payroll eligibility

## Expiry / Review

This constraint persists until a formal employment status tracking system is implemented — either within Retool, the payroll system, or via a structured monthly verification process. Should be reviewed when the organizational restructuring (Basel's operational plan) addresses payroll modernization.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]