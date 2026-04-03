---
alfred_tags:
- taliaz/leadership
- taliaz/strategy
- taliaz/operations
created: '2026-02-15'
description: Weekly team meeting covering UK clinic launch progress (Leon contract,
  CQC, insurance, March 31 target), Israel clinic capacity crisis (945 new patients
  vs 77 intakes = 8% conversion), recruitment bottlenecks, patient discharge strategy,
  and internal service improvements
janitor_note: LINK001 — Telia'z wikilinks are YAML escaping false positives (targets
  exist). Base view embed (related.base#All) references nonexistent _bases/related.base
  — vault-wide infrastructure gap, embed preserved. ORPHAN001 — no inbound wikilinks,
  consider linking from parent record.
name: Telia'z Team Meeting UK Launch Operations and Recruitment 2026-02-15
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z Innovation Program]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Rami Khouri]]'
- '[[person/Adiel Levin]]'
- '[[person/Adi Lavi]]'
- '[[person/Li Yamin]]'
- '[[person/Stav Zamir]]'
- '[[person/Alex Taliaz]]'
- '[[person/Basel Kanaaneh]]'
- '[[person/Shachar]]'
- '[[person/Shira]]'
- '[[person/Rivi Idelman]]'
relationships:
- confidence: 0.85
  context: UK launch ops inform org strategy
  source: note/Telia'z Team Meeting UK Launch Operations and Recruitment 2026-02-15.md
  target: note/Organizational Strategy Meeting 2026-02-22.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Telia'z Team Meeting: UK Launch, Operations, and Recruitment 2026-02-15

## Context

Weekly team meeting held 2026-02-15 with Dekkel Taliaz (CEO), Rami Khouri (CMIO), Adiel Levin (VP Business Development), Adi Lavi (CMO), Li Yamin (Product/HR), Stav Zamir (Innovation), and Alex Taliaz (Board). Basel Kanaaneh (Clinic GM) was on vacation. Shachar (VP R&D) joined early morning session separately.

## 1. UK Clinic Launch — Status and Timeline

### Track 1: Leon Partnership (Primary Path)
- Working with Leon, a UK family doctor who already holds his own CQC (Care Quality Commission) registration
- Leon reviewed the partnership proposal on Thursday; he is reviewing the contract over the weekend
- Once signed, Telia'z can route patients through his CQC, avoiding the need for a separate registration
- Leon met with Yael on Thursday and was shown the initial patient flow design
- **Contract status:** In negotiation with Telia'z legal
- **Key dependency:** Leon needs to review and sign the contract

### Track 2: NHS/CQC Direct (Secondary Path)
- Adiel met with a consultant on Thursday about pursuing direct CQC registration for NHS referrals
- Susan (compliance person) is being engaged for deeper conversations
- This is a longer-term play for scaling beyond Leon's practice

### Insurance
- Li Yamin is working with insurance brokers; quote was approximately $5,000 last year
- Li was asked to finalize the quote and get approval this week
- Insurance must be in place before operations begin

### Development Requirements for UK
- **Questionnaire UI:** Design/adaptation issues — functionality works but visual presentation needs fixing
- **Admin and psychiatrist views:** Admin view similar to Israel; psychiatrist view still being designed
- **Scheduling:** Not yet scoped — critical for UK since patients need appointment visibility. Added to backlog.
- **Prescriptions:** UK prescription formats differ from Israel. Rami and Stav to define required formats.
- **SOPs for ADHD:** Need to share Telia'z ADHD assessment SOP with Leon

### Case Management for UK
- Start with existing Israeli case manager (Bassem speaks English, has done this before)
- Long-term: hire locally in UK
- Basel to be looped in on hours/duration needed

### Timeline Summary
- This week: Finalize Leon contract, get insurance quote
- Next week: Begin onboarding Leon to the system
- Mid-March: Start UK marketing campaigns
- March 31: System launch target (Shachar's development deadline)
- Goal: First UK patient by end of March / early April

## 2. Israel Clinic — Capacity Crisis

### Dashboard Data (Presented by Rami)
- **945 new patients** registered this month (filled questionnaires)
- **Only 77 (8%)** received intake appointment this month
- **~600** have appointments scheduled for March; **~300** have no appointment at all
- Average wait time for those served: ~7 days (hides the hundreds still waiting)

### Capacity Expansion
- 2 new psychiatrists onboarded but not yet opening slots (pending training)
- 2 new case managers joining — adding ~80 hours of capacity
- Even with additions, only ~60 more patients served — far short of demand

### Patient Discharge Strategy (Rami's Proposal)
Proposed active patient discharge targets to free capacity:
- **10% discharged after intake** (not needing treatment, mis-referrals, personality disorders)
- **30% after 1st follow-up**
- **30% after 2nd follow-up**
- **30% after 3rd follow-up**
- Target treatment duration: 4-6 months

Implementation plan: literature review, data analysis of natural churn, identify discharge predictors, modify questionnaire, build psychiatrist-facing discharge recommendation feature. Dekkel asked for financial model alignment.

## 3. Recruitment and Onboarding

### Jobs Page
- Nearly ready but not yet tested (Roy on vacation, needed for form testing)
- Content finalized late — expanded to include child psychiatrists and international roles
- Dekkel pushed for same-day launch; Li committed to testing ASAP

### Onboarding Improvements
- 4 new staff pending but not seeing patients
- Current onboarding ~1 month; target: 1 week
- 4 layers: clinical, operational, administrative, technical
- Goal: biweekly onboarding cohort sessions
- New clinicians shadow existing ones before taking patients

### Temporary Staffing
- Alex suggested vendor/call-center to bridge case manager gap
- Similar to Maccabi's model; acknowledged as complex but worth exploring

### Psychiatry Academy
- First cohort planned for early March, training mid-March
- Rami cautioned against marketing before delivering tangible value
- Need to define curriculum before promoting externally

## 4. Marketing and Internal Service

### Recruitment Marketing Shift
- Moving from comfort messaging to innovation/technology positioning
- Rami: position Telia'z as place for "technology-enabled practitioners"
- Must deliver value before marketing it

### Staff Satisfaction Concerns
- Rivi Idelman collecting data — some case managers unhappy, would not recommend Telia'z
- Rami: not surprising given workload; structural improvements should address this
- Adi planning internal marketing to improve engagement

### Service Infrastructure
- Telephony and WhatsApp channels nearly complete
- Amit joining for phone service; Eitan briefed on integration
- Internal service processes for clinicians being developed

## Key Metrics (February 2026, Mid-Month)

| Metric | Value |
|--------|-------|
| New patient registrations | 945 |
| Intakes this month | 77 (8%) |
| Scheduled for March | ~600 |
| No appointment yet | ~300 |
| Wait time (served patients) | ~7 days |
| New staff pending onboarding | 4 |
| Additional CM hours expected | ~80 |

## Related
![[related.base#All]]