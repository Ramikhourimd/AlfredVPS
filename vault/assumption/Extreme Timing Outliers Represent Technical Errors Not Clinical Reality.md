---
alfred_tags:
- patient-data/assumptions
- ai-diagnostics/validation
based_on:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 false positive: project/Telia''z wikilink flagged due to YAML
  single-quote escaping — target verified to exist. Base view embeds (learn-assumption.base)
  reference non-existent _bases/ file — preserved per vault rules; base file may need
  creation. ORPHAN001: no inbound wikilinks — may need linking from related records.'
name: Extreme Timing Outliers Represent Technical Errors Not Clinical Reality
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data]]'
- '[[decision/Use Median With Outlier Cleaning for Timing Data]]'
relationships:
- confidence: 0.65
  context: Shared data analysis concerns
  source: assumption/Extreme Timing Outliers Represent Technical Errors Not Clinical
    Reality.md
  target: assumption/Rami Analyzed Only Half the Available Patient Dataset.md
  type: related-to
- confidence: 0.75
  context: Outliers as errors supports subset rep
  source: assumption/Extreme Timing Outliers Represent Technical Errors Not Clinical
    Reality.md
  target: assumption/Analyzed Patient Subset Is Representative of Full Dataset.md
  type: supports
source: Team consensus during 2026-02-22 research meeting
source_date: '2026-02-22'
status: active
type: assumption
---

# Extreme Timing Outliers Represent Technical Errors Not Clinical Reality

## Claim

Patients showing wait times of 170+ hours or 300+ days in the timing data are the result of unclosed patient records or technical system errors, not actual clinical wait times experienced by patients.

## Basis

Multiple team members observed extreme outliers in the time-to-case-manager and time-to-psychiatrist data. The team characterized these as "clearly technical errors" and "likely unclosed patient records." This assumption justified the decision to apply a 2.5 standard deviation threshold for outlier removal rather than investigating each case individually.

## Evidence Trail

- 2026-02-22: Noam presented timing data showing outliers up to 388 hours/300+ days
- 2026-02-22: Team agreed these are technical artifacts, not clinical reality
- Pending: Outlier cleaning at 2.5 SD threshold (assigned to Noam)

## Impact

If this assumption is wrong — if some extreme wait times reflect actual patient experiences — the outlier removal would mask genuine access-to-care problems at the clinic. The decision to use 2.5 SD removal and median reporting both rest on this assumption. The paper's time-to-treatment findings would be understated if real long-wait patients are excluded.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]