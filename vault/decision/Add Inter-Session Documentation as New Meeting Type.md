---
alfred_tags:
- clinical/inter-session-documentation
approved_by: []
based_on:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — create it to enable dynamic views. BODY DUPLICATION — entire
  decision body (Context, Options, Decision, Rationale, Consequences + base embeds)
  is repeated 3x after a --- separator. Requires manual cleanup: keep first copy,
  delete everything after first \![[learn-decision.base#Related]]. ORPHAN001 — no
  inbound wikilinks; consider linking from project/Telia''z AI Clinical Platform.'
name: Add Inter-Session Documentation as New Meeting Type
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Add Inter-Session Documentation Entity to Clinical Platform]]'
relationships:
- confidence: 0.95
  context: Similar meeting type approaches for inter-session
  source: decision/Add Inter-Session Documentation as New Meeting Type.md
  target: decision/Inter-Session Documentation via New Meeting Type.md
  type: related-to
- confidence: 0.7
  context: AI checking for meeting summaries
  source: decision/Add Inter-Session Documentation as New Meeting Type.md
  target: decision/Color-Coded Factual Checking for AI Clinical Summaries.md
  type: related-to
- confidence: 0.65
  context: JSON std for meeting summaries
  source: decision/Add Inter-Session Documentation as New Meeting Type.md
  target: decision/Standardize AI Summary Output as Structured JSON.md
  type: related-to
- confidence: 0.6
  context: Prompt calibration for meetings
  source: decision/Add Inter-Session Documentation as New Meeting Type.md
  target: decision/Use Gold Standard Psychiatrist Example to Calibrate AI Summary
    Prompt.md
  type: related-to
session: null
source: Rami Khouri, Product Development Update Meeting
source_date: '2026-02-12'
status: draft
supports: []
tags: []
type: decision
---

# Add Inter-Session Documentation as New Meeting Type

## Context

Psychiatrists sometimes need to document clinical interactions that happen outside of scheduled sessions — phone consultations, case manager escalations, informal consults with Rami. Currently, all documentation in the system is tied to scheduled sessions. When these inter-session events occur, Rami asks psychiatrists to send emails, which is not sustainable and creates untracked clinical records.

## Options Considered

1. **New meeting type entity** — Add "inter-session documentation" alongside intake, follow-up, etc.
2. **Free-text notes field on patient record** — Unstructured note-taking without session structure
3. **Email-based documentation** — Continue current workaround (rejected as unsustainable)

## Decision

Add a new meeting type definition (e.g., "inter-session documentation") to the clinical platform. This creates a proper documentation entity for between-appointment events.

## Rationale

A new meeting type is the simplest implementation that maintains consistency with the existing session-based architecture. It avoids creating a separate documentation system while capturing events that currently go unrecorded or are tracked only via email.

## Consequences

- Requires a new meeting type definition in the platform
- AI agents may need to handle this new session type differently (no transcript, no questionnaire)
- Case manager and psychiatrist workflows must be updated to include the new type
- Historical inter-session events documented via email will not be retroactively captured

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]

# Add Inter-Session Documentation as New Meeting Type

## Context

Psychiatrists sometimes need to document clinical interactions that happen outside of scheduled sessions — phone consultations, case manager escalations, informal consults with Rami. Currently, all documentation in the system is tied to scheduled sessions. When these inter-session events occur, Rami asks psychiatrists to send emails, which is not sustainable and creates untracked clinical records.

## Options Considered

1. **New meeting type entity** — Add "inter-session documentation" alongside intake, follow-up, etc.
2. **Free-text notes field on patient record** — Unstructured note-taking without session structure
3. **Email-based documentation** — Continue current workaround (rejected as unsustainable)

## Decision

Add a new meeting type definition (e.g., "inter-session documentation") to the clinical platform. This creates a proper documentation entity for between-appointment events.

## Rationale

A new meeting type is the simplest implementation that maintains consistency with the existing session-based architecture. It avoids creating a separate documentation system while capturing events that currently go unrecorded or are tracked only via email.

## Consequences

- Requires a new meeting type definition in the platform
- AI agents may need to handle this new session type differently (no transcript, no questionnaire)
- Case manager and psychiatrist workflows must be updated to include the new type
- Historical inter-session events documented via email will not be retroactively captured

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]