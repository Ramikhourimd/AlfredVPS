---
alfred_tags:
- taliaz/leadership
- taliaz/strategy
- taliaz/operations
created: '2026-02-15'
description: Weekly team meeting covering UK clinic launch timeline (March 31 target),
  Israel patient capacity crisis (945 new patients but only 8% converted to intakes),
  recruitment bottlenecks, psychiatry academy planning, and internal marketing strategy
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — create base file to enable dynamic views. ORPHAN001 — no inbound wikilinks;
  consider linking from project/Telia'z UK Expansion or project/Telia'z Clinic Israel.
name: Telia'z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z Innovation Program]]'
- '[[org/Telia''z]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[person/Adi Lavi]]'
- '[[person/Stav Zamir]]'
- '[[person/Li Yamin]]'
- '[[person/Alex Taliaz]]'
- '[[conversation/Telia''z Team Meeting UK Launch and Operations 2026-02-15]]'
relationships:
- confidence: 0.85
  context: UK patient capacity ties to strategy
  source: note/Telia'z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15.md
  target: note/Organizational Strategy Meeting 2026-02-22.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Telia'z Team Meeting: UK Launch, Patient Capacity, and Recruitment — 2026-02-15

## Context

Weekly team status meeting held via Zoom on February 15, 2026. Basel Kanaaneh was absent (on vacation). Shachar absent (early morning time zone). Meeting led by Dekkel Taliaz with Rami Khouri joining remotely (with sleeping child). Key agenda: UK clinic launch progress, Israel patient capacity metrics, recruitment pipeline, and internal service quality.

## 1. UK Clinic Launch — Track 1: Leon (GP with CQC)

Adiel reported progress on the primary UK launch track through Leon, a UK-based family doctor who already holds his own CQC registration:

- **Contract status:** Leon reviewed the contract over the weekend; signature expected imminently
- **Operational model:** Telia'z will operate under Leon's CQC license initially — patients flow through his practice website into Telia'z assessment flow
- **Clinical flow:** Yael (Li Yamin) met Leon on Thursday; she showed him the initial patient flow design
- **SOPs:** Telia'z needs to share ADHD-specific SOPs with Leon; all other clinical SOPs are his own
- **Paperwork:** CQC registration paperwork is managed by Susan; Nevin's paperwork is ready
- **Case management:** Initial case management to be handled by existing Israeli team member Basem (English-speaking), as a stopgap until local UK recruitment
- **Prescriptions:** UK prescriptions require a separate system — either integration with an external prescribing platform or a dedicated UK prescription module. Stav flagged this as critical: patients completing assessment need prescriptions, not just diagnosis
- **Timeline:** Shachar targeting system launch on March 31; campaign launch mid-March to start driving patients

### Track 2: CQC Application via NHS

- Working with a second track to obtain their own CQC registration through NHS referral pathway
- Met Dolifa Ioja on Thursday to advance this
- Adiel pressing Susan for deeper conversations to accelerate this pathway
- This is a longer-term parallel track

## 2. Product and Development Updates

Stav Zamir reported on development blockers:

- **Questionnaire UI:** Design adaptation issues — the questionnaire doesn't display correctly in the current system build. Scrolling problems and visual inconsistencies. May need design changes
- **Admin view:** Being built to match Israel's existing admin interface
- **Psychiatrist view:** Requires a different layout from the treatment tab; still being designed
- **Scheduling system:** Not yet scoped — was not part of the assessment scope but is essential for UK. Patients need to see available appointment slots. Stav recommended adding to backlog as priority since it's more complex than other scopes
- **Prescription system:** Critical for UK — patients currently get diagnosis but no prescription issuance. Need to understand UK prescription regulations and integrate with appropriate system
- **UK formats:** Rami and Stav need to define UK-specific report/document formats. To be discussed in the 2pm backlog meeting
- **Shachar's launch target:** March 31 for full UK system deployment

## 3. Israel Patient Capacity — Dashboard Review

Rami presented the operations dashboard showing a severe capacity bottleneck:

