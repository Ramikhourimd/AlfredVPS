---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by: []
janitor_note: '"LINK001 — broken base view embeds: \![[learn-decision.base#Based On]]
  and \![[learn-decision.base#Related]]. The file _bases/learn-decision.base does
  not exist. Create it or remove the embeds. Do NOT auto-remove — base view embeds
  require human decision."'
name: Unified Operational System Over Specialized Tools
project: []
related: []
session: null
source: Start Here.md introductory description
source_date: null
status: final
supports: []
tags: []
type: decision
---

# Unified Operational System Over Specialized Tools

## Context

Alfred OS needed a foundational architectural direction: build on top of multiple specialized tools (CRM, project manager, email client) or unify everything into a single connected system within Obsidian.

## Options Considered

1. **Specialized tools** — Use best-of-breed tools for each domain (CRM, PM, email) and integrate them
2. **Unified system in Obsidian** — Model everything as structured records in a single vault with an AI assistant

## Decision

Build a unified operational system in Obsidian. As stated in Start Here.md: "Not a project management tool. Not a CRM. Not an email client. All of those things — unified, connected, and intelligent."

## Rationale

A unified system eliminates context-switching between tools, prevents data duplication, and enables an AI assistant to reason across all operational data through a single graph of connected records.

## Consequences

- All operational data must be expressible as vault records with frontmatter metadata
- The system's value depends on Obsidian remaining a viable platform
- Record types must be comprehensive enough to cover all domains (PM, CRM, comms, knowledge)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
