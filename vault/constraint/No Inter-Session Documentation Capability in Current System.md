---
authority: Current Retool platform architecture
created: '2026-02-27'
janitor_note: 'LINK001 false positives: Telia''z wikilinks resolve correctly (YAML
  single-quote escaping). learn-constraint.base embeds are base view references (no
  action). ORPHAN001: no inbound links — flagging for curator review.'
location:
- '[[project/Telia''z Clinic Israel]]'
name: No Inter-Session Documentation Capability in Current System
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Inter-Session Documentation via New Meeting Type]]'
- '[[task/Add Inter-Session Documentation Entity to Clinical Platform]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
source: System design limitation — all documentation tied to scheduled sessions
source_date: '2026-02-12'
status: active
type: constraint
---

# No Inter-Session Documentation Capability in Current System

## Constraint

The current clinical platform has no mechanism for documenting events that occur between scheduled appointments. All clinical documentation is tied to meeting sessions (intake, follow-up, etc.). Phone consultations, case manager escalations, medication inquiries, and other inter-session clinical events cannot be recorded in the patient record through the system.

## Source

Architectural limitation of the Retool-based platform, which models all clinical documentation as meeting records. Identified by Rami Khouri during the 2026-02-12 product meeting when describing how psychiatrists are forced to send emails to document between-session consultations.

## Implications

- Psychiatrists' between-session clinical work is undocumented or documented via email (not part of the patient record)
- AI agents lack visibility into inter-session events, reducing cross-session summary quality
- Medico-legal risk: clinical decisions made during phone consultations have no formal record
- Workaround (email) is unsustainable and creates data silos

## Expiry / Review

Expected to be resolved when the new meeting type ("inter-session documentation") is implemented, either in the current Retool system or in Shachar's rebuilt platform.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
