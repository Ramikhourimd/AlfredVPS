---
alfred_tags:
- uk/clinical-launch
- timeline-assumptions
- prescription-pathway
based_on:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
challenged_by:
- '[[constraint/UK Clinic Launch Requires Prescription System Not Yet Built]]'
- '[[constraint/UK Controlled Substance Prescriptions Require Specific Format and
  System]]'
confidence: medium
created: '2026-03-08'
janitor_note: 'Previous janitor_note was incorrect: _bases/ directory EXISTS and learn-assumption.base
  embeds are valid. LINK001 flags are false positives. Cleared by vault-janitor 2026-03-14.
  ORPHAN001: No inbound links detected — this is expected for assumption records derived
  from specific notes. Not an error. Observed by vault-janitor 2026-03-16.'
name: UK Clinic Can Soft-Launch With Assessment-Only Service Before Prescription Module
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[contradiction/Prescription System Flagged as Critical But Not in Active Development
  Sprint]]'
- '[[assumption/March 2026 UK System Launch Timeline Is Achievable]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
relationships:
- confidence: 0.8
  context: Soft-launch helps achieve timeline
  source: assumption/UK Clinic Can Soft-Launch With Assessment-Only Service Before
    Prescription Module.md
  target: assumption/March 2026 UK System Launch Timeline Is Achievable.md
  type: supports
source: Implied by team behavior at 2026-02-15 meeting — prescription flagged as critical
  but launch timeline unchanged
source_date: '2026-02-15'
status: active
type: assumption
---

# UK Clinic Can Soft-Launch With Assessment-Only Service Before Prescription Module

## Claim

The team implicitly assumes the UK clinic can begin operations offering ADHD assessment and diagnosis without the ability to issue prescriptions through the platform. Patients would complete the three-step workflow (questionnaire → case manager → psychiatrist) and receive a diagnosis and treatment plan, but prescription issuance would need to happen through an external mechanism (e.g., Leon writing prescriptions manually, or referral back to GP).

## Basis

At the February 15, 2026 team meeting, Stav flagged prescription capability as "very critical" and noted the scheduling and prescription features were only being added to the product backlog — not yet in active development. Despite this, the March 31 system launch date was not challenged or revised. The team continued planning marketing campaigns for mid-March. This behavior implies an unspoken acceptance that the initial service offering will be assessment-only.

## Evidence Trail

- 2026-02-15: Stav flags prescription as critical, features added to backlog (not sprint)
- 2026-02-15: March 31 launch date reaffirmed by Shachar (absent but timeline referenced)
- 2026-02-15: Marketing campaign planning continues for mid-March start
- No recorded discussion of how patients receive prescriptions without the module

## Impact

If the clinic launches without prescription capability, the patient journey is incomplete. Patients diagnosed with ADHD expecting medication will need an alternative pathway. This could affect patient satisfaction, Leon's willingness to manage prescription volume manually, and the credibility of the "end-to-end" service proposition used in sales conversations.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]