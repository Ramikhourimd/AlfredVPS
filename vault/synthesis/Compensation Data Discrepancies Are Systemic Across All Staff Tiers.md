---
alfred_tags:
- compensation/discrepancies
- payroll/fragmentation
- operations/data-quality
cluster_sources:
- '[[note/Administrative Staff Rate Review and Discrepancies 2025-12-04]]'
- '[[note/Psychiatrist Payment Data Review and Cleanup Notes 2025-12-04]]'
- '[[note/Staff Rate Review and Work Hour Audit 2025-12-04]]'
- '[[contradiction/Staff Compensation Rates Diverge From Signed Agreement Terms]]'
confidence: high
created: '2026-02-26'
janitor_note: 'LINK001 false positives: project/Telia''z Clinic Israel and decision/Centralize
  Psychiatrist Payment Processing wikilinks resolve correctly (YAML single-quote escaping).
  learn-synthesis.base embeds are base view references (no action).'
name: Compensation Data Discrepancies Are Systemic Across All Staff Tiers
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Verify Staff Agreements Against Actual Payments]]'
- '[[task/Verify Psychiatrist Agreements Match Actual Payment Rates]]'
relationships:
- confidence: 0.9
  context: Both highlight systemic data quality issues
  source: synthesis/Compensation Data Discrepancies Are Systemic Across All Staff
    Tiers.md
  target: synthesis/Operational Data Quality Gaps Block All KPI and Dashboard Implementation
    Attempts.md
  type: related-to
- confidence: 0.85
  context: Linked compensation and payroll data issues
  source: synthesis/Compensation Data Discrepancies Are Systemic Across All Staff
    Tiers.md
  target: synthesis/Payroll Data Fragmentation Undermines Operational Transition.md
  type: related-to
- confidence: 0.7
  context: Both describe systemic operational failures
  source: synthesis/Compensation Data Discrepancies Are Systemic Across All Staff
    Tiers.md
  target: synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
    Cycle.md
  type: related-to
- confidence: 0.75
  context: Shared operational fragility themes
  source: synthesis/Compensation Data Discrepancies Are Systemic Across All Staff
    Tiers.md
  target: synthesis/Manual Single-Person Dependencies Create Cascading Failure Points
    Across Clinic Operations.md
  type: related-to
- confidence: 0.95
  context: Both highlight compensation data flaws
  source: synthesis/Compensation Data Discrepancies Are Systemic Across All Staff
    Tiers.md
  target: synthesis/Compensation Inequities Surface Through Data Audits Not Staff
    Advocacy.md
  type: related-to
status: draft
supports:
- '[[decision/Unify Staff Employment Agreements Across All Clinicians]]'
- '[[decision/Centralize Psychiatrist Payment Processing Into Standardized Unified
  Format]]'
type: synthesis
---

# Compensation Data Discrepancies Are Systemic Across All Staff Tiers

## Insight

The payment data review sessions on 2025-12-04 revealed that compensation discrepancies between signed agreements and actual payments are not isolated incidents but a systemic pattern spanning all staff categories: psychiatrists, case managers, administrative staff, and hourly workers. This suggests the root cause is structural (lack of centralized compensation management) rather than case-specific.

## Evidence

**Psychiatrist tier:** Multiple psychiatrists receive rates that differ from their signed agreements. One psychiatrist receives 400 NIS/hour for production when the fee schedule sets their rate at 200/100. Atef's follow-up rate of 200 NIS should be 250 NIS per the new standard.

**Administrative tier:** Lori/Ori's Excel shows 100 NIS/hour but her agreement states a different base rate structure (1,350 base to 1,650 with additions). A 9,000 NIS figure breaks down as 6,300 real + 2,700 overage. Sarah (93 NIS/hour) had no Excel data sent by Shira at all.

**Hourly workers:** Rate discrepancies between agreement scans and actual Excel-reported rates were found across multiple staff members during the audit.

**Pattern:** In every tier reviewed, at least one discrepancy was found between the contractual rate and the actual payment rate.

## Implications

- A comprehensive audit of all staff compensation (not just psychiatrists) is required
- The root cause is the absence of a single source of truth for compensation rates
- Shira's individual-per-person agreement approach has created drift between contractual and operational rates
- The decision to unify employment agreements addresses the agreement side; the payment standardization decision addresses the data side; both are needed together

## Applicability

Applies to all current and future staff at Telia'z Clinic Israel. The compensation audit task should cover every active employee, not just the psychiatrists originally targeted.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]