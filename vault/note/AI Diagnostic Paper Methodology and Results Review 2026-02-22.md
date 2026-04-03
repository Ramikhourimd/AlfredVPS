---
alfred_tags:
- ai/diagnostic-paper/review
- methodology-results
created: '2026-02-22'
description: Research meeting reviewing the multi-agent AI diagnostic pipeline methodology,
  preliminary timing results, dataset discrepancies, and key decision to split the
  paper into two — one for methodology plus clinical results, and a second for the
  bias/contextual priming findings.
janitor_note: LINK001 — base view embed (related.base#All) references _bases/related.base
  which does not exist. All Telia'z wikilinks are valid (YAML escaping false positive).
  person/Dekkel Khouri has no vault record — create person record or verify name spelling.
name: AI Diagnostic Paper Methodology and Results Review 2026-02-22
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Khouri]]'
- '[[person/Noam]]'
- '[[person/Shmulik]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.85
  context: Same date, paper methodology focus
  source: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  target: note/AI Diagnostic Paper Research Meeting 2026-02-22.md
  type: related-to
- confidence: 0.85
  context: Same date, paper methodology focus
  source: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  target: note/AI Diagnostic Paper Research Meeting Notes 2026-02-22.md
  type: related-to
- confidence: 0.9
  context: Review-related notes same date
  source: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  target: note/AI Diagnostic Paper Review Meeting Notes 2026-02-22.md
  type: related-to
- confidence: 0.65
  context: Prior related AI quality discussion
  source: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  target: note/Patient Data Research and AI Summary Quality Discussion 2025-11-11.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# AI Diagnostic Paper Methodology and Results Review 2026-02-22

## Context

Research team meeting on 2026-02-22 to review the current state of the AI diagnostic research paper. Participants: [[person/Rami Khouri]] (lead researcher, AI pipeline architect), [[person/Dekkel Khouri]] (senior advisor), and [[person/Noam]] (statistics and paper compilation). [[person/Shmulik]] provides data exports but was not present.

## Paper Structure — Current State

The paper document currently combines:
1. **Method section** — describes the overall process (already written)
2. **Analysis section** — details how record analysis is performed (recently added by Rami)
3. **Results** — diagnostic prediction outcomes

Noam noted the paper is already methods-heavy ("half the paper is methods") and adding more figures would increase that further.

## Multi-Agent Diagnostic Pipeline

Rami walked through the full pipeline architecture:

### Data Sources
- **Questionnaire** — structured patient self-report; algorithmically parsed (no LLM needed); covers depression, anxiety, PTSD well but not full DSM breadth
- **Case manager transcript** — transcription of case manager interview; initially parsed without LLM (too strict), then LLM-based extraction added for richer data
- **Case manager notes** — written notes from case managers

### Prediction Agents (Sequential Pipeline)

| Agent | Input | Method | Notes |
|-------|-------|--------|-------|
| S1 — Questionnaire | Questionnaire only | Algorithmic | Limited to depression, anxiety, PTSD due to questionnaire structure |
| S2 — Transcript | Case manager transcript | LLM extraction | Case managers ask follow-up DSM-style questions, enriching data |
| S3 — Notes | Case manager notes | LLM extraction | Additional clinical information |
| Fusion | All three sources combined | LLM-based fusion | Early version just picked one diagnosis; revised version has LLM reason across all inputs |
| Expert | Fusion output | LLM as "psychiatrist" persona | Improved predictions by applying psychiatric reasoning |
| Biased Expert | Fusion output | LLM as "psychiatrist in post-war context" | Replicated real psychiatrist bias toward PTSD |

### Key Finding — Diagnostic Bias Replication

The most significant finding was around the "biased expert" agent:

1. The **Expert agent** (LLM as generic psychiatrist) correctly identified symptoms like insomnia as non-specific — could be depression, PTSD, anxiety, etc. — and used co-occurring symptoms (e.g., anhedonia) to classify appropriately. This often produced **depression (MDD)** diagnoses.

2. The **Biased Expert agent** (LLM as psychiatrist in post-war setting) tagged ambiguous symptoms toward trauma. For example, insomnia was classified as "trauma-related insomnia" rather than generic insomnia. This produced more **PTSD** diagnoses.

3. The real psychiatrists' actual diagnoses skewed heavily toward PTSD. The Biased Expert agent's predictions **more closely matched the real psychiatrist diagnoses** than the unbiased Expert agent.

4. **Interpretation:** Psychiatrists appear to have a contextual bias — in a post-war clinical setting, they tend to diagnose PTSD even when DSM criteria better fit depression. When an LLM is given the same contextual priming, it replicates this bias.

Dekkel summarized: "If you take the textbook approach, many diagnoses would fit depression better than PTSD. But if you add background context unrelated to the patient — the environment — you get a similar bias to what real psychiatrists exhibit."

## Timing Data Results

Noam presented preliminary timing analysis from new data export received that morning:

| Metric | Mean | Median | Notes |
|--------|------|--------|-------|
| Time to case manager | ~2 weeks (avg) | 8 days | High variance, outliers up to 300+ days |
| Time to psychiatrist | 25 days (avg) | 16 days | Some records show 150-388 hours — clearly erroneous |
| Time to LTX | ~2 weeks | — | Median to be calculated |

**Issues identified:**
- Very high variance with extreme outliers (patients waiting 300+ days — likely technical errors, e.g., unclosed patient records)
- Dataset size discrepancy: new export has 6,041 records vs ~5,700 in previous export for the same date range (Dec 2023 to Aug 31, 2025)
- ~25% of records missing timing data for case manager; higher percentage for psychiatrist
- IRB submission stated ~3-5 day wait times, but actual median is 8-16 days — significant discrepancy to address

## Approval Time — Real-Time vs Transcript Mode

Two operational periods exist for psychiatrist summary approval:
1. **Pre-change (Transcript mode):** Session ended, summary auto-generated, psychiatrist reviewed hours/days later via Google Docs
2. **Post-change (Real-time mode):** During last 2 minutes of session, psychiatrist clicks "Generate Summary," reviews popup, edits, and sends — all within the session

Rami proposed measuring the delta between session end and approval for both periods. The real-time mode should show near-zero or negative delta (summary sent before session formally ends).

Rami requested Shmulik provide data split into 8 columns: intake 30min transcript, intake 30min real-time, intake 20min transcript, intake 20min real-time, plus same 4 for follow-up appointments.

## Paper Scope Decisions

Three key decisions emerged:

1. **Split into two papers:** The bias/contextual priming findings will be a separate second paper. The first paper focuses on methodology and basic clinical results.

2. **First paper scope:** Include questionnaire analysis and case manager transcript analysis results (each separately), plus timing data and demographics. Exclude fusion, expert agent, and biased expert results.

3. **Clinical results to include:** PHQ correlation data (which confirmed questionnaire aligns with depression measures, not PTSD), supporting the bias narrative. Dekkel specifically wanted some clinical insight in Paper 1 beyond just methodology.

## Open Questions

- How to calculate and present the diagnostic accuracy percentages (Noam still needs the computation method)
- Whether to mention the MDP (proprietary symptom framework) — potential IP/rights concerns
- How to reconcile the dataset size discrepancy between two Excel exports
- Whether the Google Docs modification timestamps can reliably measure editing time in the pre-change period

## Related
![[related.base#All]]