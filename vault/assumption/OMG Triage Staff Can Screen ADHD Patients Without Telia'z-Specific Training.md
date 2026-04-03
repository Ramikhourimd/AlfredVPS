---
alfred_tags:
- healthcare/adhd/triage
based_on:
- '[[note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03]]'
confidence: low
created: '2026-03-07'
janitor_note: 'LINK001 false positives: All wikilinks are valid — project/Teliaz UK
  Expansion and both decision records exist. YAML single-quote escaping (Teliaz =
  Teliaz). Base view embeds (learn-assumption.base#Depends On This, #Related) reference
  _bases/learn-assumption.base which does not exist yet — vault-wide infrastructure
  gap. Body has backslash-escaped embeds (\\![[...]]) which should be \![[...]] —
  owner should remove backslashes. ORPHAN001: no inbound wikilinks detected; consider
  linking from a project or decision record.'
name: OMG Triage Staff Can Screen ADHD Patients Without Telia'z-Specific Training
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[assumption/OMG Will Handle Initial Patient Triage for NHS ADHD Pathway]]'
- '[[decision/OMG Handles Triage and Governance While Telia''z Provides Psychiatric
  Services]]'
- '[[decision/Three-Outcome Triage Model for UK NHS ADHD Screening]]'
relationships:
- confidence: 0.9
  context: Staff screening enables OMG triage role
  source: assumption/OMG Triage Staff Can Screen ADHD Patients Without Telia'z-Specific
    Training.md
  target: assumption/OMG Will Handle Initial Patient Triage for NHS ADHD Pathway.md
  type: supports
- confidence: 0.75
  context: Both on ADHD screening efficacy
  source: assumption/OMG Triage Staff Can Screen ADHD Patients Without Telia'z-Specific
    Training.md
  target: assumption/Virtual Triage Is Clinically Sufficient for Initial ADHD Screening.md
  type: related-to
source: OMG pathway design session — implicit in task assignment
source_date: '2025-07-03'
status: active
type: assumption
---

# OMG Triage Staff Can Screen ADHD Patients Without Telia'z-Specific Training

## Claim

The team assumes OMG Healthcare's existing clinical staff can perform the initial ADHD triage (inclusion/exclusion screening using health inequity and high risk factors) without requiring specialist training from Telia'z. The triage uses standard screening criteria rather than Telia'z proprietary clinical protocols.

## Basis

In the OMG pathway design meeting (July 2025), the triage stage was assigned entirely to OMG with no mention of a training program from Telia'z. The screening uses "health inequity and high risk factors" — standard NHS screening concepts — rather than Telia'z-specific ADHD tools like ASRS or DIVA. The assumption is implicit: OMG's staff already have the clinical competence for this level of screening.

This contrasts with the case manager role (Step 2), where Telia'z explicitly provides SOPs and training because that step uses proprietary clinical workflows.

## Evidence Trail

- 2025-07-03: OMG pathway design — triage assigned to OMG with no training requirements mentioned
- Contrast: Case manager role explicitly requires Telia'z SOPs and training

## Impact

If OMG staff cannot adequately screen without training, triage quality may suffer — either over-referring (wasting psychiatric capacity) or under-referring (missing patients). This would require Telia'z to develop and deliver a triage training program, adding time and cost to the partnership setup.

\![[learn-assumption.base#Depends On This]]
\![[learn-assumption.base#Related]]