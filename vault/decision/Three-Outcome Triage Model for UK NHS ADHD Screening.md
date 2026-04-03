---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
janitor_note: 'LINK001: Base view embeds (learn-decision.base#Based On, learn-decision.base#Related)
  reference _bases/ files that do not exist — systemic infrastructure gap. Body contains
  both escaped embeds (\\![[...]]) and actual embeds (\![[...]]) creating duplicates
  — human should remove the escaped versions above the --- separator and keep only
  the actual embeds below it.'
name: Three-Outcome Triage Model for UK NHS ADHD Screening
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03]]'
- '[[decision/OMG Handles Triage and Governance While Telia''z Provides Psychiatric
  Services]]'
- '[[assumption/OMG Will Handle Initial Patient Triage for NHS ADHD Pathway]]'
session: null
source: Rami Khouri and Adiel Levin pathway design session
source_date: '2025-07-03'
status: final
supports: []
tags: []
type: decision
---

# Three-Outcome Triage Model for UK NHS ADHD Screening

## Context

During the OMG pathway design session, Rami and Adiel mapped the triage stage where OMG staff screen patients using health inequity and high risk factors. The triage produces exactly three outcomes.

## Options Considered

1. **Binary triage** — suitable or not suitable
2. **Three-outcome model** — not suitable, need more info, or suitable
3. **Scoring-based triage** — numeric risk score with threshold

## Decision

The NHS ADHD triage uses a three-outcome model:
- **Not suitable** → returned to GP with explanation
- **Need more info** → returned to GP with specific data request
- **Suitable** → referred onward to Telia'z psychiatric assessment

## Rationale

A binary model would lose patients who are potentially suitable but lack sufficient referral information. The "need more info" pathway allows GPs to supplement the referral rather than forcing a reject/accept decision on incomplete data.

## Consequences

- Creates a feedback loop with referring GPs (improving referral quality over time)
- Adds complexity to the triage workflow (three pathways vs two)
- Requires clear criteria for each outcome to ensure consistent screening
- The "need more info" pathway may introduce delays in patient progression

\![[learn-decision.base#Based On]]
\![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
