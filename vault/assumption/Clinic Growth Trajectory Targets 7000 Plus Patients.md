---
alfred_tags:
- clinic/growth
- operations/stabilization
- organizational-health
based_on:
- '[[project/Telia''z Clinic Israel]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist. Create base file to enable dynamic views.'
name: Clinic Growth Trajectory Targets 7000 Plus Patients
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Secretarial Team Will Grow to Five Full Time by Year End]]'
- '[[assumption/Pod Structure of 10 Psychiatrists is Optimal Management Span]]'
- '[[constraint/Financial Viability of New Structure Must Be Validated Before Implementation]]'
relationships:
- confidence: 0.8
  context: Growth increases complexity
  source: assumption/Clinic Growth Trajectory Targets 7000 Plus Patients.md
  target: assumption/Clinic Operational Complexity Has Reached Hospital-Level Scale.md
  type: supports
- confidence: 0.9
  context: Requires stabilization first
  source: assumption/Clinic Growth Trajectory Targets 7000 Plus Patients.md
  target: assumption/Clinic Stabilization Must Precede Growth Expansion.md
  type: depends-on
- confidence: 0.85
  context: Readiness for growth target
  source: assumption/Clinic Growth Trajectory Targets 7000 Plus Patients.md
  target: assumption/Organizational Health Score Can Quantify Growth Readiness.md
  type: related-to
source: Telia'z Clinic Israel project description
status: active
type: assumption
---

# Clinic Growth Trajectory Targets 7000 Plus Patients

## Claim

The Telia'z Clinic Israel is scaling toward a target of 7,000+ patients. This growth target implicitly drives the urgency of the organizational restructuring — management layers, pod sizing, secretary staffing, and shared services design are all calibrated to support this scale.

## Basis

The Telia'z Clinic Israel project description states the clinic is "Currently scaling up with plans to reach 7,000+ patients." This figure is referenced as a forward target, not current state.

## Evidence Trail

- Clinic Israel project record explicitly states 7,000+ patient target
- Secretary hiring urgency (5 FTE by year end) aligns with this scale
- Pod structure (groups of ~10 psychiatrists) sized to handle increased patient load
- AI diagnostic research covers ~6,000 patients, suggesting current scale approaching target

## Impact

- Restructuring urgency: management structure must support 7,000+ patients, not just current load
- Secretary team sizing (5 FTE target) calibrated to this volume
- Pod leader span of control assumptions depend on patient-to-psychiatrist ratios at this scale
- Financial viability assessment must validate revenue at 7,000+ patients against new management costs

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]