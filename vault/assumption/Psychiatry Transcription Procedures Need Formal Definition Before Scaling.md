---
based_on:
- '[[task/Define Psychiatry Transcription Procedures]]'
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
confidence: medium
created: '2026-03-08'
janitor_note: 'LINK001 false positive: Telia''z wikilinks use valid YAML single-quote
  escaping; targets exist in vault. ORPHAN001: No inbound links — consider linking
  from a parent record.'
name: Psychiatry Transcription Procedures Need Formal Definition Before Scaling
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Five-Agent Sequential Pipeline for Clinical AI Summaries]]'
- '[[decision/Store Meeting Transcripts as Database Text Not Files]]'
- '[[decision/Four-Section Structured Format for Meeting Markdown Files]]'
source: task/Define Psychiatry Transcription Procedures
status: active
type: assumption
---

# Psychiatry Transcription Procedures Need Formal Definition Before Scaling

## Claim

The AI agent pipeline currently processes case manager sessions with established transcription procedures, but psychiatry session transcription lacks equivalent standardization. Before expanding the AI summary pipeline to psychiatrist encounters, formal transcription procedures must be defined.

## Basis

A dedicated task ("Define Psychiatry Transcription Procedures") was created from the February 2026 product meeting, indicating this is recognized as a gap. The existing pipeline was built around case manager workflows first. Psychiatrist sessions have different clinical content (medication management, diagnostic assessment, treatment planning) that may require different transcription handling.

## Evidence Trail

- 2026-02-25: Product meeting identifies psychiatry transcription procedures as an action item for Rami

## Impact

- Blocks expansion of AI summary pipeline to psychiatrist sessions
- Without standardized procedures, AI agents cannot reliably process psychiatrist encounter types
- Affects the five-agent pipeline architecture which currently focuses on CM encounter types
