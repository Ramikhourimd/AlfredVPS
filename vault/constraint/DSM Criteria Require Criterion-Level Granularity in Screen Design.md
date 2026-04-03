---
alfred_tags:
- ui-design/constraints
- clinical-roles
authority: Clinical diagnostic standards
created: '2026-02-28'
janitor_note: LINK001 — [[project/Telia'z AI Clinical Platform]] is valid (YAML single-quote
  escaping false positive). No base view embeds in this file.
name: DSM Criteria Require Criterion-Level Granularity in Screen Design
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
source: Clinical requirements from case manager vs psychiatrist screen split discussion
source_date: '2025-01-12'
status: active
type: constraint
---

# DSM Criteria Require Criterion-Level Granularity in Screen Design

## Constraint

The psychiatrist meeting screen's DSM classification section must operate at the individual criterion level, not just the category level. This means the UI must support granular criterion-by-criterion assessment rather than broad diagnostic category selection.

## Source

Identified during the case manager vs psychiatrist screen responsibility split discussion (2025-01-12). Some items were removed from the case manager screen as too niche/psychiatric, and the remaining DSM criteria on the psychiatrist screen need more granularity than the initial design provided.

## Implications

- The psychiatrist screen UI must present individual DSM criteria as separate assessable items
- This increases the complexity of the screen design and data model
- AI prompts feeding into the psychiatrist session must also be structured at criterion level
- The case manager screen design is blocked until this responsibility split is finalized
- This constraint directly affects how AI-generated summaries present diagnostic information

## Expiry / Review

Active indefinitely — reflects clinical diagnostic standards. Review if DSM classification approach changes.