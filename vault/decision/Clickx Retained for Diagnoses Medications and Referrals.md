---
approved_by: []
based_on:
- '[[note/Clickx EHR System Migration and Access Management 2025-11-10]]'
challenged_by: []
confidence: high
created: '2025-11-10'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z Clinic Israel wikilink is valid (YAML single-quote
  escaping false positive). Base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist — vault-wide infrastructure
  gap, embeds preserved.'
name: Clickx Retained for Diagnoses Medications and Referrals
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Operations and System Management Meeting 2025-11-10]]'
- '[[task/Resolve Clickx Access for Staff Members]]'
- '[[task/Transition Clickx to Individual User Accounts]]'
- '[[task/Train Clinicians on Clickx System Usage Protocol]]'
session: null
source: Rami Khouri
source_date: '2025-11-10'
status: final
supports: []
tags: []
type: decision
---

# Clickx Retained for Diagnoses Medications and Referrals

## Context

The clinic has been migrating clinical documentation to its internal platform. The question arose about what role the Clickx EHR system should continue to play.

## Options Considered

1. **Full migration away from Clickx** — move all functions to the internal platform. Not feasible at this time because the internal platform does not yet support diagnosis coding, medication management, or referral generation.
2. **Retain Clickx for specific functions** — keep Clickx for functions the internal platform cannot handle. Selected as the pragmatic approach.
3. **Run both systems in parallel** — maintain full Clickx usage alongside the platform. Rejected due to duplicate data entry burden.

## Decision

Clickx is **retained specifically** for three clinical functions:
- **Diagnoses** — ICD-coded diagnosis recording
- **Medications** — prescription management
- **Referrals** — referral letter generation

All other clinical documentation is handled by the internal platform.

## Rationale

These three functions require regulatory-grade documentation that the internal platform does not yet provide. Retaining Clickx for only these functions minimizes the dual-system burden while maintaining compliance.

## Consequences

- Clinicians must use Clickx for diagnoses, medications, and referrals only
- All staff need functional Clickx access (5 currently blocked)
- Individual accounts needed for audit compliance
- ICD version compatibility must be confirmed

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
