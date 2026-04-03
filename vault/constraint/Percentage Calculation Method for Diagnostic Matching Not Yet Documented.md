---
authority: Paper methodology completeness requirement
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilink is a YAML escaping false positive (target
  verified to exist). Base view embeds (learn-constraint.base) preserved per policy
  — _bases/ files not yet created. ORPHAN001 — no inbound links; consider linking
  from a parent project or decision record.
name: Percentage Calculation Method for Diagnostic Matching Not Yet Documented
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Use Three Granularity Levels for Diagnostic Match Scoring]]'
source: Noam flagged gap during 2026-02-22 meeting while reviewing compiled method
  document
source_date: '2026-02-22'
status: active
type: constraint
---

# Percentage Calculation Method for Diagnostic Matching Not Yet Documented

## Constraint

The compiled method document is missing the calculation method for how diagnostic match percentages are computed. This must be documented before the paper can be finalized, as it is a core element of the results reporting.

## Source

Noam identified this gap during the 2026-02-22 meeting while reviewing the compiled method document. The method, analysis, and results sections had been merged into a single document, but the percentage calculation methodology was absent.

## Implications

- Paper cannot be submitted without documenting how match percentages are calculated
- Reviewers will need to understand how partial matches, multi-diagnosis comparisons, and scoring at different granularity levels are computed
- This likely ties to the three-granularity-level scoring system (exact, category, partial) already decided
- Rami needs to provide the calculation methodology to Noam for inclusion in the methods section

## Expiry / Review

Must be resolved before paper submission.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
