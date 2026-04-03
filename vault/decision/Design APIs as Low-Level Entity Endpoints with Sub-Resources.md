---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by: []
based_on:
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Shmulik]]'
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist. Create it to enable dynamic
  views. Body has DUPLICATE base view embeds (appears twice) — remove one set manually.
  Telia''z wikilinks are valid (YAML escaping false positive).'
name: Design APIs as Low-Level Entity Endpoints with Sub-Resources
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Implement Read-Only Shadow DB for Analytics]]'
- '[[constraint/Questionnaire Data Not Available in BigQuery]]'
session: ''
source: Product meeting consensus
source_date: '2026-02-25'
status: draft
supports:
- '[[task/Deliver Full API Schemas for Clinical Platform]]'
tags: []
type: decision
---

# Design APIs as Low-Level Entity Endpoints with Sub-Resources

## Context

Having decided on an API-first approach over manual data exports, the team needed to define the actual API architecture — how endpoints should be structured, what granularity to use, and how to handle related data.

## Options Considered

1. **High-level composite endpoints** — Single endpoints that return aggregated views (e.g., full patient record with all history)
2. **Low-level entity endpoints with sub-resources** — Granular entity APIs where related data is accessed through sub-resource paths

## Decision

Design the API as low-level entity endpoints with sub-resources. Core entities include:
- **Get Patient** — base patient record
- **Get Meeting** — with sub-resources for Transcript, Summary, Diagnosis, Prescription
- **Pagination** required for high-volume reads
- **Report API** with defined field scope (pending Rami's approval)

## Rationale

Low-level entity APIs provide flexibility for different consumers (AI pipeline, analytics, clinical UI, research). Sub-resources keep payloads focused and allow selective data loading. Pagination prevents performance issues on high-volume endpoints.

## Consequences

- Each entity and sub-resource needs its own schema definition
- The AI orchestration pipeline can fetch only the data it needs per step
- Research queries can compose from building blocks rather than requesting custom exports
- More endpoints to maintain, but each is simpler and more cacheable

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]