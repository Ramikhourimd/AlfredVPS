---
alfred_tags:
- healthcare/regulations
- medical-director/requirements
- physician-oversight
authority: Israeli healthcare regulatory body
created: '2026-02-25'
janitor_note: LINK001 — base view embeds fixed (removed backslash escaping). Base
  file _bases/learn-constraint.base does not exist — vault-wide infrastructure gap,
  embeds preserved. All Telia'z wikilinks valid (YAML escaping false positive). ORPHAN001
  — no inbound links; consider linking from project.
name: Medical Director Must Be Licensed Physician
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Hire Medical Director for Clinic Israel]]'
relationships:
- confidence: 0.75
  context: Licensed MD for oversight
  source: constraint/Medical Director Must Be Licensed Physician.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: part-of
- confidence: 1.0
  context: Nearly identical MD requirements
  source: constraint/Medical Director Must Be Licensed Physician.md
  target: constraint/Medical Director Must Be a Licensed Physician.md
  type: related-to
- confidence: 0.85
  context: Licensed MD enables oversight
  source: constraint/Medical Director Must Be Licensed Physician.md
  target: constraint/Ministry of Health Regulations Require Physician Oversight.md
  type: supports
- confidence: 0.95
  context: Licensed MD supports clinic MD req
  source: constraint/Medical Director Must Be Licensed Physician.md
  target: constraint/Each International Clinic Requires a Local Medical Director.md
  type: supports
source: Israeli healthcare regulations
status: active
type: constraint
---

# Medical Director Must Be Licensed Physician

## Constraint

The Medical Director position for Telia'z Clinic Israel must be filled by a licensed physician. This is a regulatory requirement, not an organisational preference.

## Source

Israeli healthcare regulations governing clinical supervision of psychiatrists. Referenced explicitly in the Medical Director hiring task.

## Implications

- Narrows the candidate pool significantly — must be a physician, not just a clinical psychologist or administrator
- May affect compensation expectations (physician-level pay for a 30% position)
- Candidate must hold a valid Israeli medical license or equivalent recognised credential

## Expiry / Review

Permanent constraint — tied to healthcare regulation. Review only if regulatory framework changes.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]