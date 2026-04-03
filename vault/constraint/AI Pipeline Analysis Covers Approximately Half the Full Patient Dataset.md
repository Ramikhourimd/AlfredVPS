---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Data availability and processing capacity
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilink in project field is valid (YAML escaping
  false positive). Base embeds (learn-constraint.base#Affected Projects, #Related)
  require _bases/learn-constraint.base which does not exist; create it to enable dynamic
  views. Embeds preserved.'
name: AI Pipeline Analysis Covers Approximately Half the Full Patient Dataset
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[constraint/All Analyses Must Use Same Verified Dataset Before Publication]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
relationships:
- confidence: 0.9
  context: similar AI analysis coverage limits
  source: constraint/AI Pipeline Analysis Covers Approximately Half the Full Patient
    Dataset.md
  target: constraint/AI Prediction Analysis Covers Approximately Half the Available
    Dataset.md
  type: related-to
- confidence: 0.75
  context: partial coverage needs verification
  source: constraint/AI Pipeline Analysis Covers Approximately Half the Full Patient
    Dataset.md
  target: constraint/All Analyses Must Use Same Verified Dataset Before Publication.md
  type: supports
source: Rami Khouri statement during 2026-02-22 meeting
source_date: '2026-02-22'
status: active
type: constraint
---

# AI Pipeline Analysis Covers Approximately Half the Full Patient Dataset

## Constraint

Rami's AI diagnostic pipeline analysis was run on approximately 3,000 patient records, while the full dataset contains 6,000+ records for the inclusion period (December 2023 to August 2025). The diagnostic prediction results are based on roughly half the available data.

## Source

Rami stated during the 2026-02-22 meeting: "he analyzed only ~3000 records for his part." The full dataset export from Shmulik contains 6,041 records (or ~5,700 in a previous export — the discrepancy is separately tracked).

## Implications

- Paper must clearly state the sample size used for AI diagnostic analysis vs the full cohort
- Demographic and timing analyses by Noam may use the full dataset while AI prediction uses a subset
- Statistical power and generalizability claims must reflect the actual analyzed sample
- If the 3,000 records are not representative of the full 6,000+ (e.g., biased toward earlier patients), findings may not generalize
- The constraint "All analyses must use same verified dataset" may conflict with this partial analysis

## Expiry / Review

This constraint should be reviewed when:
- The dataset discrepancy (6,041 vs 5,700) is resolved
- A decision is made whether to re-run AI analysis on the full verified dataset
- Paper methodology section explicitly addresses sample size

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]