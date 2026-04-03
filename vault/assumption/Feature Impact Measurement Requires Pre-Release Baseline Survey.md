---
based_on:
- '[[task/Build Psychiatrist Feedback Survey for Summary Feature Baseline]]'
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
confidence: medium
created: '2026-03-11'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-assumption.base#Depends On This, #Related)
  reference _bases/learn-assumption.base which does not exist — vault-wide infrastructure
  gap, embeds preserved. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  AI Clinical Platform or a related task/conversation record.'
name: Feature Impact Measurement Requires Pre-Release Baseline Survey
project:
- '[[project/Telia''z AI Clinical Platform]]'
related: []
source: Rami Khouri — psychiatrist feedback survey planning
source_date: '2025-01-12'
status: active
tags: []
type: assumption
---

# Feature Impact Measurement Requires Pre-Release Baseline Survey

## Claim

Before releasing new AI summary features (like the like/dislike button and expanded summaries), the team must establish baseline metrics via a psychiatrist survey. Without this baseline, there is no way to measure whether the feature improved clinical workflow or summary turnaround time.

## Basis

Rami planned a dual-purpose psychiatrist questionnaire: one layer collects satisfaction and engagement data, the other establishes quantitative baselines for AI summary usage. The metric of interest is whether features allow faster summary turnaround — but "faster" requires a before measurement to be meaningful.

## Evidence Trail

- 2025-01-12: Rami directed creation of dual-purpose survey combining satisfaction feedback with feature impact baselines
- Survey to be distributed via Shira through existing clinical communication channels

## Impact

This assumption gates feature release sequencing: new AI summary features should not ship until the baseline survey has been distributed and collected. If the survey is delayed or skipped, the team loses the ability to quantify feature ROI — reducing future features to subjective assessment only.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
