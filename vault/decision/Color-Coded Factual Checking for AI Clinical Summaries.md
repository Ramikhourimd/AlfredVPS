---
alfred_tags:
- ai/clinical-summaries/quality
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-12'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  learn-decision.base embeds reference missing _bases/learn-decision.base. Duplicate
  base view embeds (Based On and Related appear twice after --- separator) — remove
  duplicates manually.
name: Color-Coded Factual Checking for AI Clinical Summaries
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[person/Stav Zamir]]'
- '[[person/Ohad Edri]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
relationships:
- confidence: 0.75
  context: Factual checks support inter-session
  source: decision/Color-Coded Factual Checking for AI Clinical Summaries.md
  target: decision/Inter-Session Documentation via New Meeting Type.md
  type: related-to
- confidence: 0.85
  context: Color-coding is one multi-channel assessment method
  source: decision/Color-Coded Factual Checking for AI Clinical Summaries.md
  target: decision/Establish Multi-Channel AI Summary Quality Assessment Process.md
  type: part-of
- confidence: 0.7
  context: Both enhance AI clinical summary quality
  source: decision/Color-Coded Factual Checking for AI Clinical Summaries.md
  target: decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary
    Prompt.md
  type: related-to
session: null
source: Product Development Update Meeting 2026-02-12
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# Color-Coded Factual Checking for AI Clinical Summaries

## Context

AI-generated clinical summaries sometimes contain hallucinations or unsupported interpretations. Psychiatrists need a way to quickly identify reliable vs unreliable content without adding extra approval steps. The existing AI summary quality gap has been unresolved since November 2025.

## Options Considered

1. **Confirmation popup** — Require psychiatrists to click through a factual check confirmation before sending. Rejected because it adds friction and psychiatrists want to send summaries quickly.
2. **Color-coded inline annotations** — Display summary text with color coding indicating reliability. Preferred because it requires no additional clicks and integrates naturally into the editing workflow.
3. **Separate factual check report** — Generate a side report listing discrepancies. Not discussed but implied as overly complex.

## Decision

Use inline color coding within the AI summary editor:
- **Green** — Verified: content directly corroborated by session transcript
- **Red** — Hallucination: content with no corresponding reference in the transcript
- **Orange** — Interpretation: AI-generated inference or paraphrasing not directly stated

## Rationale

Color coding is the most user-friendly approach because psychiatrists can assess reliability at a glance while editing, without any additional interaction steps. It was unanimously preferred by both Rami and Rivi.

## Consequences

- Requires building a factual-checking AI agent (Rami + Stav on prompts, Ohad on build)
- Agent needs access to transcript data from R&D (Shachar)
- Frontend work needed to render color-coded text in the summary editor (Rivi)
- Three-level classification hierarchy must be defined in the agent spec

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]