---
alfred_tags:
- ai/diagnostic-paper/review
- methodology-results
created: '2026-02-25'
description: Detailed meeting notes from the research paper review covering multi-agent
  diagnostic pipeline methodology, timing data analysis, data quality issues, and
  decision to split the paper into two publications.
janitor_note: '"LINK001 false positives: Telia''z wikilinks use YAML escaping (double
  single-quotes); org/Telia''z.md, project/Telia''z Clinic Israel.md, and project/Telia''z
  AI Diagnostic Research Paper.md all exist. LINK001 fix applied: [[person/Dekkel
  Khouri]] corrected to [[person/Dekkel Taliaz]] (verified person/Dekkel Taliaz.md
  exists). Base view embed \![[related.base#All]] preserved per policy (_bases/ directory
  not present)."'
name: AI Diagnostic Paper Review Meeting Notes 2026-02-22
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Review Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Noam]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Shmulik]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[org/Telia''z]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Diagnostic Paper Review Meeting Notes 2026-02-22

## Context

Meeting between Rami, Noam, and Dekkel to review the combined method document for the AI diagnostic research paper. Noam had compiled all previously sent materials into one document. The discussion covered methodology figures, multi-agent pipeline design, timing data quality, and paper scope decisions.

## 1. Method Document Status

Noam compiled all materials Rami had previously sent into a single document containing:
- **Method section** — overview of the diagnostic process
- **Analysis section** — detailed description of how the analysis is performed (the most recent document Rami sent)
- **Results section** — diagnostic prediction outcomes

Missing element: the calculation method for percentages needs to be documented.

The method section figure currently only covers the **extraction stage** (raw data to structured data / symptom extraction). A figure for the **prediction stage** (record analysis) is still needed — likely resulting in 3 total figures.

## 2. Multi-Agent Diagnostic Pipeline (Rami's Methodology)

The pipeline has two major stages:

### Stage 1: Symptom Extraction
- **From questionnaire:** Algorithmic extraction (no LLM needed) — structured, clear rules
- **From case manager transcript:** Initially tried without LLM (very strict, limited), then used LLM to extract richer symptom data

### Stage 2: Diagnostic Prediction — Five Agent Levels

| Agent | Input | Approach |
|-------|-------|----------|
| **S1 (Questionnaire-only)** | Questionnaire symptoms | Limited to depression, anxiety, PTSD — questionnaire doesn't cover full DSM spectrum |
| **S2 (Transcript-only)** | Case manager transcript | Case managers ask DSM-style follow-up questions, so better predictive power |
| **S3 (Fusion)** | Both sources combined | LLM-based fusion — model sees outputs from both questionnaire and transcript, combines them to produce diagnosis. Earlier non-LLM fusion failed (model just picked one source, didn't truly fuse) |
| **S4 (Expert)** | Fusion output | LLM prompted as "psychiatrist" — uses DSM criteria strictly. Tended to diagnose **depression (MDD)** because there were more depression criteria in the data |
| **S5 (Biased Expert)** | Fusion output + context | LLM prompted as "post-war psychiatrist" — with contextual priming, the model made the **same PTSD over-diagnosis** as real psychiatrists |

### Key Finding: Diagnostic Bias Replication

When the LLM expert is given no context beyond DSM criteria, it diagnoses MDD (depression) based on available symptom criteria. But real psychiatrists diagnosed PTSD — likely because they have **contextual bias** (post-war setting, knowledge of patient background).

When the LLM is given the same context ("you are a psychiatrist in a post-war setting"), it replicates the same PTSD bias. This raises a fundamental question: **Is the DSM truly a diagnostic tool, or do psychiatrists diagnose based on context rather than strict criteria?**

Example: A patient reports insomnia. The unbiased expert agent classifies it as generic insomnia and groups it with related symptoms (e.g., anhedonia → depression cluster). The biased expert agent, with war context, immediately tags the insomnia as "trauma-related insomnia" and routes to PTSD diagnosis.

Dekkel's explanation: If you take the textbook strictly, many diagnoses should be depression, not PTSD. Adding environmental context (not patient-specific, but setting-level) produces the same diagnostic pattern as real psychiatrists — suggesting systemic bias.

## 3. Paper Scope Decision

**Agreed: Split into two papers.**

**Paper 1 (current):** Methodology + basic clinical results
- Method: Symptom extraction from questionnaire and case manager transcript
- Results: Individual prediction accuracy for questionnaire-only and transcript-only agents
- Clinical data: Wait times, demographics, workflow metrics
- PHQ correlation data (supports the bias finding from another angle — PHQ matched depression, not PCL/PTSD)
- No fusion or bias analysis

**Paper 2 (future):** Bias analysis + fusion methodology
- Full multi-agent fusion pipeline
- Expert and biased expert agent comparison
- PTSD vs MDD diagnostic bias analysis
- Anthropological/philosophical discussion on DSM as diagnostic tool
- Rami noted this methodology is novel — built on MDP-based symptom framework, adapted to DSM

## 4. Timing Data Analysis

### Wait Time Results (from Shmulik's latest data export)
- **Time to case manager:** Mean ~2 weeks, **Median 8 days**
- **Time to psychiatrist:** Mean 25 days, **Median 16 days** (8 days case manager + 8 days to psychiatrist)
- IRB submission stated ~3-5 days — actual times are significantly longer

### Data Quality Issues
- **Outliers:** Some patients show 150-388 days wait time — clearly erroneous (likely patients left in waiting status, technical errors)
- **Agreed approach:** Remove outliers beyond **2.5 standard deviations** from mean
- **Report median, not mean** due to high variance / skewed distribution
- ~25-30% of records have no timing data for case manager or psychiatrist visits

### Sample Size Discrepancy
- Previous Excel export: ~5,700 patients
- Latest export (same date range, Dec 2023 - Aug 2025): 6,041 patients
- Noam flagged this — needs investigation to ensure analyses run on consistent data
- Rami analyzed only ~3,000 for his AI pipeline work

## 5. Summary Approval Time (Real-Time vs Transcript)

Two operational periods:
- **Before change (transcript mode):** Session ends → summary auto-generated → psychiatrist reviews later (sometimes days)
- **After change (real-time mode):** During session's last 2 minutes, psychiatrist clicks "generate summary" → popup appears → edits and sends immediately

**Key metric to present:** Time from session end to approval (not generate-to-approve, since pre-change generation was automatic and psychiatrist didn't open it immediately)

**Proposed data structure:** 8 columns — Intake 30min transcript, Intake 30min real-time, Intake 20min transcript, Intake 20min real-time, Follow-up 30min transcript, Follow-up 30min real-time, Follow-up 20min transcript, Follow-up 20min real-time

**Literature comparison:** Published research reports ~10 minutes for clinical paperwork/summary editing. Real-time mode brings this down to approximately 1 minute.

For the transcript period, an alternative metric could be extracted from Google Drive (modified_by timestamp on Google Docs) to estimate actual editing time — but accuracy is questionable and may not add enough value.

## 6. Open Questions

- Why does the latest data export have more records than the previous one for the same date range?
- What is the exact cutoff date for the real-time vs transcript-mode change?
- Should the Google Drive editing time metric be pursued or is it not worth the effort?
- How to properly report the PHQ/PCL validation data to support the bias narrative without front-loading Paper 2's story?

## Related
![[related.base#All]]