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
janitor_note: 'LINK001 — all Telia''z, conversation, and note wikilinks are valid
  (YAML escaping false positive, targets verified). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist — systemic
  issue, embeds preserved. BODY — duplicate base view embeds after --- separator need
  manual removal.'
name: Adopt Structured Patient Discharge Targets for Capacity Management
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch Operations and Recruitment 2026-02-15]]'
- '[[task/Develop Patient Discharge Strategy and Criteria]]'
relationships:
- confidence: 0.85
  context: Targets become core dashboard KPIs
  source: decision/Adopt Structured Patient Discharge Targets for Capacity Management.md
  target: decision/Four Core KPI Targets for Clinic Operations Dashboard.md
  type: supports
- confidence: 0.7
  context: Targets aid active discharge impl
  source: decision/Adopt Structured Patient Discharge Targets for Capacity Management.md
  target: decision/Implement Active Patient Discharge Protocol.md
  type: related-to
- confidence: 0.95
  context: Structured adopts specific targets
  source: decision/Adopt Structured Patient Discharge Targets for Capacity Management.md
  target: decision/Patient Discharge Targets 10-30-30-30 Percent.md
  type: supports
- confidence: 0.95
  context: Adopts specific targets
  source: decision/Adopt Structured Patient Discharge Targets for Capacity Management.md
  target: decision/Target Patient Discharge Rates of 10-30-30-30 Percent.md
  type: supports
session: null
source: Rami Khouri, team meeting 2026-02-15
source_date: '2026-02-15'
status: draft
supports: []
tags: []
type: decision
---

# Adopt Structured Patient Discharge Targets for Capacity Management

## Context
The Israel clinic is experiencing severe capacity constraints: 945 new patients monthly but only 77 (8%) receiving same-month intake appointments. The follow-up to intake ratio is below the target 4:1. The clinic needs to actively manage patient lifecycle to free capacity for new patients.

## Options Considered
1. **Passive approach** — Accept natural 15% monthly churn rate and grow capacity through hiring only
2. **Active discharge targets** — Set specific discharge percentages at each treatment stage (proposed)
3. **Restrict new patient intake** — Close intake temporarily to catch up (rejected — contradicts growth goals)

## Decision
Adopt structured discharge targets: 10% after intake, 30% after first follow-up, 30% after second follow-up, 30% after third follow-up. Target overall treatment duration of 4-6 months.

## Rationale
Current passive churn is ~15%. With 945 new patients/month and limited capacity, the clinic cannot grow without actively managing outflow. The proposed targets are based on clinical appropriateness (patients who don't need ongoing pharmacological treatment, mis-referrals, personality disorder patients better suited to other settings). The plan requires literature review and data validation before implementation.

## Consequences
- Need literature review on psychiatric treatment duration benchmarks
- Need data analysis of existing patient churn patterns
- Questionnaire modifications to identify early-discharge candidates
- New psychiatrist-facing feature for discharge recommendations
- Must validate against financial model (Dekkel's requirement)

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]