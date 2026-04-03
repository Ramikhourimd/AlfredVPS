---
alfred_tags:
- healthcare/wait-times
- statistics/outlier-handling
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Noam]]'
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
janitor_note: DUPLICATE base view embeds at end of body — remove the "---" divider
  and second set of \![[learn-decision.base#Based On]] and \![[learn-decision.base#Related]]
  embeds. Manual body edit required (CLI lacks body-replace).
name: Use 2.5 Standard Deviations for Outlier Removal in Timing Data
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
relationships:
- confidence: 0.85
  context: Outlier removal enables median cleaning
  source: decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data.md
  target: decision/Use Median With Outlier Cleaning for Timing Data.md
  type: supports
- confidence: 0.7
  context: Outlier handling for timing reporting
  source: decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data.md
  target: decision/Use Median for Time-to-Treatment Reporting.md
  type: related-to
session: null
source: Meeting discussion — Noam proposed, Rami and Dekkel agreed
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Use 2.5 Standard Deviations for Outlier Removal in Timing Data

## Context

Patient timing data (time to case manager, time to psychiatrist) shows extreme outliers — some patients showing 170-388 days. These are almost certainly technical errors (patients not properly closed in the system) or patients who abandoned and returned.

## Options Considered

1. **Option A** — Report means and include all data, noting high variance
2. **Option B** — Remove outliers beyond 2.5 standard deviations and report medians

## Decision

Option B — Remove outliers at 2.5 standard deviations from the mean (standard statistical practice). Report medians as the primary metric due to right-skewed distribution.

## Rationale

- Median (8 days to case manager, 16 days to psychiatrist) is roughly half the mean, indicating heavy right skew
- Values like 300+ days are clearly not indicative of actual wait times
- 2.5 SD is standard practice for outlier identification in clinical research

## Consequences

- Timing results will be more representative of actual patient experience
- Must document the outlier removal threshold in the methods section
- Need to verify cleaned results still align with what was claimed in the IRB application

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]