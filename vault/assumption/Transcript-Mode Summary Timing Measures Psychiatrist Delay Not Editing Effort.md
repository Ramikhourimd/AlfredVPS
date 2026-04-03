---
alfred_tags:
- ai/summary-mode-switch
- clinic/workflow-transition
- transcript-vs-real-time
based_on:
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
confidence: high
created: '2026-02-22'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference missing
  _bases/learn-assumption.base — vault-wide infrastructure gap, embeds preserved per
  policy. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z
  AI Diagnostic Research Paper or related decision records.'
name: Transcript-Mode Summary Timing Measures Psychiatrist Delay Not Editing Effort
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
- '[[decision/Measure Summary Approval Time Not Generation Time]]'
- '[[decision/Segment Summary Approval Time Analysis Into Eight Categories]]'
- '[[assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After Boundary]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.7
  context: Timing informs mode switch boundary
  source: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  target: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  type: related-to
- confidence: 0.75
  context: Clarifies transcript-mode baseline measurement
  source: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  target: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  type: supports
- confidence: 0.7
  context: Clean transcript timing aids separability
  source: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  target: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  type: supports
source: Rami Khouri — operational analysis of summary approval workflow
source_date: '2026-02-22'
status: active
type: assumption
---

# Transcript-Mode Summary Timing Measures Psychiatrist Delay Not Editing Effort

## Claim

In the transcript-based (pre-change) summary workflow, the time between AI summary generation and psychiatrist approval does NOT measure how long the psychiatrist spent reviewing or editing the summary. It measures how long the psychiatrist took to open the document at all. Summaries were auto-generated after sessions ended, then sat in Google Docs until the psychiatrist chose to review them — sometimes hours or days later. This makes transcript-mode approval timing invalid as a measure of AI summary editing effort or clinical utility.

## Basis

Rami Khouri described the two distinct workflows during the 2026-02-22 meeting:
- **Transcript mode**: Session ends → AI auto-generates summary → psychiatrist opens it later (hours/days) → reviews and sends. The elapsed time captures scheduling delay, not editing time.
- **Real-time mode**: During last 2 minutes of session → psychiatrist clicks "generate" → reviews popup → edits → sends before session ends. This elapsed time captures actual editing effort.

## Evidence Trail

- 2026-02-22: Rami explained this distinction when discussing how to present summary approval time data. The team agreed this means transcript-mode and real-time-mode timing data cannot be directly compared as measures of the same thing.

## Impact

- Paper 1 must clearly distinguish between the two measurement periods when presenting summary approval time
- Transcript-mode timing can demonstrate the "before" state (long delays) but not editing effort
- Real-time mode timing is the valid measure for AI clinical utility claims
- This distinction affects how the 8-category timing breakdown should be interpreted

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]