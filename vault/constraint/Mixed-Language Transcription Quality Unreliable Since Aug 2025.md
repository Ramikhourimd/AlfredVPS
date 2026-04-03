---
alfred_tags:
- clinical-data/constraints
- data-access/bigquery
- data-quality/issues
authority: Technical limitation
created: '2025-08-01'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Embeds preserved
  per policy. Telia''z wikilinks are valid (YAML escaping false positive). Create
  _bases/learn-constraint.base to enable dynamic views.'
name: Mixed-Language Transcription Quality Unreliable Since Aug 2025
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[task/Explore Phone Call Transcription and De-identification Workflow]]'
- '[[note/Rivi Edelman Account Snapshot February 2026]]'
source: Innovation team meeting discussions Aug-Nov 2025
status: active
type: constraint
---

# Mixed-Language Transcription Quality Unreliable Since Aug 2025

## Constraint

Transcription of meetings and phone calls involving mixed languages (Hebrew, Arabic, English) produces unreliable output. This has been a known issue since August-November 2025 and directly affects the innovation team's ability to process clinical call data for research.

## Source

Technical limitation of available transcription tools when handling code-switching between Hebrew, Arabic, and English within a single conversation — common in the Israeli clinical context.

## Implications

- Cannot rely on automated transcription alone for clinical research data
- May require manual review or correction of transcripts
- Affects the feasibility and cost of the phone call transcription workflow being explored
- Limits the scale at which call data can be processed for AI training and research
- May require specialized transcription tools that handle multilingual content

## Expiry / Review

Review when evaluating transcription tools for the de-identification workflow. Transcription technology is improving rapidly — reassess available tools quarterly.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
