---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Institutional Review Board
created: '2026-02-25'
janitor_note: 'LINK001: Telia''z wikilink (project/Telia''z AI Diagnostic Research
  Paper) is valid (YAML escaping false positive). Base view embeds (learn-constraint.base#Affected
  Projects, #Related) reference _bases/learn-constraint.base which does not exist
  — vault-wide structural issue, embeds preserved. ORPHAN001: no inbound wikilinks
  detected.'
name: IRB Inclusion Period December 2023 to August 2025
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[contradiction/IRB Stated Wait Times vs Actual Median Wait Times]]'
source: IRB approval for AI diagnostic research
source_date: '2026-02-22'
status: active
type: constraint
---

# IRB Inclusion Period December 2023 to August 2025

## Constraint

All patient data analyses for the research paper must be limited to the IRB-approved inclusion period: first patient intake on December 1, 2023, through the cutoff date of August 31, 2025. No patient records outside this window may be included in the study.

## Source

IRB (Institutional Review Board) approval for the AI diagnostic research study. This is a regulatory requirement — the study was approved to analyze data within these specific dates only.

## Implications

- Any data exports must be filtered to this date range before analysis
- The dataset size is capped by the number of patients seen during this 21-month period (~6,000 records)
- If the team discovers additional useful data outside this window, a new IRB application or amendment would be required
- The dataset discrepancy (5,700 vs 6,041 records) must be investigated within this boundary

## Expiry / Review

This constraint is permanent for the current study. A new IRB application would be needed to extend the inclusion period for future publications.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]