---
alfred_tags:
- ui-design/constraints
- clinical-roles
authority: Clinical workflow design dependency
created: '2026-02-27'
janitor_note: 'LINK001: Telia''z wikilinks are YAML escaping false positives — links
  resolve correctly. ORPHAN001: No inbound wikilinks — consider linking from project/Telia''z
  AI Clinical Platform or project/Telia''z Clinic Israel.'
name: Case Manager Psychiatrist Role Overlap Blocks Platform Screen Redesign
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Finalize Case Manager vs Psychiatrist Clinical Role Division]]'
- '[[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]'
relationships:
- confidence: 0.95
  context: Role overlap ties to responsibility split
  source: constraint/Case Manager Psychiatrist Role Overlap Blocks Platform Screen
    Redesign.md
  target: constraint/Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility
    Split.md
  type: related-to
- confidence: 0.7
  context: Both constrain platform screen redesign
  source: constraint/Case Manager Psychiatrist Role Overlap Blocks Platform Screen
    Redesign.md
  target: constraint/DSM Criteria Require Criterion-Level Granularity in Screen Design.md
  type: related-to
source: Platform development blocker identified in commitment process meeting
source_date: '2025-01-12'
status: active
type: constraint
---

# Case Manager Psychiatrist Role Overlap Blocks Platform Screen Redesign

## Constraint

The clinical assessment sections (patient background, symptoms, DSM criteria review) are currently performed by both case managers and psychiatrists with undefined overlap. Until the role division is formally decided and documented, the Telia'z AI Clinical Platform cannot redesign meeting screens — because the case manager screen agenda (titles/subtitles) cannot be defined without knowing which assessment sections belong to which role.

## Source

Raised by Shira and her team during the 2025-01-12 commitment process and feature updates meeting. They explicitly flagged this as a blocker for the meeting screen redesign. The decision requires input from Rami (clinical authority), Ori Shukron, and Alice (platform development).

## Implications

- Platform UI development for meeting screens is blocked until role division is finalized
- Both professionals currently duplicate clinical assessment work, wasting clinical time
- Any platform feature that depends on knowing "who assesses what" is similarly blocked
- The longer this remains unresolved, the more technical debt accumulates in the platform as workarounds are built

## Expiry / Review

This constraint resolves when the case manager vs psychiatrist clinical role division is formally documented and approved. No expiry date has been set — the task remains in todo status as of the source date.