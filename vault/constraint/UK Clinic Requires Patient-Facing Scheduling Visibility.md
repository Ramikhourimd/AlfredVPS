---
alfred_tags:
- uk/scheduling
- uk/prescriptions
authority: UK clinic operations
created: '2026-03-08'
janitor_note: LINK001 — [[location/UK]] does not exist; consider creating location
  record or linking to existing UK-related location. [[project/Telia'z AI Clinical
  Platform]] is valid (YAML escaping false positive). ORPHAN001 — no inbound wikilinks;
  consider linking from project/Telia'z AI Clinical Platform or project/Telia'z UK
  Expansion.
location:
- '[[location/UK]]'
name: UK Clinic Requires Patient-Facing Scheduling Visibility
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel]]'
- '[[assumption/UK Clinical Platform Launch Targets End of March 2026]]'
- '[[task/Build UK Scheduling and Prescription System]]'
relationships:
- confidence: 0.85
  context: Shared UK scheduling scoping needs
  source: constraint/UK Clinic Requires Patient-Facing Scheduling Visibility.md
  target: constraint/UK Prescription Format and Scheduling Requirements Not Scoped.md
  type: related-to
- confidence: 0.8
  context: UK scheduling competes for shared backlog
  source: constraint/UK Clinic Requires Patient-Facing Scheduling Visibility.md
  target: constraint/UK Product Features Compete for Shared Engineering Backlog With
    Israel.md
  type: related-to
- confidence: 0.85
  context: UK scheduling visibility scoping gap
  source: constraint/UK Clinic Requires Patient-Facing Scheduling Visibility.md
  target: constraint/UK Scheduling and Prescription Features Not Yet Scoped.md
  type: related-to
source: task/Build UK Scheduling and Prescription System
status: active
type: constraint
---

# UK Clinic Requires Patient-Facing Scheduling Visibility

## Constraint

The UK clinic must provide patients with the ability to see available appointment slots before booking. This is a separate requirement from the prescription issuance constraint and represents a patient-facing scheduling interface that does not exist in the current platform.

## Source

Flagged by Stav during the team meeting on UK launch operations (2026-02-15). Not yet scoped or designed. Recommended for backlog sprint alongside the prescription system.

## Implications

- A patient-facing scheduling UI must be built before UK launch
- This may require integration with the appointment management backend
- Scope and design are undefined — creates risk for the March 31 launch target
- Israeli clinics do not have this requirement, so no existing implementation to reuse

## Expiry / Review

Active until UK clinic launch. Review against March 31, 2026 target date.