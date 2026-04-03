---
based_on:
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
confidence: high
created: '2026-03-03'
janitor_note: 'LINK001: [[project/Telia''z AI Clinical Platform]] wikilink is valid
  (YAML escaping false positive). ORPHAN001: no inbound wikilinks — consider linking
  from project/Telia''z AI Clinical Platform.'
name: CM Agenda Agent Transforms Questionnaire Answers Into Contextual Follow-Up Questions
project:
- '[[project/Telia''z AI Clinical Platform]]'
source: Ohad Edri training session demonstration
source_date: '2026-02-03'
status: active
type: assumption
---

# CM Agenda Agent Transforms Questionnaire Answers Into Contextual Follow-Up Questions

## Claim

The CM Agenda agent does not simply relay or summarize intake questionnaire responses. It transforms them into deeper, context-aware follow-up questions that guide the case manager toward clinically relevant conversation in the follow-up session. For example, a questionnaire answer about "unstable career history" becomes the follow-up question "What is your current employment status today?"

## Basis

During the 2026-02-03 onboarding session, Ohad demonstrated this transformation behavior explicitly, showing how the agent converts questionnaire data into an agenda of personalized follow-up questions. The stated design intent is to prevent case managers from re-asking basic questions the patient already answered, instead deepening the clinical conversation.

## Evidence Trail

- 2026-02-03: Ohad demonstrated the transformation pattern with specific examples during new team member training

## Impact

This assumption shapes:
- **Prompt design**: The agent's prompt must be engineered to understand questionnaire semantics well enough to formulate meaningful follow-up questions
- **Clinical quality**: If the transformation is poor (superficial rephrasing rather than genuine deepening), case managers receive less clinical value
- **Questionnaire design**: Changes to intake questionnaires directly affect what the agenda agent can produce — the two are coupled
- **Evaluation criteria**: Measuring agent quality requires assessing whether follow-up questions are genuinely deeper than the source answers, not just reformatted
