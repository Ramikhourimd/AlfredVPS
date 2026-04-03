---
alfred_instructions: null
assigned: null
blocked_by: []
created: '2025-11-09'
depends_on: []
description: 'Extract per-patient structured data tables from the database: patient
  ID, demographics (age, gender, employment, marital status), diagnosis, medication,
  session count, and timing data.'
due: null
janitor_note: 'LINK001: Telia''z AI Diagnostic Research Paper wikilink needs verification
  — may be false positive from YAML escaping; related.base#All embed references _bases/
  — systemic, do not remove embed.'
kind: task
name: Extract Structured Patient Data Tables From Database
priority: medium
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Shachar]]'
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
- '[[person/Shachar]]'
- '[[task/Build Initial Patient Data Excel Table With Column Headers]]'
relationships: []
run: null
status: active
tags: []
type: task
---

# Extract Structured Patient Data Tables From Database

## Objective

Prepare comprehensive data tables from the structured database fields for the research paper. Each row represents one patient with standardized columns.

## Required Columns

- Patient identifier
- Age (from date of birth)
- Gender
- Employment status
- Marital status
- Diagnosis (psychiatrist-assigned)
- Medication
- Number of sessions
- Session types (case manager, psychiatrist follow-up, etc.)
- Time from referral to first session
- Time per session type
- Exposure level (first line, second line, other)

## Data Source

[[person/Shachar]] can run database queries to export structured Excel tables. Rivi should work together with Rami when requesting data from Shachar, as Shachar needs context for the request.

## Assigned To

[[person/Rami Khouri]] and [[person/Rivi Idelman]]

## Deadline

Before the follow-up meeting (next Sunday after November 9, 2025)

---
## Related
![[related.base#All]]
