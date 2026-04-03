---
alfred_tags:
- taliaz/leadership
- taliaz/strategy
- taliaz/operations
created: '2026-02-15'
description: Weekly team meeting covering UK clinic launch progress (Leon contract,
  CQC, insurance, March 31 target), Israel clinic capacity crisis (945 new patients
  but only 8% intake conversion), product development blockers (questionnaire UI,
  prescriptions, scheduling), recruitment strategy (jobs page, psychiatry academy),
  and internal service/marketing initiatives.
janitor_note: 'LINK001s for Telia''z project/org/conversation links are all false
  positives (files exist, YAML escaping). Base embed LINK001 (related.base) is vault-wide
  infrastructure gap. ORPHAN001: no inbound links — human review needed. Flagged 2026-03-15.'
name: Telia'z Team Meeting UK Launch and Operations Review 2026-02-15
project: '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
- '[[org/Telia''z]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[person/Li Yamin]]'
- '[[person/Stav Zamir]]'
- '[[person/Yael Marciano]]'
- '[[person/Alex Taliaz]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Shachar]]'
- '[[person/Shira]]'
- '[[task/Launch Jobs Page for Clinician Recruitment]]'
- '[[task/Start Psychiatry Academy First Cohort]]'
- '[[task/Develop Patient Discharge Framework and Literature Review]]'
- '[[task/Launch UK Patient Acquisition Campaign]]'
- '[[task/Investigate and Address Staff Satisfaction Issues]]'
- '[[task/Add Total Appointments Metric to Clinic Dashboard]]'
- '[[decision/Patient Discharge Targets 10-30-30-30 Percent]]'
- '[[event/UK System Launch Target March 31 2026]]'
- '[[constraint/Clinic Israel At 8 Percent Intake Conversion Rate February 2026]]'
relationships:
- confidence: 0.85
  context: Launch review feeds into strategy
  source: note/Telia'z Team Meeting UK Launch and Operations Review 2026-02-15.md
  target: note/Organizational Strategy Meeting 2026-02-22.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Telia'z Team Meeting: UK Launch and Operations Review 2026-02-15

## Context

Weekly team meeting led by Dekkel Taliaz with Rami Khouri (remote, with baby), Adiel Levin, Li Yamin, Stav Zamir, Yael Marciano, and Alex Taliaz. Basel Kanaaneh was absent (on leave). Shachar was absent (early morning timezone). The meeting covered four major areas: UK launch, Israel clinic operations, product development, and recruitment/marketing.

## 1. UK Clinic Launch — Two Parallel Tracks

### Track 1: Leon Partnership (Family Doctor with CQC)
- Leon is a UK family doctor who already holds his own CQC (Care Quality Commission) registration
- The agreement structure: Telia'z will operate under Leon's CQC, transferring patients to him as a percentage arrangement
- Leon reviewed the contract over the weekend; Adiel expects signature this week
- Yael met Leon on Thursday and shared the initial patient flow design for his website
- **Navin** (regulatory/paperwork person) — all paperwork ready on Navin's side, will exchange documents after contract signing
- SOPs: Telia'z needs to share its ADHD-specific SOPs with Leon; all other SOPs are his
- Leon also wants to see the clinical system (admin and psychiatrist views) — Stav preparing demo

### Track 2: CQC via NHS
- Second parallel track: obtaining own CQC registration to receive NHS referrals
- Met with someone named Dolifa Euja on Thursday to explore this path
- Susan (legal/compliance) being pushed for deeper conversations
- This is a longer-term path but strategically important

### UK Staffing Plan
- **Case managers:** Starting with an Israeli case manager (Bassem mentioned as capable, has done it before in English) as stopgap while recruiting UK-based staff
- Adiel firm: UK case managers should ultimately be hired locally in England, not Israeli staff long-term
- Won't hire UK case manager until patient volume is confirmed
- Need to coordinate with Basel on time allocation for the Israeli stopgap

### UK Product Requirements
- Questionnaire UI has design/adaptation issues — not rendering correctly in the system Eitan is building
- Admin view similar to Israel; psychiatrist view is different from current treatment tab
- **Scheduling feature** not yet scoped — flagged as critical since patients need appointment visibility
- **Prescription system** critical for UK — patients must receive prescriptions (not just treatment recommendations), involves external system integration and UK-specific formats (e.g., for controlled substances like ADHD medications)
- Stav pushing to add scheduling and prescriptions to backlog sprint — needs to be ready by end of March
- **UK report formats** needed from Rami/Stav — different from Israel formats. Stav to coordinate with Rami separately.

### UK Timeline
- Shachar targeting **March 31 system launch**
- Campaign start: **mid-March** (could be earlier depending on contract signing)
- Google Ads approval needed for UK (different from Israel where approval was already obtained)
- Goal: first patient seen in April

