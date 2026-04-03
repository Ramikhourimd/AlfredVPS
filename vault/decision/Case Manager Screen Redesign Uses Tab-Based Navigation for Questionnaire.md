---
alfred_tags:
- ui/redesign/case-manager
- questionnaire/tabs
- dynamic-questions
approved_by: []
based_on:
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks (project/Telia''z Innovation Program,
  project/Telia''z AI Clinical Platform) are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, learn-decision.base#Related) reference
  _bases/ files that do not exist — vault-wide infrastructure issue. Note: body contains
  DUPLICATE base view embeds (same two embeds appear twice, separated by ---). Embeds
  preserved per rules; human should remove duplicates manually.'
name: Case Manager Screen Redesign Uses Tab-Based Navigation for Questionnaire
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.95
  context: Both on tab navigation for questionnaire screen
  source: decision/Case Manager Screen Redesign Uses Tab-Based Navigation for Questionnaire.md
  target: decision/Tab-Based Navigation for Case Manager Questionnaire Screen.md
  type: related-to
session: ''
source: Innovation sprint meeting 2025-01-16
source_date: '2025-01-16'
status: final
supports: []
tags: []
type: decision
---

# Case Manager Screen Redesign Uses Tab-Based Navigation for Questionnaire

## Context

The case manager questionnaire screen in the clinical platform needed redesign. The existing interface was discussed during the innovation sprint meeting on 2025-01-16, which covered three workstreams including UX improvements for the case manager workflow.

## Options Considered

1. **Single scrollable page** — All questionnaire sections on one long page
2. **Tab-based navigation** — Separate tabs for each questionnaire section, enabling focused interaction per domain

## Decision

Adopted tab-based navigation for the case manager questionnaire screen, allowing case managers to work through structured sections (e.g., PHQ, PCL-5, intake questions) in discrete tabs rather than scrolling through a single monolithic form.

## Rationale

Tab-based navigation reduces cognitive load during sessions, allows case managers to focus on one clinical domain at a time, and provides clearer progress indication through the questionnaire workflow.

## Consequences

- Each questionnaire domain gets its own tab with dedicated UI
- Navigation between sections is explicit rather than scroll-based
- Platform development team must implement tab routing and state management across sections

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]