---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by: []
based_on: []
challenged_by: []
confidence: medium
created: '2026-02-03'
decided_by:
- '[[person/Ohad Edri]]'
janitor_note: 'FIXED: Removed duplicate learn-decision.base#Based On and learn-decision.base#Related
  embeds (each appeared twice). LINK001: project wikilink [[project/Telia''z AI Clinical
  Platform]] uses YAML apostrophe escaping (Telia''''z) which is valid, not broken.
  LINK001: learn-decision.base embeds reference _bases/ infrastructure not yet created
  — vault-wide gap, not per-file fix.'
name: Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/AI Agent Pipeline Training Session 2026-02-03]]'
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[task/Define Comprehensive Patient Data API Endpoint]]'
- '[[person/Shachar]]'
session: null
source: Ohad Edri during training session
source_date: '2026-02-03'
status: draft
supports: []
tags: []
type: decision
---

# Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints

## Context

As the AI agent pipeline grows, each agent requires different combinations of patient data. The team needs to decide how agents access patient information through Shachar's API infrastructure.

## Options Considered

1. **Per-agent API endpoints** — Build a separate API endpoint for each agent type, returning only the specific data fields that agent needs (e.g., gender + age + questionnaire for post-general).
2. **Single comprehensive patient data API** — Build one API endpoint that returns all available data for a patient, letting each agent select what it needs from the full dataset.

## Decision

Ohad expressed preference for Option 2 — a single comprehensive API that returns all available patient data per patient identifier.

## Rationale

- Reduces API surface area and maintenance burden
- Agents can independently evolve their data requirements without API changes
- Simpler integration — only one endpoint to understand and maintain
- Shachar's existing Patient Export already contains all data per patient, suggesting the data model supports this approach

## Consequences

- Larger payload per API call (all data returned even if agent only needs a subset)
- Agents need logic to select relevant fields from the full response
- Single point of failure if the comprehensive endpoint breaks

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]