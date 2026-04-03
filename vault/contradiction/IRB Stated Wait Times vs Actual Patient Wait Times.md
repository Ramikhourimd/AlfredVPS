---
alfred_tags:
- psychiatry/discrepancies
- operations/claims-vs-reality
claim_a: IRB submission stated approximately 3-5 days for patient wait times to treatment
claim_b: Actual timing data shows median 8 days to case manager and 16 days to psychiatrist,
  with mean values significantly higher due to outliers
created: '2026-02-25'
janitor_note: LINK001 — no base view embeds in body (contradiction template does not
  use them by default). All Telia'z wikilinks are valid (YAML escaping false positive).
name: IRB Stated Wait Times vs Actual Patient Wait Times
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[person/Noam]]'
- '[[task/Clean Outliers From Time-to-Treatment Data]]'
relationships:
- confidence: 0.75
  context: Clinical capacity and load discrepancies
  source: contradiction/IRB Stated Wait Times vs Actual Patient Wait Times.md
  target: contradiction/Psychiatrist Session-to-Patient Ratio Exceeds Expected Clinical
    Norms.md
  type: related-to
- confidence: 0.7
  context: Service metric and wait time contradictions
  source: contradiction/IRB Stated Wait Times vs Actual Patient Wait Times.md
  target: contradiction/Same-Month Intake Conversion Rate May Understate Total Patient
    Service Rate.md
  type: related-to
- confidence: 0.65
  context: Operational planning contradictions
  source: contradiction/IRB Stated Wait Times vs Actual Patient Wait Times.md
  target: contradiction/Workforce Stabilization Priority Conflicts With Concurrent
    Recruitment Urgency.md
  type: related-to
- confidence: 0.85
  context: Both show unmet capacity commitments
  source: contradiction/IRB Stated Wait Times vs Actual Patient Wait Times.md
  target: contradiction/Psychiatrist Hour Increase Commitments vs Observed Stagnation
    Pattern.md
  type: related-to
source_a: IRB submission document
source_b: Timing data analysis by Noam from Shmulik data export (Feb 2026)
status: unresolved
type: contradiction
---

# IRB Stated Wait Times vs Actual Patient Wait Times

# IRB Stated Wait Times vs Actual Patient Wait Times

## Claim A

The IRB submission for the Telia'z AI diagnostic research study stated that patients would wait approximately 3-5 days between referral and first treatment contact (case manager and psychiatrist appointments).

## Claim B

Actual timing data analysis (from the dataset covering December 2023 through August 2025, 6041 patients) shows median wait time of 8 days to first case manager appointment and 16 days to first psychiatrist appointment. Mean values are significantly higher due to extreme outliers (some records showing 150-388 days).

## Analysis

The discrepancy likely arises from several factors: (1) the IRB figures may have been based on early operational targets rather than actual data; (2) extreme outliers from technical errors inflate means; (3) the dataset includes a significant period before real-time workflow changes; (4) approximately 25% of records have missing timing data, potentially skewing results. The team agreed to clean outliers at 2.5 standard deviations and report medians to present the most representative picture.

## Resolution

Pending. The team needs to determine whether the cleaned median figures are acceptable vis-a-vis the IRB commitment, and whether the discrepancy requires an IRB amendment or note.