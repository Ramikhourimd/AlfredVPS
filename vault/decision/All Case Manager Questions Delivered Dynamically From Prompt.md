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
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — vault-wide infrastructure gap,
  embeds preserved. Note: duplicate base embed block at end of file — consider removing
  the duplicate.'
name: All Case Manager Questions Delivered Dynamically From Prompt
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Innovation Team AI Sprint Meeting 2025-01-16]]'
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
- '[[person/Li Yamin]]'
relationships:
- confidence: 0.7
  context: Both address case manager questionnaire UX
  source: decision/All Case Manager Questions Delivered Dynamically From Prompt.md
  target: decision/Case Manager Screen Redesign Uses Tab-Based Navigation for Questionnaire.md
  type: related-to
- confidence: 0.7
  context: Both address case manager questionnaire UX
  source: decision/All Case Manager Questions Delivered Dynamically From Prompt.md
  target: decision/Tab-Based Navigation for Case Manager Questionnaire Screen.md
  type: related-to
session: null
source: Innovation Sprint Meeting 2025-01-16
source_date: '2025-01-16'
status: final
supports: []
tags: []
type: decision
---

# All Case Manager Questions Delivered Dynamically From Prompt

## Context

During the case manager UX screen redesign discussion, Li Yamin asked whether some questions should be hardcoded in the UI while others come dynamically from the AI prompt. This is a critical architectural decision for the clinical platform.

## Options Considered

1. **Mixed approach** — Some questions fixed in UI, others dynamic from prompt
2. **All dynamic from prompt** — Every question slot receives its content from the AI prompt, with no hardcoded questions in the UI

## Decision

All questions will be delivered dynamically from the prompt. There are no fixed/hardcoded questions in the UI. The prompt controls which questions appear in each slot, including follow-up variations based on questionnaire answers.

## Rationale

Rami argued that there is no predictable pattern for which questions to ask or skip — it changes constantly based on clinical needs and HMO requirements. Hardcoding questions would require UI changes every time the clinical protocol evolves. By making everything dynamic, Rami can adjust question sets entirely through prompt engineering without any system changes.

## Consequences

- Li Yamin's Retool screen design treats every question slot as dynamic content
- The prompt must define the complete question set for every session
- Question ordering, follow-up logic, and conditional display are all controlled at the prompt level
- Gives maximum flexibility but increases prompt complexity

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]