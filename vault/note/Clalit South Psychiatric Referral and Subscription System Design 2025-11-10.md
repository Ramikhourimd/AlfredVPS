---
created: '2026-03-01'
date: '2025-11-10'
description: null
janitor_note: 'LINK001: \![[related.base#All]] references missing base file. Telia
  links are valid YAML escaping (false positive).'
name: Clalit South Psychiatric Referral and Subscription System Design 2025-11-10
project: null
related: []
related_to:
- '[[org/Clalit Health Services]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
- '[[person/Rami Khouri]]'
relationships: []
session: null
status: final
subtype: null
tags:
- clalit
- referral-system
- subscription
- psychiatry
- form-17
type: note
---

# Clalit South Psychiatric Referral and Subscription System Design

## Overview

This note captures the design of the psychiatric referral and subscription system between [[project/Telia'z Clinic Israel|Telia'z]] and [[org/Clalit Health Services]] (South District), as discussed in the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]].

## Subscription Model

### Diagnostic Subscription

- **Purpose**: Single psychiatric evaluation visit
- **Form 17**: Generated automatically — no manual approval needed
- **Authorization**: Referring physician creates the referral in the Clalit system; Form 17 is auto-generated
- **Duration**: One visit
- **Pilot phase**: This is the starting pathway — see [[decision/Clalit South Pilot Starts With Diagnostic Subscriptions Only]]

### Treatment Subscription

- **Purpose**: Ongoing psychiatric treatment (multiple sessions)
- **Form 17**: Requires manual approval from district contact (Tzachi or [[person/Michal Boguz]])
- **Authorization**: Referring physician submits request; district contact must approve Form 17
- **Duration**: Indefinite — [[decision/Clalit South Patients Can Continue Treatment Indefinitely|patients can continue treatment without session limits]]
- **Status**: To be activated after pilot phase proves the diagnostic pathway

## Form 17 Workflow

1. **Diagnostic path**: Primary care physician refers patient → Clalit system auto-generates Form 17 → patient sees Telia'z psychiatrist
2. **Treatment path**: Primary care physician requests treatment subscription → district contact (Tzachi/[[person/Michal Boguz]]) approves Form 17 → patient begins ongoing treatment

Key constraint: [[constraint/Clalit Form 17 Requires Manual Approval by District Contact]] applies only to treatment subscriptions.

## Prescription Handling

- [[constraint/Clalit Pharmacies Do Not Accept External Prescriptions]] remains in effect
- Telia'z psychiatrists write prescriptions, but patients cannot fill them at Clalit pharmacies
- Workaround options: non-Clalit pharmacies or routing through Clalit primary care physician

## Volume and Capacity

- Projected volume: [[assumption/Clalit South Will Generate 200 Patients Per Week Within Three Months|~200 patients/week within 3 months]]
- Additional pipeline from former Hosen patients (facility closed) — see [[task/Contact Former Hosen Patients for Clalit South Pipeline]]
- Clalit system is noted as slower/heavier than Maccabi's; platform adaptation may be needed — see [[task/Evaluate Platform Adaptation for Clalit Subscription Workflow]]

## Operational Requirements

- Fax number needed for referral communications — see [[task/Obtain Clalit South District Fax Number]]
- BI system integration for data tracking
- Form 17 pilot testing — see [[task/Pilot Form 17 Process With Clalit South District]]

## Launch Timeline

- Target launch: November 20, 2025
- Start with diagnostic subscriptions only
- Expand to treatment subscriptions after pilot validation

## Related Preparation

This meeting was preceded by an internal [[note/Clalit Partnership Operational Planning 2025-11-09|preparation session]] where the Telia'z team anticipated many of these discussion points, including Tzachi's role in Form 17 approval and the prescription pharmacy limitation.

---
## Related
![[related.base#All]]
