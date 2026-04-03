---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  missing _bases/ file — vault-wide gap. ORPHAN001 — low-risk for draft decision.
  No fix needed.'
name: File Classification Agent Requires Image-to-Text Preprocessing
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
session: null
source: Rami Khouri — proposed during product sync
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# File Classification Agent Requires Image-to-Text Preprocessing

## Context

The Innovation team is building an AI agent that classifies and summarizes patient-uploaded files (PDFs, images, scanned documents). These files arrive in non-text formats that cannot be directly fed into the LLM-based summarization agents.

## Options Considered

1. **Preprocessing pipeline (PDF/image → text → agent)** — Convert uploaded files to text before feeding to the AI classification agent
2. **Multimodal agent (direct image/PDF input)** — Use a vision-capable model to process files directly without text extraction

## Decision

Implement a preprocessing step that converts uploaded PDFs and images to text before passing content to the clinical summary agent. This creates a two-stage pipeline: file-to-text conversion, then text-to-classification/summary.

## Rationale

The existing AI agent pipeline is text-based (prompts with variable injection). Adding a preprocessing stage maintains architectural consistency with the current pipeline rather than introducing a fundamentally different multimodal approach. It also allows the same summarization agents to handle file-derived content alongside questionnaire and transcript data.

## Consequences

- Requires coordination with Shachar's R&D team for API access (cross-team dependency)
- File-to-text conversion quality directly impacts downstream agent output
- Creates a dependency: file upload feature (Shmulik) → preprocessing pipeline → classification agent

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
