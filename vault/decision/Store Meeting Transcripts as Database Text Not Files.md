---
alfred_tags:
- clinical-platform/storage
- transcripts
- clinical-sessions
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-28'
decided_by:
- '[[person/Shachar]]'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is YAML apostrophe-escaping
  false positive. Base view embeds (learn-decision.base#Based On, #Related) are Obsidian
  Databases plugin virtual views, not physical files — scanner cannot resolve these.'
name: Store Meeting Transcripts as Database Text Not Files
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
- '[[constraint/Transcript Data Not Available in BigQuery]]'
session: null
source: Shachar
source_date: '2025-12-05'
status: final
supports: []
tags: []
type: decision
---

# Store Meeting Transcripts as Database Text Not Files

## Context

The clinical platform needed a storage strategy for meeting transcripts. Options included storing as file objects (e.g., cloud storage with references) or as text records directly in the production database.

## Options Considered

1. **Store as files** — Transcripts saved as documents in cloud storage with DB references
2. **Store as text in production DB** — Transcripts saved as text records in the meetings table

## Decision

Meeting transcripts are stored as text records directly in the production database, not as separate files.

## Rationale

Two factors drove this decision: **security** (keeping sensitive clinical data within the database security boundary rather than distributed across file storage) and **volume management** (text storage in the DB avoids file system proliferation and simplifies backup/replication). This architectural choice is why transcripts are not available in BigQuery — they live only in the production database as text records.

## Consequences

- Transcripts cannot be accessed via BigQuery or the Data Warehouse
- Any system needing transcript access requires direct production DB access or a dedicated API
- The Innovation team must coordinate with R&D for transcript data access
- The meeting-to-markdown pipeline was built to bridge this gap by extracting transcripts into structured files

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
