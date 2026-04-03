---
alfred_instructions: null
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Add documentation of how diagnostic match percentages are calculated.
  Noam noted this is missing from the current methods compilation.
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. Telia'z wikilink is valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z AI Diagnostic
  Research Paper.
kind: task
name: Document Percentage Calculation Method for Paper
priority: medium
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[person/Noam]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Document Percentage Calculation Method for Paper

Noam identified that the methods compilation is missing the explanation of how diagnostic match percentages are calculated. This needs to be written up for inclusion in the methods section.

The calculation method covers how match rates are determined at three granularity levels:
- **Specific** (ICD code + specifier, e.g., F43.10)
- **Group** (ICD code without specifier, e.g., F43)
- **Block** (diagnostic category, e.g., all trauma-related, all affective)

## Context

- [[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]

## Related
![[related.base#All]]

## Outcome
