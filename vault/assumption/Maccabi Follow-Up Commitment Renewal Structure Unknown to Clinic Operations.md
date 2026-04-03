---
alfred_tags:
- maccabi/hmo-commitments
- clinic/uncompensated-sessions
based_on:
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z Clinic Israel wikilink is valid (YAML escaping false
  positive). Base view embeds (learn-assumption.base#Depends On This, #Related) reference
  _bases/learn-assumption.base which does not exist — vault-wide issue, embeds preserved.'
name: Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic Operations
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
relationships:
- confidence: 0.9
  context: Initial vs follow-up Maccabi commitments
  source: assumption/Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic
    Operations.md
  target: assumption/Maccabi Initial Commitment Allocates 16 Case Manager Plus 4 Psychiatric
    Sessions.md
  type: related-to
- confidence: 0.8
  context: Unknown renewal causes commitment gaps
  source: assumption/Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic
    Operations.md
  target: assumption/Unresolved HMO Commitment Gaps Represent Uncompensated Clinical
    Sessions.md
  type: supports
source: Rami Khouri and Shira Lachman during operational meetings
source_date: '2025-08-01'
status: active
type: assumption
---

# Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic Operations

## Claim

Neither Rami Khouri nor Shira Lachman fully understand the exact structure of Maccabi follow-up commitment renewals — specifically how many sessions are included, what session types are covered, and what the renewal authorization process requires. Alice (Elis) was tasked with investigating the details with Maccabi, but confirmed clarity was not documented in either meeting.

## Basis

In the 2025-08-01 meeting, it was explicitly noted: "Neither Rami nor Shira fully understand the structure of the follow-up commitment (how many sessions, what types). Alice is investigating the details with Maccabi." The same gap was present in the earlier 2025-01-12 meeting, where "the exact terms of renewal commitments (session count, structure) are unclear and need clarification with Maccabi."

## Evidence Trail

- 2025-01-12: Gap first identified. Alice tasked with investigating.
- 2025-08-01: Gap still present 7 months later. Alice still investigating.

## Impact

Without understanding renewal terms, the clinic cannot:
- Build accurate session counters for renewal commitments
- Train secretaries on the renewal validation process
- Set correct expiry thresholds for proactive alerts
- Ensure billing compliance for renewed commitments

This knowledge gap blocks the entire commitment renewal system design.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]