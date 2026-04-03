---
alfred_instructions: null
assigned: '[[person/Rami Khouri]]'
blocked_by: []
created: '2026-02-12'
depends_on: []
description: Build AI agent that performs factual checking of clinical summaries against
  transcripts, producing color-coded output (green=verified, red=hallucination, orange=interpretation)
due: null
janitor_note: LINK001 — Telia'z wikilinks are YAML escaping false positives (targets
  exist). Base view embed (related.base) preserved per policy.
kind: task
name: Build Factual Check Agent for AI Clinical Summaries
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[person/Stav Zamir]]'
- '[[person/Ohad Edri]]'
- '[[person/Shachar]]'
- '[[person/Rivi Idelman]]'
- '[[decision/Color-Coded Factual Checking for AI Clinical Summaries]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Build Factual Check Agent for AI Clinical Summaries

Build an AI agent that compares generated clinical summaries against session transcripts and produces a color-coded reliability assessment:
- **Green** — Verified: content corroborated by transcript
- **Red** — Hallucination: content with no reference in transcript
- **Orange** — Interpretation: AI-generated inference or paraphrasing

## Context

Emerged from [[conversation/Product Development Update Meeting 2026-02-12]]. Rami to work with Stav on prompts and Ohad on technical build. Needs transcript data from Shachar's system. Rivi will design the frontend presentation once the agent output format is defined.

## Related
![[related.base#All]]

## Outcome
