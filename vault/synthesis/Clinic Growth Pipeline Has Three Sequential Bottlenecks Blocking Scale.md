---
alfred_tags:
- telia'z/restructuring
- clinic/operations
- innovation/program
cluster_sources:
- '[[task/Launch Careers and Jobs Page on Telia''z Website]]'
- '[[task/Launch Jobs Page for Psychiatrist and Case Manager Recruitment]]'
- '[[note/New Employee Onboarding Structure Discussion 2026-02-12]]'
- '[[note/New Employee Onboarding Framework and Technology Requirements 2026-02-12]]'
- '[[task/Investigate and Address Staff Satisfaction Issues]]'
- '[[task/Review Staff Satisfaction Survey Response Rates]]'
confidence: medium
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  VERIFIED: constraint/Staff Satisfaction Survey Data..., constraint/Quarter-Position
  Employment Model..., synthesis/Patient Volume Outpacing..., and synthesis/Demand
  Growth Outpacing... all confirmed existing. ORPHAN001 — no inbound wikilinks; consider
  linking from project/Telia''z Clinic Israel.'
name: Clinic Growth Pipeline Has Three Sequential Bottlenecks Blocking Scale
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Recruitment Marketing Campaigns Blocked Until Careers Page Goes Live]]'
- '[[constraint/Technology Access Is Hard Day-One Blocker for New Clinical Staff]]'
- '[[constraint/Clinic Israel Staff Satisfaction Risk Undermining Recruitment]]'
- '[[constraint/Staff Satisfaction Survey Data Statistically Unreliable at Current
  Response Rates]]'
- '[[synthesis/Patient Volume Outpacing Capacity Creates Dual Crisis in Recruitment
  and Retention]]'
- '[[synthesis/Demand Growth Outpacing Capacity Across All Telia''z Dimensions]]'
- '[[constraint/Quarter-Position Employment Model Creates 4x Hiring Volume for Target
  Scale]]'
relationships:
- confidence: 0.9
  context: Clinic growth depends on recruitment pipeline
  source: synthesis/Clinic Growth Pipeline Has Three Sequential Bottlenecks Blocking
    Scale.md
  target: synthesis/Recruitment Pipeline Has Sequential Dependencies Creating Compounding
    Delays.md
  type: depends-on
status: draft
supports:
- '[[assumption/Workforce Stabilization Must Precede Aggressive Recruitment]]'
- '[[assumption/Organizational Health Score Must Clear Threshold Before Growth]]'
type: synthesis
---

# Clinic Growth Pipeline Has Three Sequential Bottlenecks Blocking Scale

## Insight

The clinic's growth pipeline — from recruitment marketing through to a functioning clinician seeing patients — has three sequential bottlenecks, each of which must be cleared before the next stage can function:

1. **Recruitment funnel blocked** — Marketing campaigns cannot launch without a functional careers page (blocked by Roy Shur's form testing). No campaigns means no applicant flow. Google UK campaigns face additional approval delays.

2. **Onboarding activation blocked** — Even after hiring, new clinicians cannot see patients without Teams and HoViD access provisioned on day one. Technology setup is a hard binary blocker — there is no partial functionality.

3. **Retention undermined** — Current staff dissatisfaction (documented by Rivi Idelman) means existing employees are actively discouraging new applicants. Staff satisfaction data is too sparse to even diagnose the problem (2 responses per ~200 patients for some doctors).

These three bottlenecks are sequential: fixing recruitment without fixing onboarding produces hires who cannot work; fixing onboarding without fixing retention produces clinicians who leave or discourage others from joining.

## Evidence

- Careers page delay: Dekkel expressed frustration at 2026-02-15 meeting; page ready but form untested
- Technology blocker: Four separate onboarding discussion notes from 2026-02-12 all identify this as the single non-negotiable
- Staff satisfaction: Adi Lavi reported at 2026-02-15 meeting that staff told prospective applicants not to work at the clinic
- Survey data: Only ~16 surveys sent total, making satisfaction measurement impossible

## Implications

- The clinic cannot simply "hire more people" to close the capacity gap — three prerequisite conditions must be met first
- Each bottleneck has a different owner and timeline, requiring coordinated parallel resolution
- The 176-hire target for reaching 7,000+ patients assumes all three bottlenecks are cleared — any one remaining creates a ceiling
- Investment in downstream capacity (more psychiatrist slots) is wasted if upstream recruitment and onboarding pipelines are blocked

## Applicability

Directly applicable to Telia'z Clinic Israel scaling strategy. Also relevant to any future clinic expansion (UK, other markets) where the same three-stage pipeline will need to be built.