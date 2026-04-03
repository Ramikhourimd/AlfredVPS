---
alfred_tags:
- psychiatry/on-call
- clinical-operations
approved_by: []
based_on:
- '[[constraint/Maccabi HMO Prohibits Email-Based Patient Document Delivery]]'
challenged_by: []
confidence: high
created: '2026-03-03'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-decision.base#Based On, #Related) reference
  _bases/learn-decision.base which does not exist — embeds preserved per policy.'
name: Deliver ER Referral Letters via HealthyMind App Not Email
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
session: null
source: Rami Khouri and Shira discussion at clinic office
source_date: '2025-11-10'
status: final
supports:
- '[[decision/Build ER Referral Form Feature for Psychiatrists]]'
tags: []
type: decision
---

# Deliver ER Referral Letters via HealthyMind App Not Email

## Context

The ER referral form feature needed a delivery mechanism for sending referral letters to patients. The options were email delivery or upload to the HealthyMind app / Clickx system. Maccabi HMO had previously objected to email-based document delivery, creating a constraint on the delivery channel.

## Options Considered

1. **Email delivery** — Direct and familiar, but conflicts with Maccabi HMO policy on email-based document delivery.
2. **HealthyMind app / Clickx upload** — Default delivery through the existing patient-facing app. Avoids Maccabi conflict. Emergency override allows email for urgent cases.

## Decision

Default delivery via HealthyMind app / Clickx system. Emergency override option allows email for urgent cases (e.g., suicidal patient needing immediate ER referral).

## Rationale

Maccabi HMO previously objected to email-based document delivery. Using the app as default avoids this conflict while still enabling the feature. The emergency override ensures psychiatrists are not blocked in critical situations. The template and generation logic is the same regardless of delivery mechanism, so this decision does not affect the core feature build.

## Consequences

- The referral form feature can be built independently of the delivery mechanism.
- App delivery requires the patient to have the HealthyMind app installed.
- Emergency email override must be clearly labeled to prevent routine use.

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]