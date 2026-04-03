---
alfred_instructions: null
alfred_tags:
- clinical/roles-division
- case-manager-psychiatrist
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on: []
description: Resolve which clinical topics and questions belong on the case manager
  meeting screen vs the psychiatrist meeting screen to eliminate duplication, before
  UI development proceeds
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is YAML escaping false
  positive (target exists). Base view embed (related.base#All) references _bases/related.base
  which does not exist — vault-wide infrastructure gap, embed preserved per policy.
kind: task
name: Finalize Case Manager vs Psychiatrist Screen Responsibility Split
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Ori Shukron]]'
- '[[person/Alice]]'
relationships:
- confidence: 0.85
  context: Resp split needs role definitions
  source: task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split.md
  target: task/Finalize Case Manager vs Psychiatrist Clinical Role Division.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Finalize Case Manager vs Psychiatrist Screen Responsibility Split

The Retool meeting screens for case managers and psychiatrists need a clear responsibility split to avoid both professionals covering the same ground (background, symptoms, DSM criteria).

## Context

- Rami previously defined case manager agenda headings with Shira and Ori
- Some items were removed as too niche/psychiatric for case managers
- DSM criteria breakdown needs more granularity (criterion-level, not just category-level)
- This split directly feeds into AI prompts (what to ask in each session type)
- Blocking: case manager screen cannot be built until this is resolved

## Action Plan

- Joint meeting with Ori and Alice to finalize the clinical responsibility split
- Rami to work with Nadav on the meeting screen design
- Target: psychiatrist screen design by end of week, case manager screen following week

## Related
![[related.base#All]]

## Outcome

*Filled in on completion.*