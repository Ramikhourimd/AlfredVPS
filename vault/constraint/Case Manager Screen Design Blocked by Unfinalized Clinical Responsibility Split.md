---
alfred_tags:
- ui-design/constraints
- clinical-roles
authority: Clinical operations — requires joint decision by Ori and Alice
created: '2026-03-01'
janitor_note: LINK001 — project/Telia'z AI Clinical Platform wikilink is valid (YAML
  escaping false positive). ORPHAN001 — no inbound links; consider linking from related
  project or decision records.
name: Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility Split
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
- '[[constraint/DSM Criteria Require Criterion-Level Granularity in Screen Design]]'
- '[[assumption/CM vs Psychiatrist Screen Split Determines AI Prompt Content]]'
relationships:
- confidence: 0.65
  context: Both affect screen design requirements
  source: constraint/Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility
    Split.md
  target: constraint/DSM Criteria Require Criterion-Level Granularity in Screen Design.md
  type: related-to
source: Clinical workflow design dependency
status: active
type: constraint
---

# Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility Split

## Constraint

The case manager meeting screen cannot be designed or built until the clinical responsibility split between case managers and psychiatrists is finalized. This includes determining which topics, symptoms, and assessment areas each role covers — avoiding duplication (both covering background, symptoms, DSM criteria) while ensuring complete coverage.

## Source

This constraint arises from the clinical workflow design process. The task explicitly states "case manager screen cannot be built until this is resolved." A joint meeting between Ori and Alice is required to finalize the split. Rami previously defined case manager agenda headings with Shira and Ori, but some items were removed as too psychiatric for case managers, and DSM criteria need criterion-level granularity.

## Implications

- Case manager screen design is blocked
- AI prompt content for CM agents cannot be finalized (the split feeds directly into AI prompts)
- Downstream: CM Agenda Agent and CM Summary Agent prompt tuning is also blocked
- Nadav cannot proceed with meeting screen design until the clinical decision is made
- Creates a cascade: clinical decision → screen design → AI prompt design → agent quality

## Expiry / Review

Expires when Ori and Alice complete the joint meeting to finalize the responsibility split. Target was psychiatrist screen design by end of the week it was assigned, case manager screen the following week — but no confirmation of completion found in records.