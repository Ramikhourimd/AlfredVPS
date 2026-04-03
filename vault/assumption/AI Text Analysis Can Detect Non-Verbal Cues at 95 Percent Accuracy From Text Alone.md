---
confidence: medium
created: '2026-03-02'
date: '2025-11-13'
description: Assumption that language models can determine patient affect and detect
  absence of eye contact from text transcription alone at approximately 95% accuracy,
  making video processing unnecessary for most clinical purposes.
holder: '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Telia''z wikilinks are YAML escaping false positives (targets
  verified). Links to note/Conference Discussion and assumption/Text-Based Sentiment
  Analysis need manual verification. Base view embeds (related.base, learn-assumption.base)
  reference missing _bases/ infrastructure — vault-wide gap, not per-file fixable.
  ORPHAN001: No inbound wikilinks — consider linking from related projects or notes.'
name: AI Text Analysis Can Detect Non-Verbal Cues at 95 Percent Accuracy From Text
  Alone
projects:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic Scale
  2025-11-13]]'
- '[[assumption/Text-Based Sentiment Analysis Outperforms Standardized Questionnaires
  for Clinical Outcome Tracking]]'
source: '[[note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic
  Scale 2025-11-13]]'
status: active
tags:
- NLP
- affect-detection
- eye-contact
- text-analysis
- AI-capabilities
type: assumption
---

## Statement

Language models can accurately determine patient clinical status — including affect, tone, and even absence of eye contact — from text-based session transcription alone, achieving approximately 95% accuracy. Video analysis would only add roughly 2% additional accuracy.

## Evidence

- Claimed by Rami based on Telia'z operational experience with their AI clinical platform
- The system currently processes only text (transcription summaries) and does not store audio or video
- The practical decision not to save audio/video is partly justified by this assumption

## Conditions for Validity

- Accuracy likely depends on transcription quality and completeness
- May vary by patient population, language, and clinical presentation
- The 95% figure may be specific to certain clinical indicators (affect) and less applicable to others
- Requires calibration against gold-standard clinical assessments

## Risks if Wrong

- If text-based analysis misses significant non-verbal signals, clinical assessments could have blind spots
- Decision not to store video may result in irrecoverable loss of clinically relevant data
- Future research requiring video data would be impossible to conduct retrospectively

## Strategic Implication

This assumption supports the current operational model of text-only data retention, which reduces storage costs, bureaucratic overhead (no patient consent for recordings needed), and processing complexity.
