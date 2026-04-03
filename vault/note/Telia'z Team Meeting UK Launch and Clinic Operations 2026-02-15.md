---
alfred_tags:
- taliaz/leadership
- taliaz/strategy
- taliaz/operations
created: '2026-02-15'
description: Weekly team meeting covering UK clinic launch status (Leon contract,
  CQC, insurance), Israel clinic capacity crisis (945 new patients but only 8% intake
  conversion), product development gaps (scheduling, prescriptions for UK), recruitment
  bottleneck, and psychiatry academy planning
janitor_note: LINK001 wikilinks with Telia'z are YAML-escape false positives (Telia''z
  → Telia'z). Base embed targets (related.base) do not exist — vault-wide infrastructure
  gap. ORPHAN001 — no inbound links; may need linking from a project or conversation.
  Swept 2026-02-27.
name: Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[person/Li Yamin]]'
- '[[person/Stav Zamir]]'
- '[[person/Yael Marciano]]'
- '[[person/Alex Taliaz]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Shira]]'
- '[[person/Rivi Idelman]]'
- '[[org/Telia''z]]'
- '[[decision/Target Patient Discharge Rates of 10-30-30-30 Percent]]'
- '[[assumption/Active Discharge Protocol Can Rebalance Intake to Follow-Up Ratio]]'
- '[[task/Sign UK Clinic Contract With Leon]]'
- '[[task/Finalize UK Insurance Quote and Payment]]'
- '[[task/Launch Jobs Page for Psychiatrist and Case Manager Recruitment]]'
- '[[task/Scope UK Scheduling and Prescription Features for Product Backlog]]'
- '[[task/Prepare UK Clinical Document Formats]]'
- '[[task/Design Patient Discharge Protocol and Literature Review]]'
- '[[assumption/UK Launch Can Operate Under Partner CQC Without Own Registration]]'
relationships:
- confidence: 0.85
  context: Clinic ops relevant to strategy
  source: note/Telia'z Team Meeting UK Launch and Clinic Operations 2026-02-15.md
  target: note/Organizational Strategy Meeting 2026-02-22.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Telia'z Team Meeting: UK Launch and Clinic Operations 2026-02-15

## Context

Weekly Telia'z team meeting held 2026-02-15. Participants: Dekkel Taliaz (chair), Rami Khouri, Adiel Levin, Li Yamin, Stav Zamir, Yael Marciano, Alex Taliaz. Basel Kanaaneh and Shachar were absent. Meeting covered five major tracks: UK clinic launch, Israel patient capacity, product development, recruitment/onboarding, and marketing.

## 1. UK Clinic Launch — Track 1: Leon (GP with CQC)

Adiel Levin reported on the primary UK launch track through Leon, a family physician who already has his own CQC registration. Leon reviewed the proposed framework on Thursday and will finalize over the weekend.

**Operational model:** Leon's existing clinic serves as the shell; Telia'z sends patients to him. Yael met Leon on Thursday and showed him the initial patient flow being built for his website — patients arrive at his site and go through Telia'z assessment flow.

