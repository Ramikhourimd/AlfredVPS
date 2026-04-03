---
alfred_instructions: null
alfred_tags:
- maccabi/commitment-renewal
- retool/implementation
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on: []
description: Create workflow in Retool for patients to submit renewal commitment numbers
  after initial commitment expires, including validation against Maccabi portal, session
  balance tracking, and secretary approval flow
due: null
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide infrastructure gap.
kind: task
name: Build Commitment Renewal Workflow in Retool
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Alice]]'
relationships:
- confidence: 0.9
  context: Workflow requires terms clarity
  source: task/Build Commitment Renewal Workflow in Retool.md
  target: task/Clarify Maccabi Commitment Renewal Terms.md
  type: depends-on
- confidence: 0.8
  context: Workflow needs followup structure
  source: task/Build Commitment Renewal Workflow in Retool.md
  target: task/Clarify Maccabi Follow-Up Commitment Structure and Terms.md
  type: depends-on
run: null
status: todo
tags: []
type: task
---

# Build Commitment Renewal Workflow in Retool

Patients whose initial Maccabi commitment (intake + 16 case manager follow-ups + 4 psychiatric follow-ups) has been exhausted need a way to submit renewal commitment numbers. Currently there is no field or workflow in Retool to handle this.

## Context

- Original commitment numbers auto-populate from the patient questionnaire into Retool
- Renewal commitments arrive separately and have no entry point
- Secretaries must validate each commitment against the Maccabi web portal before approving
- At least one patient has already sent a renewal commitment with nowhere to enter it

## Requirements

1. Input field in Retool for renewal commitment numbers
2. Validation workflow matching the original commitment process
3. Session balance counter update when new commitment is entered
4. Integration with existing billing/payment request workflow

## Dependencies

- Alice must first clarify exact renewal commitment structure with Maccabi (session count, terms)

## Related
![[related.base#All]]

## Outcome

*Filled in on completion.*