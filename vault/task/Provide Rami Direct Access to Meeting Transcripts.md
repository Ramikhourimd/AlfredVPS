---
alfred_instructions: null
assigned: '[[person/Shachar]]'
blocked_by: []
created: '2025-12-05'
depends_on: []
description: Find a solution for Rami to access meeting transcripts directly without
  requesting each time from Shachar. Transcripts are stored as text in the production
  database, not in BigQuery or as files.
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist — create base file to enable dynamic views.
kind: task
name: Provide Rami Direct Access to Meeting Transcripts
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool Improvements and Data Access Planning 2025-12-05]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Provide Rami Direct Access to Meeting Transcripts

Rami needs autonomous access to clinical session transcripts for research and analysis. Currently, transcripts are stored as text in the production database (not as files, not in BigQuery). Document IDs are visible in the DWH but the actual text content requires Shachar's intervention each time.

## Context

Security and volume concerns prevent copying transcripts to BigQuery. A separate access mechanism is needed — possibly a read-only view, an API endpoint, or a dedicated query tool.

Emerged from [[conversation/Retool Improvements and Data Access Planning 2025-12-05]].

## Related
![[related.base#All]]

## Outcome
