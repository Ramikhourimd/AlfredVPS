---
based_on:
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
confidence: high
created: '2026-03-03'
janitor_note: 'LINK001 false-positive: project/Teliaz AI Clinical Platform wikilink
  is valid (YAML apostrophe escaping). ORPHAN001 — no inbound wikilinks; consider
  linking from project/Teliaz AI Clinical Platform or related AI pipeline records.'
name: AI Agent Prompts Inject Patient Demographics and Clinical Data as Template Variables
project:
- '[[project/Telia''z AI Clinical Platform]]'
source: Ohad Edri training session for new team member
source_date: '2026-02-03'
status: active
type: assumption
---

# AI Agent Prompts Inject Patient Demographics and Clinical Data as Template Variables

## Claim

Every AI agent in the clinical pipeline uses fixed structural templates with variable placeholders that are populated at runtime with patient-specific data — including gender, age, health data, and questionnaire responses. This means sensitive patient information flows directly into LLM prompts as template variables.

## Basis

During the 2026-02-03 training session, Ohad demonstrated the prompt engineering structure to a new team member. He showed that prompts contain variable placeholders populated with patient-specific data (gender, age, health data, questionnaire responses). The agenda agent specifically uses a fixed structural template that adapts questions dynamically based on these injected variables.

## Evidence Trail

- 2026-02-03: Ohad confirmed variable injection pattern in training walkthrough

## Impact

This architecture has direct implications for:
- **Data privacy**: Patient PII and PHI is transmitted to LLM providers with every agent invocation
- **Prompt security**: Variable injection must be sanitized to prevent prompt injection attacks
- **Compliance**: Any data governance or consent framework must account for this data flow
- **Agent design**: New agents inherit this pattern and must be designed with the same variable schema
