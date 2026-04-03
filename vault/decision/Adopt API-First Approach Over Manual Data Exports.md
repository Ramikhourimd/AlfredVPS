---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist (vault-wide issue). Duplicate
  base embeds at bottom of body — remove one set manually. Telia''z wikilinks are
  valid (YAML escaping false positive).'
name: Adopt API-First Approach Over Manual Data Exports
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[org/Telia''z]]'
session: null
source: Product meeting consensus
source_date: '2026-02-25'
status: final
supports: []
tags: []
type: decision
---

# Adopt API-First Approach Over Manual Data Exports

## Context

Data for research, reporting, and AI orchestration has been extracted via manual Excel exports from Shmulik. This creates delays, inconsistencies, and makes automated pipelines impossible.

## Options Considered

1. **Option A** — Continue with manual exports supplemented by ad-hoc scripts
2. **Option B** — Build stable, documented APIs for all data access needs

## Decision

Option B: All data access flows through stable, versioned APIs. Low-level entity APIs per resource: Get Patient, Get Meeting (Transcript/Summary/Diagnosis/Prescription), Get Questionnaire. All endpoints support pagination and payload limits.

## Rationale

APIs enable automation, reproducibility, and transparency. Research pipelines, AI orchestration, and reporting all benefit from consistent, authenticated data access. Manual exports are error-prone and create bottlenecks on Shmulik's time.

## Consequences

- R&D must deliver full API schemas with parameter documentation
- Access controls, logging, and anomaly detection required per endpoint
- Existing manual export workflows can be gradually retired
- Enables future MCP/orchestrator integration

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
