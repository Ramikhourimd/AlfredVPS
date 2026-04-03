---
alfred_tags:
- ai/summary-mode-switch
- clinic/workflow-transition
- transcript-vs-real-time
based_on:
- '[[decision/Use Median With Outlier Cleaning for Timing Data]]'
confidence: high
created: '2026-02-25'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Body has DUPLICATE heading (# Real-Time Summary Mode Reduces Approval to Near Zero
  appears twice consecutively) — requires manual removal, CLI does not support body
  edits.
name: Real-Time Summary Mode Reduces Approval to Near Zero
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[person/Rami Khouri]]'
- '[[task/Obtain Approval Time Data by Session Type]]'
relationships:
- confidence: 0.8
  context: Low approval relies on period separability
  source: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  target: assumption/Transcript and Real-Time Operational Periods Are Cleanly Separable.md
  type: depends-on
- confidence: 0.75
  context: Low approval relies on clean switch
  source: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  target: assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After
    Boundary.md
  type: depends-on
- confidence: 0.6
  context: Shared summary mode performance metrics
  source: assumption/Real-Time Summary Mode Reduces Approval to Near Zero.md
  target: assumption/Transcript-Mode Summary Timing Measures Psychiatrist Delay Not
    Editing Effort.md
  type: related-to
source: Rami Khouri observation from operational data
source_date: '2026-02-22'
status: active
type: assumption
---

# Real-Time Summary Mode Reduces Approval to Near Zero

# Real-Time Summary Mode Reduces Approval to Near Zero

## Claim

After switching from transcript-based (post-session) summary generation to real-time (in-session) summary generation, the time from session end to psychiatrist summary approval dropped to effectively zero or negative values (summary sent before session formally ends). Literature benchmarks approximately 10 minutes for clinical paperwork.

## Basis

Operational observation by Rami Khouri. In real-time mode, the psychiatrist clicks Generate Summary during the last 2 minutes of the session, reviews a popup, edits minimally, and sends before the session ends. This replaces the previous workflow where summaries were auto-generated post-session and psychiatrists opened them hours or days later via Google Docs.

## Evidence Trail

Pending formal data analysis. Rami requested an 8-column timing breakdown from Shmulik to quantify the difference between transcript mode and real-time mode across session types (intake/follow-up x 30min/20min).

## Impact

If confirmed, this demonstrates that AI-assisted real-time summarization reduces clinical paperwork burden from approximately 10 minutes (literature standard) to approximately 1 minute of editing. This is a key result for Paper 1.