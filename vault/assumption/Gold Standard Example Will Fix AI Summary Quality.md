---
alfred_tags:
- ai/clinical-summaries
- quality-assumptions
- research-study
based_on:
- '[[task/Obtain Gold Standard AI Session Summary Example]]'
confidence: low
created: '2026-02-26'
janitor_note: LINK001 — Telia'z Innovation Program wikilink resolves correctly (YAML
  escaping false positive). Base view embeds (\![[learn-assumption.base#Depends On
  This]], \![[learn-assumption.base#Related]]) reference _bases/learn-assumption.base
  which does not exist — create base file to enable dynamic views.
name: Gold Standard Example Will Fix AI Summary Quality
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[person/Rivi Idelman]]'
- '[[note/Rivi Edelman Account Snapshot February 2026]]'
relationships:
- confidence: 0.6
  context: Quality fixes and session timing factors
  source: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  target: assumption/Psychiatrists Naturally Compress Session Duration Below Scheduled
    Time.md
  type: related-to
- confidence: 0.8
  context: Quality fix addresses low real-time approval
  source: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  target: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  type: related-to
- confidence: 0.7
  context: Quality improvement via separable periods
  source: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  target: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  type: related-to
- confidence: 0.7
  context: Quality relies on clean mode switch
  source: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  target: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  type: related-to
- confidence: 0.9
  context: Similar example-based fixes for quality
  source: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  target: assumption/Single Representative Example Sufficient to Resolve AI Summary
    Quality Issues.md
  type: related-to
source: Nov 2025 discussion about AI summary quality
source_date: '2025-11-01'
status: active
type: assumption
---

# Gold Standard Example Will Fix AI Summary Quality

## Claim

Obtaining a single gold-standard AI post-session summary example from a senior psychiatrist (Ahmad or Uriel) will provide sufficient reference material to fix the prompt engineering issues causing AI summaries to ignore intake data.

## Basis

The current AI clinical summaries ignore intake data, producing incomplete post-session records. The proposed fix is to collect what a good summary should look like from a senior clinician and use that to update the AI prompts. This assumes the problem is primarily a prompt engineering issue solvable with better reference material.

## Evidence Trail

- Nov 2025: Task created to obtain gold standard example
- Feb 2026: Task still outstanding — no example collected after ~3 months
- Feb 2026: Account snapshot confirms this remains an active workstream

## Impact

If this assumption is wrong — e.g., if the problem is deeper than prompt engineering (data pipeline issues, model limitations, structured data integration challenges) — the team may invest time collecting and implementing the example only to find the summaries still fall short. The 3-month delay in obtaining even one example may itself signal that senior psychiatrists find this harder to produce than expected.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]