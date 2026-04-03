---
alfred_tags:
- clinical-systems/next-gen
- prototyping/strategy
- innovation/vision
approved_by: []
based_on:
- '[[note/Innovation Team Meeting Clinical Workloads AI Tools and Complex Patient
  Framework 2026-03-17]]'
challenged_by: []
confidence: high
created: '2026-03-31'
decided_by:
- '[[person/Rami Khouri]]'
name: Innovation Department Architecture Based on Three AI Agent Archetypes
project:
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Ohad Edri]]'
- '[[person/Rivi Idelman]]'
session: null
source: Rami Khouri strategic vision, 2026-03-17 innovation meeting
source_date: '2026-03-17'
status: draft
supports:
- '[[decision/Innovation Team Adopts No-Code Tools for Rapid System Development]]'
tags: []
type: decision
---

# Innovation Department Architecture Based on Three AI Agent Archetypes

## Context

Rami outlined the innovation department's strategic vision during the 2026-03-17 meeting. The department needs a unifying architectural framework that maps individual innovation projects (complex patient screening, KPIs, clinical summaries) onto a coherent system design.

## Options Considered

1. **Project-by-project approach** — each innovation project builds its own standalone solution
2. **Unified three-archetype architecture** — all projects map onto a common framework of collector, analyzer, and presenter agents

## Decision

The innovation department will build a smart system organized around three AI agent archetypes:
1. **Collector** — agents that gather all clinical information (real-time during sessions or continuously in background)
2. **Analyzer** — agents that process and interpret collected data (fastest/smartest processing)
3. **Presenter** — agents that display analyzed information to clinical decision-makers

Multiple agents work in parallel, some real-time during sessions, some running continuously. Behind the patient-facing chatbot: full live communication between all clinical actors.

## Rationale

Each innovation project maps naturally onto this spectrum. Complex patient screening is primarily a collector+analyzer problem. KPI dashboards are analyzer+presenter. AI summaries span all three. The architecture provides a coherent framework rather than a collection of one-off solutions.

## Consequences

- Every innovation project must be framed in terms of which archetype(s) it serves
- Creates a shared vocabulary for the team (collector/analyzer/presenter)
- Enables integration between projects that share the same archetype layer
- Innovation team's responsibility is differentiated IP for company valuation at exit — operational fixes belong to R&D/product team

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]