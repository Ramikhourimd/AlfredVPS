---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by: []
based_on:
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Ohad Edri]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist. Body has duplicate base view embeds
  (two sets of learn-decision.base#Based On and #Related after --- separator) — human
  must remove the duplicate set.'
name: Five-Agent Sequential Pipeline for Clinical AI Summaries
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/All Case Manager Questions Delivered Dynamically From Prompt]]'
- '[[task/Create AI Agent Inventory and Input-Output Breakdown]]'
session: null
source: Ohad Edri, AI Agent Pipeline Training Session
source_date: '2026-02-03'
status: final
supports:
- '[[decision/Standardize AI Summary Output as Structured JSON]]'
- '[[assumption/Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline]]'
tags: []
type: decision
---

# Five-Agent Sequential Pipeline for Clinical AI Summaries

## Context

The AI clinical platform needed a defined architecture for how AI agents process patient encounters. Each encounter type (intake, follow-up) requires different combinations of summarization, agenda generation, triage, and cross-session analysis.

## Options Considered

1. **Monolithic single-agent approach** — One large prompt handles all summarization
2. **Specialized sequential pipeline** — Dedicated agents for each stage, running in sequence
3. **Parallel agent execution** — Multiple agents processing simultaneously

## Decision

The platform runs five specialized AI agents in a sequential pipeline:
1. **CM Agenda Agent** — Transforms intake questionnaire responses into personalized follow-up questions
2. **CM Summary Agent** — Produces a summary of the case manager intake session
3. **Triage Agent** — Classifies and routes patient information
4. **Cross-Session Agent** — Handles data continuity across multiple sessions
5. **Patient Summary (prod)** — Generates a pre-session summary for the psychiatrist's follow-up

Each agent produces two output types: a standard summary and a specialized output.

## Rationale

Specialized agents allow each stage to be independently tuned, tested, and improved. The CM Agenda Agent specifically avoids repeating basic questions by transforming questionnaire answers into deeper, context-aware follow-up questions. Variable injection populates prompts with patient-specific data (gender, age, health data, questionnaire responses).

## Consequences

- Each agent's inputs and outputs must be formally documented (assigned to Eli)
- New agents (e.g., file classification) must fit into or extend this pipeline
- Pipeline changes require coordination across multiple prompts
- Simple orchestrator pattern is sufficient for now (no MCP needed)

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]