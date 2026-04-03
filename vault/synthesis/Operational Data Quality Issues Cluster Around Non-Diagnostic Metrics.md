---
cluster_sources:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[assumption/Extreme Timing Outliers Represent Technical Errors Not Clinical Reality]]'
- '[[task/Clean Timing Data Outliers at 2.5 SD Threshold]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
confidence: medium
created: '2026-03-08'
janitor_note: LINK001 — Telia'z wikilink (project/Telia'z AI Diagnostic Research Paper)
  is valid (YAML escaping false positive). ORPHAN001 — no inbound wikilinks; consider
  linking from project/Telia'z AI Diagnostic Research Paper or related data quality
  records.
name: Operational Data Quality Issues Cluster Around Non-Diagnostic Metrics
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/All Data Exports Depend on Single Provider Shmulik]]'
- '[[constraint/All Analyses Must Use Same Verified Dataset Before Publication]]'
- '[[decision/Use Median With Outlier Cleaning for Timing Data]]'
status: draft
supports:
- '[[decision/Five-Stage Sequential Agent Architecture for Diagnostic Prediction]]'
type: synthesis
---

# Operational Data Quality Issues Cluster Around Non-Diagnostic Metrics

## Insight

Across the 2026-02-22 research meetings, data quality concerns consistently surface around operational metrics (timing data, dataset export counts, summary approval measurements) rather than around the diagnostic prediction pipeline itself. The AI diagnostic methodology — symptom extraction, per-source prediction, fusion — is discussed in terms of architectural choices and accuracy improvement, never in terms of data integrity doubt. Meanwhile, the surrounding clinical operations data requires outlier removal, discrepancy investigation, and segmentation clarification.

## Evidence

- **Timing data**: Extreme outliers (170+ hours, 300+ days) requiring 2.5 SD threshold cleanup; mean approximately double the median
- **Dataset exports**: Two exports for the same date range show different record counts (5,700 vs 6,041) — source unknown
- **Summary approval times**: Require complex 8-category segmentation to be interpretable; confounded by mode transition timing
- **Diagnostic predictions**: No data integrity concerns raised; discussion focuses on methodology and accuracy, not data quality

## Implications

- The diagnostic pipeline's data quality may benefit from being AI-processed (structured extraction with validation), while operational metrics rely on raw clinical system logs with less validation
- Paper reviewers may challenge operational metrics more than diagnostic methodology
- Data quality investment should prioritize the timing and export pipeline, as the diagnostic pipeline appears robust

## Applicability

This pattern suggests that in AI-assisted clinical research, the AI pipeline itself may produce cleaner data than the surrounding operational infrastructure it depends on for context metrics.
