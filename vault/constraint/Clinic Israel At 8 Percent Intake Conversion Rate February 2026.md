---
alfred_tags:
- israel-clinic/constraints
- intake-conversion
- session-attrition
authority: Operational capacity limitation
created: '2026-02-15'
description: Only 77 out of 945 new patients (8%) received intake appointments in
  February 2026, indicating severe operational capacity limitation at the Israel clinic.
janitor_note: LINK001 — learn-constraint.base embeds reference missing _bases/learn-constraint.base.
  Create base file to enable dynamic views. Telia'z wikilinks are valid (YAML escaping
  false positive).
name: Clinic Israel At 8 Percent Intake Conversion Rate February 2026
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month]]'
- '[[task/Design Patient Discharge Protocol for Clinic Israel]]'
relationships:
- confidence: 0.95
  context: Nearly identical titles on Israel clinic conversion
  source: constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026.md
  target: constraint/Israel Clinic at 8 Percent Intake Conversion February 2026.md
  type: related-to
- confidence: 0.85
  context: Similar titles on Israel clinic intake conversion
  source: constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026.md
  target: constraint/Israel Clinic at 8 Percent Same-Month Intake Conversion February
    2026.md
  type: related-to
- confidence: 0.95
  context: Rate supports staff limitation
  source: constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026.md
  target: constraint/Israel Clinic 8 Percent Intake Conversion Rate Limits Availability
    of Stopgap Staff for UK Launch.md
  type: supports
source: Dashboard data presented at team meeting 2026-02-15
source_date: '2026-02-15'
status: active
type: constraint
---

# Clinic Israel At 8 Percent Intake Conversion Rate February 2026

## Constraint
As of mid-February 2026, Clinic Israel can only convert approximately 8% of new monthly patient registrations to intake appointments in the same month. Of 945 new patients, only 77 received intake appointments. The remainder (approximately 600 scheduled for future months, 300+ unscheduled) are waiting.

## Source
Operational capacity limitation. Clinic opened February at near-full capacity. Insufficient psychiatrist hours, case manager hours, and appointment slots.

## Implications
- Massive waiting list building (~300+ patients with no appointment at all)
- True wait times much longer than the reported 1-week average (which only counts patients who got appointments)
- Pressure to hire 30-40 more psychiatrists by year-end
- Drives need for active patient discharge protocols to free capacity
- Staff burnout risk from overwhelming volume

## Expiry / Review
Should improve as new staff (2 psychiatrists, 2 case managers) complete onboarding and open calendar hours. Monitor monthly.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]