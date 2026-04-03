---
alfred_instructions: null
alfred_tags:
- research/ai-diagnostic-paper
- project-management
channel: email
created: '2025-11-09'
date: '2025-11-09'
description: Team meeting to define scope, methodology, and next steps for the first
  research paper on the telepsychiatry system used after the October 7th trauma.
external_id: null
fork_reason: null
forked_from: null
janitor_note: 'LINK001 — base view embeds (conversation-detail.base#Messages, #Tasks,
  #Related) reference _bases/conversation-detail.base which does not exist — vault-wide
  infrastructure gap, embeds preserved. Telia''z wikilink in related list is valid
  (YAML escaping false positive). ORPHAN001 — no inbound wikilinks. Swept 2026-03-31.'
last_activity: '2025-11-09'
medium: video_call
message_count: 0
opened: '2025-11-09'
org: null
participants:
- '[[person/Dekkel Taliaz]]'
- '[[person/Rivi Idelman]]'
- '[[person/Noam]]'
- '[[person/Rami Khouri]]'
project: null
related:
- '[[constraint/IRB Inclusion Period December 2023 to August 2025]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[note/Research Paper Scope and Data Extraction Plan 2025-11-09]]'
- '[[decision/Focus First Paper on System Presentation and PTSD Outcomes]]'
- '[[decision/Use Per-Symptom Scoring Instead of Composite Score]]'
- '[[decision/Limit Paper to Four or Five Figures Maximum]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[task/Find NLP Outcome Scoring Literature for Transcript Analysis]]'
- '[[task/Summarize Meeting Points and Email to Team]]'
- '[[assumption/Majority of Patients Have PTSD Diagnosis]]'
- '[[assumption/Early Treatment Seekers Have Higher Recovery Rates]]'
- '[[person/Shachar]]'
relationships: []
status: archived
subject: Research Paper Scope and Methodology Planning Meeting 2025-11-09
tags: []
type: conversation
---

# Research Paper Scope and Methodology Planning Meeting 2025-11-09

## Context

Planning meeting for the first scientific paper based on data from the telepsychiatry platform deployed after the October 7th trauma. The team had recently received Helsinki (IRB) committee approval from Maale HaCarmel, enabling them to publish findings from 3,100+ patient records.

## Participants and Roles

- **Dekkel Taliaz** — Led the discussion, defined paper scope and vision. Former doctoral colleague of Noam.
- **Noam** — Academic researcher responsible for paper writing, statistical analysis, and figure preparation. Uses MATLAB for statistics.
- **Rami Khouri** — Data analyst responsible for building data extraction pipelines and running NLP analysis on transcripts.
- **Rivi Idelman** — Psychologist and researcher, assisting with data extraction and clinical interpretation.

## Key Discussion Points

### Paper Structure (4-5 Figures Maximum)

Dekkel outlined a focused paper with three main components:
1. **System presentation** — High-level overview of the telepsychiatry platform (not deep technical detail)
2. **Patient demographics and diagnoses** — Distribution of diagnoses treated post-October 7th, with emphasis on PTSD (~65-67% of patients)
3. **Clinical outcome correlation** — Correlation between time from trauma event to first treatment session and likelihood of clinical improvement

### Outcome Scoring Methodology

The team debated how to define "clinical response." Rami had previously used an NLP-based approach with thematic analysis of transcripts, categorizing outcomes by:
- Return to work
- Evacuees returning home
- Self-reported symptom reduction (flashbacks, sleep problems)
- Clinician-reported improvement

Rather than creating a single composite score, the team agreed to present per-symptom outcomes, which is harder to challenge methodologically. The idea of combining into a composite score was discussed as a secondary step.

Noam offered to search for existing validated NLP methods for scoring clinical outcomes from free-text transcripts in mental health literature.

### Data Extraction Strategy

Two data sources identified:
1. **Structured database fields** — Demographics (age, gender, employment status, marital status), diagnosis, medication, session counts, timing data. Shachar (VP R&D) can export these as Excel tables.
2. **Unstructured transcript data** — Education level, military service history, prior psychiatric history, symptom presence/absence. Requires NLP analysis.

The team decided to start with structured data extraction first, deferring transcript-based analysis until NLP scoring criteria are defined.

### Statistical Considerations

Dekkel raised concerns about running too many analyses (Bonferroni corrections would reduce statistical power). The team agreed to keep the first paper focused and descriptive rather than running complex multivariate analyses.

Noam noted that demographic statistics are relatively straightforward. The more interesting statistical question is the time-to-treatment correlation with per-symptom outcomes.

## Action Items

1. **Rami and Rivi** — Prepare data extraction tables from the structured database
2. **Noam** — Search for literature on NLP outcome scoring methods for therapy transcripts
3. **Noam** — Summarize meeting discussion points and email to the full team
4. **Noam** — Schedule follow-up meeting for the next Sunday
5. **Rami** — Share previous transcript analysis Excel with Noam

## Follow-up

Next meeting planned for the following Sunday at the same time, focused on reviewing extracted data tables, discussing Noam's literature findings on NLP scoring, and defining specific criteria for outcome scoring.

---
## Messages
![[conversation-detail.base#Messages]]

## Tasks
![[conversation-detail.base#Tasks]]

## Related
![[conversation-detail.base#Related]]