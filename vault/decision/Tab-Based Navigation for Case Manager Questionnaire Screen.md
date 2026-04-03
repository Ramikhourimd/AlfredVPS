---
alfred_tags:
- ui/redesign/case-manager
- questionnaire/tabs
- dynamic-questions
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2025-01-16'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Li Yamin]]'
janitor_note: 'LINK001 wikilink to Telia''z AI Clinical Platform is valid (YAML escaping
  false positive). Base view embeds (learn-decision.base) reference missing _bases/
  file — vault-wide gap. Body has DUPLICATE base embeds at bottom — same two embeds
  appear twice. Human review recommended: remove the duplicate pair at the end of
  the file.'
name: Tab-Based Navigation for Case Manager Questionnaire Screen
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Innovation Team AI Sprint Meeting 2025-01-16]]'
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
relationships:
- confidence: 0.9
  context: Tab nav is part of screen redesign
  source: decision/Tab-Based Navigation for Case Manager Questionnaire Screen.md
  target: decision/Case Manager Screen Redesign Uses Tab-Based Navigation for Questionnaire.md
  type: part-of
session: null
source: Innovation Sprint Meeting 2025-01-16
source_date: '2025-01-16'
status: final
supports: []
tags: []
type: decision
---

# Tab-Based Navigation for Case Manager Questionnaire Screen

## Context

The case manager screen needed a layout that supports 13+ topics with sub-categories. The original design used a vertical scrolling list, which would become unwieldy with the expanded questionnaire content.

## Options Considered

1. **Vertical scrolling list** — All topics displayed in a single scrollable column
2. **Tab-based navigation** — Horizontal tabs across the top, with content panels below

## Decision

Use tab-based navigation with horizontal tabs. Each topic is a tab; clicking opens the questions for that topic. Non-sequential navigation is allowed — case managers can jump freely between tabs based on conversation flow.

## Rationale

Case managers need to follow the patient's conversational direction, not a fixed question order. Tabs provide quick random access while keeping the interface clean. Rami specifically requested that case managers be able to start from any topic if the patient spontaneously discusses it.

## Consequences

- More complex Retool implementation (need to verify tab behavior with Lidar)
- Better UX for real clinical conversations
- Supports the bookmark/flag feature for marking topics to revisit

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]