---
alfred_tags:
- uk/clinical-launch
- timeline-assumptions
- prescription-pathway
based_on:
- '[[constraint/Clalit Pharmacies Do Not Accept External Prescriptions]]'
confidence: medium
created: '2025-11-09'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, learn-assumption.base#Related)
  reference _bases/ files that do not exist — vault-wide infrastructure gap, not per-file
  fix. Embeds preserved.
name: Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Clalit Health Services]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
relationships:
- confidence: 0.75
  context: Rx pathway supports launch timeline
  source: assumption/Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue.md
  target: assumption/March 2026 UK System Launch Timeline Is Achievable.md
  type: supports
- confidence: 0.6
  context: Pre-launch patient acquisition assumptions
  source: assumption/Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue.md
  target: assumption/Two-Week Marketing Lead Before System Launch Sufficient for UK
    Patient Acquisition.md
  type: related-to
- confidence: 0.7
  context: Rx enables full service post soft-launch
  source: assumption/Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue.md
  target: assumption/UK Clinic Can Soft-Launch With Assessment-Only Service Before
    Prescription Module.md
  type: supports
- confidence: 0.75
  context: Rx pathway supports platform launch target
  source: assumption/Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue.md
  target: assumption/UK Clinical Platform Launch Targets End of March 2026.md
  type: supports
- confidence: 0.75
  context: Rx supports March 31 launch achievability
  source: assumption/Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue.md
  target: assumption/UK March 31 System Launch Date Is Achievable.md
  type: supports
source: Telia'z team preparation meeting 2025-11-09
source_date: '2025-11-09'
status: active
type: assumption
---

# Clalit GP Prescription Pathway Will Resolve Pharmacy Access Issue

## Claim

Since Clalit pharmacies do not accept external prescriptions, Telia'z can route psychiatric medication recommendations through the patient's Clalit family doctor (GP), who will then issue the prescription within the Clalit system. This assumes GPs will cooperate with this workflow and that it does not create excessive friction or delays for patients.

## Basis

The team identified this as the most viable workaround during the 2025-11-09 preparation meeting. The alternative (requesting Clicks EHR access for prescription entry) was deemed risky due to scope creep concerns. The GP pathway is standard practice in the Israeli healthcare system for specialist recommendations.

## Evidence Trail

- 2025-11-09: Team identified the constraint and proposed GP pathway as primary solution
- Pending: Confirmation from Clalit contact on whether this pathway is acceptable and operationally feasible

## Impact

If this assumption holds, the prescription workflow is solvable without Clicks access. If GPs refuse or Clalit contact objects to the additional GP visit volume, the team may need to negotiate Clicks access for prescription-only use, which introduces operational complexity.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]