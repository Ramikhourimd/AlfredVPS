---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2025-11-10'
depends_on: []
description: Build a referral form template button in the psychiatrist clinical workflow,
  similar to the existing AI summary star button. Default delivery via app/Clickx,
  with emergency email override option.
due: null
janitor_note: '"LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive, target verified). Base view embed (\![[related.base#All]]) references
  _bases/related.base which does not exist — create base file to enable dynamic views."'
kind: task
name: Build ER Referral Form Template Feature
priority: medium
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Build ER Referral Form Feature for Psychiatrists]]'
- '[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]'
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
- '[[person/Shachar]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Build ER Referral Form Template Feature

Build a psychiatrist-facing feature to generate emergency referral letters (הפניה למיון) from within the clinical platform.

## Context

Decided in [[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]. Psychiatrists need the ability to generate formal referral letters when sending patients to the ER. The feature should follow the same UX pattern as the existing AI summary "star" button.

## Requirements

- Referral letter template with standard clinical fields
- Button in psychiatrist workflow screen
- Default delivery: upload to HealthyMind app / Clickx system
- Emergency override: option to send via email for urgent cases
- Avoid triggering Maccabi HMO objections to email-based documents

## Related
![[related.base#All]]

## Outcome

Filled in on completion.
