---
approved_by: []
based_on:
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
challenged_by: []
confidence: high
created: '2025-11-09'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z project wikilink is valid (YAML single-quote escaping
  false positive). constraint/Maccabi Commitment Validation link verified present.
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/ infrastructure
  not yet created — vault-wide gap, embeds preserved.'
name: Require Clalit Form 17 Approval Before Patient Referral to Clinic
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
  MADAC]]'
session: null
source: Rami Khouri and team, Clalit partnership preparation meeting
source_date: '2025-11-09'
status: final
supports:
- '[[decision/Clalit and Leumit Targeted as 2026 HMO Expansion Partners]]'
tags: []
type: decision
---

# Require Clalit Form 17 Approval Before Patient Referral to Clinic

## Context

During the 2025-11-09 Clalit partnership preparation meeting, the team reviewed lessons from the Maccabi rollout where patients were sent to the clinic before authorization was confirmed — creating situations where front-desk staff (Renee) could not process patients who arrived without valid commitments.

## Options Considered

1. **Allow referrals before Form 17 approval** — faster patient flow but risk of unauthorized arrivals
2. **Require Form 17 approval before referral** — slower but prevents authorization gaps

## Decision

Patients must NOT be referred to Telia'z until their Clalit Form 17 authorization is fully approved. This prevents the Maccabi-era problem of patients arriving at the clinic without valid authorization, which created operational chaos and uncompensated sessions.

## Rationale

The Maccabi experience demonstrated that patients arriving without authorization creates cascading problems: secretaries cannot process them, sessions may go uncompensated, and patients become frustrated. By requiring Form 17 completion before referral, the clinic ensures every arriving patient has a valid authorization.

## Consequences

- Slower initial patient flow from Clalit pipeline
- Cleaner authorization records from day one
- Depends on Clalit contact (Tzachi/Eli) processing Form 17s in a timely manner — SLA is undefined

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
