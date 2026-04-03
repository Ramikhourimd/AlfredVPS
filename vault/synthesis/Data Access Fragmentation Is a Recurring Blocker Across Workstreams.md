---
alfred_tags:
- process/fragmentation
- documentation/duplication
cluster_sources:
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
- '[[constraint/Transcript Data Not Available in BigQuery]]'
- '[[constraint/Questionnaire Data Not Available in BigQuery]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
- '[[task/Provide Rami Direct Access to Meeting Transcripts]]'
- '[[task/Provide Rami Direct Access to Session Transcripts]]'
- '[[task/Verify Pricing Table Location in BigQuery DWH]]'
confidence: high
created: '2026-02-26'
janitor_note: 'LINK001 — Teliaz wikilinks are YAML-escape false positives (Telia''''z
  = Telia''z). Base view embeds (learn-synthesis.base#Sources, #Related) reference
  _bases/learn-synthesis.base which does not exist — vault-wide infrastructure gap,
  embeds preserved. ORPHAN001 — no inbound links from other records.'
name: Data Access Fragmentation Is a Recurring Blocker Across Workstreams
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related: []
relationships:
- confidence: 0.8
  context: Fragmentation blocker and redundancy
  source: synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams.md
  target: synthesis/Repetitive Testing Workflows Generate Redundant Vault Records.md
  type: related-to
- confidence: 0.75
  context: Fragmentation and task repetition
  source: synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams.md
  target: synthesis/UK Launch Tasks Repeatedly Created Without Resolution Indicating
    Execution Tracking Gap.md
  type: related-to
status: draft
supports:
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
- '[[decision/Implement Read-Only Shadow DB for Analytics]]'
- '[[decision/Design APIs as Low-Level Entity Endpoints with Sub-Resources]]'
tags: []
type: synthesis
---

# Data Access Fragmentation Is a Recurring Blocker Across Workstreams

## Insight

Clinical data is scattered across multiple systems with no unified access layer, and this fragmentation surfaces as a blocker in nearly every workstream — research, AI pipeline development, reporting, and operational analytics. The pattern is consistent: each new initiative discovers that the data it needs lives somewhere inaccessible.

## Evidence

Across at least 4 source records spanning December 2025 to February 2026:

1. **Transcripts** — stored only in production DB, not in BigQuery (two separate constraints recorded)
2. **Questionnaires** — not replicated to BigQuery, requiring manual exports or production DB access
3. **Pricing tables** — location in BigQuery/DWH unverified, task created to find them
4. **General DWH** — access described as "partial and lacking full standardization"
5. **Manual exports** — Rami must request data from Shmulik each time, creating bottlenecks
6. **Two separate tasks** created for transcript access alone (session transcripts and meeting transcripts)

## Implications

- The API-first decision and Shadow DB decision are both responses to this fragmentation
- Until a unified data access layer exists, every new project will hit the same wall
- The fragmentation is not just technical — it creates human bottlenecks (Shmulik/Shachar as gatekeepers)
- Prioritizing the API layer and Shadow DB would unblock multiple workstreams simultaneously
- Research paper timelines are particularly at risk since they depend on data Rami cannot access independently

## Applicability

Applies to all projects that consume clinical data: the AI Clinical Platform, the Diagnostic Research Paper, and any future analytics or quality improvement initiatives. This is a foundational infrastructure problem, not a project-specific one.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]