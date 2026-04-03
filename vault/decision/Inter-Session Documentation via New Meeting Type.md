---
alfred_tags:
- clinical/inter-session-documentation
approved_by: []
based_on:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Add Inter-Session Documentation Entity to Clinical Platform]]'
body: '# Inter-Session Documentation via New Meeting Type


  ## Context


  All clinical documentation in the current system is tied to scheduled sessions (intake,
  follow-up, etc.). Psychiatrists frequently need to document events that occur between
  appointments — phone consultations, case manager escalations, informal clinical
  discussions — but have no place to record them. Rami described asking psychiatrists
  to send emails as a workaround, which is unsustainable.


  ## Options Considered


  1. **New meeting type definition** — Add "inter-session documentation" alongside
  existing meeting types (intake, follow-up, etc.)

  2. **Free-text notes field on patient record** — Add an unstructured notes area
  not tied to any session

  3. **Email-based documentation** — Continue using email as a workaround


  ## Decision


  Add a new meeting type (e.g., "inter-session documentation") as a first-class entity
  in the clinical platform. This is the simplest implementation path and integrates
  naturally with the existing meeting-centric data model.


  ## Rationale


  A new meeting type reuses the existing meeting infrastructure (screens, AI pipeline,
  data model) without requiring new entity types. It ensures inter-session events
  are part of the patient''s clinical record and can be consumed by AI agents for
  cross-session continuity.


  ## Consequences


  - AI agents (especially the Cross-Session Agent) will need to handle this new meeting
  type in their prompts

  - The meeting type taxonomy grows — documentation and training must reflect this

  - Reporting and analytics need to distinguish inter-session documentation from scheduled
  appointments


  ![[learn-decision.base#Based On]]

  ![[learn-decision.base#Related]]'
challenged_by: []
confidence: medium
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — learn-decision.base does not exist; body embeds (\![[learn-decision.base#Based
  On]] and \![[learn-decision.base#Related]]) reference missing base file. Duplicate
  base embeds also present in body (appears twice). Create _bases/learn-decision.base
  to enable dynamic views. Telia'z wikilink is valid (YAML escaping false positive).
name: Inter-Session Documentation via New Meeting Type
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
session: ''
source: Rami Khouri identifying gap in clinical documentation workflow
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# Inter-Session Documentation via New Meeting Type

## Context

All clinical documentation in the current system is tied to scheduled sessions (intake, follow-up, etc.). Psychiatrists frequently need to document events that occur between appointments — phone consultations, case manager escalations, informal clinical discussions — but have no place to record them. Rami described asking psychiatrists to send emails as a workaround, which is unsustainable.

## Options Considered

1. **New meeting type definition** — Add "inter-session documentation" alongside existing meeting types (intake, follow-up, etc.)
2. **Free-text notes field on patient record** — Add an unstructured notes area not tied to any session
3. **Email-based documentation** — Continue using email as a workaround

## Decision

Add a new meeting type (e.g., "inter-session documentation") as a first-class entity in the clinical platform. This is the simplest implementation path and integrates naturally with the existing meeting-centric data model.

## Rationale

A new meeting type reuses the existing meeting infrastructure (screens, AI pipeline, data model) without requiring new entity types. It ensures inter-session events are part of the patient's clinical record and can be consumed by AI agents for cross-session continuity.

## Consequences

- AI agents (especially the Cross-Session Agent) will need to handle this new meeting type in their prompts
- The meeting type taxonomy grows — documentation and training must reflect this
- Reporting and analytics need to distinguish inter-session documentation from scheduled appointments

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]