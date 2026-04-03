---
alfred_instructions: null
alfred_tags:
- clinical/roles-division
- case-manager-psychiatrist
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on: []
description: Finalize the division of clinical assessment responsibilities between
  case managers and psychiatrists — specifically which sections (background, symptoms,
  DSM criteria) each covers — to avoid duplication and inform meeting screen UI design.
due: null
janitor_note: '"LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive, targets exist). \![[related.base#All]] embed references _bases/related.base
  which does not exist yet (systemic issue, embed preserved)."'
kind: task
name: Finalize Case Manager vs Psychiatrist Clinical Role Division
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Ori Shukron]]'
- '[[person/Alice]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.9
  context: Clinical roles inform screen content split
  source: task/Finalize Case Manager vs Psychiatrist Clinical Role Division.md
  target: task/Finalize Case Manager vs Psychiatrist Screen Content Split.md
  type: supports
- confidence: 0.9
  context: Clinical roles inform screen resp split
  source: task/Finalize Case Manager vs Psychiatrist Clinical Role Division.md
  target: task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split.md
  type: supports
run: null
status: todo
tags: []
type: task
---

# Finalize Case Manager vs Psychiatrist Clinical Role Division

Decide and document which clinical assessment sections (patient background, symptoms, DSM criteria review) are handled by the case manager vs. the psychiatrist. Currently both professionals cover overlapping ground, which is inefficient. This division directly determines what appears on each meeting screen in the platform.

## Context

From [[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]. Shira and her team raised this as a blocker for the meeting screen redesign. The case manager screen agenda (titles/subtitles) cannot be defined until this is resolved.

## Related
![[related.base#All]]

## Outcome