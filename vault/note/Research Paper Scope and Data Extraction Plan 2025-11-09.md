---
alfred_tags:
- research/paper-scope
- telepsychiatry/ptsd
created: '2025-11-09'
description: 'Summary of decisions and plans from the research paper scope meeting:
  paper structure, NLP-based outcome scoring approach, data extraction strategy, and
  statistical methodology.'
janitor_note: '"LINK001 — Telia''z wikilink in project field is valid (YAML escaping
  false positive). Base embed \![[related.base#All]] requires _bases/related.base
  which does not exist; create it to enable dynamic views. Embed preserved."'
name: Research Paper Scope and Data Extraction Plan 2025-11-09
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rivi Idelman]]'
- '[[decision/Focus First Paper on System Presentation and PTSD Outcomes]]'
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
- '[[decision/Limit Paper to Four or Five Figures Maximum]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
- '[[assumption/Majority of Patients Have PTSD Diagnosis]]'
- '[[assumption/Early Treatment Seekers Have Higher Recovery Rates]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
relationships: []
session: null
status: active
subtype: null
tags: []
type: note
---

# Research Paper Scope and Data Extraction Plan 2025-11-09

## Paper Structure

The first paper on the post-October 7th telepsychiatry platform will contain a maximum of 4-5 figures and focus on three layers:

1. **System overview** — High-level description of the telepsychiatry platform, not a detailed technical breakdown
2. **Patient demographics and diagnosis distribution** — Pie chart of diagnoses, with PTSD comprising ~65-67% of the 3,100+ patients
3. **Time-to-treatment correlation** — Correlation between elapsed time from trauma event to first treatment session and clinical improvement indicators

## Outcome Scoring Approach

Instead of a single composite clinical outcome score, the team will present outcomes per individual symptom dimension:

- **Return to work** — Binary: returned / not returned
- **Return home** (for evacuees) — Binary: returned / not returned
- **Sleep improvement** — Self-reported reduction in sleep disturbances
- **Flashback reduction** — Self-reported reduction in flashback frequency
- **Clinician-reported improvement** — Psychiatrist assessment

Rami had previously developed an NLP pipeline (Python-based language model) to extract these indicators from session transcripts via thematic analysis. The question of whether to also combine these into a composite score (0-100 scale with response thresholds) was deferred pending Noam's literature review.

## Data Sources

### Structured (Database)
Per-patient table with: patient ID, age, gender, employment status, marital status, diagnosis, medication, session count, session types, timing data (referral to first session, time per session type).

### Unstructured (Transcripts)
Education level, military service history, prior psychiatric diagnosis, prior treatment, symptom presence/absence. Requires NLP extraction.

## Statistical Approach

- Keep analyses focused to avoid Bonferroni correction penalties
- Demographic data: descriptive statistics (means, standard deviations)
- Primary analysis: correlation between time-to-treatment and per-symptom outcomes
- Noam will handle statistical analysis using MATLAB
- Complex predictive analyses (e.g., who develops PTSD, military service correlations) deferred to future papers

## Key Insight

This is an observational study, not a predictive algorithm paper. The strength lies in sample size (3,100+ patients) and a unique dataset with a precise trauma onset date (October 7th), enabling clean time-to-treatment analysis.

---
## Related
![[related.base#All]]