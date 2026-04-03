---
approved_by: []
based_on:
- '[[assumption/Feature Impact Measurement Requires Pre-Release Baseline Survey]]'
challenged_by: []
confidence: medium
created: '2026-03-30'
decided_by:
- '[[person/Rami Khouri]]'
name: Combine Psychiatrist Satisfaction Survey With Feature Baseline Measurement
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build Psychiatrist Feedback Survey for Summary Feature Baseline]]'
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
session: null
source: Rami Khouri — dual-purpose survey concept during feature planning
source_date: '2025-01-12'
status: draft
supports: []
tags: []
type: decision
---

# Combine Psychiatrist Satisfaction Survey With Feature Baseline Measurement

## Context

Rami planned a psychiatrist satisfaction survey. Separately, the team identified the need for baseline metrics before releasing AI summary features (like/dislike button, expanded summaries). Rather than running two separate instruments, Rami decided to combine both purposes into a single survey.

## Options Considered

1. **Separate surveys** — One for general satisfaction, one for feature baseline. Clean data but survey fatigue risk with busy psychiatrists.
2. **Combined dual-purpose survey** — Single instrument covering both satisfaction and baseline metrics. Efficient but requires careful question design.

## Decision

Use a single survey instrument that serves both purposes: collecting psychiatrist satisfaction feedback AND establishing baseline metrics for measuring the impact of upcoming AI summary features. The key metric to establish is whether the current AI feature allows faster summary turnaround, with clear success/failure criteria defined before the next feature release.

## Rationale

Psychiatrists have limited bandwidth for administrative tasks. A single well-designed survey maximizes response rates while capturing both the satisfaction baseline and the feature impact baseline needed for future evaluation. Distribution goes through Shira via Alice/Elis to leverage existing clinical communication channels.

## Consequences

- Feature impact measurement is tied to satisfaction survey timeline — if the survey is delayed, baseline data is delayed
- Survey must be designed to cleanly separate satisfaction questions from feature-specific baseline questions
- Summary turnaround speed becomes a measurable, trackable KPI for AI feature evaluation

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
