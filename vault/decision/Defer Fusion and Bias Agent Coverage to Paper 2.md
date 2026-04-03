---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on:
- '[[decision/First Paper Covers Methodology Plus Basic Clinical Results]]'
- '[[decision/Split AI Diagnostic Research Into Two Papers]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Noam]]'
- '[[person/Dekkel Khouri]]'
janitor_note: 'LINK001 — person/Dekkel Khouri does not exist, possible match: person/Dekkel
  Taliaz. Telia''z wikilinks are valid (YAML escaping false positive). Base view embeds
  (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base which
  does not exist.'
name: Defer Fusion and Bias Agent Coverage to Paper 2
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Create Methodology Figures for Record Analysis Stage]]'
- '[[task/Prepare Additional Figures for Paper Methods Section]]'
relationships:
- confidence: 0.85
  context: Complementary Paper 1/2 scopes
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  type: related-to
- confidence: 0.8
  context: Scoping Paper 1 methodology
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/Limit Paper 1 Methodology to Three Figures.md
  type: related-to
- confidence: 0.95
  context: Requires split into two papers
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/Split AI Diagnostic Research Into Two Papers.md
  type: depends-on
- confidence: 0.9
  context: Depends on research split
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/Split AI Research Into Two Papers.md
  type: depends-on
- confidence: 0.8
  context: Both address bias deferral
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/Split Bias Findings Into Separate Paper.md
  type: related-to
- confidence: 0.95
  context: Defers coverage of biased agent
  source: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  target: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  type: depends-on
session: null
source: Team consensus at research meeting
source_date: '2026-02-22'
status: final
supports:
- '[[decision/Split AI Diagnostic Research Into Two Papers]]'
tags: []
type: decision
---

# Defer Fusion and Bias Agent Coverage to Paper 2

## Context

After deciding to split the research into two papers, the team needed to allocate specific pipeline components between papers. The methodology section is already extensive, and Paper 1 is methods-heavy.

## Options Considered

1. **Include full pipeline in Paper 1** — Cover all agents including fusion and bias in the first paper. Risk: paper becomes too long and unfocused.
2. **Split at fusion boundary** — Paper 1 covers per-source prediction (S1 questionnaire, S2 transcript, S3 notes). Paper 2 covers fusion, expert agent, and biased agent with contextual priming findings.

## Decision

Paper 1 covers extraction and per-source prediction methodology with basic clinical results. Fusion, expert agent, and biased agent (including PTSD diagnostic bias findings) are deferred to Paper 2. Methodology figures follow the same split — Paper 1 gets extraction and per-source prediction figures; fusion and bias figures go to Paper 2.

## Rationale

Paper 1 is already methods-heavy. Adding fusion and bias methodology would make it unmanageably long. The bias findings are substantively different (clinical insight vs methodology) and warrant their own paper. Clean separation at the fusion boundary creates two coherent, focused papers.

## Consequences

- Paper 1 figures limited to: symptom extraction figure (exists) + record analysis figure (to create)
- Paper 2 will contain the novel bias replication finding, which is arguably the more impactful result
- Per-source prediction results in Paper 1 provide the baseline that Paper 2 builds upon

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]