---
alfred_tags:
- clinical-data/constraints
- ai-research/limitations
authority: Data quality review
created: '2026-02-26'
janitor_note: LINK001 — _bases/learn-constraint.base does not exist yet; base view
  embeds in body are present but non-functional until base file is created. Telia'z
  project wikilinks are valid (YAML single-quote escaping false positive).
location: []
name: Clinical Dataset Contains Noise Requiring Statistical Cleaning
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[assumption/Production Data Begins Around March 10 Prior Events Are Tests]]'
- '[[task/Clean Open and Test Sessions From Reports]]'
source: Product meeting analysis
source_date: '2026-02-25'
status: active
tags: []
type: constraint
---

# Clinical Dataset Contains Noise Requiring Statistical Cleaning

## Constraint

The clinical dataset contains significant contamination: unreasonable wait times, impossible patient ages, open/unclosed sessions, and test session data mixed with production records. Any analytical or research use of this data requires systematic statistical cleaning before results are trustworthy.

## Source

Identified during the product meeting on 2026-02-25. Shmulik was asked to provide a list of 22 patients with unreasonable ages and confirm report gaps under the new approval logic.

## Implications

- All reports, AI training, and research outputs must implement outlier filtering (statistical thresholds / standard deviations)
- Age-specific cleaning rules needed for impossible values
- Cannot naively use raw data for KPIs, research papers, or AI model training
- Manual intervention may be needed to resolve ambiguous session statuses

## Expiry / Review

Ongoing constraint. Should be re-evaluated after the data cleaning pipeline is implemented and the initial dataset is sanitized.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]