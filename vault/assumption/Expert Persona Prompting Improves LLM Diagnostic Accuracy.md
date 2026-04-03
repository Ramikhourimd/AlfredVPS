---
based_on:
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-26'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist yet — create base file to enable dynamic views.'
name: Expert Persona Prompting Improves LLM Diagnostic Accuracy
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming]]'
- '[[synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs]]'
source: Rami Khouri — pipeline results presentation
source_date: '2026-02-22'
status: active
tags:
- methodology
- expert-agent
- persona-prompting
type: assumption
---

# Expert Persona Prompting Improves LLM Diagnostic Accuracy

## Claim

Prompting the fusion LLM as a "psychiatrist" using DSM reasoning (the Expert Agent stage) improves diagnostic accuracy compared to the raw fusion output. The persona-based prompt causes the model to apply clinical reasoning patterns — such as keeping symptoms general rather than prematurely attributing them to specific disorders — that produce better diagnostic predictions.

## Basis

Stated in the 2026-02-22 methodology review: "The expert agent is prompted as a 'psychiatrist' using DSM reasoning. This improved diagnostic accuracy." The improvement is attributed to the model applying structured clinical reasoning rather than pattern-matching symptoms to diagnoses.

## Evidence Trail

- 2026-02-22: Rami presented the Expert Agent as a distinct pipeline stage that improved accuracy over raw fusion. The improvement mechanism is described as DSM-based clinical reasoning.
- Note: This is distinct from the Biased Agent finding. The Expert Agent improves accuracy; the Biased Agent (with contextual priming) replicates human diagnostic bias. The two are sequential stages with different effects.

## Impact

- Validates the multi-stage pipeline architecture — the Expert Agent stage adds measurable value.
- Suggests that persona-based prompting is a viable technique for domain-specific LLM applications in clinical settings.
- Quantitative accuracy improvement should be documented in Paper 1 results to justify the additional pipeline stage.
- If accuracy improvement is marginal, the additional pipeline complexity may not be justified.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
