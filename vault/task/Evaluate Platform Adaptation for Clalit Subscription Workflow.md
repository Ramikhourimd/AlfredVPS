---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2026-03-01'
date: '2025-11-10'
depends_on: []
description: null
due: null
janitor_note: LINK001 — Telia'z Clinic Israel wikilink is YAML single-quote escaping
  false positive (target verified to exist). Base view embed (related.base#All) references
  _bases/related.base which does not exist — create base file to enable dynamic views.
kind: task
name: Evaluate Platform Adaptation for Clalit Subscription Workflow
owner:
- '[[person/Dekkel Taliaz]]'
priority: medium
project: null
related: []
related_to:
- '[[org/Clalit Health Services]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]'
- '[[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]]'
- '[[person/Shachar]]'
relationships: []
run: null
status: todo
tags:
- clalit
- platform
- technical
- integration
type: task
---

# Evaluate Platform Adaptation for Clalit Subscription Workflow

## Objective

Determine whether the Telia'z platform needs adaptation to accommodate Clalit's subscription and referral workflow, given that the Clalit IT system is slower and heavier than Maccabi's system.

## Context

Discussed during the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]. The Clalit system was described as significantly slower than the Maccabi system that Telia'z currently integrates with. [[person/Shachar]] may need to evaluate platform adjustments.

## Evaluation Areas

1. API response time handling — does the platform need longer timeouts for Clalit?
2. Workflow differences between Clalit and Maccabi subscription models
3. Form 17 data format compatibility
4. BI system integration requirements
5. User interface adjustments for clinician-facing workflows

## Expected Output

Technical assessment with recommendations for any platform changes needed before the November 20, 2025 launch.

---
## Related
![[related.base#All]]
