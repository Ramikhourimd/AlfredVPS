---
alfred_tags:
- ai/clinical-summaries
- quality-assumptions
- research-study
based_on:
- '[[note/Patient Data Research and AI Summary Quality Discussion 2025-11-11]]'
confidence: high
created: '2026-03-08'
janitor_note: LINK001 — Telia'z wikilinks use YAML single-quote escaping — all targets
  verified to exist (project/Telia'z AI Diagnostic Research Paper, constraint/AI-Generated
  Clinical Summaries Require Psychiatrist Approval Before Patient Record Entry). False
  positives, no fix needed.
name: AI Summary System Excluded Case Manager Intake Data During Study Period
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval Before
  Patient Record Entry]]'
- '[[decision/Measure Summary Approval Time Not Generation Time]]'
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
relationships:
- confidence: 0.7
  context: Assumptions on data handling and quality fixes
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Gold Standard Example Will Fix AI Summary Quality.md
  type: related-to
- confidence: 0.6
  context: Assumptions impacting study session data
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Psychiatrists Naturally Compress Session Duration Below Scheduled
    Time.md
  type: related-to
- confidence: 0.65
  context: Data exclusion affects real-time approval
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  type: related-to
- confidence: 0.75
  context: Study period data separation assumptions
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  type: related-to
- confidence: 0.75
  context: Assumptions on clean data boundaries
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  type: related-to
- confidence: 0.85
  context: Both address AI summary quality issues
  source: assumption/AI Summary System Excluded Case Manager Intake Data During Study
    Period.md
  target: assumption/Single Representative Example Sufficient to Resolve AI Summary
    Quality Issues.md
  type: related-to
source: Rami Khouri, reported in 2025-11-11 meeting with Rivi Idelman
source_date: '2025-11-11'
status: active
type: assumption
---

# AI Summary System Excluded Case Manager Intake Data During Study Period

## Claim

During at least part of the research study period, the AI clinical summary system generated post-session summaries based only on the psychiatrist session, ignoring the extensive case manager intake interview data (developmental history, symptom timeline, life events). This means the summaries psychiatrists reviewed and approved — whose approval time is a key paper metric — were incomplete representations of the patient's clinical picture.

## Basis

In the 2025-11-11 meeting between Rami Khouri and Rivi Idelman, Rami identified this as a "critical gap" in the AI summaries. A remediation plan was discussed: a psychiatrist would provide a gold-standard example of what a complete summary should include, which would then be used to update the AI prompt.

## Evidence Trail

- 2025-11-11: Gap identified; psychiatrists complaining about summary quality in WhatsApp group
- 2025-11-11: Remediation plan initiated (gold-standard example from psychiatrist)
- Status of fix unknown — if unresolved during study period, summary approval times reflect approval of incomplete summaries

## Impact

- Summary approval time metrics in the paper may reflect time to approve incomplete summaries, not comprehensive ones
- The transition from transcript-based to real-time summary generation may have occurred while this data gap still existed
- If the gap was fixed mid-study, approval time comparisons across periods may conflate two variables (mode change + content completeness change)