---
alfred_tags:
- ai/summary-mode-switch
- clinic/workflow-transition
- transcript-vs-real-time
based_on:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[task/Obtain Approval Time Data by Session Type]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide infrastructure gap, embeds preserved. ORPHAN001
  — no inbound wikilinks; consider linking from project/Telia''z AI Diagnostic Research
  Paper.'
name: Transcript and Real-Time Operational Periods Are Cleanly Separable
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Measure Summary Approval Time Not Generation Time]]'
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
relationships:
- confidence: 0.85
  context: Separability relies on clean boundary
  source: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  target: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  type: depends-on
- confidence: 0.75
  context: Separable periods enable low approval
  source: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  target: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  type: supports
- confidence: 0.7
  context: Separability ties to Transcript timing metric
  source: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  target: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  type: related-to
source: Implied in meeting discussions about before/after comparison
source_date: '2026-02-22'
status: active
type: assumption
---

# Transcript and Real-Time Operational Periods Are Cleanly Separable

## Claim

The clinic's switch from transcript-based (post-session) summary generation to real-time (during-session) summary generation represents a clean operational cutover, allowing the data to be split into two distinct periods for before/after comparison.

## Basis

The 8-column timing data request assumes sessions can be categorized as either "transcript mode" or "real-time mode" without overlap or ambiguity. The team plans to compare approval times between these two modes as evidence of the real-time system's clinical efficiency improvement.

## Evidence Trail

- 2026-02-22: Rami requested 8-column segmented data splitting by mode (transcript vs real-time)
- Pending: Shmulik to provide the segmented data export

## Impact

If the transition was gradual (e.g., pilot rollout, partial adoption, or mixed-mode operation during a transition period), sessions from the transition period could contaminate both groups. This would weaken the before/after comparison. The paper's claims about real-time mode efficiency gains depend on clean separation of the two operational periods.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]