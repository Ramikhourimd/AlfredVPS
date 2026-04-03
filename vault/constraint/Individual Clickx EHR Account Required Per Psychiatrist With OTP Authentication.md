---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Clinic data governance policy
created: '2026-03-06'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  ORPHAN001 — no inbound links; may need to be referenced from related conversation
  or project notes.
name: Individual Clickx EHR Account Required Per Psychiatrist With OTP Authentication
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Clickx Retained for Diagnoses Medications and Referrals]]'
- '[[conversation/Clinic Israel Team Meeting 2025-09-01]]'
relationships:
- confidence: 0.7
  context: Both psychiatrist workflow constraints
  source: constraint/Individual Clickx EHR Account Required Per Psychiatrist With
    OTP Authentication.md
  target: constraint/No Automated Detection of Legacy Clinical Workflow Usage.md
  type: related-to
- confidence: 0.95
  context: Shared auth constraints and issues
  source: constraint/Individual Clickx EHR Account Required Per Psychiatrist With
    OTP Authentication.md
  target: constraint/Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions.md
  type: related-to
source: Clinic Israel Team Meeting 2025-09-01
source_date: '2025-09-01'
status: active
type: constraint
---

# Individual Clickx EHR Account Required Per Psychiatrist With OTP Authentication

## Constraint

Each psychiatrist must have their own individual Clickx EHR account with proper OTP authentication. Shared account usage is prohibited — Manal was found entering summaries using Elias's user account, which was flagged as incorrect practice during the 2025-09-01 team meeting.

## Source

Identified during the Clinic Israel Team Meeting 2025-09-01 when Elinor took over as Clickx point of contact. The practice of shared accounts was discovered and immediately corrected. A cloud-based remote desktop solution exists for overseas psychiatrists (Elinor, Noa) to access Clickx without VPN.

## Implications

Every new psychiatrist onboarding must include Clickx account provisioning as a prerequisite. Overseas psychiatrists require the remote desktop solution to be configured. The constraint compounds the onboarding timeline — a psychiatrist without Clickx access cannot enter diagnoses, medications, or referrals, which are the functions Clickx is retained for. New staff member Oriel/Uriel was specifically noted as still lacking access, demonstrating this is an active operational gap.

## Expiry / Review

Active as long as Clickx is retained for diagnoses, medications, and referrals. Review if the clinic fully migrates clinical documentation to the internal platform.