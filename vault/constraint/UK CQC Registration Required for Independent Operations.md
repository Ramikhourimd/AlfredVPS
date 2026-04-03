---
alfred_tags:
- healthcare/cqc
- uk/regulation
authority: Care Quality Commission (CQC), UK
created: '2026-02-15'
description: UK healthcare regulations require Care Quality Commission (CQC) registration
  to operate independently. Until obtained, Telia'z must operate under a partner's
  existing CQC registration.
janitor_note: 'LINK001 false positives: All three Telia''z wikilinks are valid YAML
  single-quote escaping (Telia''''z = Telia''z). Base view embeds (learn-constraint.base#Affected
  Projects, #Related) reference _bases/learn-constraint.base which does not exist
  yet — vault-wide infrastructure gap, not a per-record issue.'
name: UK CQC Registration Required for Independent Operations
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch Operations and Capacity 2026-02-15]]'
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
- '[[decision/Operate UK Clinic Under Leon CQC Registration]]'
relationships:
- confidence: 0.6
  context: Regulatory ops requirements
  source: constraint/UK CQC Registration Required for Independent Operations.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: related-to
- confidence: 0.95
  context: Req supports lack as constraint
  source: constraint/UK CQC Registration Required for Independent Operations.md
  target: constraint/Telia'z Lacks Independent UK CQC Registration.md
  type: supports
- confidence: 0.88
  context: Similar CQC registration reqs
  source: constraint/UK CQC Registration Required for Independent Operations.md
  target: constraint/UK Clinic Requires CQC Registration to Operate.md
  type: related-to
source: UK healthcare regulations
source_date: '2026-02-15'
status: active
type: constraint
---

# UK CQC Registration Required for Independent Operations

## Constraint
Operating a healthcare clinic in the UK requires CQC (Care Quality Commission) registration. Telia'z does not have its own CQC registration and must either obtain one or operate under a registered provider.

## Source
UK healthcare regulation. CQC is the independent regulator of health and social care in England.

## Implications
- Cannot operate independently in UK without own CQC
- Current workaround: partner with Leon who holds his own CQC
- Parallel track: applying for own CQC to eventually receive NHS referrals
- Insurance also required (~$5,000 estimated)
- Limits operational independence in the short term

## Expiry / Review
Active until Telia'z obtains own CQC registration. Second track with NHS pathway being explored.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]