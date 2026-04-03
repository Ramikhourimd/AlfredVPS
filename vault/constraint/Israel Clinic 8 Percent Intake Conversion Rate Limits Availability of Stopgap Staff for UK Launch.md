---
alfred_tags:
- israel-clinic/constraints
- intake-conversion
- session-attrition
authority: Operational capacity data
created: '2026-03-15'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  note/Telia''z Team Meeting link target may not exist — verify. Base view embeds
  (learn-constraint.base#Affected Projects, #Related) reference missing _bases/learn-constraint.base
  — vault-wide infrastructure gap, embeds preserved. ORPHAN001 — no inbound wikilinks;
  consider linking from project/Telia''z UK Expansion.'
name: Israel Clinic 8 Percent Intake Conversion Rate Limits Availability of Stopgap
  Staff for UK Launch
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[synthesis/Single Israeli Team Serves Dual Markets Creating Resource Contention]]'
- '[[assumption/Single Israeli Case Manager Can Handle Initial UK Patient Volume]]'
relationships:
- confidence: 0.95
  context: Limit depends on conversion rate
  source: constraint/Israel Clinic 8 Percent Intake Conversion Rate Limits Availability
    of Stopgap Staff for UK Launch.md
  target: constraint/Israel Clinic at 8 Percent Intake Conversion February 2026.md
  type: depends-on
- confidence: 0.9
  context: Limit depends on rate variant
  source: constraint/Israel Clinic 8 Percent Intake Conversion Rate Limits Availability
    of Stopgap Staff for UK Launch.md
  target: constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February
    2026.md
  type: depends-on
- confidence: 0.95
  context: Staff limits depend on 8% conversion rate
  source: constraint/Israel Clinic 8 Percent Intake Conversion Rate Limits Availability
    of Stopgap Staff for UK Launch.md
  target: constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026.md
  type: depends-on
source: Rami Khouri dashboard presentation, Feb 15 2026 team meeting
source_date: '2026-02-15'
status: active
type: constraint
---

# Israel Clinic 8 Percent Intake Conversion Rate Limits Availability of Stopgap Staff for UK Launch

## Constraint

The Israel clinic is operating at an 8.1% intake conversion rate (945 new patients in the period, only 77 received intake appointments). This severe capacity bottleneck means the Israeli case management staff earmarked as UK launch stopgap (specifically Bassem) are already overwhelmed with domestic demand.

## Source

Rami Khouri presented dashboard data during the February 15, 2026 team meeting showing the conversion crisis. The same meeting confirmed Bassem as the planned UK stopgap case manager, creating a direct resource conflict.

## Implications

- The planned UK stopgap staffing model (using Israeli case manager Bassem) competes directly with acute Israel capacity needs
- Basel's time allocation for the Israeli stopgap needs coordination, but Basel was absent from the meeting
- The 8% conversion suggests systemic capacity constraints, not temporary overload — UK launch adds demand to an already strained system
- Alex Taliaz suggested outsourcing case management to an external vendor/call center as an alternative, indicating the team recognizes the internal capacity problem

## Expiry / Review

Review when Israel intake conversion improves above 20% or when UK hires local case managers, removing dependency on Israeli staff.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]