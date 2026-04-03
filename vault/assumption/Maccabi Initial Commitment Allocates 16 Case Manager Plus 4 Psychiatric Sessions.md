---
alfred_tags:
- maccabi/hmo-commitments
- clinic/uncompensated-sessions
based_on:
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
confidence: high
confirmed_by:
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, learn-assumption.base#Related)
  reference non-existent _bases/learn-assumption.base — vault-wide infrastructure
  gap, embeds preserved. ORPHAN001 — no inbound wikilinks from other records. Swept
  2026-02-27.
name: Maccabi Initial Commitment Allocates 16 Case Manager Plus 4 Psychiatric Sessions
project:
- '[[project/Telia''z Clinic Israel]]'
relationships:
- confidence: 0.75
  context: Initial allocation amid HMO gaps
  source: assumption/Maccabi Initial Commitment Allocates 16 Case Manager Plus 4 Psychiatric
    Sessions.md
  target: assumption/Unresolved HMO Commitment Gaps Represent Uncompensated Clinical
    Sessions.md
  type: related-to
source: Maccabi HMO commitment terms as understood by clinic operations
source_date: '2025-01-12'
status: active
type: assumption
---

# Maccabi Initial Commitment Allocates 16 Case Manager Plus 4 Psychiatric Sessions

## Claim

The Maccabi HMO initial patient commitment for Telia'z Clinic Israel provides a fixed allocation of 20 sessions: 16 case manager follow-up sessions and 4 psychiatric follow-up sessions, issued separately from the intake commitment. This allocation structure determines commitment renewal timing and drives the requirement for expiry alerts, renewal workflows, and secretary task automation.

## Basis

Consistently referenced across multiple operational meetings between Rami Khouri and Shira Lachman as the established commitment structure:
- [[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]: "one for intake and one for follow-up sessions (16 case manager follow-ups + 4 psychiatric follow-ups)"
- [[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]: "follow-up commitment (limited to 16 case manager sessions + 4 psychiatric sessions)"
- [[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]: Same 16+4 allocation cited as baseline

The structure appears to be a standard Maccabi allocation term, not a clinic-negotiated arrangement.

## Evidence Trail

- 2025-01-12: First documented reference to 16+4 structure in commitment renewal discussion
- 2025-08-01: Same structure confirmed in separate meeting seven months later without dispute
- Structure referenced in system requirements for Retool renewal fields and expiry alert timing

## Impact

This allocation is the quantitative foundation for:
- Commitment expiry alert timing (proposed: 2 sessions before exhaustion)
- Secretary pre-session call workflows for renewal reminders
- Retool renewal field and session balance counter requirements
- Patient lifecycle capacity planning and discharge protocol design
- The unresolved question of what the RENEWAL commitment allocates (distinct from initial)

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]