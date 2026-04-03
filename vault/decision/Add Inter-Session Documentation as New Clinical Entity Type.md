---
alfred_tags:
- clinical/inter-session-documentation
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — vault-wide infrastructure gap,
  embeds preserved. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  AI Clinical Platform.'
name: Add Inter-Session Documentation as New Clinical Entity Type
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Add Inter-Session Documentation Entity to Clinical Platform]]'
relationships:
- confidence: 0.95
  context: Alternative proposals for inter-session doc
  source: decision/Add Inter-Session Documentation as New Clinical Entity Type.md
  target: decision/Add Inter-Session Documentation as New Meeting Type.md
  type: related-to
- confidence: 0.9
  context: Alternative approaches to inter-session doc
  source: decision/Add Inter-Session Documentation as New Clinical Entity Type.md
  target: decision/Inter-Session Documentation via New Meeting Type.md
  type: related-to
- confidence: 0.7
  context: AI summaries enhance clinical entities
  source: decision/Add Inter-Session Documentation as New Clinical Entity Type.md
  target: decision/Color-Coded Factual Checking for AI Clinical Summaries.md
  type: related-to
- confidence: 0.65
  context: JSON output for clinical summaries
  source: decision/Add Inter-Session Documentation as New Clinical Entity Type.md
  target: decision/Standardize AI Summary Output as Structured JSON.md
  type: related-to
- confidence: 0.6
  context: Calibrated prompts for entities
  source: decision/Add Inter-Session Documentation as New Clinical Entity Type.md
  target: decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary
    Prompt.md
  type: related-to
session: null
source: Rami Khouri — identified gap in clinical documentation workflow
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# Add Inter-Session Documentation as New Clinical Entity Type

## Context

All clinical documentation in the current system is tied to scheduled meeting sessions (intake, follow-up, etc.). However, psychiatrists frequently need to document events that occur between appointments — phone consultations, case manager escalations, urgent patient communications, and informal clinical discussions. Currently, psychiatrists send emails to document these events, which is unsustainable and creates unstructured records outside the clinical platform.

## Options Considered

1. **New meeting type entity (e.g., "inter-session documentation")** — Add alongside intake, follow-up, etc.
2. **Free-text notes attached to patient record** — Unstructured note field without meeting structure
3. **Continue with email-based documentation** — Status quo

## Decision

Add a new meeting type definition (e.g., "inter-session documentation") to the clinical platform alongside the existing intake and follow-up meeting types. This gives between-appointment notes the same structured treatment as scheduled sessions.

## Rationale

Using the existing meeting type infrastructure is the simplest implementation path. It allows inter-session notes to flow through the same AI agent pipeline (summarization, cross-session analysis) without requiring a separate documentation subsystem. It also ensures these notes appear in the patient timeline alongside scheduled sessions.

## Consequences

- Requires a new meeting type definition in the platform configuration
- AI agents may need prompt adjustments to handle inter-session context differently from scheduled sessions
- Enables more complete patient records and better cross-session AI analysis

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]