**Pending items:**
- Contract still being negotiated (led by Telia'z legal)
- Leon needs to see the admin and psychiatrist system views
- ADHD SOPs need to be shared with Leon — all other SOPs are his; only ADHD protocol is Telia'z proprietary
- Case manager: starting with existing Israel-based case manager (Bassem suggested as he has prior English experience), as stopgap until UK-based hiring
- Prescription system: UK requires specific prescription formats and processes (not yet scoped in product backlog)

**Timeline:** Adiel aims to sign contract this week, begin patient onboarding in parallel, target mid-March campaign start, system launch March 31.

## 2. UK Clinic Launch — Track 2: CQC/NHS

A second track is advancing for Telia'z to obtain its own CQC registration and receive NHS referrals. Adiel met with Daolifa Eujah on Thursday and is pushing Susan for deeper conversations to establish this pathway.

## 3. Insurance (UK Compliance)

Li Yamin is working with the insurance broker. Quote from previous year was approximately $5,000. Dekkel emphasized this is critical and must be finalized. Li committed to pushing for resolution this week but noted the broker's pace is outside their control.

## 4. Israel Clinic — Patient Capacity Crisis

Rami presented the operational dashboard showing a severe conversion bottleneck:

- **945 new patients** registered this month (filled questionnaire)
- **Only 77 (8%)** received intake case manager appointments this month
- **~600** were scheduled for next month (March)
- **~300** remain unscheduled (waiting list)
- **Wait time:** 7 days median for those who did get appointments — but this is misleading because hundreds haven't been scheduled at all
- **Two new psychiatrists** not yet opening hours (pending onboarding/training)
- **Two new case managers** also pending onboarding

Adiel noted the gap is staggering — 92% of patients who arrived this month did not receive an appointment this month. Dekkel pushed for the dashboard to be Basel's primary operational tool, with conversion targets visible at all times.

## 5. Patient Discharge Strategy (New)

Rami presented a plan to manage patient load by actively controlling patient lifecycle:

**Target discharge rates:**
- 10% of patients released after intake
- 30% released after first follow-up
- 30% released after second follow-up
- 30% released after third follow-up

**Implementation approach:**
1. Literature review on psychiatric patient treatment patterns
2. Cross-reference with Telia'z own data — identify who drops off naturally, when, and why
3. Modify intake questionnaire to better identify patients suitable for short-term treatment
4. Build features for psychiatrists: automated recommendations to discharge patients based on clinical indicators
5. Goal: shift clinic from retention-heavy to intake-heavy operation

Dekkel and Oren want to validate this against financial models to ensure it aligns with business sustainability.

## 6. Product/Development Status

Stav Zamir reported:
- **Questionnaire UI:** Design adaptation issues — scrolling problems, visual mismatch with intended design. Functional but cosmetically needs work.
- **Admin/psychiatrist views:** Stav's team building new UK-specific admin and psychiatrist interfaces
- **Scheduling feature:** Not yet scoped (was outside assessment scope). Critical for UK — patients need to know when they can receive their next session.
- **Prescription system:** Required for UK launch — cannot prescribe medication without it. Different from Israel. Needs scoping and integration with external systems. Stav wants it added to backlog.
- **UK formats (Rami):** Clinical document formats needed for UK. To be worked on with Stav — target: ready by March.

A backlog prioritization meeting is scheduled for today at 2 PM.

## 7. Recruitment and Onboarding

**Jobs page:** Li Yamin reported the page structure is ready but hasn't been tested for form submissions. Roy Shur (developer) is needed for email verification but was absent. Dekkel expressed frustration at the delay — the page is a critical blocker for recruitment campaigns. Target: go live today/tomorrow.

**Onboarding acceleration:** Four new staff members not yet working full hours. Basel is working to compress onboarding from ~1 month to ~1 week. Training has four layers:
1. Clinical training (not all roles need this)
2. Operational/process training
3. Administrative training (system, scheduling, office contacts)
4. Technical training (mandatory before opening hours — Shira currently delivers this)

Target: biweekly training cohorts. Rami planning first psychiatry academy cohort for early March.

**Staffing idea (Alex Taliaz):** Suggested using a vendor/call-center model as a stopgap for case management capacity — similar to how Maccabi uses external case management services. Under evaluation.

## 8. Marketing and Internal Service

**External marketing:** Yael Marciano's recruitment campaigns ready to deploy once jobs page goes live. Also preparing patient acquisition campaigns for UK.

**Internal marketing to clinicians:** Rami emphasized that before marketing the company externally as innovative, they need to actually deliver innovation value to existing clinicians. Proposed building a structured training program — "how to be a technology-enabled psychiatrist" — before using innovation as a recruitment message. Rami warned against marketing promises without substance.

**Employee satisfaction concern:** Yael flagged information from Rivi Idelman that some clinicians (including case managers) would not recommend working at the clinic. Rami acknowledged this is not surprising given current workload pressures and said the stabilization work (new hires, Rivi's engagement, training improvements) is the remedy. Dekkel emphasized this must be addressed.

**Service infrastructure:** Telephony and WhatsApp systems are set up. Amit is joining to handle day-to-day service operations.

## Key Tensions Surfaced

1. **Growth vs. stabilization:** 945 new patients/month with only 8% conversion shows demand far outpaces capacity. Some want to push harder on recruitment; Rami argues stabilize first.
2. **Marketing innovation vs. delivering it:** Rami insists building the actual training program must precede marketing it. Others want to move faster on messaging.
3. **UK timeline pressure:** March 31 system launch target, but prescription and scheduling features not yet scoped.
4. **Dashboard interpretation:** Disagreement on whether 7-day wait time is meaningful when 300+ patients have no appointment at all.

## Related
![[related.base#All]]