---
approved_by: []
based_on:
- '[[task/Define Complex Patient Protocol Criteria]]'
challenged_by: []
confidence: medium
created: '2026-03-31'
decided_by:
- '[[person/Rivi Idelman]]'
janitor_note: 'LINK001 — Telia''z wikilink is YAML single-quote escaping false positive
  (project/Telia''z Innovation Program exists). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist — vault-wide
  infrastructure gap, embeds preserved. ORPHAN001 — no inbound wikilinks; consider
  linking from project/Telia''z Innovation Program.'
name: Use Manus AI for Complex Patient Triage Prototype
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[task/Build Front-End Prototype for Complex Patient Triage Using Manus AI]]'
- '[[task/Complete Optica Template Chapters 1 and 2 for Complex Patient Project]]'
- '[[conversation/Innovation Team Meeting Clinical Workloads and AI Tools 2026-03-17]]'
session: null
source: Innovation team meeting
source_date: '2026-03-17'
status: draft
supports: []
tags: []
type: decision
---

# Use Manus AI for Complex Patient Triage Prototype

## Context

The complex patient triage project needed a front-end prototype to visualize the screening and routing workflow. The team needed to choose a prototyping approach.

## Options Considered

1. **Traditional design tools** — Figma, manual wireframing
2. **AI-assisted prototyping with Manus AI** — rapid generation of interactive front-end prototypes
3. **Developer-built prototype** — custom code from engineering

## Decision

Use Manus AI to build the front-end prototype for the complex patient triage system. This aligns with the innovation team's pattern of adopting no-code/AI tools for rapid system development.

## Rationale

Manus AI enables rapid prototyping without requiring dedicated engineering resources from the CTO team. Consistent with the existing decision to use no-code tools for innovation projects (Make.com, n8n pattern). Allows Rivi to iterate on concept design independently.

## Consequences

- Faster prototype iteration cycles
- Prototype quality depends on Manus AI capabilities for clinical UX
- May need engineering rebuild for production implementation

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
