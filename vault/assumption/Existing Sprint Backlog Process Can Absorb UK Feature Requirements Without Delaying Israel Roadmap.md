---
based_on:
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[decision/Route UK Product Features Through Existing Sprint Backlog Process]]'
challenged_by:
- '[[constraint/UK Product Features Compete for Shared Engineering Backlog With Israel]]'
confidence: low
created: '2026-03-31'
name: Existing Sprint Backlog Process Can Absorb UK Feature Requirements Without Delaying
  Israel Roadmap
project:
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Scope UK Scheduling and Prescription Features for Product Backlog]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
source: Implied by Feb 15 team meeting backlog discussion
source_date: '2026-02-15'
status: active
tags:
- uk-launch
- product-development
- capacity
type: assumption
---

# Existing Sprint Backlog Process Can Absorb UK Feature Requirements Without Delaying Israel Roadmap

## Claim

The team's existing engineering sprint process can accommodate UK-specific product features (prescription module, scheduling system, report format adaptation, questionnaire localization) alongside ongoing Israel feature development, without significant delays to either roadmap.

## Basis

During the Feb 15 team meeting, Stav and Rami agreed to discuss UK features at the regular 2 PM backlog meeting. No separate development track or additional engineering resources were proposed. The implicit belief is that the current process and team can handle both markets.

## Evidence Trail

- **Challenging**: Stav explicitly noted that prescription and scheduling features are "more complex than other backlog items" — suggesting they may strain capacity
- **Challenging**: The existing constraint [[constraint/UK Product Features Compete for Shared Engineering Backlog With Israel]] acknowledges the resource contention
- **Challenging**: Shachar's March 31 target requires these features to be ready in approximately 6 weeks alongside Israel work

## Impact

If this assumption fails, either UK launch slips past March 31 or Israel feature development stalls. The prescription module is particularly critical — [[constraint/UK Clinic Launch Requires Prescription System Not Yet Built]] means patients cannot receive medication without it.
