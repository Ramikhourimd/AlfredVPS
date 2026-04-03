---
alfred_instructions: null
alfred_tags:
- organization/chart
- clinic/management
assigned: '[[person/Oren Taliaz]]'
assigned_to: ''
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Create and finalize the complete organizational chart for Teliaz reflecting
  the new structure discussed in the 2026-02-22 leadership meeting, including C-level
  roles, clinic management, shared services, and team pod structure.
due: null
janitor_note: 'FIXED: assigned_to → assigned (value corrected from person/Oren Khouri
  to person/Oren Taliaz). FIXED: related_to entries merged into related field. REMAINING:
  assigned_to and related_to fields emptied but could not be deleted via CLI — manual
  removal recommended. Base view embed (related.base#All) references _bases/related.base
  which does not exist — embed preserved. All Telia''z wikilinks are false positives
  (YAML escaping). ORPHAN001 — now has inbound links from related field entries.'
kind: task
name: Finalize Organizational Chart
priority: high
project: '[[project/Telia''z Organizational Restructuring]]'
related:
- '[[org/Telia''z]]'
- '[[project/Telia''z Organizational Restructuring]]'
- '[[decision/CMO Role Required at Company Level]]'
- '[[decision/Shared Services Model for Clinic Support Functions]]'
- '[[note/Telia''z Leadership Meeting 2026-02-22 Organizational Structure and Roles]]'
- '[[conversation/Telia''z Leadership Meeting 2026-02-22 Organizational Structure
  and Roles]]'
- '[[conversation/Telia''z Organizational Restructuring Meeting]]'
related_to: ''
relationships:
- confidence: 0.9
  context: Finalize depends on detailed chart build
  source: task/Finalize Organizational Chart.md
  target: task/Build Detailed Organizational Chart.md
  type: depends-on
- confidence: 0.85
  context: Finalize depends on clinic chart build
  source: task/Finalize Organizational Chart.md
  target: task/Build Organizational Chart for Telia'z Clinic Israel.md
  type: depends-on
run: null
status: todo
tags:
- org-chart
- restructuring
type: task
---

## Description

Create and finalize the organizational chart reflecting the agreed-upon "district" model. The chart should show the parent company level (shared services) and the clinic district level (Clinical Director, Operations Manager, Administrative Manager).

## Context

The Feb 22 meeting reached conceptual agreement on the district model but did not produce a finalized chart. Multiple versions were discussed (Basel and Leah's proposals vs Rami's counter-proposals). A definitive chart is needed before new hires can proceed.

## Deliverables

- Visual organizational chart
- Role descriptions for each position
- Reporting lines and dotted-line relationships
- Resource sharing agreements between parent and clinic

---
## Related
![[related.base#All]]