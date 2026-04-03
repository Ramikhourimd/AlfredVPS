---
approved_by: []
based_on:
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Shachar]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML apostrophe escaping false
  positive). Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — embeds preserved. DUPLICATE base view embeds at end of body
  — two sets of learn-decision.base embeds exist. ORPHAN001 — no inbound wikilinks;
  consider linking from project or conversation records.'
name: Rebuild Clinic Management Platform from Scratch
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Compile Retool Improvement Priority List]]'
- '[[task/Fix Retool Login Issue for Psychiatrists]]'
session: ''
source: Shachar (CTO)
source_date: '2025-12-05'
status: final
supports:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
tags: []
type: decision
---

# Rebuild Clinic Management Platform from Scratch

## Context

The existing Retool-based case management system has accumulated significant technical debt — login issues for psychiatrists, broken Teams integration, missing KPI dashboards, and limited extensibility. Iterating on the existing Retool system was considered insufficient.

## Options Considered

1. **Iterate on existing Retool system** — Fix issues within the current platform
2. **Rebuild from scratch** — Build a new system with modern architecture, incorporating lessons learned

## Decision

Shachar is rebuilding the clinic management platform from scratch rather than continuing to patch the Retool system. The existing system will be maintained with critical fixes (Track 1) during the transition, while Track 2 (UI design) and Track 3 (new functionality) target the new system.

## Rationale

The rebuild allows design decisions to be baked in from the start at no additional cost versus keeping the old design. The three-track approach ensures critical operational needs are met during the transition while the new system is built properly.

## Consequences

- Parallel effort required: maintaining Retool while building the new system
- Track 2 design decisions must be made now to avoid rework
- Staff requirements gathering (secretaries, psychiatrists) feeds both tracks
- The transition period creates a window where both systems need support

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
