---
alfred_tags:
- training/frontal-requirements
- clinical/feature-changes
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2025-01-12'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — vault-wide issue, embeds preserved. NOTE: file has duplicate
  base view embeds at bottom — consider removing duplicates.'
name: Require Frontal Training Before Removing Legacy Feature Workflows
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.85
  context: Legacy removal is major feature change
  source: decision/Require Frontal Training Before Removing Legacy Feature Workflows.md
  target: decision/Require Frontal Training for Major Feature Changes.md
  type: part-of
- confidence: 0.85
  context: Workflow removal is significant change
  source: decision/Require Frontal Training Before Removing Legacy Feature Workflows.md
  target: decision/Require Frontal Training for Significant Feature Changes.md
  type: part-of
session: null
source: Rami Khouri and Shira Lachman during commitment process meeting
source_date: '2025-01-12'
status: final
supports: []
tags: []
type: decision
---

# Require Frontal Training Before Removing Legacy Feature Workflows

## Context

When rolling out the new summary feature, some psychiatrists continued editing in Google Docs (the old workflow), unaware that changes no longer persist. Sending training booklets and WhatsApp updates proved insufficient — part-time psychiatrists do not reliably read documentation.

## Options Considered

1. **Send documentation only** — Training booklets and WhatsApp group announcements
2. **Frontal training before legacy removal** — Live training sessions, then remove old workflow only after confirmation

## Decision

When a new feature replaces an existing workflow, the old workflow must NOT be removed until all affected staff have received frontal (live) training on the replacement. Documentation alone is insufficient for part-time clinical staff.

## Rationale

Psychiatrists at Telia'z work part-time (6-8 hours/week) and do not prioritize reading training materials. Removing a workflow they depend on without confirmed training creates confusion, complaints, and potential clinical documentation gaps.

## Consequences

- Feature rollouts require a training step before deprecation of old features
- Alice assigned as the coordinator for psychiatrist training
- Slightly slower feature deployment cycle, but reduced friction and complaints

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]