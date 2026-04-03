---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-22'
decided_by: '[[person/Dekkel Taliaz]]'
janitor_note: LINK001 — Fixed [[person/Dekkel Khouri]] → [[person/Dekkel Taliaz]]
  in decided_by. Telia'z wikilinks are valid (YAML escaping false positive). Base
  view embeds (learn-decision.base) reference _bases/ which does not exist — create
  it to enable dynamic views. Body contains duplicate base embed blocks.
name: First Paper Covers Methodology Plus Basic Clinical Results
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
relationships:
- confidence: 0.85
  context: Detail Paper 1 content limits
  source: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  target: decision/Limit Paper 1 Methodology to Three Figures.md
  type: related-to
- confidence: 0.9
  context: P1 coverage assumes split
  source: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  target: decision/Split AI Diagnostic Research Into Two Papers.md
  type: depends-on
- confidence: 0.9
  context: Requires AI research split
  source: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  target: decision/Split AI Research Into Two Papers.md
  type: depends-on
- confidence: 0.75
  context: P1 basic excludes bias
  source: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  target: decision/Split Bias Findings Into Separate Paper.md
  type: related-to
session: null
source: Research meeting 2026-02-22
source_date: '2026-02-22'
status: final
supports:
- '[[decision/Split Bias Findings Into Separate Paper]]'
tags: []
type: decision
---

# First Paper Covers Methodology Plus Basic Clinical Results

## Context

After deciding to split the research into two papers, the team needed to define the exact scope of Paper 1. Dekkel emphasized the need to include some clinical insight beyond just methodology.

## Options Considered

1. **Pure methodology paper** — only describe the pipeline without clinical results. Rejected — Dekkel wanted clinical value in Paper 1.
2. **Methodology plus per-source prediction results** — include questionnaire-only and case manager-only prediction accuracy, plus timing data and demographics. Selected.
3. **Methodology plus all prediction results** — include fusion and expert agents too. Rejected — too much for one paper.

## Decision

Paper 1 includes:
- Full methodology description (symptom extraction pipeline)
- Questionnaire-only diagnostic prediction results
- Case manager transcript-only diagnostic prediction results
- Patient demographics
- Timing data (wait times for case manager, psychiatrist, summary approval)
- PHQ correlation data (showing questionnaire aligns with depression, not PTSD)
- Comparison of real-time vs transcript-based summary approval times

Paper 1 excludes:
- Fusion model results
- Expert agent results
- Biased expert agent results
- Bias/contextual priming analysis

## Rationale

- Includes enough clinical insight to be publishable as a clinical paper, not just a methods paper
- PHQ correlation data supports the bias narrative without requiring the full bias analysis
- Timing data provides operational value for the telehealth community
- Keeps the paper focused and manageable

## Consequences

- Noam needs to add figures for the case manager record analysis methodology
- Need to resolve dataset size discrepancy before finalizing
- Paper 2 will build on this foundation

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]