- **New patients this month:** 945 completed questionnaires
- **Intakes scheduled this month:** Only 77 (8.1% conversion rate)
- **Reason:** Month started with near-full capacity; no available slots for new intakes
- **Waiting list:** ~300+ patients with no appointment scheduled at all
- **Forward bookings:** ~600 patients scheduled for March and beyond
- **Average wait time (current month):** ~7 days for those who got appointments — but this metric excludes the hundreds still waiting with no appointment
- **Incoming capacity:** 2 new psychiatrists and 2 new case managers in onboarding pipeline, adding ~80 case manager hours

### Capacity Analysis

Adiel noted the data shows ~92% of patients who register don't get an appointment in the same month, calling this a critical operational metric. Dekkel emphasized this dashboard needs to be in front of Basel constantly.

Rami proposed the dashboard should be enhanced to show not just same-month conversions but total patients with/without appointments across all future months.

## 4. Patient Discharge Framework (Rami's Proposal)

Rami presented a draft plan to manage patient flow through active discharge:

- **Natural churn rate:** Estimated ~15% monthly (needs validation)
- **Proposed discharge targets:**
  - 10% discharged after intake
  - 30% discharged after 1st follow-up
  - 30% discharged after 2nd follow-up
  - 30% discharged after 3rd follow-up
- **Methodology:** Literature review of psychiatric patient behavior → cross-reference with Telia'z data → identify early discharge indicators → build into questionnaire and psychiatrist decision support
- **Goal:** Shift clinic profile from retention-heavy to intake-heavy, reducing average treatment duration to 4-6 months
- **Patient selection:** Also needs to address patient mix — currently no screening for severity, leading to complex personality disorder patients who are difficult for telehealth model

Dekkel agreed this needs a dedicated planning session with Rami (and possibly Basel) to map the business/financial implications.

## 5. Recruitment and Onboarding

### Jobs Page
- Adi reported the careers page is nearly complete; most content finalized as of this meeting
- Delays caused by iterating on content (adult vs. child psychiatrist vs. international roles) and needing Roy Shur for form testing
- Dekkel pushed for immediate launch — even imperfect
- Google UK campaign requires approval process which takes time; Israel campaigns can launch immediately

### Onboarding Pipeline
- 4 new staff in onboarding but haven't opened schedule hours yet
- Rami reported onboarding has 4 layers: clinical training, operational orientation, administrative procedures, technical system training
- Technical training (system) is the only hard prerequisite before opening hours
- Currently Shira handles most training; exploring delegation
- Target: biweekly onboarding cohorts (weekly unrealistic given hiring pace)
- New staff shadow existing clinicians before taking their own patients

### Psychiatry Academy
- Rami reported first cohort planned for early March, with training sessions starting mid-March
- Purpose: structured program to train clinicians on tech-enabled psychiatry
- Rami emphasized this should be positioned as value proposition for recruitment — clinicians joining a technology-forward practice
- Adi agreed the marketing narrative is shifting toward innovation/technology positioning
- Rami cautioned: must build the actual training program before marketing it externally

### Stopgap Ideas
- Alex Taliaz suggested outsourcing case management to a vendor/call center temporarily to handle the patient volume gap
- Dekkel noted this is worth exploring but complex operationally

## 6. Internal Service and Clinician Satisfaction

- Adi building internal marketing plan to improve clinician engagement and satisfaction
- Rivi Idelman collecting data showing some staff dissatisfaction — some employees actively discouraging new hires from joining
- Rami: not surprising given current workload; the stabilization work (new hires, Rivi's work, training improvements) is designed to address this
- Rami emphasized: before pursuing growth, need to stabilize existing team
- Dekkel acknowledged this but noted the reality of 945 monthly patients demands action on both fronts simultaneously

## 7. Telephony and Service Setup

- Telephony/WhatsApp service channels are mostly configured and ready
- Amit being onboarded for telephony operations; Eitan to do handoff
- Final testing needed before going live

## Key Takeaways

1. **UK launch is on aggressive timeline** — March 31 system launch, mid-March campaign start, but contract not yet signed and prescription/scheduling systems not built
2. **Israel capacity is in crisis** — 92% of new patients cannot be served in the month they register
3. **Recruitment is the bottleneck** — both psychiatrists and case managers, with onboarding taking too long
4. **Stabilization vs growth tension persists** — Rami advocates for stabilizing before growing, leadership pushing for both simultaneously
5. **Internal satisfaction risk** — staff dissatisfaction could undermine recruitment efforts

## Related
![[related.base#All]]