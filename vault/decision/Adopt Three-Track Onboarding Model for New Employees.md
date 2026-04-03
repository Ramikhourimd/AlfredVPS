---
alfred_tags:
- clinic/scaling
- psychiatrist/management
- operations/structures
approved_by: []
based_on:
- '[[note/New Employee Onboarding Structure Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Structure and Technology Requirements 2026-02-12]]'
- '[[note/New Employee Onboarding Framework Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Framework and Technology Requirements 2026-02-12]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — create base file to enable dynamic
  views.'
name: Adopt Three-Track Onboarding Model for New Employees
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[process/Clinic Israel New Employee Onboarding]]'
relationships:
- confidence: 0.65
  context: Onboards staff for psych intakes
  source: decision/Adopt Three-Track Onboarding Model for New Employees.md
  target: decision/Formal Patient Discharge Requires Completed Psychiatry Intake Examination.md
  type: supports
- confidence: 0.75
  context: Recruitment and onboarding for staff
  source: decision/Adopt Three-Track Onboarding Model for New Employees.md
  target: decision/Psychiatrist Residency Pipeline Recruitment Model.md
  type: related-to
- confidence: 0.65
  context: Onboarding aids UK rollout
  source: decision/Adopt Three-Track Onboarding Model for New Employees.md
  target: decision/Replicate Israel Three-Step Clinical Workflow for UK.md
  type: supports
session: ''
source: Rami Khouri
source_date: '2026-02-12'
status: final
supports:
- '[[task/Formalize New Employee Onboarding Process]]'
tags: []
type: decision
---

# Adopt Three-Track Onboarding Model for New Employees

## Context

As Clinic Israel scales its hiring of psychiatrists and case managers, the lack of a structured onboarding process created recurring problems — new clinicians arriving unable to access clinical systems, unclear expectations about workflows, and delayed productivity. Rami Khouri and Elias Jahjah discussed this across multiple 1:1 clinical management meetings on 2026-02-12.

## Options Considered

1. **Single comprehensive onboarding session** — Cover everything in one session. Rejected because it overloads new hires and creates scheduling bottlenecks.
2. **Three-track model with mandatory technology prerequisite** — Separate operational, administrative, and technology tracks. Technology is the hard day-one requirement; other tracks can flex.
3. **Ad hoc onboarding** — Continue the informal approach. Rejected because it repeatedly left new clinicians blocked on basic access.

## Decision

Adopt a three-track onboarding model:
1. **Technology Track (MANDATORY day-one)** — Microsoft Teams and HoViD access. Without this, a new clinician cannot see patients or communicate.
2. **Operational Track** — Clinical workflows, patient handling, system usage. Can start without formal session.
3. **Administrative Track** — HR, payroll, agreements. Can start independently.

Cadence: Monthly or bi-weekly, flexing based on hiring volume. Delivery: Stav Zamir or Shira leads the combined technology + operational session.

## Rationale

The critical failure mode is a new clinician arriving without Teams access — in a fully remote telepsychiatry clinic, this completely blocks all clinical work. By isolating technology as a mandatory prerequisite and allowing other tracks to flex, the model ensures new hires are productive from day one while accommodating variable hiring volumes.

## Consequences

- Technology setup becomes a hard gate in the hiring workflow
- Stav Zamir or Shira take on formal onboarding delivery responsibility
- Clinical onboarding (supervision, protocols) remains separate from operational onboarding

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]