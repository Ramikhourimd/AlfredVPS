---
authority: Study design — outcome measure applicability
created: '2026-03-14'
janitor_note: 'LINK001 — Telia''z wikilinks are YAML escaping false positives (all
  targets exist). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist — vault-wide infrastructure
  gap, not a per-file issue. ORPHAN001 — no inbound links from other records; may
  need to be linked from a related project or synthesis.'
location: []
name: Evacuee-Specific Outcome Measures Create Subgroup Analysis Requirement
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Five Clinical Outcome Dimensions for Per-Symptom Analysis]]'
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
- '[[constraint/AI Prediction Analysis Covers Approximately Half the Available Dataset]]'
source: Research Paper Scope and Data Extraction Plan 2025-11-09
source_date: '2025-11-09'
status: active
tags: []
type: constraint
---

# Evacuee-Specific Outcome Measures Create Subgroup Analysis Requirement

## Constraint

The "return home" clinical outcome dimension only applies to patients who were evacuated from their homes after October 7th. This means at least one of the five selected outcome measures cannot be applied uniformly across the full patient cohort, requiring subgroup identification and separate analysis tracks.

## Source

Defined in the 2025-11-09 research paper scope note: "Return home (for evacuees) — Binary: returned / not returned." The parenthetical qualifier "(for evacuees)" explicitly limits this measure to a patient subset.

## Implications

- The dataset must include an evacuee/non-evacuee classification for each patient
- Evacuee status may need NLP extraction from unstructured text if not in structured fields
- Statistical analyses involving "return home" must report the applicable n separately from the full cohort
- Reviewers may question why one outcome measure has a different denominator than the others
- The paper must clearly describe this subgroup limitation in the methods section

## Expiry / Review

Active for the duration of the research paper. Should be reviewed when finalizing the statistical analysis plan with Noam.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
