---
alfred_tags:
- clinic/capacity-management
- patient/discharge
- case-management/staffing
approved_by: []
based_on:
- '[[assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio]]'
- '[[assumption/Monthly Patient Churn Rate Is Approximately 15 Percent]]'
challenged_by: []
confidence: medium
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base) reference missing _bases/ files — vault-wide
  infrastructure gap. Body contains duplicate base embed block (second set of Based
  On / Related after --- separator) — needs manual removal; vault CLI cannot replace
  body content.
name: Implement Active Patient Discharge Protocol
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[assumption/Clinic Israel Serving Only 8 Percent of Monthly Patient Demand]]'
- '[[constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026]]'
session: null
source: Rami Khouri, team meeting 2026-02-15
source_date: '2026-02-15'
status: draft
supports: []
tags: []
type: decision
---

# Implement Active Patient Discharge Protocol

## Context

Clinic Israel is experiencing a severe capacity crisis: 945 new patients registered in February 2026 but only 77 (8%) received intake appointments. The clinic opened the month near full capacity, leaving no room for new intakes. The natural churn rate (~15%) is insufficient to create enough capacity for the incoming volume.

## Options Considered

1. **Option A: Aggressive hiring** — Add 30-40 psychiatrists by year-end. Addresses volume but slow to implement and risks quality dilution.
2. **Option B: Active discharge protocol** — Systematically manage patient lifecycle to free capacity faster. Requires clinical framework but can be implemented with existing staff.
3. **Option C: Limit new patient intake** — Cap new registrations. Protects current patients but contradicts growth objectives.

## Decision

Pursue Option B — design and implement an active patient discharge protocol with the following targets:
- 10% discharged after intake (patients who don't need psychiatric medication)
- 30% discharged after first follow-up
- 30% discharged after second follow-up
- 30% discharged after third follow-up

This targets a 4-6 month average treatment duration.

## Rationale

The clinic must shift from a retention-heavy to an intake-heavy operation. Without active discharge management, the growing waitlist will cause wait times to extend to months, damaging patient outcomes and HMO relationships.

## Consequences

- Requires literature review on psychiatric patient treatment patterns
- Must cross-reference with actual Telia'z patient data to identify discharge signals
- Questionnaire modifications needed for better patient profiling at intake
- Psychiatrist-facing recommendation features need to be built
- Must validate against financial model (Dekkel/Oren requirement)
- Patient selection criteria at intake also need improvement (currently no screening for severity, suicidality, or treatment-medication appropriateness)

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]