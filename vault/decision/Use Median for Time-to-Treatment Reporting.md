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
janitor_note: LINK001 — Fixed Dekkel Khouri -> Dekkel Taliaz. Telia'z wikilinks valid
  (YAML escaping false positive). learn-decision.base embeds reference missing _bases/learn-decision.base.
  Body has DUPLICATE base view embeds (appears twice) — remove one set manually. ORPHAN001
  — no inbound links.
name: Use Median for Time-to-Treatment Reporting
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Progress Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[task/Clean Outliers From Time-to-Treatment Data]]'
relationships:
- confidence: 0.65
  context: Reporting uses cleaned timing data
  source: decision/Use Median for Time-to-Treatment Reporting.md
  target: decision/Use 2.5 Standard Deviations for Outlier Removal in Timing Data.md
  type: depends-on
- confidence: 0.9
  context: Reporting uses cleaned median timing
  source: decision/Use Median for Time-to-Treatment Reporting.md
  target: decision/Use Median With Outlier Cleaning for Timing Data.md
  type: depends-on
session: null
source: AI Diagnostic Paper Progress Meeting 2026-02-22
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Use Median for Time-to-Treatment Reporting

## Context

Time-to-treatment data shows extremely high variance with outliers of 170+ hours and 300+ days. The mean is approximately double the median, making it unrepresentative of the typical patient experience.

## Options Considered

1. **Report mean** — Standard but misleading given the extreme outlier distribution.
2. **Report median** — Better represents typical patient experience. Selected.
3. **Report both** — Possible but mean is so distorted by outliers that it may confuse readers.

## Decision

Report median values for all time-to-treatment metrics. Outliers will first be removed at 2.5 standard deviations, then median of cleaned data will be reported.

## Rationale

- Median (8 days to case manager, 16 days to psychiatrist) reflects actual patient experience
- Mean (~14 days to case manager, 25 days to psychiatrist) is inflated by data artifacts
- Standard statistical approach for skewed clinical data with known outlier sources

## Consequences

- Must document outlier removal methodology in the paper
- Need to report the outlier threshold and number of removed records for transparency

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]