---
approved_by: []
based_on:
- '[[conversation/Alfred Chat — No, I dont have access to the web 2026-03-31]]'
challenged_by: []
confidence: high
created: '2026-03-31'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — conversation/Alfred Chat — No, I dont have access to the
  web 2026-03-31 target not found (may not exist or filename mismatch). learn-decision.base
  embeds (#Based On, #Related) reference non-existent _bases/learn-decision.base —
  vault-wide infrastructure gap, embeds preserved. ORPHAN001 — no inbound wikilinks,
  new decision record. Swept 2026-03-31.'
name: Use Claude Sonnet 4.6 via OpenRouter as Alfred LLM Backend
project:
- '[[project/Alfred Development]]'
related: []
session: null
source: Revealed in chat session
source_date: '2026-03-31'
status: final
supports: []
tags: []
type: decision
---

# Use Claude Sonnet 4.6 via OpenRouter as Alfred LLM Backend

## Context

Alfred needed an LLM backend to power conversations. The choice of model and access method affects cost, latency, capability, and vendor lock-in.

## Options Considered

1. **Direct Anthropic API** — Claude models accessed directly
2. **OpenRouter** — Multi-model gateway providing access to Claude and other models
3. **Other LLM providers** — OpenAI, Google, etc.

## Decision

Alfred uses Anthropic's Claude Sonnet 4.6, accessed via OpenRouter as the routing layer.

## Rationale

OpenRouter provides flexibility to switch models without code changes, while Claude Sonnet 4.6 offers strong reasoning and tool-use capabilities suited for a vault assistant. The routing layer adds model portability.

## Consequences

- Alfred benefits from Claude's strong structured output and tool-calling capabilities
- OpenRouter adds a layer of abstraction enabling future model swaps
- Dependency on both Anthropic (model) and OpenRouter (routing)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
