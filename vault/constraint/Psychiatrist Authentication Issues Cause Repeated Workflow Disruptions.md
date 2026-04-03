---
alfred_tags:
- psychiatry/constraints
- on-call/workflows
- patient-safety/protocols
authority: Retool platform authentication system
created: '2026-02-27'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embeds (learn-constraint.base) reference missing _bases/
  files — vault-wide infrastructure gap. ORPHAN001 — no inbound wikilinks found.
name: Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[task/Gather Secretary and Clinic Staff System Requirements]]'
source: WhatsApp feedback from psychiatrists, Retool system behavior
source_date: '2025-12-05'
status: active
type: constraint
---

# Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions

## Constraint

Psychiatrists using the Retool-based clinical platform experience repeated authentication lockouts that disrupt their clinical workflow. The login issues cause therapists and psychiatrists to get stuck, requiring intervention and wasting session time.

## Source

Reported via WhatsApp feedback from psychiatrists. Raised by Shachar during the 2025-12-05 prioritization meeting as a known issue from the existing Retool system. Classified as a Track 1 (critical fix) item.

## Implications

- Psychiatrists lose productive session time dealing with login failures
- Staff frustration reduces system adoption and trust
- Workarounds (staying logged in, sharing sessions) may introduce security risks
- This is classified as fixable but "not trivial" per Shachar
- Being addressed as part of the platform rebuild rather than patching the current system

## Expiry / Review

Expected to be resolved when Shachar's rebuilt platform replaces the current Retool system. Should be reviewed if the rebuild timeline extends beyond H1 2026.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]