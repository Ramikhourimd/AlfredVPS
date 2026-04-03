---
alfred_tags:
- ai/clinical-summaries
- quality-assumptions
- research-study
based_on:
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
confidence: low
created: '2026-03-31'
name: Informal Clinical Staff WhatsApp Feedback Captures Representative AI Quality
  Issues
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/Psychiatrist AI Feedback Collected Through Informal WhatsApp Channel]]'
- '[[decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary Prompt]]'
source: Rami Khouri, 2025-11-11 meeting with Rivi Idelman
source_date: '2025-11-11'
status: active
type: assumption
---

# Informal Clinical Staff WhatsApp Feedback Captures Representative AI Quality Issues

## Claim

Psychiatrist complaints and observations posted in informal WhatsApp group channels represent a reliable and sufficiently representative sample of AI-generated clinical summary quality issues. Monitoring and extracting patterns from these messages can drive systematic quality improvements to the AI summary system.

## Basis

During the 2025-11-11 meeting, Rami directed Rivi to monitor the psychiatrist WhatsApp group, extract complaint patterns, and compile a prioritized system complaint list. This approach treats informal chat messages as actionable quality data, implying the feedback is representative rather than anecdotal.

The constraint that feedback is collected through WhatsApp (rather than structured surveys or formal reporting) is documented separately. This assumption concerns whether that informally collected feedback is actually reliable enough to base system changes on.

## Evidence Trail

- 2025-11-11: Rami establishes WhatsApp monitoring as a primary feedback channel for AI summary quality
- Gold standard summary example approach also established as complementary evidence (separate decision)

## Impact

If this assumption holds: WhatsApp monitoring is a low-cost, high-signal quality assurance mechanism.

If this assumption fails: Quality improvements based on WhatsApp complaints may address vocal minority issues while missing systematic quality problems that clinicians don't bother to report. A structured feedback survey or systematic quality audit may be needed.

The research paper's claims about clinical acceptance of AI summaries may partly rest on this informal evidence.