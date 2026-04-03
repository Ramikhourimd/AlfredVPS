---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-22'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist — embeds preserved per
  policy. Body has DUPLICATE base view embeds — needs manual dedup (remove second
  set after ---). Fixed: decided_by [[person/Dekkel Khouri]] → [[person/Dekkel Taliaz]].'
name: Split Bias Findings Into Separate Paper
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
relationships:
- confidence: 0.95
  context: Findings from biased agent
  source: decision/Split Bias Findings Into Separate Paper.md
  target: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  type: depends-on
session: null
source: Research meeting 2026-02-22
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Split Bias Findings Into Separate Paper

## Context

The AI diagnostic research generated two distinct categories of findings: (1) the methodology for extracting symptoms and predicting diagnoses from questionnaires and case manager data, and (2) a novel finding about psychiatrist diagnostic bias (PTSD over-diagnosis driven by contextual priming rather than DSM criteria). Combining both into one paper would make the methods section excessively long and dilute the bias finding.

## Options Considered

1. **Single paper with everything** — all methodology, clinical results, and bias findings in one paper. Rejected because it would be too methods-heavy and the bias story deserves focused treatment.
2. **Two papers — methodology first, bias second** — Paper 1 covers the diagnostic pipeline methodology with basic clinical results (questionnaire and case manager predictions, timing data). Paper 2 builds on Paper 1 to present the bias/contextual priming findings with anthropological analysis.

## Decision

Split into two papers. Paper 1 focuses on methodology and basic clinical prediction results. Paper 2 presents the bias/contextual priming findings as a standalone contribution.

## Rationale

- The bias finding tells "a different story" (Rami's words) that deserves its own focused treatment
- The methodology for symptom extraction is itself novel and warrants detailed presentation
- Paper 1 is already methods-heavy; adding fusion/expert/biased-expert agents would overload it
- The bias finding could potentially be a standalone paper with anthropological analysis

## Consequences

- Paper 1 includes: questionnaire analysis, case manager transcript analysis, timing data, demographics, PHQ correlation
- Paper 1 excludes: fusion model, expert agent, biased expert agent results
- Paper 2 will need to reference Paper 1 for methodology baseline
- Paper 2 may require additional analysis work on the bias finding

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]