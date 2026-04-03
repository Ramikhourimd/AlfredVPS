---
alfred_instructions: This note is a complementary record to note/AI Diagnostic Paper
  Research Meeting Notes 2026-02-22.md, which is the canonical meeting summary.
alfred_tags:
- ai/diagnostic-paper/review
- methodology-results
created: '2026-02-22'
description: Meeting notes from research team discussion on the AI psychiatric diagnostic
  prediction paper. Covers multi-agent LLM pipeline methodology, diagnostic bias findings,
  time-to-treatment data analysis, and decision to split into two papers.
janitor_note: LINK001 — person/Dekkel Khouri fixed to person/Dekkel Taliaz. Base view
  embed (related.base#All) references _bases/related.base which does not exist — vault-wide
  infrastructure gap. Embeds preserved per policy.
name: AI Diagnostic Paper Methodology and Results Discussion
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
- '[[org/Telia''z]]'
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[decision/Split AI Research Into Two Papers]]'
- '[[synthesis/Psychiatrist PTSD Diagnostic Bias Replicated by Contextual LLM Priming]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[note/AI Diagnostic Paper Research Meeting Notes 2026-02-22]]'
- '[[contradiction/IRB Stated Wait Times vs Actual Patient Wait Times]]'
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
- '[[assumption/Questionnaire Is Not a Strong Predictive Tool for Full DSM Diagnoses]]'
- '[[decision/Split AI Research Into Two Papers]]'
relationships:
- confidence: 0.95
  context: Methodology/results discussion & review
  source: note/AI Diagnostic Paper Methodology and Results Discussion.md
  target: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  type: related-to
- confidence: 0.85
  context: Discuss paper methodology/results
  source: note/AI Diagnostic Paper Methodology and Results Discussion.md
  target: note/AI Diagnostic Paper Research Meeting 2026-02-22.md
  type: related-to
- confidence: 0.85
  context: Discuss paper methodology/results
  source: note/AI Diagnostic Paper Methodology and Results Discussion.md
  target: note/AI Diagnostic Paper Research Meeting Notes 2026-02-22.md
  type: related-to
- confidence: 0.8
  context: Discuss paper methodology/results
  source: note/AI Diagnostic Paper Methodology and Results Discussion.md
  target: note/AI Diagnostic Paper Review Meeting Notes 2026-02-22.md
  type: related-to
- confidence: 0.7
  context: Prior AI patient data discussion
  source: note/AI Diagnostic Paper Methodology and Results Discussion.md
  target: note/Patient Data Research and AI Summary Quality Discussion 2025-11-11.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Diagnostic Paper Methodology and Results Discussion

## Context

Meeting between Rami Khouri (AI system architect), Dekkel Khouri (clinical strategy), and Noam (statistician/paper lead) to review progress on the AI-assisted psychiatric diagnostic prediction paper. The paper describes a system built on Telia'z Clinic Israel patient data (intake questionnaires + case manager transcripts) to predict DSM-based psychiatric diagnoses.

## AI Prediction Pipeline — Multi-Agent Architecture

Rami presented the full diagnostic prediction pipeline, which consists of multiple stages:

### Stage 1: Symptom Extraction (Structured Data from Raw Input)

Three data sources feed the system:
1. **Patient questionnaire** — Structured and rule-based extraction (no LLM needed). Covers depression (PHQ), anxiety, PTSD (PCL), sleep, and eating disorders. Limited diagnostic scope.
2. **Case manager transcript** — Initially attempted without LLM (strict rule-based), but switched to LLM-based extraction to capture richer symptom data. Case managers ask DSM-oriented follow-up questions, so transcripts contain more diagnostic criteria.
3. **Case manager notes** — Additional structured notes from case managers.

### Stage 2: Diagnostic Prediction (Record Analysis)

Multiple "agents" (models) generate diagnostic predictions independently and in combination:

| Agent | Input | Approach |
|-------|-------|----------|
| **S1 (Questionnaire-only)** | Questionnaire symptoms | Rule-based matching against known diagnostic criteria. Known to be weak predictor since questionnaire doesn't cover all DSM diagnoses. |
| **S2 (Transcript-only)** | Case manager transcript symptoms | LLM-extracted symptoms matched to DSM criteria. Stronger predictor since case managers ask DSM-oriented questions. |
| **S3 (Notes-only)** | Case manager notes | Extracted symptoms from clinical notes. |
| **Fusion** | Combined S1+S2+S3 | LLM-based fusion model that sees outputs from all three sources and synthesizes a unified diagnosis. Replaces earlier non-LLM fusion which simply picked one diagnosis without true synthesis. |
| **Expert Agent** | Fusion output | LLM prompted as "you are a psychiatrist" — applies clinical reasoning to refine fusion output. Focuses strictly on DSM symptom criteria. |
| **Biased Expert Agent** | Fusion output + contextual priming | Same psychiatrist-prompted LLM but given contextual framing (e.g., "post-war setting"). This is the key experimental agent. |

