---
alfred_instructions: null
alfred_tags:
- organization/chart
- clinic/management
assigned: null
assigned_to:
- Incoming Manager
blocked_by: []
created: '2026-03-01'
date: '2025-11-09'
depends_on: []
description: Create a formal organizational chart documenting reporting lines, role
  boundaries, and authority levels for Telia'z Clinic Israel as the first priority
  task for the new incoming manager
due: null
janitor_note: 'FM001 fixed: YAML parse error from unescaped apostrophes in Telia''z
  wikilinks (changed single quotes to double quotes). Set project from context. Non-schema
  fields present: assigned_to, date — may need manual review. LINK001: All Telia''z
  wikilinks resolve correctly (YAML escaping false positives). Base view embed (related.base#All)
  references _bases/related.base which does not exist — vault-wide issue.'
kind: task
name: Build Organizational Chart for Telia'z Clinic Israel
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[project/Telia''z Organizational Restructuring]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Operational Processes and Office Planning Discussion 2025-11-09]]'
- '[[person/Rami Khouri]]'
- '[[person/Oren Taliaz]]'
relationships:
- confidence: 0.8
  context: Clinic chart part of detailed org
  source: task/Build Organizational Chart for Telia'z Clinic Israel.md
  target: task/Build Detailed Organizational Chart.md
  type: part-of
- confidence: 0.75
  context: Clinic build aids final chart
  source: task/Build Organizational Chart for Telia'z Clinic Israel.md
  target: task/Finalize Organizational Chart.md
  type: supports
run: null
status: todo
tags:
- organizational-structure
- management
- priority-task
type: task
---

## Task Description

Create a comprehensive organizational chart for [[project/Telia'z Clinic Israel]] that clearly documents:

1. **Reporting Lines**: Who reports to whom for clinical, operational, and administrative matters
2. **Role Boundaries**: Clear delineation of responsibilities for each position
3. **Authority Levels**: Decision-making authority at each level
4. **Dual Roles**: Document positions with dual responsibilities (e.g., medical director)
5. **Communication Channels**: Formal channels for clinical feedback, operational issues, and development requests

## Priority

This was identified as the **first priority task** for the incoming clinic manager. The current lack of a formal organizational chart creates ambiguity in:
- Role boundaries between clinical and operational staff
- Reporting structure for the medical director dual role
- Communication channels for system development feedback
- Escalation paths for operational issues

## Context

Discussed in [[conversation/Operational Processes and Office Planning Discussion 2025-11-09]]. Strong consensus from [[person/Rami Khouri]], [[person/Oren Taliaz]], and [[person/Dekkel Taliaz]] that this is urgently needed.

## Acceptance Criteria

- [ ] All current positions documented with clear role descriptions
- [ ] Reporting lines clearly drawn for both clinical and operational domains
- [ ] Dual roles explicitly documented with separate reporting lines per function
- [ ] Communication channels for system development documented
- [ ] Shared with all team members for validation

---
## Related
![[related.base#All]]