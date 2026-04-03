---
alfred_tags:
- clinical-systems/next-gen
- prototyping/strategy
- innovation/vision
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds reference missing _bases/learn-decision.base (vault infrastructure
  gap, embeds preserved). ACTION NEEDED: Remove duplicate base embed block at end
  of file (second set of Based On/Related after --- separator).'
name: Three-Track Approach to Retool System Improvements
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[project/Telia''z Clinic Israel]]'
session: null
source: Rami and Shachar planning call
source_date: '2025-12-05'
status: draft
supports: []
tags: []
type: decision
---

# Three-Track Approach to Retool System Improvements

## Context

Shachar is rebuilding the clinic management platform. He and Rami needed to align on how to structure the requirements and prioritize development work given limited engineering bandwidth.

## Options Considered

1. **Ad-hoc feature requests** — handle requests as they come, no structured prioritization
2. **Single prioritized backlog** — one list ranked by importance
3. **Three-track framework** — separate tracks for different types of work (chosen)

## Decision

Structure all Retool improvement work into three distinct tracks:

1. **Track 1: Critical fixes for H1 2026** — things the clinic cannot operate without in the first 6 months (KPIs, Teams integration, login issues, secretary workflow)
2. **Track 2: New system UI/UX** — since the system is being rebuilt, design the new interface now rather than replicating the old one (same development cost, better result)
3. **Track 3: New functionality** — additional features beyond current capabilities, lowest priority

## Rationale

The three-track approach separates urgent operational fixes from strategic design decisions and expansion features. Track 2 is uniquely time-sensitive because UI decisions made during the rebuild are free (same effort), while retrofitting later would be expensive.

## Consequences

- Rami must compile prioritized requirements for each track
- Shachar can plan development sprints by track
- Track 1 items may justify hiring contractors (e.g., Teams fix at 3-4 months)
- Budget available given clinic growth trajectory

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
