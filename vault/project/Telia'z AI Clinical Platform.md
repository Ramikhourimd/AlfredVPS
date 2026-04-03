---
alfred_tags:
- healthcare/telepsychiatry
- ai/clinical-platform
- business/expansion
approved_by: []
based_on: []
blocked_by: []
client: '[[org/Telia''z]]'
created: '2026-02-25'
depends_on: []
description: Product and engineering initiative to build the AI-powered clinical platform
  for Telia'z clinics. Covers API design (patient, meeting, questionnaire endpoints),
  report generation, AI summary orchestration, data architecture (Read-Only/Shadow
  DB), webhook triggers, JSON output standardization, and psychiatry transcription
  workflows.
janitor_note: LINK001 — All Telia'z wikilinks valid (YAML escaping false positive).
  project.base#* embeds are standard template patterns but _bases/project.base does
  not exist — create base file to enable dynamic views.
location: null
name: Telia'z AI Clinical Platform
owner: '[[person/Rami Khouri]]'
parent: '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Telia''z]]'
- '[[person/Rami Khouri]]'
- '[[person/Shmulik]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[asset/Predictics]]'
- '[[constraint/Meeting Transcripts Not Accessible via BigQuery]]'
- '[[constraint/Transcript Data Not Available in BigQuery]]'
- '[[note/Meeting Markdown Validation Audit Report]]'
- '[[note/Meeting Data Validation Audit Report 2026-02-26]]'
- '[[task/Ingest 338 Remaining Meetings Into Supabase Knowledge Base]]'
- '[[note/Meeting Transcript Validation Audit Report]]'
- '[[decision/Prefer Single Comprehensive Patient Data API Over Per-Agent Endpoints]]'
- '[[decision/Color-Coded Factual Checking for AI Clinical Summaries]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Build Case Manager Tab-Based Questionnaire Screen in Retool]]'
relationships:
- confidence: 0.85
  context: AI platform supports clinic ops
  source: project/Telia'z AI Clinical Platform.md
  target: project/Telia'z Clinic Israel.md
  type: supports
- confidence: 0.9
  context: AI platform part of innovations
  source: project/Telia'z AI Clinical Platform.md
  target: project/Telia'z Innovation Program.md
  type: part-of
- confidence: 0.7
  context: Both Telia'z initiatives
  source: project/Telia'z AI Clinical Platform.md
  target: project/Telia'z Organizational Restructuring.md
  type: related-to
- confidence: 0.6
  context: Shared Telia'z projects
  source: project/Telia'z AI Clinical Platform.md
  target: project/Telia'z UK Expansion.md
  type: related-to
- confidence: 0.95
  context: Part of Telia'z organization
  source: project/Telia'z AI Clinical Platform.md
  target: org/Telia'z.md
  type: part-of
status: active
supports: []
tags: []
type: project
---

# Telia'z AI Clinical Platform

Product and engineering initiative to build the AI-powered clinical platform for Telia'z clinics. Encompasses API layer design, data architecture, AI summary orchestration, clinical reporting, and transcription infrastructure.

Key workstreams:
- **API Layer**: Low-level entity APIs (Patient, Meeting, Questionnaire) with pagination and payload limits
- **Data Architecture**: Read-Only/Shadow DB for analytics queries, BigQuery/DWH integration for pricing
- **AI Summaries**: Orchestrator for clinical session summaries, standardized JSON output, original vs long summary comparison
- **Report Engine**: Monthly clinic reports with rich fields (status, cancellation reasons, therapist, creation times)
- **Transcription**: Teams Captions for real-time transcription, Transcript as backup, local recorder exploration
- **Triggers**: Webhook-based pipeline triggers with Start API as interim solution

---

## Assumptions
![[project.base#Assumptions]]

## Decisions
![[project.base#Decisions]]

## Constraints
![[project.base#Constraints]]

## Contradictions
![[project.base#Contradictions]]

## Dependencies
![[project.base#Dependencies]]

## Tasks
![[project.base#Tasks]]

## Sub-projects
![[project.base#Sub-projects]]

## Sessions
![[project.base#Sessions]]

## Learnings
![[project.base#Learnings]]

## Conversations
![[project.base#Conversations]]

## Inputs
![[project.base#Inputs]]

## Notes
![[project.base#Notes]]