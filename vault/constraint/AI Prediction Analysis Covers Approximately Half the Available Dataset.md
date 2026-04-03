---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Dataset processing scope
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML single-quote escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, learn-constraint.base#Related)
  reference _bases/learn-constraint.base which does not exist — vault-wide infrastructure
  gap.
name: AI Prediction Analysis Covers Approximately Half the Available Dataset
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[constraint/All Analyses Must Use Same Verified Dataset Before Publication]]'
source: Rami Khouri stated during 2026-02-22 meeting he analyzed only ~3000 records
source_date: '2026-02-22'
status: active
type: constraint
---

# AI Prediction Analysis Covers Approximately Half the Available Dataset

## Constraint

Rami's AI diagnostic prediction analysis was run on approximately 3,000 patient records, while the full available dataset contains 6,041 records (latest export). The paper must clearly report this analysis sample size and justify any discrepancy with the demographic/timing analyses that may use the full dataset.

## Source

Rami stated during the 2026-02-22 meeting that he analyzed only ~3,000 records for his part. This was mentioned in the context of the dataset discrepancy discussion where Noam flagged 6,041 records in the newer export.

## Implications

- Paper must clearly state the sample size used for AI prediction vs demographic analysis
- If Noam's statistical analyses use 6,041 records but AI predictions cover ~3,000, the discrepancy needs explanation
- Possible reasons: records without required data sources (missing questionnaire or transcript), records outside inclusion criteria for AI analysis, or processing limitations
- Reviewers will question why not all available records were analyzed

## Expiry / Review

Resolve before paper submission — either expand analysis to full dataset or document inclusion/exclusion criteria for the AI analysis subset.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]