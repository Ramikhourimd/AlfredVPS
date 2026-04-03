---
alfred_tags:
- clinic-israel/patient-intake
- intake-conversion-rates
- discharge-protocols
created: '2026-03-01'
date: '2025-11-10'
janitor_note: 'LINK001 for [[project/Telia''z Clinic Israel]] is a false positive
  — target exists, YAML double-apostrophe escaping causes scanner mismatch. Non-standard
  frontmatter: uses "related_to" instead of "related", and has extra "date" field
  not in assumption schema. Human review: rename "related_to" to "related" if appropriate,
  decide whether "date" should be "source_date".'
name: Clalit South Will Generate 200 Patients Per Week Within Three Months
related_to:
- '[[org/Clalit Health Services]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]'
- '[[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]]'
relationships:
- confidence: 0.8
  context: Clalit South patients contribute to total intake
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Clinic Israel Receiving Approximately 1000 New Patients Per Month.md
  type: related-to
- confidence: 0.65
  context: Impacts same-month conversion capacity
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Clinic Israel Same-Month Patient Intake Conversion Is Below 10
    Percent.md
  type: related-to
- confidence: 0.65
  context: Affects demand-service ratio
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand.md
  type: related-to
- confidence: 0.55
  context: Relates to intake conversion analysis
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Same-Month Intake Conversion Rate Understates Actual Patient
    Service Coverage.md
  type: related-to
- confidence: 0.75
  context: Increased patients support scaling need
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Scaling Requires Approximately 176 Individual Quarter-Position
    Hires.md
  type: supports
- confidence: 0.75
  context: Intake growth needs capacity free
  source: assumption/Clalit South Will Generate 200 Patients Per Week Within Three
    Months.md
  target: assumption/Israel Discharge Framework Can Free Case Manager Capacity for
    UK Launch.md
  type: related-to
status: active
tags:
- clalit
- volume
- capacity-planning
type: assumption
---

# Clalit South Will Generate 200 Patients Per Week Within Three Months

## Assumption

The Clalit South District referral pathway will generate approximately 200 psychiatric patients per week within three months of launch.

## Source

Discussed during the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]. Volume projection was shared by Tzachi (Clalit South District representative) based on the district's patient population and demand.

## Basis

- Clalit South District covers a large geographic area with significant psychiatric care demand
- Closure of Hosen (mental health facility) creates additional displaced patient volume — see [[task/Contact Former Hosen Patients for Clalit South Pipeline]]
- Clalit is the largest HMO in Israel with substantial southern presence

## Risk if Wrong

- **If overestimate**: Telia'z may over-invest in capacity (staffing, scheduling) for the Clalit pipeline
- **If underestimate**: Could face capacity constraints and patient wait times, damaging the partnership early

## Validation Plan

- Track referral volume weekly from launch
- Compare actual vs. projected at 4-week, 8-week, and 12-week marks
- Adjust staffing and scheduling based on observed trajectory