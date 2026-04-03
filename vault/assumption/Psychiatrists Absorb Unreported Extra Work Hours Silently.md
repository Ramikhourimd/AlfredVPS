---
alfred_tags:
- telepsychiatry/workload
- staff/sustainability
- burnout/thresholds
based_on:
- '[[note/Employee Experience Research and System Prototype Planning 2026-02-18]]'
confidence: high
created: '2026-02-18'
janitor_note: 'LINK001 — Teliaz wikilinks valid (YAML escaping false positive). conversation/Employee
  Experience Research Methodology and System Prototype Meeting 2026-02-18 wikilink
  valid (target file exists; scanner false positive, likely YAML multiline formatting).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference non-existent
  _bases/learn-assumption.base — embeds preserved, create base file to enable dynamic
  views. ORPHAN001 — no inbound links; consider linking from source records. Swept
  2026-03-11.'
name: Psychiatrists Absorb Unreported Extra Work Hours Silently
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Employee Experience Research Methodology and System Prototype Meeting
  2026-02-18]]'
- '[[person/Rivi Idelman]]'
- '[[constraint/Clinical Paperwork Literature Benchmark of 10 Minutes]]'
relationships:
- confidence: 0.95
  context: Silent extra work via underreporting
  source: assumption/Psychiatrists Absorb Unreported Extra Work Hours Silently.md
  target: assumption/Psychiatrists Underreport Working Hours to Avoid Scrutiny.md
  type: supports
- confidence: 0.55
  context: Extra work and shift optimization
  source: assumption/Psychiatrists Absorb Unreported Extra Work Hours Silently.md
  target: assumption/Shorter Concentrated Clinical Shifts Reduce Burnout More Than
    Distributed Hours.md
  type: related-to
- confidence: 0.85
  context: Extra hours contradict 6-8 threshold
  source: assumption/Psychiatrists Absorb Unreported Extra Work Hours Silently.md
  target: assumption/Six to Eight Weekly Hours Is Sustainable Threshold for Clinical
    Staff.md
  type: contradicts
- confidence: 0.8
  context: Extra hours contradict telepsych threshold
  source: assumption/Psychiatrists Absorb Unreported Extra Work Hours Silently.md
  target: assumption/Six to Eight Weekly Hours Is Sustainable Threshold for Telepsychiatry
    Clinicians.md
  type: contradicts
source: Multiple psychiatrist interviews via Rivi Idelman
source_date: '2026-02-18'
status: active
type: assumption
---

# Psychiatrists Absorb Unreported Extra Work Hours Silently

## Claim

Psychiatrists at Telia'z routinely work additional hours beyond their reported shifts (preparation before sessions, reviewing AI summaries, rewriting documentation) but have stopped reporting these hours because they know the company discourages overtime. This creates a hidden labor cost and a building resentment factor.

## Basis

Rivi Idelman reported from multiple psychiatrist interviews that this is a widespread pattern. Psychiatrists spend time before sessions reviewing complex cases, and after sessions editing summaries that the AI system does not produce to satisfactory quality. They know reporting these hours will invite questions, so they absorb the cost silently.

## Evidence Trail

- 2026-02-18: Rivi reports pattern from staff interviews
- Correlates with known AI summary quality issues (see synthesis: AI Clinical Summary Quality Gap)
- Case managers are less affected as their overtime is still within reportable range

## Impact

- True labor cost per session is higher than reported metrics suggest
- Compensation calculations may be systematically underpaying for actual work
- Improving AI summary quality would directly reduce unreported hours
- Risk of sudden departures when resentment reaches a tipping point

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]