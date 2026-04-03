---
alfred_tags:
- healthcare/wait-times
- statistics/outlier-handling
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-22'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
janitor_note: 'LINK001 — FIXED: decided_by Dekkel Khouri → Dekkel Taliaz. Base view
  embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — vault-wide infrastructure issue. Duplicate base embeds appear
  twice in body — needs manual removal of second set after --- separator. Telia''z
  wikilinks are valid (YAML escaping false positive).'
name: Use Median With Outlier Cleaning for Timing Data
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
relationships:
- confidence: 0.9
  context: Median cleaning basis for reporting
  source: decision/Use Median With Outlier Cleaning for Timing Data.md
  target: decision/Use Median for Time-to-Treatment Reporting.md
  type: supports
- confidence: 0.85
  context: Uses 2.5 SD method for cleaning
  source: decision/Use Median With Outlier Cleaning for Timing Data.md
  target: decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data.md
  type: depends-on
session: null
source: Research meeting 2026-02-22
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Use Median With Outlier Cleaning for Timing Data

## Context

Timing data (wait times to case manager, psychiatrist, and summary approval) showed extremely high variance. Mean values were heavily skewed by outliers — some records showed 300+ day waits, which are clearly technical errors (e.g., unclosed patient records) rather than real wait times.

## Options Considered

1. **Report means** — distorted by extreme outliers, not representative
2. **Report medians only** — more representative but loses variance information
3. **Clean outliers at 2.5 SD threshold, then report median** — removes technical errors while preserving statistical rigor

## Decision

Use median for primary reporting. Clean outliers using 2.5 standard deviation threshold from the mean. Patients beyond this threshold are classified as outliers (likely technical errors) and excluded.

## Rationale

- Median is roughly half the mean, indicating severe right-skew from outliers
- 2.5 SD is a standard statistical threshold for outlier removal
- Values like 300+ days to case manager are clearly not real clinical wait times
- This approach is defensible in the paper's methods section

## Consequences

- Need to verify the cleaned data still aligns with what was reported to the IRB (which stated 3-5 day wait times)
- Report must disclose the outlier cleaning methodology
- Median of 8 days (case manager) and 16 days (psychiatrist) after cleaning is clinically reasonable

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]