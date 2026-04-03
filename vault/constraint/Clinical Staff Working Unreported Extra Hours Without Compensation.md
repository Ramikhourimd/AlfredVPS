---
alfred_tags:
- operations/unreported-hours
- clinic/psychiatrists
- finance/labor-costs
authority: Employment law and organizational policy
created: '2026-02-27'
janitor_note: 'LINK001: Teliaz wikilinks are valid (YAML single-quote escaping false
  positive). Base view embeds (learn-constraint.base#Affected Projects, #Related)
  reference _bases/learn-constraint.base which does not exist — vault-wide infrastructure
  gap, embeds preserved per policy. ORPHAN001 — no inbound wikilinks; consider linking
  from project/Teliaz Clinic Israel or project/Teliaz Innovation Program.'
location: []
name: Clinical Staff Working Unreported Extra Hours Without Compensation
project:
- '[[project/Telia''z Innovation Program]]'
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/6-8 Weekly Hours Is Sustainable Threshold for Telepsychiatry Staff]]'
- '[[synthesis/Telepsychiatry Burnout Driven by Intensity Per Hour Not Total Hours]]'
- '[[constraint/Clinic Israel Staff Satisfaction Risk Undermining Recruitment]]'
relationships:
- confidence: 0.9
  context: Unreported hours by clinical staff/psychiatrists
  source: constraint/Clinical Staff Working Unreported Extra Hours Without Compensation.md
  target: constraint/Psychiatrists Underreporting Working Hours Masks True Labor Cost.md
  type: related-to
- confidence: 0.95
  context: Clinical staff and psychiatrists unreported extra hours
  source: constraint/Clinical Staff Working Unreported Extra Hours Without Compensation.md
  target: constraint/Psychiatrists Working Unreported Extra Hours Beyond Scheduled
    Sessions.md
  type: related-to
- confidence: 0.85
  context: Unreported extra hours in clinical staff contexts
  source: constraint/Clinical Staff Working Unreported Extra Hours Without Compensation.md
  target: constraint/Staff Report Unreported Extra Hours Beyond Scheduled Sessions.md
  type: related-to
- confidence: 0.9
  context: Clinical staff includes psych extra hours
  source: constraint/Clinical Staff Working Unreported Extra Hours Without Compensation.md
  target: constraint/Psychiatrists Working Unreported Extra Hours Outside Scheduled
    Sessions.md
  type: related-to
source: Staff interviews conducted by Rivi Idelman
source_date: '2026-02-18'
status: active
type: constraint
---

# Clinical Staff Working Unreported Extra Hours Without Compensation

## Constraint

Psychiatrists at Telia'z are regularly working unreported extra hours — arriving early to review cases, preparing before sessions, and completing documentation after sessions end — without these hours being tracked or compensated.

## Source

Multiple psychiatrist interviews conducted by Rivi Idelman and reported during the 2026-02-18 meeting. Specifically noted in the Employee Experience Research notes: "Psychiatrists are working extra hours (preparation before sessions...)" that are neither tracked nor compensated by the organization.

## Implications

- **Legal/compliance risk**: Untracked working hours may create employment law exposure depending on contractual arrangements
- **Burnout amplification**: The actual working hours exceed reported hours, meaning the 6-8 hour sustainable threshold may be lower than assumed when preparation time is included
- **Satisfaction distortion**: Staff satisfaction surveys measuring "hours worked" may undercount true workload if staff report only scheduled hours
- **Retention risk**: Staff who feel their true effort is invisible may become disengaged or leave

## Expiry / Review

This constraint persists until the organization implements either: (a) a time-tracking mechanism that captures preparation and documentation time, or (b) a compensation model that accounts for total engagement time rather than just scheduled session time. Should be addressed in the staff satisfaction survey design.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]