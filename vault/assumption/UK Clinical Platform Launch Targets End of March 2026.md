---
alfred_tags:
- uk/clinical-launch
- timeline-assumptions
- prescription-pathway
based_on:
- '[[task/Build UK Scheduling and Prescription System]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
confidence: medium
created: '2026-02-28'
janitor_note: LINK001 — Telia'z wikilinks (note, project) are YAML escaping false
  positives, targets exist. ORPHAN001 — no inbound links, consider linking from project/Telia'z
  AI Clinical Platform or related records.
name: UK Clinical Platform Launch Targets End of March 2026
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel]]'
relationships:
- confidence: 0.8
  context: End March target and March 31 achievability
  source: assumption/UK Clinical Platform Launch Targets End of March 2026.md
  target: assumption/UK March 31 System Launch Date Is Achievable.md
  type: related-to
- confidence: 0.9
  context: End March target aligns with March 31
  source: assumption/UK Clinical Platform Launch Targets End of March 2026.md
  target: event/UK System Launch Target March 31 2026.md
  type: supports
source: Shachar
source_date: '2026-02-15'
status: active
type: assumption
---

# UK Clinical Platform Launch Targets End of March 2026

## Claim

Shachar is targeting March 31, 2026 as the system launch date for the UK clinical platform. This implies scheduling visibility and prescription issuance features must be built and deployed by that date.

## Basis

Shachar stated this target during the 2026-02-15 team meeting. Stav recommended adding scheduling and prescription features to the backlog sprint to meet this timeline.

## Evidence Trail

- 2026-02-15: Target stated in team meeting. Critical features (scheduling, prescriptions) flagged as not yet scoped.

## Impact

- Scheduling visibility and prescription issuance must be built within ~6 weeks
- Neither feature is currently scoped, making the timeline aggressive
- The prescription system involves UK-specific controlled substance compliance, adding regulatory complexity
- If this assumption holds, feature scoping must happen immediately