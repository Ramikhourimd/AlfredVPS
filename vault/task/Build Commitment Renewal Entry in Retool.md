---
alfred_instructions: null
alfred_tags:
- maccabi/commitment-renewal
- retool/implementation
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on:
- '[[task/Clarify Maccabi Commitment Renewal Terms]]'
description: Add field in Retool for entering patient commitment renewal numbers from
  Maccabi. Must include validation workflow against MADAC portal and session counter
  reset.
due: null
janitor_note: 'LINK001 — [[project/Telia''z Clinic Israel]] wikilink is valid (YAML
  single-quote escaping false positive: '''' represents literal apostrophe). Base
  view embed [[related.base#All]] references _bases/related.base which does not exist
  — vault-wide infrastructure gap; embed preserved per policy.'
kind: task
name: Build Commitment Renewal Entry in Retool
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[person/Nadav Blatt]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
relationships:
- confidence: 0.9
  context: Entry part of renewal workflow
  source: task/Build Commitment Renewal Entry in Retool.md
  target: task/Build Commitment Renewal Workflow in Retool.md
  type: part-of
- confidence: 0.9
  context: Build requires clarified terms
  source: task/Build Commitment Renewal Entry in Retool.md
  target: task/Clarify Maccabi Commitment Renewal Terms.md
  type: depends-on
- confidence: 0.8
  context: Build needs followup structure
  source: task/Build Commitment Renewal Entry in Retool.md
  target: task/Clarify Maccabi Follow-Up Commitment Structure and Terms.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Build Commitment Renewal Entry in Retool

Add a new commitment entry field in Retool so that secretaries can record renewal commitment numbers for patients whose initial commitments have expired. Must integrate with the existing MADAC validation workflow and update the session balance counter.

## Context

Emerged from [[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]. Currently patients who exhaust their initial Maccabi commitment (intake + 16 case manager + 4 psychiatric follow-ups) have no way to enter a renewal commitment in the system.

## Related
![[related.base#All]]

## Outcome