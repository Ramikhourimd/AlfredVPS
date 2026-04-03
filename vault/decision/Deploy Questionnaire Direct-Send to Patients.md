---
approved_by: []
based_on:
- '[[note/Platform Questionnaire Direct-Send Verification Call 2025-10-09]]'
challenged_by: []
confidence: high
created: '2025-10-09'
decided_by:
- '[[person/Shachar]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML single-quote escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — vault-wide systemic issue; embeds
  preserved per policy.'
name: Deploy Questionnaire Direct-Send to Patients
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[project/Telia''z Clinic Israel]]'
session: null
source: Shachar Segev — confirmed deployment during verification call
source_date: '2025-10-09'
status: final
supports: []
tags: []
type: decision
---

# Deploy Questionnaire Direct-Send to Patients

## Context

The clinical platform previously required manual intervention to send intake questionnaires to patients. A change was requested to automate this so questionnaires are sent directly to patients upon record creation.

## Options Considered

1. **Manual questionnaire distribution** — staff manually sends questionnaires after intake entry (status quo)
2. **Automatic direct-send** — system sends questionnaire directly to patient when record is opened and details entered

## Decision

Deploy automatic questionnaire direct-send. Shachar confirmed the change was implemented during a verification call on 2025-10-09.

## Rationale

Reduces manual steps in the intake workflow and ensures patients receive questionnaires promptly without staff having to remember to send them.

## Consequences

- Requires patient phone number to be present in the record for delivery to work
- Data quality at intake becomes critical — missing contact details will silently prevent questionnaire delivery
- Identified data quality issue during verification: a case where patient name was not recorded, raising questions about completeness of intake data entry

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
