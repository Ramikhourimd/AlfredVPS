---
alfred_tags:
- clinical-data/constraints
- research/dataset-limitations
authority: System architecture
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — create it to enable dynamic views.'
location: []
name: Questionnaire Data Not Available in BigQuery
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
source: Shachar (CTO) confirmation
source_date: '2025-12-05'
status: active
tags: []
type: constraint
---

# Questionnaire Data Not Available in BigQuery

## Constraint

Clinical questionnaire data is not replicated to BigQuery. While most structured patient and session data is available in the DWH, questionnaire responses and configurations remain only in the production database. This is a separate gap from the transcript access limitation.

## Source

Shachar confirmed during the Retool prioritization discussion on 2025-12-05 that BigQuery contains most structured data columns but NOT questionnaire data or meeting transcripts.

## Implications

- Questionnaire-based analysis and research requires direct production DB access or manual exports
- AI summary pipelines that need questionnaire context cannot source it from BigQuery
- The API-first approach will need to include questionnaire endpoints to bridge this gap
- Compounds the existing data fragmentation problem alongside transcript and pricing table gaps

## Expiry / Review

Review when the API-first design is implemented — questionnaire APIs may provide an alternative access path.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]