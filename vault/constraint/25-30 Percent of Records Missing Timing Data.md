---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Data quality limitation in Telia'z clinic system
created: '2026-02-25'
janitor_note: LINK001 — fixed project wikilink (Teliaz → Telia'z). LINK001 — all constraint.base#*
  embeds reference _bases/constraint.base which does not exist — vault-wide structural
  issue, embeds preserved. ORPHAN001 — no inbound links, flagged for review.
name: 25-30 Percent of Records Missing Timing Data
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[person/Noam]]'
relationships:
- confidence: 0.8
  context: Missing data supports verification policy
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/All Analyses Must Use Same Verified Dataset Before Publication.md
  type: supports
- confidence: 0.75
  context: Both clinical data quality issues
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Clinical Dataset Contains Noise Requiring Statistical Cleaning.md
  type: related-to
- confidence: 0.7
  context: Access issues cause data incompleteness
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/DWH Access Is Partial and Lacks Full Standardization.md
  type: related-to
- confidence: 0.6
  context: Transcription issues impact timing data
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Mixed-Language Transcription Quality Unreliable Since Aug 2025.md
  type: related-to
- confidence: 0.65
  context: Session ID issues affect timing records
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Open Test Sessions Cannot Be Reliably Identified Without Manual
    Review.md
  type: related-to
- confidence: 0.8
  context: Timing depends on transcript access
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Transcript Data Not Available in BigQuery.md
  type: depends-on
- confidence: 0.55
  context: Unstable webhooks cause missing data
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Webhook Trigger Mechanism Is Currently Unstable.md
  type: related-to
- confidence: 0.75
  context: Both describe partial dataset coverage issues
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/AI Pipeline Analysis Covers Approximately Half the Full Patient
    Dataset.md
  type: related-to
- confidence: 0.75
  context: Both indicate incomplete dataset usage
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/AI Prediction Analysis Covers Approximately Half the Available
    Dataset.md
  type: related-to
- confidence: 0.65
  context: Timing data ties to IRB period
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/IRB Inclusion Period December 2023 to August 2025.md
  type: related-to
- confidence: 0.65
  context: Both data availability gaps
  source: constraint/25-30 Percent of Records Missing Timing Data.md
  target: constraint/Questionnaire Data Not Available in BigQuery.md
  type: related-to
source: Data quality analysis by Noam — research meeting 2026-02-22
source_date: '2026-02-22'
status: active
type: constraint
---

# 25-30 Percent of Records Missing Timing Data

## Constraint

Approximately 25-30% of patient records in the dataset lack timing data for case manager appointments. The percentage of missing data increases further for psychiatrist appointment timing. This limits the sample size available for time-to-treatment analyses.

## Source

Data quality assessment during research meeting 2026-02-22. Noam identified this gap while reviewing the data exports from Shmulik.

## Implications

- Time-to-treatment analyses will have a smaller effective sample size than the total patient count
- Must report the missing data percentage in the paper's methods section
- Statistical methods must account for non-random missingness — patients with missing timing data may differ systematically from those with complete records
- The increasing missingness for psychiatrist timing (compared to case manager timing) may indicate a pattern worth investigating (e.g., patients dropping out before seeing psychiatrist)

## Expiry / Review

This is a fixed property of the existing dataset. Cannot be remediated retroactively. Should be addressed as a limitation in the paper and reviewed if a follow-up study is designed.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]