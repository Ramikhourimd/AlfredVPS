---
alfred_tags:
- bituach-leumi/forms
- clinician/hours
approved_by: []
based_on:
- '[[note/National Insurance Form Filling Workflow 2025-11-10]]'
challenged_by: []
confidence: high
created: '2025-11-10'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z Clinic Israel wikilink is valid (YAML single-quote
  escaping false positive). Base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist — vault-wide infrastructure
  gap, embeds preserved.'
name: National Insurance Form Hours Approved as Admin Time
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Operations and System Management Meeting 2025-11-10]]'
- '[[task/Track National Insurance Form Volume]]'
relationships:
- confidence: 0.7
  context: Both handle hours logging/approval
  source: decision/National Insurance Form Hours Approved as Admin Time.md
  target: decision/Rivi Logs Overtime Clinical Hours Via Email to Basel.md
  type: related-to
- confidence: 0.9
  context: Decision is part of NI form workflow
  source: decision/National Insurance Form Hours Approved as Admin Time.md
  target: note/National Insurance Form Filling Workflow 2025-11-10.md
  type: part-of
session: null
source: Rami Khouri
source_date: '2025-11-10'
status: final
supports: []
tags: []
type: decision
---

# National Insurance Form Hours Approved as Admin Time

## Context

Clinicians spend time filling out national insurance (Bituach Leumi) forms for patients who need disability or welfare documentation. This work was not formally categorized in the workload tracking system.

## Options Considered

1. **Count as clinical time** — include in clinical session hours. Rejected because it inflates clinical capacity metrics.
2. **Count as administrative time** — separate category acknowledging the work. Selected as the honest approach.
3. **Uncompensated** — treat as unpaid extra work. Rejected as unfair to clinicians.

## Decision

National insurance form filling is approved as **administrative time**. Clinicians should log hours spent on NI forms separately from clinical sessions. Volume tracking is required to assess ongoing workload impact.

## Rationale

NI forms are a necessary part of patient care that require clinical expertise to complete properly. Categorizing them as admin time acknowledges the work without distorting clinical capacity metrics.

## Consequences

- Clinicians compensated for NI form work
- Volume tracking enables workload planning
- May need dedicated time slots if volume grows
- Clear categorization for payroll and scheduling

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]