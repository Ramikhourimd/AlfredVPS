---
alfred_instructions: null
assigned: '[[person/Shachar]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Find a solution for Rami to independently access clinical session transcript
  texts, which are stored in the production database (not BigQuery). Currently Rami
  must request transcripts from Shachar each time.
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist. Create it to enable dynamic views.
kind: task
name: Provide Rami Direct Access to Session Transcripts
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[person/Rami Khouri]]'
- '[[constraint/Transcript Data Not Available in BigQuery]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Provide Rami Direct Access to Session Transcripts

Rami needs independent access to clinical session transcript texts for research, quality review, and AI development work. Currently:

- Structured patient data is in BigQuery and accessible
- Transcript texts are stored only in the production database (not as files anymore)
- The meeting_text table has file IDs but the actual content lives in the database
- Shachar does not replicate transcripts to BigQuery for security and data volume reasons
- Every time Rami needs transcripts, he must request them from Shachar manually

Shachar committed to finding a solution.

## Context

Raised in [[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]. Critical for [[project/Telia'z AI Diagnostic Research Paper]] and ongoing clinical quality work.

## Related
![[related.base#All]]

## Outcome

Pending — Shachar to propose an access mechanism.
