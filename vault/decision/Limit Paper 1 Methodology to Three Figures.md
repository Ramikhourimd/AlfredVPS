---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on:
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
- '[[constraint/Paper Methods Section Length Limits Additional Content]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Noam]]'
janitor_note: 'LINK001 — Telia''z wikilink (project/Telia''z AI Diagnostic Research
  Paper) is valid (YAML escaping false positive). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist. Duplicate
  base view embeds at end of body need manual cleanup. ORPHAN001 — no inbound wikilinks
  from other records.'
name: Limit Paper 1 Methodology to Three Figures
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Create Methodology Figures for Record Analysis Stage]]'
- '[[task/Add Figures for Record Analysis Methodology]]'
- '[[decision/Defer Fusion and Bias Agent Coverage to Paper 2]]'
relationships:
- confidence: 0.85
  context: P1 limits need paper split
  source: decision/Limit Paper 1 Methodology to Three Figures.md
  target: decision/Split AI Diagnostic Research Into Two Papers.md
  type: depends-on
session: ''
source: Research meeting consensus
source_date: '2026-02-22'
status: final
supports:
- '[[decision/First Paper Covers Methodology Plus Basic Clinical Results]]'
tags:
- paper-structure
- figures
type: decision
---

# Limit Paper 1 Methodology to Three Figures

## Context

The paper's methods section already constitutes approximately half the paper. Noam noted that the existing single figure only covers the symptom extraction stage and does not represent the diagnostic prediction pipeline. Additional figures were needed, but adding too many would further inflate the methods-heavy paper.

## Options Considered

1. **One figure only** — Keep the existing extraction figure and describe prediction stages in text only
2. **Three figures** — Extraction figure (exists) + record analysis figure (per-source prediction) + optional fusion figure
3. **Four or more figures** — Full visual coverage of every pipeline stage

## Decision

Three total figures for Paper 1 methodology: (1) existing symptom extraction figure, (2) new record analysis figure showing per-source diagnostic prediction, and (3) an optional overall pipeline figure. Fusion and bias agent figures are deferred to Paper 2.

## Rationale

The paper is already methods-heavy. Three figures provide sufficient visual support for the reader to understand the pipeline without overwhelming the methods section. The fusion and bias agent stages belong to Paper 2's scope anyway, so their figures naturally defer.

## Consequences

- Noam and Rami need to collaborate on creating figures 2 and 3.
- Paper 1 readers will not see a visual representation of the fusion or bias stages — these are described only in the future work section.
- Keeps Paper 1 focused on the core methodology: extraction and per-source prediction.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]