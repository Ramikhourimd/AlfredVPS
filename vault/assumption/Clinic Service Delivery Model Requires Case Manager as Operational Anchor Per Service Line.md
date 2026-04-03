---
based_on:
- '[[note/On-Call Project Accountability and Role Ownership 2025-09-22]]'
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
confidence: medium
created: '2026-03-03'
janitor_note: 'LINK001 — broken wikilinks: note/On-Call Case Review Ra''ut (possible
  apostrophe in filename), project/Telia''z Clinic Israel (YAML escaping false positive
  — verify target exists), assumption/Project Ownership Requires End-to-End Verification
  (verify target exists), synthesis/Manual Single-Person Dependencies (verify target
  exists). ORPHAN001 — no inbound links; consider linking from project/Telia''z Clinic
  Israel or process records.'
name: Clinic Service Delivery Model Requires Case Manager as Operational Anchor Per
  Service Line
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Project Ownership Requires End-to-End Verification Including Delegated
  Tasks]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
- '[[synthesis/Manual Single-Person Dependencies Create Cascading Failure Points Across
  Clinic Operations]]'
source: On-call incident review 2025-09-22 revealed structural gap when on-call service
  had no case manager
source_date: '2025-09-22'
status: active
type: assumption
---

# Clinic Service Delivery Model Requires Case Manager as Operational Anchor Per Service Line

## Claim

The Telia'z Clinic Israel operational management framework implicitly depends on each patient-facing service line having a dedicated case manager who serves as the operational anchor. When a service line (such as the on-call psychiatrist service) launches without a case manager, the operational ownership chain — onboarding, training, day-to-day management, and escalation — has no natural owner.

## Basis

During the September 2025 on-call incident review, leadership discussion revealed that existing onboarding processes split between Shira (clinical training) and Roy Shur (system access/accounts), but the on-call service had neither a case manager nor a clear operational lead. The on-call psychiatrists (Atef, Ahmad) were added to the system but never formally trained because no one owned the training step for a service without a case manager.

The standard operational model routes: (1) clinical training through the clinic manager, (2) system access through the tech admin, and (3) day-to-day operations through the service's case manager. When the on-call service violated this assumption by having no case manager, both training and operational management fell through the cracks.

## Evidence Trail

- 2025-09-21: First real on-call alert activation exposed multiple training and communication gaps
- 2025-09-22: Leadership debrief attributed failures to unclear operational ownership, not clinical incompetence
- Resolution: Rami was assigned full end-to-end ownership as a workaround, but the structural dependency on the case-manager-per-service model was not formally addressed

## Impact

As the clinic scales and potentially launches additional service lines (group therapy, crisis intervention, expanded children's services, new HMO partnerships), any service that doesn't fit the case-manager-per-service model will face the same operational ownership vacuum. Future service launches should explicitly assign an operational anchor when no case manager role exists.
