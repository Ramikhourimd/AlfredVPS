---
alfred_tags:
- clinical-platform/storage
- transcripts
- clinical-sessions
approved_by: []
based_on:
- '[[note/Meeting Transcript Validation Audit Report]]'
- '[[note/Meeting Data Validation Audit Report 2026-02-26]]'
- '[[note/Meeting Transcript Validation Audit Report 2026-02-26]]'
challenged_by: []
confidence: high
created: '2026-03-03'
decided_by: []
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is YAML escaping false
  positive. Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — vault-wide infrastructure issue, embeds preserved. ORPHAN001
  — no inbound wikilinks; may need linking from parent project or related records.'
name: Four-Section Structured Format for Meeting Markdown Files
project:
- '[[project/Telia''z AI Clinical Platform]]'
related: []
relationships:
- confidence: 0.6
  context: Session text handling policies
  source: decision/Four-Section Structured Format for Meeting Markdown Files.md
  target: decision/Retain Only Text Summaries Not Audio or Video From Clinical Sessions.md
  type: related-to
- confidence: 0.85
  context: MD files vs DB text storage
  source: decision/Four-Section Structured Format for Meeting Markdown Files.md
  target: decision/Store Meeting Transcripts as Database Text Not Files.md
  type: contradicts
session: null
source: Meeting transcript validation audit
source_date: null
status: final
supports: []
tags: []
type: decision
---

# Four-Section Structured Format for Meeting Markdown Files

## Context

The clinical platform needed a standardized format for converting meeting recordings (stored as Google Docs) into structured markdown files suitable for AI processing, search, and knowledge base ingestion. A format decision was needed to ensure consistency across all 401+ meeting files.

## Options Considered

1. **Unstructured markdown** — Free-form transcript text with minimal formatting
2. **Four-section structured format** — Standardized sections with metadata tables, topic lists, and speaker-attributed transcripts

## Decision

All meeting markdown files follow a mandatory four-section structure:
1. **Meeting Details table** — date, title, classification, category, meeting type, source URL
2. **Participants table** — name, role, confidence score
3. **Key Topics** — bullet list of discussion themes
4. **Full Transcript** — with speaker names replacing generic labels

## Rationale

The structured format enables reliable downstream processing: AI agents can parse specific sections, search can target metadata vs. content, and validation can verify completeness programmatically. All 401 generated files were validated against this structure with a 100% pass rate.

## Consequences

- Every new meeting file must conform to this 4-section schema
- Validation pipelines can programmatically verify structural completeness
- Speaker attribution (replacing generic labels with names) is a required processing step, not optional
- The format is the contract between the transcript generation pipeline and all downstream consumers (KB ingestion, AI agents, search)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]