---
alfred_tags:
- healthcare/cqc
- uk/regulation
authority: Care Quality Commission (CQC)
created: '2026-02-15'
janitor_note: '"LINK001: project and related fields contain Telia''z with apostrophe
  — YAML single-quote escaping produces false positive broken links. Actual wikilinks
  are valid. Body contains base view embeds (\![[learn-constraint.base#Affected Projects]]
  and \![[learn-constraint.base#Related]]) referencing _bases/ infrastructure not
  yet created — preserve embeds, do not remove."'
name: UK Clinic Requires CQC Registration to Operate
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[conversation/Telia''z Team Meeting UK Launch and Clinic Operations 2026-02-15]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.6
  context: UK regulatory ops req
  source: constraint/UK Clinic Requires CQC Registration to Operate.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: related-to
- confidence: 0.92
  context: Clinic req supports Telia'z lack
  source: constraint/UK Clinic Requires CQC Registration to Operate.md
  target: constraint/Telia'z Lacks Independent UK CQC Registration.md
  type: supports
- confidence: 0.85
  context: Clinic req part of indep ops req
  source: constraint/UK Clinic Requires CQC Registration to Operate.md
  target: constraint/UK CQC Registration Required for Independent Operations.md
  type: part-of
source: UK healthcare regulation
status: active
type: constraint
---

# UK Clinic Requires CQC Registration to Operate

## Constraint

Any clinical operation in the UK must operate under a Care Quality Commission (CQC) registration. Telia'z does not have its own CQC yet, so the initial strategy is to partner with Leon (a family doctor who holds his own CQC) and operate under his registration.

## Source

UK healthcare regulations. The CQC is the independent regulator of health and social care in England.

## Implications

- Short-term: Must sign partnership with Leon to use his CQC (percentage-based arrangement)
- Medium-term: Pursuing own CQC registration via NHS pathway (second track)
- Operational: All SOPs except ADHD are Leon's; Telia'z provides its ADHD-specific SOPs
- Staffing: All UK clinical staff must meet CQC requirements

## Expiry / Review

Ongoing regulatory requirement. Review when own CQC application progresses.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]