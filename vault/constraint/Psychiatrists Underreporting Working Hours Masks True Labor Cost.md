---
alfred_tags:
- operations/unreported-hours
- clinic/psychiatrists
- finance/labor-costs
authority: Internal operational reality
created: '2026-02-18'
janitor_note: LINK001 wikilinks to Telia'z records are valid (YAML double-quote escaping).
  Base view embeds (learn-constraint.base) reference missing _bases/ files — vault-wide
  infrastructure gap, not a per-file fix. ORPHAN001 low-risk for active constraint.
  No fix needed; all links resolve correctly.
name: Psychiatrists Underreporting Working Hours Masks True Labor Cost
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Employee Experience Research Methodology and System Prototype Meeting
  2026-02-18]]'
- '[[note/Employee Experience Research and System Prototype Meeting 2026-02-18]]'
- '[[person/Rivi Idelman]]'
- '[[assumption/Psychiatrists Staying at Telia''z Primarily for Convenience Not Engagement]]'
relationships:
- confidence: 0.9
  context: Extra hours explain underreporting & cost masking
  source: constraint/Psychiatrists Underreporting Working Hours Masks True Labor Cost.md
  target: constraint/Psychiatrists Working Unreported Extra Hours Beyond Scheduled
    Sessions.md
  type: supports
- confidence: 0.8
  context: Psychiatrist underreporting and staff unreported hours
  source: constraint/Psychiatrists Underreporting Working Hours Masks True Labor Cost.md
  target: constraint/Staff Report Unreported Extra Hours Beyond Scheduled Sessions.md
  type: related-to
- confidence: 0.92
  context: Underreporting due to extra unreported hours
  source: constraint/Psychiatrists Underreporting Working Hours Masks True Labor Cost.md
  target: constraint/Psychiatrists Working Unreported Extra Hours Outside Scheduled
    Sessions.md
  type: related-to
source: Staff self-reports via Rivi Idelman interviews
source_date: '2026-02-18'
status: active
type: constraint
---

# Psychiatrists Underreporting Working Hours Masks True Labor Cost

## Constraint

Psychiatrists at Telia'z Clinic Israel routinely work unreported extra hours — preparation before shifts, post-session summary review and rewriting, case research on complex patients. They have stopped reporting these hours because they know it will trigger efficiency questions from management. This creates a systematic undercount of the true labor cost per session and masks the actual time burden of remote clinical work.

## Source

Rivi Idelman's qualitative staff interviews, reported during 2026-02-18 meeting with Rami. Multiple psychiatrists confirmed this pattern. Case managers also work extra hours on summaries but face less pushback on reporting them.

## Implications

- Financial models based on reported hours underestimate the true cost per session
- Burnout metrics based on reported hours underestimate actual workload
- AI summary quality improvements could partially address this (reducing rewriting time)
- Any efficiency analysis using current reported hours is based on incomplete data
- The culture of non-reporting could indicate broader trust/transparency issues

## Expiry / Review

Should be reassessed after AI summary quality improves and after employee satisfaction survey instrument is deployed to measure actual vs. reported hours.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]