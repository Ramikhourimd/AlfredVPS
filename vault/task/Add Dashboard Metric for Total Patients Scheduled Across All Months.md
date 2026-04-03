---
alfred_instructions: null
alfred_tags:
- operations/dashboard
- appointments/metrics
- patients/scheduling
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-15'
depends_on: []
description: Add a new metric to the clinic operations dashboard showing how many
  patients received any appointment (not just same-month), to complement the current
  same-month conversion view. Adiel flagged that seeing only same-month data is misleading.
due: null
janitor_note: LINK001 — Telia'z wikilinks are YAML escaping false positives (files
  exist). Base view embed (related.base#All) references _bases/related.base which
  does not exist — create it to enable dynamic views.
kind: task
name: Add Dashboard Metric for Total Patients Scheduled Across All Months
priority: medium
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch Operations and Recruitment 2026-02-15]]'
relationships:
- confidence: 0.8
  context: Similar scheduling metrics for dashboards
  source: task/Add Dashboard Metric for Total Patients Scheduled Across All Months.md
  target: task/Add Total Appointments Metric to Clinic Dashboard.md
  type: related-to
- confidence: 0.8
  context: Similar scheduling metrics for dashboards
  source: task/Add Dashboard Metric for Total Patients Scheduled Across All Months.md
  target: task/Add Total Appointments Metric to Operations Dashboard.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Add Dashboard Metric for Total Patients Scheduled Across All Months

The current dashboard shows same-month conversion (8%) which alarmed stakeholders. Add a complementary view showing total patients who have any appointment scheduled (including future months) to give a more complete picture.

## Context

During the meeting, Adiel pointed out that showing only "77 out of 945" is misleading since ~600 have March appointments. Rami agreed to add this metric.

## Related
![[related.base#All]]

## Outcome