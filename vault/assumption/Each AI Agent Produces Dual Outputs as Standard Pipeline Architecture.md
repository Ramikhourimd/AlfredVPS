---
based_on:
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
confidence: high
confirmed_by:
- '[[decision/Five-Agent Sequential Pipeline for Clinical AI Summaries]]'
- '[[decision/Sequential Multi-Agent Pipeline for Clinical Encounters]]'
created: '2026-02-28'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML apostrophe
  escaping false positive, target exists). No actual broken links.
name: Each AI Agent Produces Dual Outputs as Standard Pipeline Architecture
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Standardize AI Summary Output as Structured JSON]]'
source: Ohad Edri training session
source_date: '2026-02-03'
status: active
type: assumption
---

# Each AI Agent Produces Dual Outputs as Standard Pipeline Architecture

## Claim

Every AI agent in the clinical pipeline produces two distinct output types: a standard summary and an additional specialized output specific to the agent's function. This dual-output pattern is consistent across all five agents (CM Agenda, CM Summary, Triage, Cross-Session, Patient Summary).

## Basis

Observed during the AI pipeline training session led by Ohad Edri on 2026-02-03. The training explicitly described each agent as having "two output types: a standard summary and an additional specialized output." For example, the CM Agenda agent produces both a questionnaire synopsis (summary) and personalized follow-up questions (specialized output).

## Evidence Trail

- 2026-02-03: Ohad demonstrated the dual-output pattern during new team member onboarding. The Retool interface shows both outputs for each session.

## Impact

- Any new agent added to the pipeline should follow the dual-output convention
- The output JSON schema must accommodate both output types per agent
- Downstream consumers (Retool UI, reports, cross-session analysis) must handle both output types
- The standardized JSON output decision should account for this dual structure
