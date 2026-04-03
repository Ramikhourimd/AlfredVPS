---
alfred_tags:
- healthcare/regulations
- medical-director/requirements
- physician-oversight
created: '2026-02-25'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  FM002 — copied related_to values to standard related field. Human action needed:
  remove the non-standard related_to field manually (alfred vault edit --set cannot
  delete fields).'
name: Ministry of Health Regulations Require Physician Oversight
related:
- '[[project/Telia''z Clinic Israel]]'
- '[[assumption/Physician Must Lead Clinical Operations]]'
- '[[conversation/Telia''z Organizational Restructuring Meeting]]'
related_to:
- '[[project/Telia''z Clinic Israel]]'
- '[[assumption/Physician Must Lead Clinical Operations]]'
- '[[conversation/Telia''z Organizational Restructuring Meeting]]'
relationships:
- confidence: 0.95
  context: Basis for oversight req
  source: constraint/Ministry of Health Regulations Require Physician Oversight.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: supports
- confidence: 0.85
  context: Oversight via local MD
  source: constraint/Ministry of Health Regulations Require Physician Oversight.md
  target: constraint/Each International Clinic Requires a Local Medical Director.md
  type: supports
source: '[[person/Rami Khouri]]'
status: active
tags:
- regulatory
- ministry-of-health
- compliance
type: constraint
---

## Constraint

Israeli Ministry of Health regulations require physician oversight for psychiatric clinical operations. This is a non-negotiable regulatory requirement that shapes the organizational structure.

## Impact

- Every clinic district must have a designated physician in a leadership role
- Certain clinical decisions cannot be delegated to non-physician staff
- Regulatory inspections will verify physician oversight is in place
- This constraint supports Rami's argument for clinical authority in the organizational structure