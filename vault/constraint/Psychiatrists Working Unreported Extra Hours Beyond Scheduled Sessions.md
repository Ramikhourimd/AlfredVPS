---
alfred_tags:
- operations/unreported-hours
- clinic/psychiatrists
- finance/labor-costs
authority: Operational reality reported by clinical staff
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Assumption link valid (YAML line-wrap false positive). Base view embeds (learn-constraint.base#Affected
  Projects, #Related) reference _bases/learn-constraint.base which does not exist
  — vault-wide infrastructure gap. Embeds preserved.'
location: []
name: Psychiatrists Working Unreported Extra Hours Beyond Scheduled Sessions
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Six to Eight Hours Per Week Is Sustainable Telepsychiatry Workload
  Threshold]]'
- '[[constraint/Clinic Israel Staff Satisfaction Risk Undermining Recruitment]]'
relationships:
- confidence: 0.9
  context: Psychiatrists/staff unreported extra hours beyond sessions
  source: constraint/Psychiatrists Working Unreported Extra Hours Beyond Scheduled
    Sessions.md
  target: constraint/Staff Report Unreported Extra Hours Beyond Scheduled Sessions.md
  type: related-to
- confidence: 0.98
  context: Near-identical psych extra hours beyond/outside
  source: constraint/Psychiatrists Working Unreported Extra Hours Beyond Scheduled
    Sessions.md
  target: constraint/Psychiatrists Working Unreported Extra Hours Outside Scheduled
    Sessions.md
  type: related-to
source: Staff interviews conducted by Rivi Idelman
source_date: '2026-02-18'
status: active
tags:
- staffing
- burnout
- labor
type: constraint
---

# Psychiatrists Working Unreported Extra Hours Beyond Scheduled Sessions

## Constraint

Psychiatrists are working unreported extra hours — arriving early to review cases before sessions, spending time on documentation after scheduled blocks, and handling follow-up outside their billed hours. This labor is invisible in scheduling and compensation systems.

## Source

Reported during staff interviews conducted by Rivi Idelman, shared in the 2026-02-18 meeting with Rami. Multiple psychiatrists confirmed working preparation and follow-up time that is not captured in their scheduled hours.

## Implications

- Actual per-hour compensation is lower than reported, which may affect recruitment and retention
- Burnout calculations based on scheduled hours underestimate true workload
- The 6-8 hours/week sustainability threshold may actually represent more real work hours than assumed
- Any staffing model or satisfaction survey must account for total hours, not just scheduled sessions
- This creates a hidden labor cost that is not visible in financial planning

## Expiry / Review

Active until the scheduling/compensation system captures preparation and follow-up time. Should be measured in the upcoming employee satisfaction survey.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]