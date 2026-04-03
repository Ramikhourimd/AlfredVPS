---
alfred_tags:
- partnerships/clalit/constraints
authority: Clalit Health Services district contact (Tzachi/Eli)
created: '2025-11-09'
janitor_note: 'LINK001: project wikilink [[project/Telia''z Clinic Israel]] uses YAML
  apostrophe escaping (Telia''''z) which is valid, not broken. ORPHAN001: no inbound
  links — legitimate standalone constraint, may gain links as Clalit partnership develops.'
name: Clalit Form 17 Processing Turnaround Time Undefined
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
- '[[decision/Require Clalit Form 17 Approval Before Patient Referral to Clinic]]'
- '[[constraint/Clinic Israel Average Wait Time Rising Trend January 2026]]'
relationships:
- confidence: 0.95
  context: Both concern Clalit Form 17 processing
  source: constraint/Clalit Form 17 Processing Turnaround Time Undefined.md
  target: constraint/Clalit Form 17 Requires Manual Approval by District Contact.md
  type: related-to
- confidence: 0.65
  context: Clalit processing and volume constraints
  source: constraint/Clalit Form 17 Processing Turnaround Time Undefined.md
  target: constraint/Clalit Partnership Patient Volume Ceiling Unknown.md
  type: related-to
source: Clalit partnership preparation meeting
source_date: '2025-11-09'
status: active
type: constraint
---

# Clalit Form 17 Processing Turnaround Time Undefined

## Constraint

There is no defined SLA for how quickly the Clalit district contact (Tzachi/Eli) processes Form 17 authorization requests. Since the team decided patients must not be referred before Form 17 approval, the contact's processing speed directly determines patient wait times for the entire Clalit pipeline.

## Source

Identified during the 2025-11-09 Clalit partnership preparation meeting as a critical unknown. The team planned to raise this with the Clalit contact at the next-day meeting.

## Implications

- Patient wait times for Clalit-referred patients are unbounded until an SLA is established
- If the contact processes approvals slowly (days/weeks), this creates a hidden bottleneck that adds to the clinic's already-rising average wait times
- Without turnaround time data, the clinic cannot accurately project Clalit patient flow rates for capacity planning
- The contact's insistence on personally approving each Form 17 makes this a single-person bottleneck

## Expiry / Review

Should be monitored from first Clalit patient referrals. If turnaround exceeds 48 hours, escalation process needed.