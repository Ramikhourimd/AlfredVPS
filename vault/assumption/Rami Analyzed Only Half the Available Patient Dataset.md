---
alfred_tags:
- patient-data/assumptions
- ai-diagnostics/validation
based_on: []
challenged_by:
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
confidence: high
created: '2026-02-25'
janitor_note: 'Base view embeds (learn-assumption.base#Depends On This, #Related)
  reference _bases/learn-assumption.base which does not exist — vault-wide infrastructure
  gap. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z AI
  Diagnostic Research Paper.'
name: Rami Analyzed Only Half the Available Patient Dataset
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Noam]]'
relationships:
- confidence: 0.95
  context: Only half analyzed undermines rep
  source: assumption/Rami Analyzed Only Half the Available Patient Dataset.md
  target: assumption/Analyzed Patient Subset Is Representative of Full Dataset.md
  type: contradicts
- confidence: 0.6
  context: Both question analysis data completeness
  source: assumption/Rami Analyzed Only Half the Available Patient Dataset.md
  target: assumption/Extreme Timing Outliers Represent Technical Errors Not Clinical
    Reality.md
  type: related-to
source: Research meeting discussion — Rami Khouri
source_date: '2026-02-22'
status: active
type: assumption
---

# Rami Analyzed Only Half the Available Patient Dataset

## Claim

Rami's AI diagnostic pipeline analysis was run on approximately 3,000 patient records, while the full dataset contains approximately 5,700-6,041 records for the IRB inclusion period. This means roughly half the available data was processed through the diagnostic pipeline.

## Basis

During the 2026-02-22 research meeting, the team noted that Rami had analyzed approximately 3,000 patients while the exports showed 5,700-6,041 total records. The reason for the discrepancy was not fully discussed — it may relate to data availability at the time of analysis, pipeline processing limitations, or filtering criteria.

## Evidence Trail

- 2026-02-22: Noam flagged that Rami analyzed ~3,000 while exports show ~6,000
- Dataset count discrepancy itself (5,700 vs 6,041) is separately tracked as a contradiction

## Impact

If Paper 1 reports diagnostic prediction results based on ~3,000 records while claiming a dataset of ~6,000, this must be clearly explained in the methods section. Reviewers will question why only half the data was used. The team must decide whether to re-run the pipeline on the full dataset or justify the subset.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]