### Stage 3: Results Granularity

Results are evaluated at three levels of diagnostic specificity:
- **Specific** — Full ICD code with decimal (e.g., F43.10 for PTSD)
- **Group** — F-code without decimal (e.g., F43 for stress-related disorders)
- **Block** — Entire diagnostic category (e.g., all affective disorders, all trauma disorders, all psychotic disorders)

## Key Finding: Diagnostic Bias Replication

The most significant finding discussed was about **contextual diagnostic bias**:

1. The **Expert Agent** (psychiatrist-prompted, no context) classified symptoms strictly by DSM criteria. When seeing insomnia as a symptom, it left it as generic insomnia. Combined with anhedonia, it would classify toward depression.

2. The **Biased Expert Agent** (psychiatrist-prompted WITH post-war context) tagged the same insomnia as "trauma-related insomnia," shifting the diagnostic prediction toward PTSD.

3. This mirrors what real psychiatrists do: in the post-war clinical setting, they tend to diagnose PTSD even when the symptom profile better matches MDD (Major Depressive Disorder), because contextual priming influences their diagnostic reasoning.

4. The biased agent's predictions more closely matched the actual psychiatrist diagnoses (the ground truth), which paradoxically suggests the psychiatrists themselves were biased.

5. **PHQ correlation supports this**: When Rami previously analyzed sample sizes, PHQ scores correlated with the AI predictions but NOT with PCL scores — suggesting patients were being treated for depression symptoms while receiving PTSD diagnoses.

Dekkel noted this finding is "remarkable" and constitutes a separate paper on its own — essentially an anthropological analysis of diagnostic bias.

## Paper Structure Decision

The team agreed to **split the research into two papers**:

**Paper 1 (current):**
- Methodology: System architecture, symptom extraction from questionnaires and transcripts
- Basic clinical results: Questionnaire-only accuracy, transcript-only accuracy (without fusion/bias analysis)
- Time-to-treatment data: Time to case manager, time to psychiatrist, time to summary approval
- Demographic data
- Comparison to literature on paperwork time

**Paper 2 (future):**
- Fusion model results and multi-agent synthesis
- Expert vs Biased Expert diagnostic predictions
- Diagnostic bias analysis (PTSD vs MDD classification patterns)
- DSM utility as a diagnostic tool — philosophical discussion
- MDP-based symptom framework (novel methodology, IP considerations noted)

## Time-to-Treatment Data Issues

Noam presented preliminary time analysis from Shmulik's data:

- **Data discrepancy**: Latest Excel has 6,041 records vs ~5,700 in previous file for same date range (Dec 2023 – Aug 2025 per IRB). Must be investigated before finalizing.
- **Missing data**: ~25% of records lack time-to-case-manager data; percentage increases for psychiatrist timestamps.
- **Extreme outliers**: Some records show 170, 300+ hours/days — clearly data artifacts (patients left in waiting list, technical errors).
- **Agreed approach**: Remove outliers at 2.5 standard deviations from mean.
- **Median vs Mean**: Given high variance and outliers, team agreed to report median (not mean). Median shows 8 days to case manager, 16 days (8+8) to psychiatrist — reasonable numbers.

## Summary Approval Time — Real-Time vs Transcript Mode

Two distinct periods exist in the data:

1. **Pre-change (transcript mode)**: After the session ended, an AI summary was auto-generated. Psychiatrist opened it later (sometimes days later) to review and send. The time between generation and approval is not meaningful for measuring editing time — it measures psychiatrist delay, not AI utility.

2. **Post-change (real-time mode)**: During the last 2 minutes of the session, the psychiatrist clicks "generate summary," reviews it in a popup, edits, and sends — all before the session ends. This gives meaningful editing time data.

Rami requested Shmulik provide an 8-column breakdown: Intake 30min (transcript), Intake 30min (real-time), Intake 20min (transcript), Intake 20min (real-time), Follow-up 30min (transcript), Follow-up 30min (real-time), Follow-up 20min (transcript), Follow-up 20min (real-time).

**Key metric**: Time from session end to summary approval. Before real-time mode: days. After: effectively zero (sent during session). Literature benchmark: ~10 minutes for paperwork.

## Methodology Figures

Current paper has one figure covering symptom extraction. Noam and Rami agreed that 2-3 figures are needed total:
1. Symptom extraction from raw data (exists)
2. Record analysis / diagnostic prediction pipeline (to be created)
3. Possibly a third for the fusion process

Dekkel noted this makes the Methods section very heavy — "half the paper is methods" — but acknowledged it's unavoidable given the complexity.

## IRB Compliance

- Data inclusion period: December 1, 2023 through August 31, 2025
- IRB originally specified ~3-5 days for time-to-treatment; actual data shows median of 8-16 days
- Must verify the 25-day median-to-psychiatrist figure aligns with IRB commitments

## Related
![[related.base#All]]