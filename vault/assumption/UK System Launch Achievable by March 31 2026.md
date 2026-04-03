---
confidence: medium
created: '2026-02-26'
depends_on:
- '[[task/Build UK Prescription and Scheduling Features]]'
- '[[task/Sign Contract With Leon for UK CQC Partnership]]'
description: Shachar estimated the UK Telia'z system (product features including prescriptions,
  scheduling, and questionnaires adapted for UK) can be ready by March 31, 2026.
janitor_note: LINK001 — Telia'z wikilinks are false positives (YAML apostrophe escaping,
  targets exist). Base view embed (related.base#All) references _bases/related.base
  which does not exist. Note and conversation wikilinks with Telia'z prefix follow
  same YAML escaping pattern.
name: UK System Launch Achievable by March 31 2026
related:
- '[[project/Telia''z UK Expansion]]'
- '[[event/UK System Launch Target March 31 2026]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
source: '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
status: invalidated
tags:
- uk-launch
- timeline
- product
type: assumption
---

# UK System Launch Achievable by March 31 2026

## Assumption

The technical system for the UK Telia'z clinic — including prescription handling, scheduling, UK-format reports, and questionnaire adaptations — can be development-complete by March 31, 2026.

## Basis

Shachar (product/development) provided this estimate during the 2026-02-15 team meeting. The estimate accounts for:
- UK prescription format implementation
- Scheduling system adaptations
- UK report formats
- Questionnaire UI fixes (dropdown issues, Hebrew text cleanup)

## Risks

- **Medium confidence**: Estimate depends on no major scope additions
- Leon contract must be signed to finalize exact UK regulatory requirements
- Questionnaire UI issues may surface additional bugs during testing
- UK insurance and compliance requirements may add unforeseen development work

## Validation Plan

Track development progress against March 31 milestone. If features are not code-complete by March 15, escalate and re-evaluate timeline.

## Related
![[related.base#All]]
