---
alfred_tags:
- clinical-documentation/inter-session
- ai/clinical-summaries
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML single-quote escaping false
  positive). Base view embeds reference learn-decision.base which does not exist in
  _bases/; create it to enable dynamic views. Do NOT remove the embeds. BODY — duplicate
  base view embeds found after --- separator (Based On and Related sections appear
  twice). Remove the second set manually: delete everything after the first set of
  embeds ending with \![[learn-decision.base#Related]].'
name: Standardize AI Summary Output as Structured JSON
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
session: null
source: Product meeting consensus
source_date: '2026-02-25'
status: draft
supports: []
tags: []
type: decision
---

# Standardize AI Summary Output as Structured JSON

## Context

AI-generated clinical session summaries currently lack a uniform output format, making downstream processing, scoring, and comparison difficult. Different summary types may use different section names and hierarchies.

## Options Considered

1. **Option A** — Free-text summaries with no enforced structure
2. **Option B** — Structured JSON with uniform section hierarchy, with optional HTML rendering

## Decision

Option B: Move to structured JSON output with a standardized section hierarchy. HTML alternative available for display purposes when needed. Product and Engineering to define the schema contract.

## Rationale

Structured output enables automated scoring, comparison between original and long summaries, consistent rendering across clients, and downstream analytics. A uniform schema contract prevents integration fragility.

## Consequences

- Product + Engineering must define and agree on JSON schema (section names, hierarchy)
- Existing summary generation pipelines need migration to the new format
- Enables original vs long summary comparison API
- International deployments benefit from configurable section names

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
