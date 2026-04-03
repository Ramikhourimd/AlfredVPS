---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Maccabi Healthcare Services
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  VERIFIED: [[constraint/Maccabi Commitment Validation Requires Manual Portal Check
  Against MADAC]] confirmed existing. Base view embeds (learn-constraint.base) reference
  missing _bases/ files — vault-wide infrastructure gap. ORPHAN001 — no inbound wikilinks
  found.'
location: []
name: Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
  MADAC]]'
- '[[assumption/Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic Operations]]'
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
relationships:
- confidence: 0.75
  context: Both limit Maccabi commitment handling
  source: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  target: constraint/No System Support for Maccabi Commitment Renewals in Retool.md
  type: related-to
- confidence: 0.7
  context: Cap needs renewal workflow support
  source: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  target: constraint/No Commitment Renewal Workflow Exists in Retool.md
  type: related-to
- confidence: 0.7
  context: Cap enforcement requires entry mech
  source: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  target: constraint/No Renewal Commitment Entry Mechanism Exists in Retool.md
  type: related-to
- confidence: 0.7
  context: Renewal numbers for capped sessions
  source: constraint/Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle.md
  target: constraint/No System Entry Point for Commitment Renewal Numbers.md
  type: related-to
source: Maccabi HMO contract terms
source_date: '2025-01-12'
status: active
tags: []
type: constraint
---

# Maccabi Follow-Up Commitment Capped at 20 Sessions Per Cycle

## Constraint

Each Maccabi patient's initial follow-up commitment (התחייבות) is limited to exactly 20 sessions: 16 case manager sessions and 4 psychiatric follow-up sessions. When these sessions are exhausted, a new commitment (renewal) must be obtained from Maccabi before further treatment can be billed.

## Source

Maccabi HMO contract terms, consistently referenced across multiple operational meetings (2025-01-12, 2025-08-01) by both Rami Khouri and Shira Lachman. The 16+4 structure is stated identically in all references.

## Implications

- Every patient hits a predictable "commitment wall" after 20 follow-up sessions, requiring renewal action
- The clinic must proactively track session counts per patient to anticipate renewals
- Without a system-level renewal workflow (currently absent from Retool), patients risk having sessions conducted against expired commitments — which cannot be billed
- The renewal commitment terms (session count, structure) remain unclear, creating operational uncertainty after the first cycle expires
- Secretary workload includes manual tracking and patient outreach for renewals

## Expiry / Review

This constraint is structural to the Maccabi HMO contract and persists as long as the clinic operates under Maccabi. Review if contract terms are renegotiated or if Maccabi changes their commitment structure.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]