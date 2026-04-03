---
alfred_instructions: null
assigned: '[[person/Rivi Idelman]]'
blocked_by: []
created: '2025-11-11'
depends_on: []
description: Rivi to build an initial Excel table with column headers for all extractable
  patient data fields from questionnaire and rubrics, then Rami will complete and
  validate in a ping-pong approach
due: null
janitor_note: 'LINK001: Telia''z wikilink is YAML single-quote escaping false positive
  (valid). related.base#All is a base view embed referencing _bases/ infrastructure
  not yet created — vault-wide gap.'
kind: task
name: Build Initial Patient Data Excel Table With Column Headers
priority: medium
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Build Initial Patient Data Excel Table With Column Headers

Rivi to create an Excel spreadsheet with column headers for all patient data fields extractable from the patient docs files, starting with structured questionnaire fields and rubrics before moving to unstructured transcript data.

## Context

Rami has a folder of patient Google Docs files, each containing the full clinical record (questionnaire, transcripts, notes, summary). The research paper needs structured tabular data extracted from these. Rami proposed a ping-pong approach: Rivi builds the initial table structure, Rami fills and validates via automated AI extraction.

## Column Categories

**From Questionnaire:**
- Year of birth, HMO, birth order
- Employment status, marital status, living situation, education
- Military service (yes/no), role, reason for non-service
- Pre-18 life events, substance use history, mental health treatment history

**From Rubrics:**
- Diagnosis, medication
- Session type indicators (case manager, psychiatrist)

## Related
![[related.base#All]]

## Outcome
