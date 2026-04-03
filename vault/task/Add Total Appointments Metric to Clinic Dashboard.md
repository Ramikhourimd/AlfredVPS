---
alfred_instructions: null
alfred_tags:
- operations/dashboard
- appointments/metrics
- patients/scheduling
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-26'
depends_on: []
description: Add a metric to the clinic operations dashboard showing total appointments
  scheduled across all months (not just current month), so leadership can see the
  full pipeline beyond same-month conversions. Adiel requested this to understand
  the gap between same-month intake (8%) and total scheduled appointments.
due: null
janitor_note: LINK001 — Teliaz wikilinks are YAML-escape false positives (Telia''z
  = Telia'z). Base view embed (related.base#All) references _bases/related.base which
  does not exist — vault-wide infrastructure gap, embed preserved.
kind: task
name: Add Total Appointments Metric to Clinic Dashboard
priority: medium
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[person/Adiel Levin]]'
relationships:
- confidence: 0.95
  context: Same metric added to different dashboards
  source: task/Add Total Appointments Metric to Clinic Dashboard.md
  target: task/Add Total Appointments Metric to Operations Dashboard.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Add Total Appointments Metric to Clinic Dashboard

Enhance the clinic operations dashboard to show not just same-month intake conversions but total appointments scheduled across all future months.

## Context

At the 2026-02-15 team meeting, Adiel raised confusion about the dashboard showing only 8% (77/945) intake conversion. The dashboard currently only counts appointments booked for the same month. In reality, approximately 600 patients were booked for the following month. The dashboard needs an additional metric showing total scheduled appointments regardless of month to give a more complete picture.

## Related
![[related.base#All]]

## Outcome