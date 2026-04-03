---
alfred_instructions: null
assigned: '[[person/Rivi Idelman]]'
blocked_by: []
created: '2026-02-12'
depends_on: []
description: Add a new meeting type for between-appointment clinical documentation
  — free-text notes not attached to a scheduled session, for recording phone consultations
  and inter-session events
due: null
janitor_note: LINK001 — All wikilinks are valid (YAML escaping false positive for
  apostrophes). Base view embed (related.base#All) references _bases/related.base
  which does not exist — vault-wide infrastructure gap.
kind: task
name: Add Inter-Session Documentation Entity to Clinical Platform
priority: medium
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[person/Rami Khouri]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Add Inter-Session Documentation Entity to Clinical Platform

Add a new meeting type (or clinical documentation entity) for between-appointment notes. Currently, all documentation is tied to scheduled sessions. Psychiatrists need a way to record phone consultations, case manager escalations, and other inter-session events directly in the patient record.

## Context

Emerged from [[conversation/Product Development Update Meeting 2026-02-12]]. Rami described the gap: when a psychiatrist consults him between sessions, there is no way to document it in the system. Currently asking them to send emails, but this is not sustainable.

The simplest implementation: add a new meeting type definition (e.g., "inter-session documentation") alongside intake, follow-up, etc.

## Related
![[related.base#All]]

## Outcome
