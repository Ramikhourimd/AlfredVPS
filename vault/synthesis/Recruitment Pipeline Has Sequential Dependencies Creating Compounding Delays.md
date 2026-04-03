---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[task/Launch Careers and Jobs Page on Telia''z Website]]'
- '[[task/Launch Jobs Page for Psychiatrist and Case Manager Recruitment]]'
- '[[task/Investigate and Address Staff Satisfaction Issues]]'
- '[[constraint/Recruitment Marketing Campaigns Blocked Until Careers Page Is Live]]'
- '[[constraint/Quarter-Position Employment Model Creates 4x Hiring Volume for Target
  Scale]]'
- '[[assumption/Scaling Requires Approximately 176 Individual Quarter-Position Hires]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001 — All Telia''z wikilinks valid (YAML escaping false positive).
  All link targets verified: task/Launch Careers, constraint/Quarter-Position, synthesis/Patient
  Volume Outpacing, synthesis/Demand Growth Outpacing all exist. learn-synthesis.base
  embeds reference missing _bases/ — vault-wide gap, preserved. ORPHAN001 — no inbound
  links; consider linking from project.'
name: Recruitment Pipeline Has Sequential Dependencies Creating Compounding Delays
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/Workforce Stabilization Must Precede Aggressive Recruitment]]'
- '[[constraint/Clinic Israel Staff Satisfaction Risk Undermining Recruitment]]'
relationships:
- confidence: 0.8
  context: Recruitment is a bottleneck in clinic growth
  source: synthesis/Recruitment Pipeline Has Sequential Dependencies Creating Compounding
    Delays.md
  target: synthesis/Clinic Growth Pipeline Has Three Sequential Bottlenecks Blocking
    Scale.md
  type: part-of
status: draft
supports:
- '[[synthesis/Patient Volume Outpacing Capacity Creates Dual Crisis in Recruitment
  and Retention]]'
- '[[synthesis/Demand Growth Outpacing Capacity Across All Telia''z Dimensions]]'
tags:
- recruitment
- capacity
- pipeline
- scaling
type: synthesis
---

# Recruitment Pipeline Has Sequential Dependencies Creating Compounding Delays

## Insight

The clinic's recruitment pipeline contains at least four sequential dependencies, each introducing its own delay. Because these are sequential (not parallel), delays compound multiplicatively rather than additively: careers page → marketing campaigns → candidate applications → hiring decisions → onboarding → clinical availability. As of February 2026, the pipeline is stalled at step one (careers page not live), meaning no downstream progress can occur regardless of how urgently leadership pushes for capacity expansion.

## Evidence

1. **Careers page blocks campaigns**: Li Yamin confirmed page structure is ready but form testing requires Roy Shur. Dekkel expressed frustration at the delay. Yael Marciano's campaigns cannot launch without a live application endpoint (task records from 2026-02-15).

2. **Campaigns block applications**: Google UK campaigns require a separate approval process described as "slow." Israel campaigns can launch immediately but only once the page exists.

3. **Staff satisfaction blocks referrals**: Adi Lavi reported that current staff are actively discouraging prospective applicants from joining (2026-02-15 team meeting). This means even when campaigns generate interest, word-of-mouth is working against recruitment.

4. **Onboarding blocks availability**: New hires cannot see patients until technology access (Teams, HoViD) is set up — and this depends on Stav or Shira's availability for orientation sessions (onboarding discussion 2026-02-12).

5. **Quarter-position model multiplies volume**: Each full-position equivalent requires ~4 individual hires, meaning the pipeline must process roughly 4x the number of recruitment cycles compared to full-time hiring.

## Implications

The compounding effect means that a 2-week delay at the careers page stage translates to a 6-8 week delay before the first new clinician sees their first patient. At the projected scale (176 hires needed), even small friction at each stage accumulates into months of lost capacity. Leadership's urgency about recruitment is structurally mismatched with the pipeline's sequential reality.

## Applicability

This pattern applies specifically to Clinic Israel's current scaling push. It also has implications for the planned UK expansion, where Google campaign approval adds an additional sequential dependency. Any future hiring surge will encounter the same pipeline constraints unless the sequential dependencies are parallelized or pre-staged.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]