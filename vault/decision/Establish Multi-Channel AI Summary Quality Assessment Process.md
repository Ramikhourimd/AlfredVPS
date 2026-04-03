---
alfred_tags:
- ai/clinical-summaries/quality
approved_by: []
based_on:
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
challenged_by: []
confidence: high
created: '2026-03-31'
decided_by:
- '[[person/Rami Khouri]]'
name: Establish Multi-Channel AI Summary Quality Assessment Process
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/Psychiatrist AI Feedback Collected Through Informal WhatsApp Channel]]'
- '[[assumption/Informal Clinical Staff WhatsApp Feedback Captures Representative
  AI Quality Issues]]'
- '[[assumption/AI Summary System Excluded Case Manager Intake Data During Study Period]]'
relationships:
- confidence: 0.75
  context: Assessment process and prompt calibration linked
  source: decision/Establish Multi-Channel AI Summary Quality Assessment Process.md
  target: decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary
    Prompt.md
  type: related-to
session: null
source: Rami Khouri
source_date: '2025-11-11'
status: final
supports:
- '[[decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary Prompt]]'
tags: []
type: decision
---

# Establish Multi-Channel AI Summary Quality Assessment Process

## Context

During the 2025-11-11 meeting, Rami identified that AI-generated clinical summaries had a quality gap — specifically, summaries were ignoring case manager intake data. A single feedback mechanism would be insufficient to fully characterize AI quality issues because different stakeholders observe different aspects of quality.

## Options Considered

1. **Single channel (WhatsApp only)** — Monitor psychiatrist complaints informally
2. **Structured survey** — Formal quality assessment survey for clinical staff
3. **Multi-channel parallel assessment** — Combine informal monitoring, gold standard calibration, structured complaint compilation, and clinical workflow investigation

## Decision

Establish four parallel feedback channels for AI summary quality assessment:
1. **WhatsApp complaint monitoring** — Rivi monitors psychiatrist WhatsApp group for informal quality complaints and extracts patterns
2. **Gold standard example procurement** — Obtain a representative psychiatrist-created summary to serve as quality calibration target for the development team
3. **Structured complaint list** — Compile and prioritize system complaints from clinical staff into a formal document
4. **Patient follow-up flow investigation** — Rivi works with Shira and Renee to map the end-to-end patient workflow, identifying where AI summary quality affects clinical outcomes

## Rationale

Each channel captures different quality dimensions: WhatsApp reveals immediate frustrations, gold standard examples define target quality, structured lists enable systematic prioritization, and workflow investigation reveals downstream impact. Together they provide comprehensive quality assessment.

## Consequences

- Requires Rivi's time across multiple parallel workstreams
- Creates multiple evidence sources that may conflict (WhatsApp complaints may not align with workflow investigation findings)
- Provides the research paper with multi-dimensional evidence for AI clinical acceptance claims

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]