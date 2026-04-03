---
alfred_tags:
- clinic/scaling
- psychiatrist/management
- operations/structures
approved_by: []
based_on:
- '[[assumption/Clinic Growth Trajectory Targets 7000 Plus Patients]]'
challenged_by: []
confidence: high
created: '2025-07-14'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Alex Taliaz]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Oren Taliaz]]'
janitor_note: 'LINK001: Telia''z wikilink is false positive (YAML escaping). Base
  view embeds reference non-existent _bases/learn-decision.base — vault-wide gap,
  embeds preserved. BODY-FIX NEEDED: duplicate base view embeds after --- separator
  at end of file — remove the duplicated block manually (CLI cannot edit body content).'
name: Psychiatrist Residency Pipeline Recruitment Model
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Rami Shira Management Meeting 2025-07-14]]'
- '[[note/Rami Shira Management Meeting Notes 2025-07-14]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[decision/Clinical Compensation Target 35 to 50 Percent of Revenue]]'
relationships:
- confidence: 0.9
  context: Provides psychs for intake exams
  source: decision/Psychiatrist Residency Pipeline Recruitment Model.md
  target: decision/Formal Patient Discharge Requires Completed Psychiatry Intake Examination.md
  type: supports
- confidence: 0.7
  context: Recruitment enables UK workflow
  source: decision/Psychiatrist Residency Pipeline Recruitment Model.md
  target: decision/Replicate Israel Three-Step Clinical Workflow for UK.md
  type: supports
- confidence: 0.75
  context: Staffing pipeline for district clinics
  source: decision/Psychiatrist Residency Pipeline Recruitment Model.md
  target: decision/Adopt District Model for Clinic Israel.md
  type: supports
session: null
source: Rami Khouri, Rami-Shira management meeting 2025-07-14
source_date: '2025-07-14'
status: final
supports:
- '[[task/Build Psychiatry Academy Digital Platform]]'
- '[[task/Launch Psychiatry Academy First Cohort]]'
tags: []
type: decision
---

# Psychiatrist Residency Pipeline Recruitment Model

## Context

Telia'z faces a structural challenge: experienced psychiatrists command high rates (450+ NIS/hour) while the clinic needs to maintain average hourly costs around 340 NIS to sustain profitability. After the Maccabi transition reduced professional variety, experienced staff began leaving for better-paying alternatives. A sustainable recruitment model was needed.

## Options Considered

1. **Compete on salary for experienced specialists** — Unsustainable at scale; cost per hour too high for break-even
2. **Recruit only early-career psychiatrists** — Lower cost but no senior expertise for complex cases or tender credibility
3. **Residency pipeline with tiered compensation** — Recruit from year 1, provide training, graduate through pay tiers; mix with 20% specialists (chosen)

## Decision

Implement a three-tier recruitment pipeline aligned with psychiatry residency stages:

| Stage | Role | Compensation |
|-------|------|-------------|
| Year 1 (no hospital clearance) | Case Manager | 120 NIS/hour |
| Year 2+ (post-clearance, pre-Stage A) | Psychiatrist | 300 NIS/hour |
| Post-Stage A exam | Psychiatrist | 350 NIS/hour |
| Post-Stage B exam (specialist) | Psychiatrist | 450 NIS/hour |

Target team composition: maximum 20% post-Stage B specialists. Two recruitment campaigns: first-year residents and second-year residents. No recruitment of specialists or late-career psychiatrists.

## Rationale

The tiered model creates a self-sustaining talent pipeline: residents join cheaply as case managers, get trained (Psychiatry Academy), and progress to full psychiatrist roles. The blended average cost converges to ~340 NIS/hour, enabling break-even at 1M NIS monthly revenue. The 20% specialist cap preserves expertise for complex cases and tender credibility while controlling costs.

Previous experiment with residents Sofian and Hala failed due to insufficient support in year 1 — the Psychiatry Academy training tracks directly address this gap.

## Consequences

- Requires building a Psychiatry Academy with three training tracks by September 2025
- Need instructors, syllabus, and digital learning platform
- Recruitment messaging can immediately promote training as a differentiator
- Higher initial management overhead for junior staff
- 12-18 month lead time before year-1 recruits become revenue-generating psychiatrists
- Reduces dependency on expensive specialist recruitment

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]