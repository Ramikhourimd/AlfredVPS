---
alfred_tags:
- healthcare/operations
- staff/issue-management
- proactive/problem-detection
approved_by: []
based_on: []
challenged_by: []
confidence: medium
created: '2026-03-08'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — embeds preserved per policy. Body has DUPLICATE base view
  embeds — needs manual dedup (remove second set after ---). note/Conference Discussion
  and synthesis/Remote Telepsychiatry links VERIFIED VALID. ORPHAN001 — no inbound
  wikilinks; consider linking from project/Telia''z Innovation Program.'
name: Build Frustration Detection Agent to Route Staff Issues Automatically
project:
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic Scale
  2025-11-13]]'
- '[[constraint/Staff WhatsApp Messages Frequently Go Unanswered]]'
- '[[synthesis/Remote Telepsychiatry Creates Structural Isolation Beyond Communication
  Fixes]]'
relationships:
- confidence: 0.9
  context: Both analyze convos for proactive issue handling
  source: decision/Build Frustration Detection Agent to Route Staff Issues Automatically.md
  target: decision/Deploy Conversation Analysis Dashboard for Proactive Problem Identification.md
  type: related-to
- confidence: 0.75
  context: Both improve staff/operational issue routing
  source: decision/Build Frustration Detection Agent to Route Staff Issues Automatically.md
  target: decision/Empower Renee to Report Operational Issues Directly to Management.md
  type: related-to
session: null
source: Rami Khouri
source_date: '2025-11-13'
status: draft
supports:
- '[[synthesis/Staff Isolation Is Systemic Risk Across All Clinical Roles]]'
tags: []
type: decision
---

# Build Frustration Detection Agent to Route Staff Issues Automatically

## Context

Clinical staff frustrations and complaints are surfaced in team meetings but often go unresolved because they are not routed to the correct organizational function. WhatsApp messages frequently go unanswered, and remote staff lack visibility into whether their issues are being addressed.

## Options Considered

1. **Manual triage by clinic manager** — Shira or Basel manually reviews meeting notes and routes issues
2. **Structured feedback form** — Staff submit issues through a form with category selection
3. **AI agent that monitors meeting content** — Automated detection and routing

## Decision

Build an AI frustration detection agent that monitors staff meeting content, identifies issues, proposes solutions, and routes each issue to the appropriate organizational function — framework coordinator, clinical manager, or innovation team.

## Rationale

Automated detection and routing addresses two systemic problems simultaneously: (1) staff frustrations going unheard in the remote work environment, and (2) issues reaching the wrong person and stalling. The AI agent can process meeting content faster and more consistently than manual review.

## Consequences

- Faster issue resolution by routing to the correct function immediately
- Staff may feel more heard if issues are acknowledged and tracked automatically
- Requires integration with meeting recording/transcription infrastructure
- Creates a data trail of recurring issues that can inform operational improvements

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]