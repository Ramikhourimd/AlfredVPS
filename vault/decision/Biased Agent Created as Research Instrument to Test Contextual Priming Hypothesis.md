---
alfred_tags:
- ai/diagnostics
- research/paper-planning
- publication/scope
approved_by: []
based_on:
- '[[assumption/Psychiatrist PTSD Diagnostic Bias Driven by Contextual Priming]]'
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
- '[[decision/Five-Stage Sequential Agent Architecture for Diagnostic Prediction]]'
challenged_by: []
confidence: high
created: '2026-02-28'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Base view embeds (learn-decision.base) reference missing _bases/
  directory — vault-wide infrastructure issue, not per-file. BODY: Duplicate base
  embed section at end of body (appears twice with --- separator) — human should remove
  the duplicate block. ORPHAN001: No inbound wikilinks — needs linking from a conversation
  or synthesis record.'
name: Biased Agent Created as Research Instrument to Test Contextual Priming Hypothesis
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM Priming]]'
- '[[decision/Split AI Diagnostic Research Into Two Papers]]'
relationships:
- confidence: 0.95
  context: Biased agent creation and its deferral to P2
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/Defer Fusion and Bias Agent Coverage to Paper 2.md
  type: related-to
- confidence: 0.75
  context: P1 content decisions involving bias agent
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/First Paper Covers Methodology Plus Basic Clinical Results.md
  type: related-to
- confidence: 0.7
  context: Scoping P1 methodology around bias agent
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/Limit Paper 1 Methodology to Three Figures.md
  type: related-to
- confidence: 0.8
  context: Splitting diagnostic research including bias
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/Split AI Diagnostic Research Into Two Papers.md
  type: related-to
- confidence: 0.75
  context: Splitting AI research including bias agent
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/Split AI Research Into Two Papers.md
  type: related-to
- confidence: 0.92
  context: Splitting bias findings from biased agent
  source: decision/Biased Agent Created as Research Instrument to Test Contextual
    Priming Hypothesis.md
  target: decision/Split Bias Findings Into Separate Paper.md
  type: related-to
session: null
source: Rami Khouri — research methodology design
source_date: '2026-02-22'
status: final
supports:
- '[[synthesis/Contextual Priming Replicates Psychiatrist Diagnostic Bias in LLMs]]'
- '[[decision/Defer Fusion and Bias Agent Coverage to Paper 2]]'
tags: []
type: decision
---

# Biased Agent Created as Research Instrument to Test Contextual Priming Hypothesis

## Context

After the Expert Agent (LLM prompted as psychiatrist using DSM reasoning) showed improved diagnostic accuracy, the team observed that real psychiatrists in the post-war clinical context showed a consistent bias toward PTSD diagnosis even when symptoms better fit depression or anxiety. The question arose: could contextual priming cause the same bias in an LLM?

## Options Considered

1. **Report Expert Agent results only** — Present the unbiased LLM diagnostic accuracy and note the discrepancy with psychiatrist diagnoses as a limitation
2. **Create a Biased Agent stage** — Add contextual priming to the Expert Agent (e.g., "you are a psychiatrist in a post-war context") and compare its output against both the unbiased Expert Agent and human psychiatrist diagnoses

## Decision

Create a separate "Biased Agent" as the final pipeline stage — the Expert Agent with additional contextual priming matching the real clinical context. This serves as a research instrument to test whether contextual framing causes LLMs to replicate human diagnostic bias.

## Rationale

The Biased Agent is not intended to improve diagnostic accuracy. It is a controlled experimental condition that isolates the effect of contextual priming on LLM diagnostic behavior. By comparing Expert Agent (DSM-only reasoning) against Biased Agent (DSM + contextual framing), the research can demonstrate that the same contextual factors influencing human psychiatrists also influence LLM outputs. This transforms an observation about psychiatrist bias into a testable, reproducible finding.

## Consequences

- The pipeline gains an additional stage specifically for research purposes, not clinical use
- The bias finding becomes strong enough to warrant a separate paper (Paper 2)
- The methodology demonstrates that LLM diagnostic bias can be controlled via prompt engineering
- Paper 1 can exclude the Biased Agent (deferred to Paper 2), keeping the methods section focused

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]