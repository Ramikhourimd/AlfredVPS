---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Scientific methodology standards
created: '2026-02-25'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z AI Diagnostic
  Research Paper.
name: All Analyses Must Use Same Verified Dataset Before Publication
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[task/Investigate Sample Size Discrepancy Between Excel Files]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
relationships:
- confidence: 0.85
  context: Verification depends on noise cleaning
  source: constraint/All Analyses Must Use Same Verified Dataset Before Publication.md
  target: constraint/Clinical Dataset Contains Noise Requiring Statistical Cleaning.md
  type: depends-on
- confidence: 0.8
  context: DWH limits affect verified dataset use
  source: constraint/All Analyses Must Use Same Verified Dataset Before Publication.md
  target: constraint/DWH Access Is Partial and Lacks Full Standardization.md
  type: related-to
source: Data integrity requirement flagged by Noam
source_date: '2026-02-22'
status: active
type: constraint
---

# All Analyses Must Use Same Verified Dataset Before Publication

## Constraint

All analyses in the paper — demographic, time-to-treatment, and diagnostic prediction — must operate on the same verified dataset. Currently three different record counts exist: ~5,700 (first Excel export), 6,041 (latest Excel export), and ~3,000 (Rami's AI analysis subset). No analysis can be considered final until the dataset discrepancy is resolved and all analyses are aligned.

## Source

Noam flagged the discrepancy between Excel exports at the 2026-02-22 meeting. Both exports cover the same inclusion period (December 1, 2023 through August 31, 2025) but show different record counts. Additionally, Rami's diagnostic prediction analysis was run on approximately 3,000 records — a subset that also needs reconciliation.

## Implications

- No final results can be published until the source of the ~340 record discrepancy is identified (duplicates, changed inclusion criteria, or data processing differences)
- Rami's AI analysis on ~3,000 records may need to be re-run on the full verified dataset
- Demographic statistics, timing statistics, and diagnostic prediction results all need recalculation on the aligned dataset
- Shmulik (data provider) may need to clarify export methodology

## Expiry / Review

This constraint is blocking until resolved. Review after Noam and Shmulik investigate the dataset discrepancy.