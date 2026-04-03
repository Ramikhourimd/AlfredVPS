---
alfred_tags:
- taliaz/leadership
- taliaz/strategy
- taliaz/operations
created: '2025-11-09'
description: Preparation meeting for next-day Clalit partnership kickoff covering
  Form 17 authorization, patient flow, prescription workflows, EHR access, and strategy
  for managing Clalit contact's desire for operational control.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide infrastructure issue. Link to note/Clalit South Psychiatric Referral
  and Subscription System Design 2025-11-10 appears in related_to field — verify target
  file exists.
name: Clalit Partnership Operational Planning 2025-11-09
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
- '[[org/Clalit Health Services]]'
- '[[org/Telia''z]]'
- '[[person/Rami Khouri]]'
- '[[decision/Clalit and Leumit Targeted as 2026 HMO Expansion Partners]]'
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[process/Clinic Patient Intake]]'
- '[[note/Cognitive Training Partnership and Clalit Growth Strategy 2025-11-09]]'
related_to: '[[note/Clalit South Psychiatric Referral and Subscription System Design
  2025-11-10]]'
relationships:
- confidence: 0.85
  context: Operational planning supports strategy
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Organizational Strategy Meeting 2026-02-22.md
  type: supports
- confidence: 0.7
  context: Planning linked to leadership frustration
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Rami Leadership Frustration Debrief 2025-12-05.md
  type: related-to
- confidence: 0.75
  context: Planning informs org structure/roles
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Leadership Meeting 2026-02-22 Organizational Structure and
    Roles.md
  type: supports
- confidence: 0.85
  context: Planning supports strategic goals
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Strategic Goals and Clinical Sustainability Meeting 2025-12-04.md
  type: supports
- confidence: 0.8
  context: Partnership supports UK launch ops
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Team Meeting UK Launch Operations and Recruitment 2026-02-15.md
  type: supports
- confidence: 0.8
  context: Partnership supports UK patient capacity
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15.md
  type: supports
- confidence: 0.8
  context: Partnership supports clinic operations
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15.md
  type: supports
- confidence: 0.8
  context: Partnership supports ops review
  source: note/Clalit Partnership Operational Planning 2025-11-09.md
  target: note/Telia'z Team Meeting UK Launch and Operations Review 2026-02-15.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Clalit Partnership Operational Planning 2025-11-09

## Context

The Telia'z team (Rami Khouri and at least one colleague) held a preparation meeting ahead of a critical next-day session with their Clalit Health Services contact (referred to as "Eli" and "Tzachi"). The Clalit partnership represents a significant expansion of Telia'z's HMO client base beyond Maccabi. The meeting focused on anticipating operational challenges and defining what outcomes the team needed from the Clalit meeting.

## Key Concerns: Clalit Contact Wants Excessive Control

The central concern was that the Clalit contact (Eli/Tzachi) wants to maintain personal control over the entire process:
- **He wants to approve each Form 17** (referral authorization) personally — not just bulk-authorize
- **He wants to review patient summaries** and approve whether patients proceed to follow-up care after intake
- **He hints that Form 17 approval is internal to Clalit**, meaning patients are not locked to Telia'z exclusively
- This mirrors a problematic pattern from Maccabi but is potentially more restrictive

The team discussed proposing a **pilot period** (1-2 months) where the contact can approve follow-ups, with the understanding that this oversight should not continue indefinitely.

## Form 17 Authorization Strategy

Form 17 is Clalit's internal referral/authorization form that patients need before receiving external services. Key issues:
- The team needs **full end-to-end Form 17** — covering both intake (6 case manager sessions + psychiatric intake) and follow-up sessions
- They need to understand if there is a **patient volume cap** — if the team suddenly sends 300 patients/month, will that be a problem?
- **SLA for Form 17 approval**: How quickly does Tzachi process approvals? This determines patient wait times
- Critical decision: patients should **not be sent to Telia'z before Form 17 is approved**, to avoid the Maccabi-era problem where patients arrived without authorization (Renee couldn't handle those cases)

## Prescription Challenge

A significant operational blocker emerged around prescriptions:
- **Clalit pharmacies do not accept external/private prescriptions** (unlike Maccabi's Haidok system)
- Very few private pharmacies work with Clalit; Super-Pharm does accept private prescriptions but likely doesn't coordinate with Clalit billing
- The preferred solution is to have **family doctors (GPs) issue prescriptions** based on Telia'z psychiatric recommendations
- This means each patient seen potentially generates an additional GP visit, which has budget implications for Clalit
- Team debated requesting **Clicks access solely for prescription entry** — but colleague warned this would invite scope creep from the Clalit contact

## System Access and Integration

The team identified several system-related questions for the Clalit meeting:
- **Clicks (Clalit EHR)**: Clalit uses Clicks internally. Team debated whether to request access — consensus was to avoid it if possible, as it creates dependency and additional demands
- **Safe/Kasefet (secure document storage)**: Need to determine if they can access the secure storage for sharing clinical summaries, as per the contract
- **Contact details**: Need to get names and contacts for IT/system access people at Clalit

## Patient Acquisition Strategy

The team discussed how patients would learn about and access the service:
- Clalit contact requested a **brochure for family doctors** to distribute — indicating a referral-based acquisition model
- Team wants to maintain flexibility: either Clalit pushes patients via referrals, or Telia'z runs marketing (like current operations)
- Potentially use messaging like "ask your doctor" to maintain flexibility without overcommitting
- Key goal: **patients should not arrive without Form 17**, but the team wants to preserve the option to do their own marketing

## Meeting Objectives Summary

The team identified these must-have outcomes from the next-day Clalit meeting:
1. Full Form 17 authorization — intake and follow-up
2. Clarity on patient volume limits
3. Pilot proposal for Clalit contact's follow-up approval oversight
4. Guidance for patients on how to get follow-up authorizations
5. SLA for Form 17 approval turnaround
6. How patients hear about and reach the service
7. System access contacts (safe, potentially Clicks)
8. Prescription workflow resolution
9. Whether Clalit contact wants to see clinical summaries

## Comparison With Maccabi Process

The team repeatedly referenced their Maccabi experience:
- Maccabi patients filled questionnaires and arrived — Form 17 was automatic
- With Clalit, the process is more manual and approval-dependent
- The Maccabi experience of patients arriving without authorization was described as "madness" and must be avoided with Clalit

## Related
![[related.base#All]]



## Follow-Up

The Clalit meeting that this planning session prepared for occurred on November 10, 2025. See [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]] and [[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]] for the outcomes.