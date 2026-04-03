---
based_on:
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
confidence: medium
created: '2026-03-01'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is YAML apostrophe-escaping
  false positive (double single-quote in YAML represents literal apostrophe). Scanner
  does not resolve YAML-escaped characters in wikilink targets. No fix needed.
name: CM vs Psychiatrist Screen Split Determines AI Prompt Content
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Five-Agent Sequential Pipeline for Clinical AI Summaries]]'
- '[[constraint/DSM Criteria Require Criterion-Level Granularity in Screen Design]]'
source: task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split
status: active
type: assumption
---

# CM vs Psychiatrist Screen Split Determines AI Prompt Content

## Claim

The clinical responsibility split between case managers and psychiatrists directly determines what each AI agent asks and summarizes. The screen design decisions for each role are the upstream input that shapes AI prompt content — what topics the CM Agenda agent covers vs what the Psychiatrist Summary agent covers.

## Basis

The task to finalize the CM vs psychiatrist screen responsibility split explicitly states: "This split directly feeds into AI prompts (what to ask in each session type)" and that "case manager screen cannot be built until this is resolved." This creates a direct dependency chain from clinical workflow design to AI agent behavior.

## Evidence Trail

- 2025-01-12: Task created to finalize CM vs psychiatrist screen split, explicitly noting AI prompt dependency
- 2026-02-03: AI Agent Pipeline Training session showed agents use variable injection from patient/session data, with fixed templates adapted dynamically — confirming prompts are parameterized by session type

## Impact

If the clinical responsibility split changes, all downstream AI agent prompts for both CM and psychiatrist encounter types must be re-tuned. Delays in finalizing the split cascade into delays for AI agent development and screen design.
