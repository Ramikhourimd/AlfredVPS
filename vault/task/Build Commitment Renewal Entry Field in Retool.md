---
alfred_instructions: null
alfred_tags:
- maccabi/commitment-renewal
- retool/implementation
assigned: '[[person/Nadav Blatt]]'
blocked_by: []
created: '2026-02-26'
depends_on: []
description: Add a field in Retool for entering follow-up commitment numbers when
  patients renew their Maccabi commitment after the initial 16+4 session cycle expires.
  Must include validation workflow against Maccabi website and session balance tracking.
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist.
kind: task
name: Build Commitment Renewal Entry Field in Retool
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[person/Nadav Blatt]]'
relationships:
- confidence: 0.95
  context: Field is component of Entry
  source: task/Build Commitment Renewal Entry Field in Retool.md
  target: task/Build Commitment Renewal Entry in Retool.md
  type: part-of
- confidence: 0.85
  context: Field part of renewal workflow
  source: task/Build Commitment Renewal Entry Field in Retool.md
  target: task/Build Commitment Renewal Workflow in Retool.md
  type: part-of
- confidence: 0.9
  context: Build requires clarified terms
  source: task/Build Commitment Renewal Entry Field in Retool.md
  target: task/Clarify Maccabi Commitment Renewal Terms.md
  type: depends-on
- confidence: 0.8
  context: Build needs followup structure
  source: task/Build Commitment Renewal Entry Field in Retool.md
  target: task/Clarify Maccabi Follow-Up Commitment Structure and Terms.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Build Commitment Renewal Entry Field in Retool

What needs to be done and why.

## Context

Links to relevant records that triggered this task.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — what was done, any follow-ups created.