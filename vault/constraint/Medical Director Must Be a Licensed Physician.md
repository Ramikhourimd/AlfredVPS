---
alfred_tags:
- healthcare/regulations
- medical-director/requirements
- physician-oversight
constraint_type: regulatory
created: '2026-02-25'
description: Israeli medical regulations require that the Medical Director of a healthcare
  clinic be a licensed physician. This constraint shapes hiring decisions and role
  definitions for the Teliaz clinic management structure.
janitor_note: 'LINK001 — all Telia''z wikilinks are valid (YAML escaping false positive).
  Non-schema field: constraint_type is not in the constraint schema — consider removing
  or proposing schema addition. No base view embed issues — constraint template does
  not use base views by default.'
name: Medical Director Must Be a Licensed Physician
related:
- '[[org/Telia''z]]'
- '[[project/Telia''z Organizational Restructuring]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[decision/CMO Role Required at Company Level]]'
- '[[note/Telia''z Leadership Meeting 2026-02-22 Organizational Structure and Roles]]'
relationships:
- confidence: 0.75
  context: Licensed MD for oversight
  source: constraint/Medical Director Must Be a Licensed Physician.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: part-of
- confidence: 0.85
  context: Licensed MD enables oversight
  source: constraint/Medical Director Must Be a Licensed Physician.md
  target: constraint/Ministry of Health Regulations Require Physician Oversight.md
  type: supports
- confidence: 0.95
  context: Licensed MD supports clinic MD req
  source: constraint/Medical Director Must Be a Licensed Physician.md
  target: constraint/Each International Clinic Requires a Local Medical Director.md
  type: supports
source: Israeli Ministry of Health regulations
status: active
type: constraint
---

## Regulatory Requirement

Israeli healthcare regulations mandate that any medical clinic must have a designated Medical Director who holds an active medical license. This is a non-negotiable compliance requirement for Telia'z's clinic operations.

## Impact on Organizational Structure

This constraint directly affects the Telia'z organizational restructuring in several ways:

1. **Medical Director Hiring**: The clinic must hire a licensed physician as Medical Director. The current plan is for a 30% (part-time) position, as the role is primarily supervisory and regulatory rather than full-time clinical.

2. **Role Separation**: Rami (who is a licensed physician) currently fulfills this requirement informally, but the restructuring aims to separate this from his other responsibilities. The new Medical Director will handle day-to-day medical oversight while Rami focuses on CMO-level and innovation work.

3. **Clinical Operations Manager**: The Clinical Operations Manager role (Basel) handles operational management but cannot serve as Medical Director without a medical license. This reinforces the three-pillar model: Clinical Ops Manager + Medical Director + Administrative Manager.

## Compliance Notes

- The Medical Director must maintain active licensure with the Israeli Medical Association
- Regular audits may verify the Medical Director's involvement in clinical oversight
- The Medical Director has legal responsibility for clinical standards and patient safety
- This requirement applies to each physical clinic location