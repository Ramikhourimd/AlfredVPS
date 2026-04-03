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
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Telia''z wikilinks are YAML single-quote escaping false positives
  (valid). Conversation link [[conversation/Clinic Operations Commitment Renewal and
  Feature Updates Meeting 2025-08-01]] needs verification. Base view embeds (learn-decision.base#Based
  On, #Related) are duplicated in body — cannot remove per rules, consider manual
  cleanup.'
name: Require Frontal Training for Major Feature Changes
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Operations Commitment Renewal and Feature Updates Meeting
  2025-08-01]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
relationships:
- confidence: 0.95
  context: Similar policies for major/significant changes
  source: decision/Require Frontal Training for Major Feature Changes.md
  target: decision/Require Frontal Training for Significant Feature Changes.md
  type: related-to
session: null
source: Shira Lachman and Rami Khouri during operations meeting
source_date: '2025-08-01'
status: draft
supports: []
tags: []
type: decision
---

# Require Frontal Training for Major Feature Changes

## Context

Psychiatrists at the clinic were not properly adopting new features (particularly the AI session summary workflow). Despite receiving training booklets and WhatsApp updates, some were still editing in Google Docs expecting changes to persist. The team realized that sending written materials is insufficient for ensuring adoption of significant workflow changes.

## Options Considered

1. **Continue with written materials and WhatsApp updates** — Low effort, but clearly failing to achieve adoption
2. **Require in-person/frontal training sessions for major feature changes** — Higher effort, but proven effective (Ori's previous Retool training session was well-received)
3. **Remove old features immediately to force adoption** — Risky without confirming all users are trained

## Decision

For significant feature changes that alter existing workflows, frontal (in-person or video) training sessions must be conducted before the old workflow is removed. Written booklets serve as reference material only, not primary training.

## Rationale

- Psychiatrists work part-time and do not prioritize reading internal documentation
- The previous frontal training by Ori for Retool was effective
- Removing old features without training creates confusion and resistance
- Shira proposed the rule: only remove old workflow options after confirming all users are trained on the replacement

## Consequences

- Higher overhead for feature rollouts (must schedule and conduct training)
- More predictable adoption curves
- Reduces support burden from confused users

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]