---
alfred_tags:
- vehicles/inspections
- automotive/certifications
approved_by: []
based_on:
- '[[note/Vehicle Pre-Purchase Inspection Report 2025-11-03]]'
- '[[note/Pre-Purchase Vehicle Inspection Findings 2025-11-03]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist — vault-wide infrastructure
  gap. Body contains DUPLICATE base view embeds (same two embeds appear twice, separated
  by ---). Embeds preserved per rules; human should remove duplicates manually. ORPHAN001
  — no inbound wikilinks.'
name: Require Garage Engine Certification Before Vehicle Purchase
project: []
related:
- '[[task/Get Vehicle Engine Inspected at Garage Before Purchase]]'
- '[[note/Pre-Purchase Vehicle Inspection Report 2025-11-03]]'
- '[[note/Pre-Purchase Vehicle Inspection Findings 2025-11-03]]'
- '[[note/Vehicle Pre-Purchase Inspection Report 2025-11-03]]'
relationships:
- confidence: 0.9
  context: Inspection findings relate to engine cert policy
  source: decision/Require Garage Engine Certification Before Vehicle Purchase.md
  target: note/Pre-Purchase Vehicle Inspection Findings 2025-11-03.md
  type: related-to
- confidence: 0.9
  context: Inspection report relates to engine cert policy
  source: decision/Require Garage Engine Certification Before Vehicle Purchase.md
  target: note/Pre-Purchase Vehicle Inspection Report 2025-11-03.md
  type: related-to
- confidence: 0.9
  context: Inspection report relates to engine cert policy
  source: decision/Require Garage Engine Certification Before Vehicle Purchase.md
  target: note/Vehicle Pre-Purchase Inspection Report 2025-11-03.md
  type: related-to
- confidence: 0.95
  context: Decision directly supports engine inspection task
  source: decision/Require Garage Engine Certification Before Vehicle Purchase.md
  target: task/Get Vehicle Engine Inspected at Garage Before Purchase.md
  type: supports
session: null
source: Pre-purchase vehicle inspector recommendation, 2025-11-03
source_date: '2025-11-03'
status: draft
supports: []
tags: []
type: decision
---

# Require Garage Engine Certification Before Vehicle Purchase

## Context

A pre-purchase inspection of a diesel 4x4 vehicle (153,000 km) on 2025-11-03 revealed multiple engine-related concerns: excessive crankcase blowby, widespread oil contamination, unreadable engine number, and signs of prior hood removal. The inspector could not determine whether the issues indicated engine failure, prior engine replacement, or a benign explanation (loose dipstick cap).

## Options Considered

1. **Proceed with purchase based on seller's explanation** — Accept the handler's claim that oil contamination is from a loose dipstick cap and buy the vehicle.
2. **Require independent garage verification** — Take the vehicle to a professional garage for engine diagnosis before committing to purchase.
3. **Walk away from the deal** — Decline the purchase based on the inspection red flags.

## Decision

Require professional garage engine certification before proceeding with the vehicle purchase. The inspector explicitly stated that if the garage certifies the engine as sound, the garage assumes responsibility — not the inspector.

## Rationale

The inspection revealed too many unresolved concerns to proceed on faith. The competing explanations (engine blowby vs. dipstick cap) cannot be resolved without professional teardown. The responsibility transfer framework (inspector → garage) provides clear accountability.

## Consequences

- Purchase delayed until garage inspection completed
- Additional cost for garage diagnosis
- Clear accountability chain established: garage certifies → garage bears responsibility

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]