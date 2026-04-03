---
alfred_tags:
- psychiatry/ai-evaluation
- constraints/ground-truth
authority: Telia'z Clinic clinical governance
created: '2026-03-07'
janitor_note: LINK001 — Telia'z wikilink (project/Telia'z AI Diagnostic Research Paper)
  is valid (YAML apostrophe escaping false positive). ORPHAN001 — no inbound wikilinks;
  decision records link to this constraint, may gain inbound links naturally.
name: AI-Generated Clinical Summaries Require Psychiatrist Approval Before Patient
  Record Entry
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Use Summary Approval Time as Clinical Efficiency Metric]]'
- '[[decision/Measure Summary Approval Time Not Generation Time]]'
- '[[decision/Measure Summary Approval as Delta From Session End]]'
- '[[decision/Segment Summary Approval Time Analysis Into Eight Categories]]'
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
relationships:
- confidence: 0.8
  context: Approval depends on absent gold std
  source: constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval
    Before Patient Record Entry.md
  target: constraint/No Gold Standard Reference Exists for AI Clinical Summary Evaluation.md
  type: depends-on
- confidence: 0.6
  context: Shared psychiatrist process concerns
  source: constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval
    Before Patient Record Entry.md
  target: constraint/Psychiatrist AI Feedback Collected Through Informal WhatsApp
    Channel.md
  type: related-to
- confidence: 0.85
  context: Approval depends on biased edits
  source: constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval
    Before Patient Record Entry.md
  target: constraint/Psychiatrist Edits Biased by AI Model Received.md
  type: depends-on
- confidence: 0.85
  context: Approval depends on biased edits
  source: constraint/AI-Generated Clinical Summaries Require Psychiatrist Approval
    Before Patient Record Entry.md
  target: constraint/Psychiatrist Edits Biased by AI Output They Received.md
  type: depends-on
source: Clinical workflow policy at Telia'z Clinic
status: active
type: constraint
---

# AI-Generated Clinical Summaries Require Psychiatrist Approval Before Patient Record Entry

## Constraint

AI-generated clinical summaries — whether produced from transcripts (post-session) or in real-time (during session) — must be reviewed and approved by the treating psychiatrist before they become part of the official patient record. No AI output enters the clinical record without human approval.

## Source

Clinical workflow policy at [[org/Telia'z]] clinic. This is a standard clinical governance requirement ensuring that AI-assisted documentation does not bypass clinician accountability.

## Implications

- The approval step creates a measurable time delta (session end → approval) that serves as the primary efficiency metric in the research paper
- Even in real-time mode where summaries are generated during the session, the approval timestamp is what matters — not generation time
- This constraint is what makes "summary approval time" a meaningful clinical efficiency metric rather than a pure technical benchmark
- The constraint drives the entire 8-category timing analysis (intake/follow-up × 20/30min × transcript/real-time)
- Removing this constraint (auto-approval) would eliminate the key efficiency metric but raise significant clinical governance concerns

## Expiry / Review

This constraint is unlikely to expire as it reflects fundamental clinical governance principles. It may evolve if regulatory frameworks establish standards for AI-generated clinical documentation that allow reduced oversight.