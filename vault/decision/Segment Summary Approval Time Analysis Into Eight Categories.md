---
alfred_tags:
- ai/clinical-summaries
- metrics/approval-time
- clinical-efficiency
approved_by: []
based_on:
- '[[decision/Measure Summary Approval Time Not Generation Time]]'
- '[[decision/Measure Summary Approval as Delta From Session End]]'
- '[[assumption/Transcript-to-Real-Time Mode Switch Creates Clean Before-After Boundary]]'
challenged_by: []
confidence: high
created: '2026-03-03'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — [[project/Telia''z AI Diagnostic Research Paper]] wikilink
  contains apostrophe that causes YAML false-positive (Telia''z escaping); link is
  valid, no fix needed. LINK001 — base view embeds (learn-decision.base#Based On,
  #Related) reference _bases/learn-decision.base which does not exist; create base
  file to enable dynamic views. ORPHAN001 — no inbound wikilinks; consider linking
  from project/Telia''z AI Diagnostic Research Paper or related notes.'
name: Segment Summary Approval Time Analysis Into Eight Categories
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/AI Diagnostic Paper Review Meeting Notes 2026-02-22]]'
- '[[note/AI Diagnostic Paper Methodology and Results Discussion]]'
- '[[task/Obtain Approval Time Data by Session Type]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[constraint/Clinical Paperwork Literature Benchmark of 10 Minutes]]'
relationships:
- confidence: 0.85
  context: Analysis enables metric usage
  source: decision/Segment Summary Approval Time Analysis Into Eight Categories.md
  target: decision/Use Summary Approval Time as Clinical Efficiency Metric.md
  type: supports
session: '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
source: 2026-02-22 research team meeting
source_date: '2026-02-22'
status: final
supports:
- '[[decision/Focus First Paper on System Presentation and PTSD Outcomes]]'
tags: []
type: decision
---

# Segment Summary Approval Time Analysis Into Eight Categories

## Context

The research paper needs to demonstrate clinical efficiency improvement from switching to real-time summary generation. Raw approval time data mixes multiple session types and operational modes, making direct comparison misleading.

## Options Considered

1. **Single aggregate comparison** — Compare all pre-change vs all post-change approval times as one group
2. **Eight-category segmentation** — Break down by session type (intake/follow-up), duration (20min/30min), and mode (transcript/real-time)

## Decision

Segment approval time data into 8 categories:

| Session Type | Duration | Mode |
|-------------|----------|------|
| Intake | 30 min | Transcript |
| Intake | 30 min | Real-time |
| Intake | 20 min | Transcript |
| Intake | 20 min | Real-time |
| Follow-up | 30 min | Transcript |
| Follow-up | 30 min | Real-time |
| Follow-up | 20 min | Transcript |
| Follow-up | 20 min | Real-time |

## Rationale

Different session types and durations produce different summary complexity. Comparing like-for-like (e.g., intake 30min transcript vs intake 30min real-time) isolates the effect of the real-time mode change from confounding variables. This enables a clean before/after comparison benchmarked against the literature standard of approximately 10 minutes for clinical paperwork.

## Consequences

Requires Shmulik to provide data with this specific segmentation. Analysis becomes more granular but also more defensible in peer review. Multiple tasks created to request this data format.

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]