---
alfred_tags:
- ai/diagnostic-paper/review
- methodology-results
created: '2026-02-25'
description: Meeting notes covering the multi-agent AI diagnostic pipeline methodology,
  paper structure decisions, timing data analysis, and the discovery of psychiatrist
  PTSD diagnostic bias in post-war context.
janitor_note: LINK001 — Fixed [[person/Dekkel Khouri]] → [[person/Dekkel Taliaz]]
  in related. Telia'z wikilinks are valid (YAML escaping false positive). Base view
  embed (related.base#All) references _bases/related.base which does not exist — create
  it to enable dynamic views.
name: AI Diagnostic Paper Research Meeting Notes 2026-02-22
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
- '[[person/Shmulik]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[decision/Split AI Research Into Two Papers]]'
- '[[synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM Priming]]'
- '[[task/Clean Outliers From Time-to-Treatment Data]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[task/Investigate Sample Size Discrepancy Between Excel Files]]'
relationships:
- confidence: 0.85
  context: Meeting notes same date/topic
  source: note/AI Diagnostic Paper Research Meeting Notes 2026-02-22.md
  target: note/AI Diagnostic Paper Review Meeting Notes 2026-02-22.md
  type: related-to
- confidence: 0.95
  context: Meeting notes are part of meeting
  source: note/AI Diagnostic Paper Research Meeting Notes 2026-02-22.md
  target: note/AI Diagnostic Paper Research Meeting 2026-02-22.md
  type: part-of
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Diagnostic Paper Research Meeting Notes 2026-02-22

## Context

Research meeting between Rami Khouri, Dekkel Khouri, and Noam to review the methodology and results for the Telia'z AI-assisted psychiatric diagnostic paper. The discussion covered the full diagnostic pipeline, timing data issues, and a significant finding about psychiatrist diagnostic bias.

## Multi-Agent Diagnostic Pipeline

Rami presented the complete AI diagnostic methodology, structured as a pipeline of agents:

### Data Sources
1. **Questionnaire (S1)** — Structured extraction using algorithmic rules (no LLM). The questionnaire primarily covers depression, anxiety, and PTSD symptoms. It is known upfront to be a weak predictive tool as it does not cover the full DSM spectrum.
2. **Case Manager Transcript** — Initially attempted without LLM (strict/rule-based), then upgraded to LLM-based extraction for better symptom capture. Case managers ask DSM-oriented follow-up questions, providing richer diagnostic signal.
3. **Case Manager Notes** — Separate data source from the transcript.

### Prediction Stages
1. **Per-source prediction** — Each data source (questionnaire, transcript, notes) is evaluated independently for diagnostic prediction.
2. **Fusion** — Initially attempted a non-LLM fusion that simply picked one diagnosis without truly combining sources. This was abandoned.
3. **LLM-based Fusion** — A language model sees outputs from all three sources and produces an integrated diagnosis.
4. **Expert Agent** — The fusion model is prompted as a "psychiatrist" using DSM reasoning. This improved diagnostic accuracy. Notably, symptoms like insomnia are kept general (not attributed to a specific disorder) and grouped with related symptoms contextually.
5. **Biased Agent** — The expert agent is additionally given contextual priming (e.g., "you are a psychiatrist in a post-war context"). This replicates the same diagnostic bias observed in human psychiatrists.

### Key Finding: Psychiatrist PTSD Bias
When the Expert Agent (no context) analyzed symptoms using pure DSM criteria, it frequently diagnosed depression (MDD) rather than PTSD, because the available symptom criteria better matched depression. However, actual psychiatrists who met patients face-to-face predominantly diagnosed PTSD.

When the Biased Agent was given the post-war context, it began tagging ambiguous symptoms (e.g., insomnia) as trauma-related rather than depression-related, producing PTSD diagnoses that matched the human psychiatrists' diagnoses more closely.

This suggests psychiatrists carry a contextual bias — diagnosing PTSD based on the setting/population rather than strictly on DSM symptom criteria. Rami noted this could be a standalone anthropological/clinical paper.

## Timing Data Analysis

### Current Median Timing (from new dataset)
- Time to case manager: **median 8 days** (mean much higher due to outliers)
- Time to psychiatrist: **median 16 days** (8 days to case manager + 8 more)
- These medians are roughly half the means, indicating significant right-skew from outliers

### Data Quality Issues
- New dataset contains 6,041 records vs ~5,700 in previous export for the same date range (Dec 2023 — Aug 2025). Discrepancy needs investigation.
- ~25% of records missing case manager timing data; percentage increases for psychiatrist timing.
- Extreme outliers: some patients showing 170, 300+ days — likely technical errors (patients not properly closed in system).
- Rami analyzed only ~3,000 records in his AI pipeline work.

### Outlier Handling Decision
Agreed to remove outliers beyond 2.5 standard deviations from mean and report medians rather than means.

## Summary Approval Time — Real-Time vs Transcript Mode

Two operational periods exist:
1. **Transcript mode (earlier)**: After session ended, AI generated a summary in Google Docs. Psychiatrist opened it later (sometimes days later) to review and approve. The time-to-approve metric here includes idle waiting time, not actual editing time.
2. **Real-time mode (current)**: During the last 2 minutes of the session, the psychiatrist clicks "generate summary," a popup appears, they edit and send immediately. Approval happens within minutes, often before the session formally ends.

Rami requested Shmulik provide timing data segmented into 8 categories: intake/follow-up × 30min/20min × transcript/real-time. This enables:
- Before/after comparison of real-time vs transcript mode
- Comparison against literature (which reports ~10 min for paperwork)
- Demonstration that real-time mode reduces editing to ~1 minute

## Paper Structure Decision

Dekkel proposed splitting the work into two papers:
1. **Paper 1 (current)**: Methodology paper — the diagnostic extraction pipeline, basic clinical results (demographics, timing data), and per-source prediction accuracy (questionnaire alone, case manager alone, notes alone). No fusion or bias analysis.
2. **Paper 2 (future)**: Bias analysis paper — the fusion methodology, expert agent, biased agent, PTSD bias discovery, and anthropological/clinical implications. References Paper 1 as the foundation.

Rationale: The methods section is already very heavy. Adding the bias analysis would make the paper overwhelmingly method-focused. The bias finding tells "a different story" and deserves its own paper.

## Questionnaire Validation Connection

Rami mentioned earlier analysis showing the questionnaire correlated with PHQ (depression scale) but not with PCL (PTSD scale). This supports the bias finding: patients were being treated for PTSD, but their questionnaire data actually aligned with depression symptoms. Dekkel found this "amazing" and complementary to the bias analysis — further evidence that diagnoses were context-driven rather than symptom-driven.

## IRB Compliance Note

The IRB approval specified approximately 3-5 days wait time for patients. Actual timing data shows median of 8 days to case manager and 16 days to psychiatrist. Noam flagged this discrepancy warrants awareness, though the analysis inclusion criteria (up to Aug 31, 2025) match the IRB date range.

## Related
![[related.base#All]]