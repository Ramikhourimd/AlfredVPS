---
alfred_tags:
- project/risks
- healthtech/uk-launch
claim_a: Scheduling does not need to be controlled by Telia'z — partners can handle
  their own scheduling
claim_b: Telia'z product team is building UK scheduling modules as a critical launch
  requirement
created: '2026-02-27'
janitor_note: LINK001 — Fixed [[task/Build UK Scheduling and Prescription Features]]
  → [[task/Build UK Prescription and Scheduling Features]]. Telia'z wikilinks (project,
  note) are valid (YAML escaping false positive). Base view embed (learn-contradiction.base#Related)
  references missing _bases/learn-contradiction.base — vault-wide issue, embed preserved.
  ORPHAN001 — no inbound links, consider linking from project/Telia'z UK Expansion.
name: Scheduling Ownership Undefined Between Telia'z Platform and UK Partners
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[note/UK ADHD Platform Demo Rehearsal Notes 2025-02-11]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
- '[[task/Scope UK Scheduling and Prescription Features for Product Backlog]]'
- '[[constraint/UK Scheduling and Prescription Features Not Yet Scoped]]'
relationships:
- confidence: 0.75
  context: 'UK project risks: ownership and scoping'
  source: contradiction/Scheduling Ownership Undefined Between Telia'z Platform and
    UK Partners.md
  target: contradiction/UK Launch Target March 31 vs Critical Features Unscoped Six
    Weeks Prior.md
  type: related-to
source_a: Adiel Levin, demo rehearsal (2025-02-11)
source_b: Stav Zamir, team meeting (2026-02-15)
status: unresolved
type: contradiction
---

# Scheduling Ownership Undefined Between Telia'z Platform and UK Partners

## Claim A

During the GP Confederation demo rehearsal (2025-02-11), Adiel Levin positioned the platform such that "scheduling does not need to be controlled by Telia'z." This framing suggests partners (GP Confed, OMG, Leon) can use their own scheduling systems, and Telia'z focuses on the clinical assessment platform.

## Claim B

In the team meeting (2026-02-15), Stav Zamir flagged scheduling as a critical product feature that Telia'z needs to build: "Patients need to see available appointment slots and book directly." This was added to the product backlog as a UK launch requirement alongside the prescription module.

## Analysis

These positions may not be strictly contradictory if they apply to different tracks: GP Confed/OMG may handle their own scheduling (Claim A), while the Leon private track requires Telia'z to provide scheduling (Claim B). However, this distinction has not been explicitly documented. The product team is building scheduling without clarity on which tracks require it. If scheduling is only needed for the Leon track, the scope and urgency may be different than if it's needed for all UK operations.

The 12-month gap between these statements (Feb 2025 vs Feb 2026) suggests the team's position may have evolved as they moved from sales pitch (flexibility) to implementation (ownership), but the evolution hasn't been reconciled.

## Resolution

*Unresolved.* The team should clarify: (1) which UK tracks require Telia'z-owned scheduling vs partner scheduling, and (2) whether the product team is building scheduling for all tracks or only the Leon track. This affects scope, timeline, and resource allocation.

![[learn-contradiction.base#Related]]