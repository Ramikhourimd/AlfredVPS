---
alfred_tags:
- training/frontal-requirements
- clinical/feature-changes
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
janitor_note: LINK001 — Telia'z wikilinks are YAML escaping false positives (targets
  exist). Base view embeds preserved per policy. Duplicate base embeds at bottom of
  body — remove one set manually.
name: Require Frontal Training Before Deprecating Old Clinical Features
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
relationships:
- confidence: 0.9
  context: Both require training before legacy feature removal
  source: decision/Require Frontal Training Before Deprecating Old Clinical Features.md
  target: decision/Require Frontal Training Before Removing Legacy Feature Workflows.md
  type: related-to
- confidence: 0.85
  context: Deprecation is a type of major feature change
  source: decision/Require Frontal Training Before Deprecating Old Clinical Features.md
  target: decision/Require Frontal Training for Major Feature Changes.md
  type: part-of
- confidence: 0.85
  context: Deprecation falls under significant changes
  source: decision/Require Frontal Training Before Deprecating Old Clinical Features.md
  target: decision/Require Frontal Training for Significant Feature Changes.md
  type: part-of
session: null
source: '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
source_date: '2025-01-12'
status: final
supports: []
tags: []
type: decision
---

# Require Frontal Training Before Deprecating Old Clinical Features

## Context

When the new AI summary feature was rolled out, some psychiatrists were still editing in Google Docs (the old workflow) without realizing the changes would not persist. Sending a training booklet via WhatsApp proved insufficient — part-time psychiatrists often do not read documentation. Ori had previously conducted a frontal training on Retool, but it did not specifically cover the summary feature in depth.

## Options Considered

1. **Continue sending WhatsApp updates and training booklets** — Minimal effort, but clearly failing as psychiatrists are not reading them
2. **Require frontal (live) training session before deprecating old workflows** — Higher effort per rollout, but ensures all users understand the new system

## Decision

Before removing any old clinical feature/workflow, a mandatory frontal (live) training session must be conducted with all affected staff. Only after verifying that everyone has been trained should the old method be disabled.

## Rationale

- Psychiatrists work part-time (6-8 hrs/week) and do not prioritize reading documentation
- When old and new systems coexist, psychiatrists default to familiar workflows
- The summary feature incident showed that passive communication creates billing and clinical data risks
- Shira's suggestion that "if a new feature replaces the old way, why keep both options" is valid — but only after training is complete

## Consequences

- Every significant feature change requires a planned training session before rollout
- Product team (Nadav/Alice) must coordinate training logistics with clinic management (Shira)
- Longer rollout cycles but higher adoption rates and fewer data quality issues

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]