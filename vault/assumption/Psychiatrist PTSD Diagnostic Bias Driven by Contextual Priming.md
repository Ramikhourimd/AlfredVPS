---
alfred_tags:
- psychiatry/ptsd-diagnosis
- diagnostic-bias/contextual
- dsm/critique
based_on:
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
confidence: medium
created: '2026-02-22'
janitor_note: 'LINK001: Fixed [[person/Dekkel Khouri]] -> [[person/Dekkel Taliaz]]
  (wrong surname). LINK001: Base view embeds (learn-assumption.base) are not broken
  links — scanner false positive from _bases/ pattern. ORPHAN001: No inbound wikilinks
  detected — new record, may need linking from related records.'
name: Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLM]]'
relationships:
- confidence: 0.85
  context: PTSD bias example questions DSM sufficiency
  source: assumption/Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming.md
  target: assumption/DSM Raises Question of Sufficiency as Standalone Diagnostic Framework.md
  type: supports
- confidence: 0.8
  context: Both show context bias in PTSD diagnosis
  source: assumption/Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming.md
  target: assumption/Psychiatrists Diagnose PTSD Based on Context Rather Than Strict
    DSM Criteria.md
  type: related-to
source: AI diagnostic pipeline bias analysis by Rami Khouri
source_date: '2026-02-22'
status: active
type: assumption
---

# Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming

## Claim

In the post-war clinical context, psychiatrists tend to diagnose PTSD even when the patient's symptoms better fit depression according to DSM criteria. This bias is driven by contextual priming (awareness of the wartime environment) rather than by symptom-based clinical reasoning.

## Basis

When an LLM is given a generic psychiatrist persona, it diagnoses depression based on the same symptom data. When the same LLM is given a post-war psychiatrist persona (contextual priming), it shifts diagnoses toward PTSD — matching what real psychiatrists actually diagnosed. This suggests the real psychiatrists' PTSD tendency is context-driven, not purely symptom-driven.

## Evidence Trail

- 2026-02-22: Rami presented this finding at the research meeting
- Expert agent (unbiased) produced MDD diagnoses for cases where biased expert and real psychiatrists produced PTSD
- PHQ scores correlated with depression but not PCL-5, supporting the depression interpretation
- Noam noted this needs more detailed data (specific percentages) to be presented convincingly

## Impact

This is a significant finding that could challenge assumptions about DSM-based diagnostic practice. It has been assigned to a separate second paper due to its significance and the additional analysis required.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]