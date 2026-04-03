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
janitor_note: 'Body contains duplicate base view embeds: learn-decision.base#Based
  On and learn-decision.base#Related each appear twice (once in main body, once after
  a --- separator). Remove the duplicate block after the --- separator manually. Base
  view embeds themselves reference _bases/ files that do not exist yet (vault-wide
  gap).'
name: Sequential Multi-Agent Pipeline for Clinical Encounters
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Standardize AI Summary Output as Structured JSON]]'
- '[[decision/Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints]]'
session: ''
source: Ohad Edri training session demonstrating the live pipeline
source_date: '2026-02-03'
status: final
supports:
- '[[assumption/Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline]]'
tags: []
type: decision
---

# Sequential Multi-Agent Pipeline for Clinical Encounters

## Context

The AI clinical platform needs to process each patient encounter through multiple analytical lenses — intake agenda generation, session summarization, triage classification, cross-session continuity, and pre-appointment briefing. The team needed to decide whether to run these as independent agents or as a coordinated pipeline.

## Options Considered

1. **Sequential multi-agent pipeline** — Five agents run in sequence per encounter, each receiving outputs from prior agents as additional context
2. **Independent parallel agents** — Each agent runs independently against raw patient data
3. **Single monolithic agent** — One large prompt handles all analytical tasks

## Decision

Adopted a sequential multi-agent pipeline with five stages: CM Agenda Agent → CM Summary Agent → Triage Agent → Cross-Session Agent → Patient Summary Agent. Each agent produces two output types (standard summary + specialized output). Prompts use variable injection with patient-specific data populated at runtime.

## Rationale

Sequential execution allows each agent to build on prior outputs, improving context quality. The fixed structural template with dynamic question adaptation balances consistency with personalization. Two output types per agent allow different consumers (clinicians vs. system) to use appropriate formats.

## Consequences

- Pipeline latency scales linearly with agent count — adding agents increases total processing time
- Agent ordering matters — downstream agents depend on upstream outputs
- Each agent's prompt must be maintained independently, requiring an agent inventory
- New team members need structured onboarding to understand the full pipeline (as demonstrated in the 2026-02-03 training session)

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]