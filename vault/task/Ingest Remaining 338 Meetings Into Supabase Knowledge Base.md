---
alfred_instructions: null
alfred_tags:
- meetings/validation
- supabase/ingestion
assigned: null
blocked_by: []
created: '2026-02-26'
depends_on: []
description: 338 of 401 validated meeting markdown files (84.3%) are not yet present
  in the Supabase meeting_metadata table. Ingest these files to bring KB coverage
  from 15.7% to 100%.
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is YAML escaping false
  positive (double single-quotes = literal apostrophe). Base view embed references
  non-existent _bases/related.base file — embed preserved per policy but base file
  missing.
kind: task
name: Ingest Remaining 338 Meetings Into Supabase Knowledge Base
priority: medium
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Meeting Transcript Validation Audit Report 2026-02-26]]'
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
- '[[note/Meeting Transcript Validation Audit Report]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Ingest Remaining 338 Meetings Into Supabase Knowledge Base

338 of 401 validated meeting markdown files are not yet present in the Supabase `meeting_metadata` table. The validation audit confirmed all files are structurally complete and data-accurate, so they are ready for ingestion.

## Context

The [[note/Meeting Transcript Validation Audit Report 2026-02-26]] confirmed 100% structural validity of all 401 meeting files. Current KB coverage is only 15.7% (63/401 meetings). Closing this gap brings the full meeting corpus into the knowledge base for querying, AI pipeline consumption, and analytics.

## Related
![[related.base#All]]

## Outcome

Filled in on completion — confirm final KB record count and any files that failed ingestion.
