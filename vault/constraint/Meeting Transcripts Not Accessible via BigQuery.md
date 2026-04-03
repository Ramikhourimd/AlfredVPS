---
alfred_tags:
- clinical-data/constraints
- dataset-limitations
- research-data-issues
authority: '[[person/Shachar]]'
created: '2025-12-05'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. All Telia''z wikilinks are valid (YAML escaping false positive).'
name: Meeting Transcripts Not Accessible via BigQuery
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[person/Rami Khouri]]'
- '[[conversation/Retool Improvements and Data Access Planning 2025-12-05]]'
source: Technical architecture — security and volume concerns
source_date: '2025-12-05'
status: active
type: constraint
---

# Meeting Transcripts Not Accessible via BigQuery

## Constraint

Clinical session meeting transcripts (meeting_text table) are stored in the production database as text records but are NOT replicated to BigQuery. Document IDs appear in the DWH, but the actual transcript content is inaccessible through BigQuery. Rami cannot access transcripts independently.

## Source

Shachar confirmed on 2025-12-05 that transcripts are excluded from BigQuery replication for two reasons:
1. **Security** — sensitive clinical content should not be broadly accessible
2. **Volume** — transcript data is too large for efficient BigQuery storage

Older transcripts were stored as files, but current architecture stores them directly as text in the database.

## Implications

- Rami's diagnostic research and AI analysis work requires transcript access, creating a dependency on Shachar for each data request
- Any automated pipeline needing transcript content must connect to the production database, not BigQuery
- A separate access mechanism (read-only view, API, or query tool) is needed

## Expiry / Review

Active until Shachar implements an access solution. Review when [[task/Provide Rami Direct Access to Meeting Transcripts]] is completed.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]