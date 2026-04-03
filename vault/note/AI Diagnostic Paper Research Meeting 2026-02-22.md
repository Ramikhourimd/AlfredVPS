---
alfred_tags:
- ai/diagnostic-paper/review
- methodology-results
created: '2026-02-25'
description: Detailed meeting notes from Rami, Dekkel, and Noam discussing the AI
  diagnostic research paper methodology, multi-agent pipeline architecture, diagnostic
  bias findings, data quality issues, and paper structure decisions
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. All Telia'z wikilinks are valid (YAML escaping false positive).
  Fixed person/Dekkel Khouri → person/Dekkel Taliaz.
name: AI Diagnostic Paper Research Meeting 2026-02-22
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
- '[[person/Shmulik]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/AI Diagnostic Paper Methodology Review Meeting 2026-02-22]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.95
  context: Meeting summary and detailed notes
  source: note/AI Diagnostic Paper Research Meeting 2026-02-22.md
  target: note/AI Diagnostic Paper Research Meeting Notes 2026-02-22.md
  type: part-of
- confidence: 0.8
  context: Same date paper meetings
  source: note/AI Diagnostic Paper Research Meeting 2026-02-22.md
  target: note/AI Diagnostic Paper Review Meeting Notes 2026-02-22.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Diagnostic Paper Research Meeting 2026-02-22

## Context

Meeting between Rami Khouri, Dekkel Khouri, and Noam (research collaborator/statistician) to review the methodology, figures, and results for the AI diagnostic research paper. The paper documents a multi-agent LLM pipeline for psychiatric diagnosis prediction at Telia'z Clinic Israel.

Noam had previously compiled a combined document merging the methodology, analysis approach, and results. Rami noted that two additional pipeline stages were missing from the figures.

## Multi-Agent Diagnostic Pipeline

The AI diagnostic system uses a multi-step pipeline with the following "agents" (models/approaches):

### Data Sources
1. **Patient Questionnaire** — Structured self-report instrument. Symptom extraction uses a simple algorithm (no LLM needed) due to clear, rule-based structure. Covers depression, anxiety, and PTSD questions well, but has limited coverage for other diagnoses (sleep, eating disorders, etc.)
2. **Case Manager Transcript** — Transcribed case manager intake sessions. Initially attempted extraction without LLM (strict/rule-based), but switched to LLM-based extraction for better data capture. Case managers ask DSM-informed follow-up questions during sessions.
3. **Case Manager Notes** — Written notes by case managers after sessions.

### Prediction Agents
- **S1 (Questionnaire-Only Agent)** — Predicts diagnosis based solely on questionnaire data. Known limitation: questionnaire does not cover full DSM spectrum, so predictive power is inherently limited.
- **S2 (Transcript Agent)** — Predicts based on case manager transcript. Expected to perform better due to DSM-informed questioning by case managers.
- **S3 (Notes Agent)** — Predicts based on case manager notes.
- **Fusion Agent (no LLM)** — Initially attempted a non-LLM fusion of S1+S2+S3. The model tended to just pick one source's diagnosis rather than truly fusing. This approach was abandoned.
- **Fusion Agent (LLM-based)** — Uses an LLM to see outputs from all sources and synthesize a combined diagnosis. Significant improvement over non-LLM fusion.
- **Expert Agent** — LLM prompted as "you are a psychiatrist" to apply clinical reasoning. This improved diagnosis quality, particularly by associating symptoms with DSM categories more accurately.
- **Biased Expert Agent** — LLM prompted as "you are a psychiatrist in a post-war context." This added contextual bias that replicated the diagnostic patterns of actual psychiatrists — specifically, classifying insomnia as trauma-related insomnia (PTSD) rather than depression-related insomnia.

### Key Insight: Diagnostic Bias
The core finding: when the LLM expert agent was given no context, it diagnosed based purely on DSM criteria and often classified patients as having depression (MDD). When given the post-war context, it shifted diagnoses toward PTSD — mirroring what actual psychiatrists did. This suggests psychiatrists may be applying contextual bias (prior knowledge about the patient population) when diagnosing, rather than strictly following DSM criteria.

This bias finding:
- Matches the PHQ/PCL discrepancy Rami found earlier: questionnaire responses correlated better with PHQ (depression) than PCL (PTSD), yet psychiatrists diagnosed PTSD
- Raises fundamental questions about whether DSM is a sufficient diagnostic tool
- Dekkel noted this is an important finding to share with the clinical team, though not necessarily requiring practice changes

## Paper Structure Decision

Dekkel proposed and the team agreed: **split into two papers**.

**Paper 1 (Current):** Methodology and clinical workflow metrics
- Multi-agent pipeline methodology (symptom extraction + prediction)
- Time-to-treatment data (time to case manager, time to psychiatrist)
- Real-time vs post-session summary approval times
- Demographic data
- Basic diagnostic prediction results (questionnaire alone + case manager transcript alone)
- Comparison to literature on clinical paperwork time

**Paper 2 (Future):** Diagnostic bias analysis
- Full fusion and expert agent pipeline
- Bias analysis (expert vs biased expert)
- PHQ/PCL discrepancy as supporting evidence
- Novel symptom extraction methodology (MDP-based to DSM mapping)
- Could stand alone as an anthropological/methodology paper

## Data Quality Issues

### Sample Size Discrepancy
Two Excel data exports from Shmulik showed different patient counts for the same date range (Dec 2023 — Aug 2025):
- First export: approximately 5,700 patients
- Second export: 6,041 patients
- Rami analyzed approximately 3,000 patients
- Noam flagged this as requiring investigation before analyses can be finalized

### Time-to-Treatment Outliers
Raw timing data contains extreme outliers (e.g., 170+ hours, 300+ days to case manager):
- These likely represent technical errors (patients not properly closed in the system)
- Team agreed to clean outliers using **2.5 standard deviation cutoff**
- Median values (more robust to outliers) are more representative than means:
  - Median time to case manager: 8 days
  - Median time to psychiatrist: 16 days (8 + 8)
  - Previously claimed ~2 weeks to psychiatrist in average

### Missing Data
Approximately 25-30% of records lack timing data for case manager or psychiatrist appointments. This percentage increases for psychiatrist timing data.

### Approval Time Data
- **Pre-change period:** Summary auto-generated after session, psychiatrist would open Google Doc later (sometimes days later), edit, and approve. The delta between generation and approval was misleading — included idle time, not just editing time.
- **Post-change (real-time) period:** Psychiatrist clicks "generate summary" during last 2 minutes of session, edits inline, sends before session ends. Approval time effectively zero.
- Team decided the meaningful metric is: **time from session end to summary approval**
- Rami requested Shmulik provide 8-column breakdown: intake vs follow-up x 30min vs 20min x transcript vs real-time

### Literature Comparison
The team noted that published literature cites approximately 10 minutes for clinical paperwork/documentation per session. If the real-time system reduces this to under 1 minute, that is a strong result for the paper.

## IRB Compliance
- Inclusion period defined in IRB: up to August 31, 2025
- First patient intake: December 1, 2023
- All analyses must respect these boundaries

## Related
![[related.base#All]]