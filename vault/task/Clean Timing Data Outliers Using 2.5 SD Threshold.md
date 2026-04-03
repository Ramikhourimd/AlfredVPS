---
alfred_instructions: null
assigned: '[[person/Noam]]'
blocked_by: []
created: '2026-02-25'
depends_on: []
description: Remove statistical outliers from patient wait time data using 2.5 standard
  deviations from mean as threshold. Apply to time-to-case-manager and time-to-psychiatrist
  columns. Report median instead of mean.
due: null
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. All Telia'z wikilinks are valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project or conversation
  records.
kind: task
name: Clean Timing Data Outliers Using 2.5 SD Threshold
priority: high
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Clean Timing Data Outliers Using 2.5 SD Threshold

Remove statistical outliers from patient wait time data. Some records show 150-388 day waits, which are clearly erroneous (technical errors, patients left in waiting status).

## Context

Agreed at meeting on 2026-02-22 that 2.5 standard deviations from the mean is the appropriate cutoff. Report median values rather than mean due to skewed distribution.

## Related
![[related.base#All]]

## Outcome
