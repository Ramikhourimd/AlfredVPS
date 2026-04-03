---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
- '[[person/Noam]]'
janitor_note: 'LINK001 — FIXED: decided_by Dekkel Khouri → Dekkel Taliaz. Base view
  embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist (vault-wide issue). Body has DUPLICATE base view embeds — needs
  manual removal of second set after the --- separator. Telia''z wikilinks are valid
  (YAML escaping false positive). DUP001 — possible duplicate of decision/Split AI
  Diagnostic Research Into Two Papers.md.'
name: Split AI Research Into Two Papers
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
relationships:
- confidence: 0.85
  context: AI split supports deferral
  source: decision/Split AI Research Into Two Papers.md
  target: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  type: supports
session: null
source: Meeting discussion between Dekkel, Rami, and Noam
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Split AI Research Into Two Papers

## Context

The methods section of the AI diagnostic paper is already very heavy, with multiple extraction pipelines and prediction stages. Adding the fusion and bias analysis would make it overwhelmingly method-focused and tell two distinct stories.

## Options Considered

1. **Option A** — Single comprehensive paper covering the full pipeline including fusion and bias analysis
2. **Option B** — Split into two papers: methodology/clinical paper first, bias analysis paper second

## Decision

Option B — Split into two papers.

**Paper 1**: Diagnostic extraction pipeline methodology, demographic data, timing analysis, and per-source prediction accuracy (questionnaire, case manager transcript, case manager notes each independently). No fusion, no bias analysis.

**Paper 2**: Fusion methodology, expert agent, biased agent, PTSD bias discovery, DSM validity discussion, and clinical/anthropological implications. References Paper 1 as foundation.

## Rationale

- The methods section is already dense with extraction methodology alone
- The bias finding "tells a different story" — it deserves dedicated treatment
- Paper 2 can build on Paper 1 as an established reference
- Each paper has a clearer narrative arc

## Consequences

- Paper 1 can be finalized sooner as it only needs timing data cleanup
- Bias analysis work is preserved for a standalone publication
- May increase total publication output from one to two papers

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]