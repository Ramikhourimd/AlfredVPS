---
authority: Telia'z Clinic database design
created: '2026-03-03'
janitor_note: LINK001 — Teliaz wikilinks are YAML-escape false positives (double single-quote).
  assumption/Text-Based Sentiment Analysis... wikilink also verified as YAML-escape
  false positive (target exists). ORPHAN001 — no inbound links; consider linking from
  project/Teliaz AI Diagnostic Research Paper or project/Teliaz Clinic Israel.
name: Key Demographic Variables Only Available Through NLP Extraction From Unstructured
  Text
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[note/Research Paper Scope and Data Extraction Plan 2025-11-09]]'
- '[[assumption/Text-Based Sentiment Analysis Outperforms Standardized Questionnaires
  for Clinical Outcome Tracking]]'
- '[[project/Telia''z Clinic Israel]]'
source: Data architecture of Telia'z Clinic system
source_date: '2025-11-09'
status: active
type: constraint
---

# Key Demographic Variables Only Available Through NLP Extraction From Unstructured Text

## Constraint

Several important patient demographic and clinical history variables are not captured in the structured database. They can only be extracted from unstructured therapy session transcripts using NLP methods:

- Education level
- Military service history
- Prior psychiatric diagnosis
- Prior treatment history

The structured database contains: patient ID, age, gender, employment status, marital status, diagnosis, medication, session counts, and timing data.

## Source

Identified during the 2025-11-09 paper scope meeting when the team catalogued which data comes from structured (database) vs unstructured (transcript) sources. This is a consequence of the clinic's intake system design, which captures basic demographics in structured fields but relies on clinical conversation for detailed history.

## Implications

- Demographic analysis quality depends on NLP extraction pipeline accuracy and coverage
- Patients without transcripts or with poor-quality transcripts will have missing demographic data
- Structured and unstructured data have different reliability tiers
- Any analysis using NLP-extracted demographics must acknowledge extraction methodology as a limitation
- Creates a dependency on Rami's NLP pipeline for variables that ideally would be structured data

## Expiry / Review

This constraint persists until the clinic modifies its data collection system to capture these variables in structured format at intake. No timeline for such a change has been discussed.
