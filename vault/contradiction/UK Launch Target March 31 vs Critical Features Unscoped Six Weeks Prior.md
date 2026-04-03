---
alfred_tags:
- project/risks
- healthtech/uk-launch
claim_a: Shachar targets March 31, 2026 as the UK clinical platform system launch
  date
claim_b: UK scheduling visibility and prescription issuance features were not yet
  scoped as of February 15, 2026 — six weeks before launch
created: '2026-03-31'
name: UK Launch Target March 31 vs Critical Features Unscoped Six Weeks Prior
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z UK Expansion]]'
related:
- '[[task/Build UK Scheduling and Prescription System]]'
- '[[assumption/UK Clinical Platform Launch Targets End of March 2026]]'
- '[[constraint/UK Clinic Requires Patient-Facing Scheduling Visibility]]'
- '[[constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel]]'
- '[[constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
  Compliance]]'
source_a: Stav Zamir relaying Shachar timeline in team meeting 2026-02-15
source_b: Same team meeting 2026-02-15 — features flagged as unscoped and recommended
  for backlog sprint
status: unresolved
type: contradiction
---

# UK Launch Target March 31 vs Critical Features Unscoped Six Weeks Prior

## Claim A

Shachar is targeting March 31, 2026 as the system launch date for the UK clinical platform. This date was communicated during the team meeting on 2026-02-15 and implies all critical features must be production-ready by that date.

## Claim B

During the same February 15, 2026 meeting, Stav flagged two critical features — patient-facing scheduling visibility and prescription issuance — as "not yet scoped." She recommended adding them to the backlog sprint. The prescription system also requires UK-specific controlled substance regulatory compliance (ADHD medications) and external system integration, adding significant implementation complexity.

## Analysis

The contradiction arises from the same meeting producing both a firm launch date and an acknowledgment that critical features haven't been scoped. Six weeks is insufficient to scope, design, implement, test, and deploy two complex features — especially prescription issuance, which involves regulatory compliance and external system integration. This suggests either: (a) the March 31 date was aspirational rather than committed, (b) the features will be deferred to a post-launch release, or (c) the timeline has since been revised.

## Resolution

Unresolved as of extraction date. The March 31, 2026 target date is today — resolution should be verified against actual launch status.