### UK Insurance
- Insurance quote (~$5,000) obtained previously but was over a year ago
- Li Yamin working with the insurance provider to get updated quote
- Dekkel emphasized this is critical — wants it locked down this week
- Li to share final proposal by end of week

## 2. Israel Clinic Operations — Capacity Crisis

### Dashboard Review (Rami presenting)
- **945 new patients** registered this month (filled questionnaires)
- Only **77 patients (8%)** received intake appointments this month
- Remainder (~868) are waiting — roughly 600 have appointments scheduled for future months, ~300+ have no appointment at all
- Average wait time showing ~1 week, but this only counts patients who got appointments — true wait for unscheduled patients is much longer
- Opened the month at near-full capacity, which explains the low conversion

### Capacity Bottleneck
- Two new psychiatrists hired but haven't opened calendar hours yet (awaiting onboarding/orientation)
- Two new case managers also pending
- Additional ~80 case manager hours expected to come online soon
- Even with additions, Dekkel estimates needing 30-40 more psychiatrists by year-end to meet demand
- Adiel flagged: at current pace, only 4% of incoming patients are being served per month

### Patient Churn and Retention Strategy (Rami)
- Natural churn rate estimated at ~15%
- Rami proposing active patient lifecycle management with discharge targets:
  - **10%** discharged after intake (not appropriate for service)
  - **30%** discharged after 1st follow-up
  - **30%** discharged after 2nd follow-up
  - **30%** discharged after 3rd follow-up
- This would shift the clinic's character toward more intake-heavy, fewer long-term follow-ups
- Requires: literature review on psychiatric patient treatment duration, cross-referencing with Telia'z data, identifying early signals for appropriate discharge, potentially modifying the intake questionnaire
- Also includes patient selection/screening improvements — currently no filtering for severity, suicidality, personality disorders, or patients who don't need pharmacotherapy
- Dekkel wants to review this plan with Rami in a dedicated session, and then validate against business/financial model

### Onboarding Process
- 4 new staff members not yet treating patients (hired but in onboarding pipeline)
- Target: reduce onboarding from 1 month to 1 week
- Four training layers: clinical, operational, administrative (systems), technical
- Technical training is the minimum barrier to opening calendar hours
- Shira currently handles most training
- Goal: establish bi-weekly cohort-based onboarding sessions
- Also need to account for HMO registration delays (Maccabi, Clalit approval timelines)
- Alex suggested using a vendor/call-center as stopgap for case management capacity — similar to what Maccabi uses

## 3. Recruitment and Marketing

### Jobs Page
- Nearly complete but delayed due to multiple dependencies (content, form testing, Roy Shur unavailable)
- Needs to support separate listings: adult psychiatrists, child psychiatrists, international psychiatrists, case managers
- Li Yamin coordinating final testing; Yael ready to connect campaigns once live
- Dekkel frustrated at delay — emphasized this should have been up already

### Recruitment Marketing Strategy
- Shift from purely clinical appeal (work from home, flexible hours) to also emphasizing **innovation and technology**
- Rami cautioned: need to actually deliver on the innovation promise internally before marketing it externally — currently staff don't receive structured technology training
- Rami proposed a concrete internal training program (how to be a "technology-enabled psychiatrist/psychologist/social worker") before external marketing
- Yael incorporating technology/innovation messaging into recruitment campaigns

### Psychiatry Academy
- First cohort targeting early March enrollment, training sessions starting mid-March
- Rami working on curriculum
- Yael requested details for marketing coordination

## 4. Internal Service and Employee Satisfaction

### Telephony and WhatsApp Service
- Telephony and WhatsApp communication channels mostly set up
- Amit (new service person) being onboarded by Eitan for phone/service operations
- Goal: streamline patient-facing communication

### Employee Satisfaction Concerns
- Rivi Idelman collecting data showing some staff members (case managers) would not recommend working at Telia'z
- Not clear if this is widespread or isolated
- Rami: not surprised — staff burnout is known issue, current improvement initiatives (new hires, Rivi's work, training) aim to address this before scaling recruitment
- Yael building internal marketing plan: create stronger employee connection, personal outreach, feedback channels
- Shira handles clinician relationship management currently

## Key Takeaways

1. UK launch is on a tight March 31 timeline with multiple parallel workstreams (contract, insurance, product, SOPs, campaigns)
2. Israel clinic is experiencing severe capacity constraint — demand (945 patients/month) vastly outstrips capacity (77 intakes/month = 8%)
3. Patient lifecycle management (active discharge protocol) is being designed to address the intake-to-follow-up ratio imbalance
4. Product team has critical UK-specific features to build (prescriptions, scheduling, report formats) within 6 weeks
5. Internal employee satisfaction needs attention before aggressive external recruitment marketing

![[related.base#All]]

---
## Related
![[related.base#All]]