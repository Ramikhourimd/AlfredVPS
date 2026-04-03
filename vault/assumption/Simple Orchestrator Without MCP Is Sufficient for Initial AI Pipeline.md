---
confidence: medium
created: '2026-02-25'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is a false positive
  (YAML single-quote escaping; file exists). Base view embeds (learn-assumption.base#Depends
  On This, #Related) require _bases/learn-assumption.base to be created — embeds preserved.'
name: Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[decision/Standardize AI Summary Output as Structured JSON]]'
source: Product meeting discussion
source_date: '2026-02-25'
status: active
type: assumption
---

# Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline

## Claim

The initial AI summary orchestration pipeline can run with a simple, deterministic orchestrator without implementing MCP (Model Context Protocol). MCP should be deferred to later phases when chatbot and advanced orchestration needs arise.

## Basis

The current summary generation flow is relatively linear (trigger -> collect data -> generate summary -> return/push). Complex decision trees and dynamic tool selection are not yet required. Starting simple reduces development risk and time-to-pilot.

## Evidence Trail

- 2026-02-25: Product meeting agreed to start without MCP, keep it as an option for future chat integration

## Impact

- AI pipeline can be built and piloted faster
- Architecture must remain MCP-compatible for future extension
- Chat/advanced orchestration features are deferred

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
