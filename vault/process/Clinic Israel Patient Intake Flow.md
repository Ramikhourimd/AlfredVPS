---
alfred_tags:
- clinic-israel/onboarding
area: clinical operations
created: '2025-12-04'
depends_on: []
description: End-to-end patient onboarding workflow from referral application through
  first contact screening, professional clinical interview, to psychiatrist assignment
  at Telia'z Clinic Israel
frequency: as-needed
governed_by: []
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Base view embeds (process.base#Dependencies, #Runs, #Notes) reference _bases/process.base
  which does not exist.'
name: Clinic Israel Patient Intake Flow
owner: '[[person/Shira]]'
related:
- '[[project/Telia''z Clinic Israel]]'
- '[[person/Rana Khouri]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[org/Telia''z]]'
- '[[note/Clinic Patient Intake Process and Compensation Review 2025-12-04]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
relationships:
- confidence: 0.95
  context: Israel flow based on general intake
  source: process/Clinic Israel Patient Intake Flow.md
  target: process/Clinic Patient Intake.md
  type: depends-on
status: active
tags: []
type: process
---

# Clinic Israel Patient Intake Flow

The standard patient onboarding process for Telia'z Clinic Israel, handling referrals from HMOs (primarily Clalit and Maccabi) and direct applications.

## Steps

1. **Application received** — Patient referral arrives via HMO contract (Clalit, Maccabi) or direct application
2. **First Contact screening (Rana)** — Rana Khouri conducts initial phone screening ("rishon mitkadem"). Preliminary assessment of patient needs, eligibility, and urgency
3. **Professional Interview (Shira/Uri/Waseem)** — Clinical professional conducts deeper evaluation. Shira or Uri handles standard adult cases; Waseem handles couples therapy referrals
4. **Clinical Assignment** — Patient assigned to appropriate psychiatrist based on clinical needs, availability, and fee schedule tier (old vs new scheme). If no slot available, Rami can handle the clinical interview directly
5. **Agreement and onboarding** — Administrative setup including payment scheme, system registration, and scheduling

## Notes

- The flow was documented during a 2025-12-04 discussion between Rami and Basel
- There is ambiguity about whether the "new scheme" vs "old scheme" distinction affects the routing at step 4
- Administrative vs clinical responsibility at the assignment stage needs clearer ownership

## Dependencies
![[process.base#Dependencies]]

## Runs
![[process.base#Runs]]

## Notes
![[process.base#Notes]]