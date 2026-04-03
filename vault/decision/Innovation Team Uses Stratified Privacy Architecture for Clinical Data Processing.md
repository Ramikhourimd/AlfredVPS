---
approved_by: []
based_on:
- '[[note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic Scale
  2025-11-13]]'
challenged_by: []
confidence: medium
created: '2026-03-07'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Base view embeds reference _bases/ files not yet created (systemic).
  Duplicate base embeds at end of body need manual removal (lines after --- are duplicates).
  note/Conference Discussion link target verified — exists in vault (false positive).
  ORPHAN001: No inbound links. Teliaz wikilink is valid (YAML escaping false positive).'
name: Innovation Team Uses Stratified Privacy Architecture for Clinical Data Processing
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline]]'
session: null
source: Rami Khouri, conference discussion with Rambam colleague
source_date: '2025-11-13'
status: draft
supports: []
tags: []
type: decision
---

# Innovation Team Uses Stratified Privacy Architecture for Clinical Data Processing

## Context

During a psychiatric conference on 2025-11-13, Rami described the innovation team's approach to handling clinical data in their AI analysis pipeline to a Rambam-affiliated colleague. The conversation revealed a deliberate three-tier privacy architecture that stratifies data sensitivity across processing stages.

## Options Considered

1. **Fully local processing** — All AI processing including transcription runs on local infrastructure only
2. **Fully cloud-based** — Use external LLM APIs for both code generation and data processing
3. **Stratified approach** — Use external LLMs for code generation only, keep patient data analysis local, accept external transcription services

## Decision

The innovation team adopted a stratified privacy architecture with three tiers:

- **Code generation (external, no patient data)**: GPT-4 writes Python analysis code. The model never sees patient data — only code generation prompts.
- **Data analysis (local only)**: All patient data processing runs locally using the generated code. Demographic, clinical, and outcome data never leaves local infrastructure.
- **Transcription (external, accepted risk)**: Claude is used for clinical session transcription. The team acknowledges this is not local but continues using it, implying an accepted risk tradeoff — likely because no local alternative exists at comparable quality.

## Rationale

The primary concern is preventing patient data from being processed by external LLMs where terms of service may allow data retention or training use. By using LLMs only for code generation, the analytical processing stays entirely local. Transcription is treated as an acceptable risk — possibly because raw audio is harder to de-anonymize in isolation, or because operational necessity outweighs the privacy concern.

## Consequences

- Patient demographic and clinical analysis data never leaves local infrastructure
- Transcription data (audio and text) does pass through external services (Claude)
- Any future regulatory scrutiny (UK GDPR, Israeli privacy law) may require revisiting the transcription tier
- The architecture enables rapid iteration on analysis methodology without exposing patient data

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
