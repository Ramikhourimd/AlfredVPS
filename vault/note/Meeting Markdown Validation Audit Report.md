---
alfred_tags:
- meetings/data-validation
- data-pipelines/audit
- data-quality/readiness
created: '2026-02-26'
description: DUPLICATE — see note/Meeting Data Validation Audit Report 2026-02-26
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — systemic issue. Embeds preserved.
name: Meeting Markdown Validation Audit Report
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[org/Telia''z]]'
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
- '[[task/Provide Rami Direct Access to Meeting Transcripts]]'
relationships:
- confidence: 0.9
  context: Companion validation reports
  source: note/Meeting Markdown Validation Audit Report.md
  target: note/Meeting Transcript Validation Audit Report 2026-02-26.md
  type: related-to
- confidence: 0.9
  context: Meeting validation audits
  source: note/Meeting Markdown Validation Audit Report.md
  target: note/Meeting Transcript Validation Audit Report.md
  type: related-to
- confidence: 0.8
  context: Audit supports ingestion
  source: note/Meeting Markdown Validation Audit Report.md
  target: task/Ingest 338 Remaining Meetings Into Supabase Knowledge Base.md
  type: supports
- confidence: 0.8
  context: Audit supports ingestion
  source: note/Meeting Markdown Validation Audit Report.md
  target: task/Ingest Remaining 338 Meetings Into Supabase Knowledge Base.md
  type: supports
- confidence: 0.9
  context: Audit supports pipeline synthesis
  source: note/Meeting Markdown Validation Audit Report.md
  target: synthesis/Meeting Data Pipeline Is Production-Ready but Ingestion Backlog
    Limits Utility.md
  type: supports
- confidence: 0.75
  context: Supports data quality findings
  source: note/Meeting Markdown Validation Audit Report.md
  target: synthesis/Feature Technical Readiness Outpaces Data Quality and Operational
    Process Readiness.md
  type: supports
session: null
status: draft
subtype: reference
tags: []
type: note
---

# Meeting Markdown Validation Audit Report

## Context

This audit validates the pipeline that generates structured markdown files from meeting recordings stored as Google Docs. The 401 source meetings were tracked in an Excel file and processed into individual markdown files with standardized structure. The audit compares these files against the Supabase `meeting_metadata` knowledge base table.

## Key Findings

### Completeness: 100% (401/401)
- All 401 meeting files were successfully generated
- 400 files contain full transcript content
- 1 file (Row 371, dated 2026-01-22) contains minimal content — verified as accurate reflection of the source Google Doc (only 50 characters)

### Structural Integrity: 100%
Every file contains all four required sections:
1. **Meeting Details table** — date, title, classification, category, meeting type, source URL
2. **Participants table** — name, role, confidence score
3. **Key Topics** — bullet list of discussion topics
4. **Full Transcript** — with speaker names replacing generic labels

### Knowledge Base Coverage: 15.7%
- **63 of 401 meetings** (15.7%) have matching records in the Supabase `meeting_metadata` table
- **338 meetings** (84.3%) are not yet ingested into the KB
- This gap is expected — the Excel source contains a broader set of meetings than what has been processed into the knowledge base

## Implications

1. The meeting markdown generation pipeline is validated and production-ready
2. The 338 meetings not yet in KB represent a significant ingestion backlog
3. The structured format (4 sections with speaker-attributed transcripts) provides a solid foundation for downstream AI processing
4. Data quality is high — only 1 file has minimal content, and that accurately reflects the source

## Related
![[related.base#All]]