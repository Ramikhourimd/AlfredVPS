---
alfred_tags:
- healthcare/regulations
- medical-director/requirements
- physician-oversight
authority: Local healthcare regulatory bodies
created: '2026-02-25'
janitor_note: 'LINK001 — base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create it
  to enable dynamic views. Telia''z wikilinks are valid (YAML escaping false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z Organizational
  Restructuring.'
name: Each International Clinic Requires a Local Medical Director
project:
- '[[project/Telia''z UK Expansion]]'
- '[[project/Telia''z Organizational Restructuring]]'
related:
- '[[constraint/Medical Director Must Be a Licensed Physician]]'
- '[[decision/Clinic District Model With Three Parallel Management Tracks]]'
relationships:
- confidence: 0.95
  context: MD must be licensed physician
  source: constraint/Each International Clinic Requires a Local Medical Director.md
  target: constraint/Medical Director Must Be Licensed Physician.md
  type: depends-on
- confidence: 0.95
  context: MD must be licensed physician
  source: constraint/Each International Clinic Requires a Local Medical Director.md
  target: constraint/Medical Director Must Be a Licensed Physician.md
  type: depends-on
- confidence: 0.75
  context: MD satisfies oversight regs
  source: constraint/Each International Clinic Requires a Local Medical Director.md
  target: constraint/Ministry of Health Regulations Require Physician Oversight.md
  type: related-to
- confidence: 0.7
  context: UK intl clinic compliance needs
  source: constraint/Each International Clinic Requires a Local Medical Director.md
  target: constraint/UK CQC Registration Required for Independent Operations.md
  type: related-to
- confidence: 0.85
  context: Local MD ensures oversight
  source: constraint/Each International Clinic Requires a Local Medical Director.md
  target: constraint/Clinical Operations Require Physician Oversight.md
  type: part-of
source: Healthcare regulations per jurisdiction
source_date: '2026-02-22'
status: active
type: constraint
---

# Each International Clinic Requires a Local Medical Director

## Constraint

Every Telia'z clinic in a new country must have its own locally licensed Medical Director. The company-level CMO cannot serve as the Medical Director for international clinics remotely.

## Source

The UK Expansion project explicitly states "Need a local Medical Director for each international clinic." This reflects healthcare regulations that typically require a locally licensed physician to serve as the responsible medical officer for any clinical operation. The Israeli requirement for a licensed Medical Director (already captured as a separate constraint) sets the precedent, and similar requirements are expected in the UK and other target markets.

## Implications

- Each new country requires recruiting a local Medical Director before the clinic can operate
- Expansion timelines are directly gated by the ability to find qualified local physicians
- The CMO role at company level is oversight and standards, not a substitute for local medical leadership
- Cost structure must include a Medical Director salary for every clinic district

## Expiry / Review

This constraint is permanent for regulated healthcare markets. Review only needed if Telia'z explores markets with different regulatory frameworks (unlikely for psychiatric care).

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]