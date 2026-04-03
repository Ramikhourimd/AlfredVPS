---
alfred_tags:
- ai/summary-mode-switch
- clinic/workflow-transition
- transcript-vs-real-time
based_on:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[task/Obtain Approval Time Data by Session Type]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-27'
invalidated_by: []
janitor_note: 'LINK001: project wikilink [[project/Telia''z AI Diagnostic Research
  Paper]] uses YAML apostrophe escaping (Telia''''z) which is valid, not broken.'
name: Transcript-to-Real-Time Mode Switch Creates Clean Before-After Boundary
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
- '[[decision/Use Summary Approval Time as Clinical Efficiency Metric]]'
relationships:
- confidence: 0.9
  context: Switch supports separability of periods
  source: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  target: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  type: supports
- confidence: 0.85
  context: Clean switch enables real-time low approval
  source: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  target: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  type: supports
- confidence: 0.7
  context: Sequential transcript-to-realtime modes
  source: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  target: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  type: related-to
source: Implied across task and conversation records about timing analysis
source_date: '2026-02-22'
status: active
type: assumption
---

# Transcript-to-Real-Time Mode Switch Creates Clean Before-After Boundary

## Claim

The Telia'z clinic system transitioned from transcript-based (post-session) summary generation to real-time summary generation at a specific point in time. The paper's timing analysis assumes this transition created two distinct operational periods that can be cleanly compared as a before/after natural experiment.

## Basis

Multiple task records request timing data segmented by "transcript mode" vs "real-time mode," implying these are two non-overlapping operational periods. The 8-category timing segmentation (intake/follow-up × 20/30min × transcript/real-time) depends on each session belonging clearly to one mode or the other.

## Evidence Trail

- 2026-02-22: Task records consistently reference "pre-change" and "post-change" periods for real-time implementation
- The request for 8-column segmentation assumes clean mode assignment per session

## Impact

If the transition was gradual, overlapping, or inconsistent across session types, the before/after comparison would be confounded. The paper's efficiency claims about real-time mode depend on this being a clean boundary. The team should verify the exact switchover date and confirm no sessions operated in a mixed mode.