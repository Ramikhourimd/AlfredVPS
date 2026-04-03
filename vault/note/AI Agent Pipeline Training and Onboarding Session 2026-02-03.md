---
alfred_tags:
- clinical/operations
- staff/onboarding
created: '2026-02-03'
description: Comprehensive onboarding session led by Ohad Edri training a new team
  member (Eli) on the AI agent pipeline architecture, Retool platform navigation,
  prompt engineering patterns, patient data workflows, and API integration with Shachar's
  endpoints.
janitor_note: LINK001 — Teliaz wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide issue, embed preserved.
name: AI Agent Pipeline Training and Onboarding Session 2026-02-03
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Ohad Edri]]'
- '[[person/Rami Khouri]]'
- '[[person/Stav Zamir]]'
- '[[person/Shachar]]'
- '[[person/Nadav Blatt]]'
- '[[person/Adiel Levin]]'
- '[[org/Telia''z]]'
- '[[conversation/AI Agent Pipeline Training Session 2026-02-03]]'
- '[[project/Telia''z Innovation Program]]'
relationships:
- confidence: 0.85
  context: AI onboarding relates to framework discussion
  source: note/AI Agent Pipeline Training and Onboarding Session 2026-02-03.md
  target: note/New Employee Onboarding Framework Discussion 2026-02-12.md
  type: related-to
- confidence: 0.8
  context: AI onboarding relates to framework tech reqs
  source: note/AI Agent Pipeline Training and Onboarding Session 2026-02-03.md
  target: note/New Employee Onboarding Framework and Technology Requirements 2026-02-12.md
  type: related-to
- confidence: 0.75
  context: AI onboarding relates to structure discussion
  source: note/AI Agent Pipeline Training and Onboarding Session 2026-02-03.md
  target: note/New Employee Onboarding Structure Discussion 2026-02-12.md
  type: related-to
- confidence: 0.7
  context: AI onboarding relates to structure tech reqs
  source: note/AI Agent Pipeline Training and Onboarding Session 2026-02-03.md
  target: note/New Employee Onboarding Structure and Technology Requirements 2026-02-12.md
  type: related-to
- confidence: 0.7
  context: Shared onboarding and training themes
  source: note/AI Agent Pipeline Training and Onboarding Session 2026-02-03.md
  target: note/Clinic Operations and Staff Onboarding Update 2025-09-01.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Agent Pipeline Training and Onboarding Session 2026-02-03

## Context

Ohad Edri led a hands-on training session for a new team member (Eli) on the AI clinical platform's agent pipeline. Rami Khouri was briefly present at the beginning. The session covered the full technical stack — from Retool UI navigation to prompt engineering patterns to API data flows — providing the new team member with the knowledge needed to work on AI agents independently.

## AI Agent Pipeline Overview

The platform runs several AI agents in a pipeline for each patient encounter:

1. **CM Agenda Agent** — Takes the intake questionnaire responses and generates a personalized follow-up agenda for the case manager. Instead of asking basic questions again, it transforms questionnaire answers into deeper, context-aware follow-up questions (e.g., "You described unstable career history — what is your current employment status today?").
2. **CM Summary Agent** — Produces a summary of the case manager intake session.
3. **Triage Agent** — Classifies and routes patient information.
4. **Cross-Session Agent** — Handles data across multiple sessions for continuity.
5. **Patient Summary (prod)** — Generates a summary before the psychiatrist's follow-up session, combining prior session data.

Each agent has two output types: a standard summary and an additional specialized output.

## Retool Platform Walkthrough

- Ohad demonstrated the Retool interface where all meetings are accessible.
- Navigating by "CM Intake" shows individual patient sessions.
- Each session has a **Summary** (questionnaire synopsis in bullet points) and an **Agenda** (personalized follow-up questions derived from questionnaire data).
- The agenda uses a fixed structural template but adapts questions dynamically based on questionnaire responses.

## Prompt Engineering Structure

- **Variables injection:** Prompts contain variable placeholders that get populated with patient-specific data (gender, age, health data, questionnaire responses).
- **Question & Response format:** Prompts use HTML-structured Q&A format for input.
- **Enforced output structure:** Most prompts enforce a JSON-like output schema so downstream systems can consume the results predictably.
- **Legacy prompts:** Some prompts still use Nadav Blatt's original format (noted as surprising they're still in use). New prompts are more structured.
- **Agent projects in Retool:** Each agent is organized as a "project" folder. Within each, there are subfolders (e.g., "CM Agenda") containing logs with input, result, and prompt trace data.

## Patient Data Workflows

- **Patient Export folders:** Per-patient data exports containing all available information — ID, clinic, date of birth, questionnaire, meeting details (start, type, duration), transcripts, summaries.
- **Data access pattern:** Enter a patient HMCB identifier to access all their data through Retool or the Patient Export drive.
- **Log structure:** Each agent folder has input, result, and log files per patient per run.

## API Integration (Shachar's API)

- Data is pulled via Shachar Segev's API endpoints (e.g., `post-general`).
- The API provides patient data fields: gender, age, health info, and questionnaire data.
- **Two API approaches discussed:**
  1. Separate API endpoints per agent (each requesting specific input combinations)
  2. A single comprehensive API that returns all available patient data, letting the agent select what it needs (preferred approach)
- **Agent trigger requirements:** Each agent needs meeting ID, session type, and patient identifier to know what data to request and where to fetch it from.

## Automation and Storage

- **n8n automation:** Used for uploading and processing workflows.
- **Google Drive upload flow:** Meeting recordings and transcripts auto-upload to Google Drive.
- **Recording storage:** Ohad mentioned having a personal automation that uploads recordings, suggesting the pipeline will need similar infrastructure.

## Team Process Expectations

- New team member must send a written summary after each training meeting.
- Must coordinate with Stav Zamir for completeness checks on agent inventory.
- Immediate assignment: Create a comprehensive breakdown document listing all agents, their inputs, and outputs. Verify against the shared prompt folder that nothing is missing.
- Should examine 10+ patient export samples to understand the data structure and verify the agent inventory is complete.

## Key References

- **Prompt repository:** Shared folder with all agent prompts (linked in meeting)
- **Format folder:** Contains both active and inactive format definitions for each agent's input/output
- **Patient Export (September):** Sample patient data exports for reference
- **Nadav Blatt's legacy prompts:** Some still in production, referenced as baseline

## Related
![[related.base#All]]