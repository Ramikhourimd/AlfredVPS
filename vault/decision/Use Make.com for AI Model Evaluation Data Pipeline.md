---
approved_by: []
based_on:
- '[[note/Innovation Sprint AI Model Evaluation and UX Design 2025-01-16]]'
challenged_by: []
confidence: medium
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Ahmed Masalha]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base) reference missing _bases/ infrastructure
  — vault-wide gap. BODY FIX NEEDED: Remove lines 27-30 (duplicate --- and base embed
  block after Consequences section). ORPHAN001 — no inbound wikilinks; consider linking
  from project/Telia''z Innovation Program.'
name: Use Make.com for AI Model Evaluation Data Pipeline
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[decision/Start AI Evaluation With Independent Scoring Before Pairwise Comparison]]'
session: ''
source: Innovation sprint meeting
source_date: '2025-01-16'
status: final
supports:
- '[[task/Populate AI Model Evaluation Table With O1 and Gemini Results]]'
tags:
- automation
- make-com
- ai-evaluation
type: decision
---

# Use Make.com for AI Model Evaluation Data Pipeline

## Context

The AI model evaluation process requires extracting patient session data from Google Drive, running it through multiple AI models, and populating a comparison spreadsheet with results and latency metrics.

## Options Considered

1. **Manual data extraction** — Manually copy-paste data between systems
2. **Make.com automation** — Build automated scenarios to extract, process, and populate
3. **Custom script** — Write a bespoke pipeline in Python or similar

## Decision

Use Make.com to build an automated scenario for data extraction and evaluation table population. Ahmad (Ahmed Masalha) was assigned to build a cleaner scenario.

## Rationale

Make.com is already in use within the team's workflow. It provides visual automation, integrates with Google Drive natively, and can be modified by non-developers. A custom script would be more flexible but harder to maintain.

## Consequences

The evaluation pipeline depends on Make.com's reliability and API limits. Ahmad needs to build and test the scenario. Any changes to Google Drive structure or evaluation criteria require scenario updates.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
