---
alfred_tags:
- clinic/capacity-management
- patient/discharge
- case-management/staffing
approved_by: []
based_on: []
challenged_by: []
confidence: medium
created: '2026-02-15'
decided_by:
- '[[person/Rami Khouri]]'
description: Implement structured patient discharge protocol instead of waiting for
  natural churn, targeting 10% initial discharge to create capacity for new intake
  appointments.
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist — vault-wide infrastructure gap. Embeds preserved. NOTE: duplicate
  base embeds at end of file — consider removing duplicates.'
name: Active Patient Discharge Protocol Over Passive Churn
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[assumption/Monthly Patient Churn Rate Is Approximately 15 Percent]]'
- '[[task/Design Patient Discharge Protocol for Clinic Israel]]'
relationships:
- confidence: 0.75
  context: Active protocol supports capacity targets
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Adopt Structured Patient Discharge Targets for Capacity Management.md
  type: supports
- confidence: 0.65
  context: Discharge protocol impacts KPIs
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Four Core KPI Targets for Clinic Operations Dashboard.md
  type: related-to
- confidence: 0.95
  context: Decision favors active implementation
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Implement Active Patient Discharge Protocol.md
  type: supports
- confidence: 0.8
  context: Protocol requires discharge targets
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Patient Discharge Targets 10-30-30-30 Percent.md
  type: supports
- confidence: 0.8
  context: Active protocol sets discharge rates
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Target Patient Discharge Rates of 10-30-30-30 Percent.md
  type: supports
- confidence: 0.6
  context: Discharge in retool improvements
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Three-Track Approach to Retool System Improvements.md
  type: part-of
- confidence: 0.7
  context: Discharge part of scaling framework
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Two-Domain Protocol Framework for Clinic Scaling.md
  type: part-of
- confidence: 0.6
  context: Discharge affects patient volume
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Delay UK Case Manager Hiring Until Patient Volume Confirmed.md
  type: related-to
- confidence: 0.75
  context: Needs case mgmt staffing support
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/External Vendor or Call Center Proposed as Case Management Stopgap.md
  type: depends-on
- confidence: 0.65
  context: Staffing enables discharge
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Recruit UK Case Managers Locally Not From Israel.md
  type: related-to
- confidence: 0.65
  context: Staffing enables discharge
  source: decision/Active Patient Discharge Protocol Over Passive Churn.md
  target: decision/Start UK Case Management With Israeli Staff.md
  type: related-to
session: null
source: Rami Khouri proposal at team meeting 2026-02-15
source_date: '2026-02-15'
status: draft
supports: []
tags: []
type: decision
---

# Active Patient Discharge Protocol Over Passive Churn

## Context
Clinic Israel faces severe capacity constraint: 945 new patients/month but only 77 (8%) get intake appointments. The follow-up-to-intake ratio is imbalanced — too many long-term patients consume capacity that should serve new intakes.

## Options Considered
1. **Option A** — Continue passive churn (~15% natural attrition) and only scale by adding staff
2. **Option B** — Implement active patient lifecycle management with discharge targets at each treatment milestone

## Decision
Pursue Option B: implement structured discharge protocol with targets (10% after intake, 30% after each of first three follow-ups). Still needs financial validation and literature review before implementation.

## Rationale
At current intake conversion of 8%, passive churn alone cannot address capacity. Shifting clinic character to more intake-heavy, shorter treatment cycles would serve more patients. Includes better patient screening at intake to filter inappropriate referrals.

## Consequences
- Requires literature review, data analysis, questionnaire modification
- Must validate against financial model (Dekkel requirement)
- Changes clinic character fundamentally
- Improves capacity utilization for new patients
- May face clinician pushback on shorter treatment relationships

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]