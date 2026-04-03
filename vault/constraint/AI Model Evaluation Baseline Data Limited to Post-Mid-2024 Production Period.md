---
authority: Production deployment schedule
created: '2026-02-28'
janitor_note: 'LINK001 false positives: project/Telia''z Innovation Program wikilink
  resolves correctly (YAML single-quote escaping). learn-constraint.base embeds are
  base view references (no action). ORPHAN001: no inbound links — flagging for curator
  review.'
location: []
name: AI Model Evaluation Baseline Data Limited to Post-Mid-2024 Production Period
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[constraint/AI Summary Evaluation Lacks Uncontaminated Ground Truth]]'
- '[[decision/Start AI Model Evaluation with Independent Scoring Before Pairwise Comparison]]'
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
source: Technical limitation — production O1 deployment timeline
source_date: '2025-01-16'
status: active
tags:
- ai-evaluation
- data-quality
type: constraint
---

# AI Model Evaluation Baseline Data Limited to Post-Mid-2024 Production Period

## Constraint

Production O1 model data only became available from approximately month 17 of operations (around July-August 2024). All data before that point is preview/test quality and cannot be used for reliable model comparison. This limits the volume and time range of production data available for the AI model evaluation framework.

## Source

During the January 2025 sprint meeting, Rami walked through the evaluation spreadsheet and noted that production data (O1 regular) has been running since approximately month 17. Earlier results in the spreadsheet are preview/test data with different quality characteristics.

## Implications

- Statistical power of model comparisons is limited by the available production data window
- Historical trend analysis for model quality cannot extend before mid-2024
- Any evaluation methodology must account for this limited baseline when drawing conclusions
- Newer models (O1 Med, Gemini 2.0 Flash) have even shorter production data windows

## Expiry / Review

This constraint becomes less significant over time as more production data accumulates. Review relevance by mid-2026 when ~2 years of production data should be available.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
