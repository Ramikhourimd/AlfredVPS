---
alfred_tags:
- clinical-data/constraints
- dataset-limitations
- research-data-issues
authority: CTO (Shachar) — data security policy
created: '2026-02-25'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive,
  targets exist). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist — create base file to
  enable dynamic views.
name: Transcript Data Not Available in BigQuery
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[task/Provide Rami Direct Access to Session Transcripts]]'
- '[[person/Shachar]]'
source: Data architecture — security and volume restrictions
source_date: '2025-12-05'
status: active
type: constraint
---

# Transcript Data Not Available in BigQuery

## Constraint

Clinical session transcript texts (from the meeting_text table) are not replicated to BigQuery. They exist only in the production database. This means anyone needing transcript data (e.g., for research, AI training, quality review) must request it from the CTO directly.

## Source

CTO (Shachar) confirmed during the 2025-12-05 planning call that transcript data is intentionally excluded from BigQuery replication for two reasons:
1. **Security** — transcript texts contain sensitive patient clinical content
2. **Volume** — the data volume is too large for cost-effective BigQuery storage

The meeting_text table has file identifiers, but the actual text content is stored in the database, not as files.

## Implications

- Rami cannot independently conduct transcript-based research or AI model training
- Every transcript request creates a dependency on Shachar's availability
- Blocks autonomous progress on the AI Diagnostic Research Paper transcript analysis
- May need a purpose-built access solution (read-only view, API, or scoped export tool)

## Expiry / Review

Active until Shachar implements a direct access mechanism for authorized users.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]