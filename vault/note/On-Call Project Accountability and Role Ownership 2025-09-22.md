---
alfred_tags:
- on-call-system/issues
- incident-review
- project/accountability
created: '2025-09-22'
description: Accountability discussion during the on-call incident review meeting.
  Dekkel clarified that Rami owns the on-call project end-to-end, including ensuring
  training happens even if delegated. Rami proposed bringing Elinor into operational
  management for projects without case managers.
janitor_note: 'LINK001: All flagged links are false positives — Telia''z and org/Telia''z
  wikilinks use YAML quote escaping and resolve correctly, related.base#All is a structural
  template embed.'
name: On-Call Project Accountability and Role Ownership 2025-09-22
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Oren Taliaz]]'
- '[[person/Alex Lellouche]]'
- '[[org/Telia''z]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[task/Bring Elinor Into On-Call Operational Management]]'
relationships:
- confidence: 0.7
  context: Accountability vs later failure
  source: note/On-Call Project Accountability and Role Ownership 2025-09-22.md
  target: note/On-Call Schedule Failure and Patient Intake Verification 2025-10-09.md
  type: related-to
- confidence: 0.6
  context: Role issues in verification
  source: note/On-Call Project Accountability and Role Ownership 2025-09-22.md
  target: note/Platform Questionnaire Direct-Send Verification Call 2025-10-09.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# On-Call Project Accountability and Role Ownership 2025-09-22

## Context

During the [[conversation/On-Call Incident Review Leadership Meeting 2025-09-22]], a significant accountability discussion took place between [[person/Dekkel Taliaz]], [[person/Oren Taliaz]], and [[person/Rami Khouri]] about project ownership for the on-call psychiatrist service.

## The Accountability Gap

Multiple issues "fell between the chairs" leading to the on-call incident:
- On-call psychiatrists (Atef and Ahmad) were added to a WhatsApp group but never formally trained on the alert system
- Training was supposed to happen but got missed when Rami was abroad
- The operational management of the on-call service (as distinct from clinical oversight) had no clear owner
- Existing onboarding processes split between Shira (clinical training) and Roy Shur (system access/accounts), but this new service had neither a case manager nor a clear operational lead

## Dekkel's Position

[[person/Dekkel Taliaz]] stated clearly:
- From the leadership perspective, the on-call project was a **"closed project"** — meaning it was Rami's responsibility end-to-end
- Even if Rami delegates tasks to Roy, Shachar, or others, Rami must **verify they happen**
- If Rami believes someone else should own part of the project, he must **flag it proactively** to leadership, not let it fall through
- The same principle applies as with the clinic: Rami is the operational driver

## Rami's Response

[[person/Rami Khouri]] partially disagreed:
- He was the de facto on-call operator himself and was closely managing the system
- The training gap specifically happened because he was abroad twice, and during that absence the doctors who took over on-call duty were not trained
- He acknowledged the gap but argued it was a timing issue, not a structural ownership failure
- He proposed bringing Elinor (or Shira) into operational project management for services that lack case managers, as a structural fix

## Structural Issue Identified

The broader issue surfaced: the clinic's operational management (onboarding, training, system setup) is split across multiple people:
- **Shira** — clinical training and onboarding
- **Roy Shur** — system accounts and technical setup
- **Shachar** — telephony and platform components
- **Nadav** (previously) / Roy (currently) — non-clinical onboarding elements

For the on-call service specifically, there was no case manager and no designated operational lead other than Rami, creating a single point of failure when he traveled.

## Resolution

- Rami accepted the accountability framing going forward
- Rami will manage the immediate fixes and report to leadership
- Leadership (Oren, Dekkel) agreed to stay informed but not micromanage the fixes
- [[person/Alex Lellouche]] will attend the lessons-learned session if available
- Rami proposed bringing Elinor into operational management as a structural solution — see [[task/Bring Elinor Into On-Call Operational Management]]

## Related
![[related.base#All]]