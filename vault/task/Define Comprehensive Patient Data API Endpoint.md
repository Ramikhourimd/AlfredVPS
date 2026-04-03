---
alfred_instructions: null
assigned: '[[person/Shachar]]'
blocked_by: []
created: '2026-02-03'
depends_on: []
description: Design and build a single API endpoint that returns all available data
  for a given patient, so AI agents can select what they need rather than requiring
  separate endpoints per agent. Alternative to building per-agent API endpoints. Requires
  coordination with Shachar Segev.
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). related.base#All is a template-standard base view embed referencing
  _bases/related.base which may not exist.
kind: task
name: Define Comprehensive Patient Data API Endpoint
priority: medium
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/AI Agent Pipeline Training Session 2026-02-03]]'
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[person/Ohad Edri]]'
- '[[person/Shachar]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Define Comprehensive Patient Data API Endpoint

Currently, data is pulled via Shachar's API using specific endpoints (e.g., post-general). The team discussed two approaches:

1. **Per-agent endpoints** — Each agent gets a tailored API returning only its needed inputs
2. **Single comprehensive endpoint** — One API returns all available patient data; the agent selects what it needs (preferred)

Ohad expressed preference for option 2. This task covers designing that unified patient data API, requiring coordination with [[person/Shachar]] who built the existing API infrastructure.

The agent needs at minimum: meeting ID, session type, and patient identifier to know what data to fetch.

## Context

Discussed during [[conversation/AI Agent Pipeline Training Session 2026-02-03]].

## Related
![[related.base#All]]

## Outcome
