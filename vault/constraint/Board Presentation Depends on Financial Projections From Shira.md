---
alfred_tags:
- clinical/uk-expansion
- capacity/bottlenecks
- board/challenges
authority: Data dependency
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. ORPHAN001 — no inbound wikilinks; consider linking from
  project/Telia''z Organizational Restructuring or task/Present Clinic and Innovation
  Plans to Board. All Telia''z wikilinks are valid (YAML escaping false positive).'
name: Board Presentation Depends on Financial Projections From Shira
project:
- '[[project/Telia''z Organizational Restructuring]]'
related:
- '[[task/Present Clinic and Innovation Plans to Board]]'
- '[[assumption/Board Presentation to Alex Required Before Restructuring Implementation]]'
- '[[constraint/Financial Viability of New Structure Must Be Validated Before Implementation]]'
relationships:
- confidence: 0.7
  context: Both involve board-level presentation issues
  source: constraint/Board Presentation Depends on Financial Projections From Shira.md
  target: constraint/Rami Analytical Presentations Dismissed by Board-Level Leadership.md
  type: related-to
- confidence: 0.65
  context: Board pres by board lacking physician
  source: constraint/Board Presentation Depends on Financial Projections From Shira.md
  target: constraint/No Physician on Board of Directors.md
  type: related-to
source: task/Present Clinic and Innovation Plans to Board.md
source_date: '2026-02-22'
status: active
type: constraint
---

# Board Presentation Depends on Financial Projections From Shira

## Constraint

The board presentation to Alex requires financial projections that must be gathered from Shira. Without these projections, the presentation covering organizational restructuring, clinic operations, innovation roadmap, and potential UK expansion cannot be completed.

## Source

The task "Present Clinic and Innovation Plans to Board" lists "Gather financial projections from Shira" as an explicit action item. This creates a dependency on Shira's availability and output.

## Implications

- The board presentation is blocked until Shira provides financial projections
- This cascades to blocking restructuring implementation (which requires board approval per existing assumption)
- If Shira's projections challenge the financial viability of the new structure, the entire plan may need revision
- The presentation scope is ambitious (4 topics: restructuring, clinic ops, innovation, UK expansion) — each requiring financial justification

## Expiry / Review

Active until Shira delivers the financial projections and the board presentation is scheduled.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]