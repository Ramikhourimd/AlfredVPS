---
alfred_tags:
- research/ai-diagnostic-paper
- meetings/methodology-review
created: '2025-11-11'
description: Meeting notes from Rami-Rivi discussion covering AI summary quality gap,
  patient follow-up flow investigation, questionnaire field review, and research data
  extraction methodology
janitor_note: 'LINK001: Body contains embed to related.base (All section) which does
  not exist in _bases/. Also contains Telia''z project links with apostrophe. Human
  review needed for base view infrastructure.'
name: Patient Data Research and AI Summary Quality Discussion 2025-11-11
project: '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Rivi Idelman]]'
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
- '[[person/Shira]]'
- '[[person/Ori Shukron]]'
- '[[task/Obtain Gold Standard AI Session Summary Example]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[task/Compile Prioritized System Complaint List for Clinical Staff]]'
- '[[assumption/Gold Standard Example Will Fix AI Summary Quality]]'
- '[[synthesis/AI Clinical Summary Quality Gap Unresolved Since November 2025]]'
relationships:
- confidence: 0.8
  context: Earlier AI quality discussion supports
  source: note/Patient Data Research and AI Summary Quality Discussion 2025-11-11.md
  target: note/AI Diagnostic Paper Methodology and Results Discussion.md
  type: supports
- confidence: 0.8
  context: Patient data quality informs review
  source: note/Patient Data Research and AI Summary Quality Discussion 2025-11-11.md
  target: note/AI Diagnostic Paper Methodology and Results Review 2026-02-22.md
  type: supports
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Patient Data Research and AI Summary Quality Discussion 2025-11-11

## Context

One-on-one meeting between Rami Khouri (CMO) and Rivi Idelman (Innovation Team Lead/Researcher) at the clinic office on 2025-11-11. Covered multiple topics: AI summary quality issues, patient follow-up flow, research data extraction, and questionnaire design.

## AI Summary Quality Gap

Rami and Rivi discussed a critical gap in the AI clinical summaries. The current system generates post-session summaries that **ignore case manager intake data**, producing summaries based only on the psychiatrist session. This means the extensive intake interview data (developmental history, symptom timeline, life events) is lost in the summary output.

**Action plan:**
- A psychiatrist will provide a "gold standard" example of what a high-quality summary should look like — not from a real patient but a representative example showing ideal structure and content
- Rivi will collect the example and forward it to Tav (the development team) so the AI prompt can be updated
- This aligns with the existing assumption that a gold standard example will fix AI summary quality

## Psychiatrist Complaints and Staff Concerns

Rami noted that psychiatrists have been raising complaints in the WhatsApp group, particularly about summary quality. He directed Rivi to:
- Review the clinical team WhatsApp discussions (she is not in the psychiatrist-only group)
- Extract insights from recent threads — Elinor and case managers had an extended discussion, and Naomi wrote a detailed post
- Compile findings and send a summary of key themes back to Rami
- Conduct direct conversations with psychiatrists to understand subjective vs objective concerns, giving them the feeling their issues are being addressed

## Patient Follow-Up Flow Investigation

Rami directed Rivi to investigate the full patient experience flow:
- Talk to **Shira** first — she can map the entire workflow
- Then talk to **Renee** — who can explain what actually happens with patients between sessions and before they start
- Understand what automatic questionnaires, messages, and notifications patients receive
- Also talk to **Roy** about follow-up questionnaires
- The goal is for Rivi to experience the flow herself as a pseudo-patient and identify gaps

## Research Work Hours and Compensation

Rivi raised a clarification about research hours:
- The research component is considered voluntary/supplementary — not separately compensated
- Rami confirmed: research is included within the fixed hours allocation
- Rivi currently spends about 5-6 hours per week on research
- Rivi tracks her hours for self-awareness and will escalate if research systematically exceeds allocation
- Rami emphasized: if research hours consistently exceed the allocation, they would revisit, but for now it's a fixed payment arrangement

## Patient Questionnaire Review

Rami walked Rivi through the patient intake questionnaire fields:
- **Demographics:** Year of birth, HMO affiliation, birth order
- **Social:** Employment status, marital/family status, living situation, education level
- **Military:** Military service (yes/no), military role, reason for non-service
- **History (before age 18):** Relevant life events, sexual assault, crime victimization, legal issues, prior diagnoses
- **Substance use:** Options for various substances
- **Mental health treatment history:** Psychotherapy, psychiatric treatment, hospitalization, and side effects
- Rivi noted the questionnaire's mental health history question may feel overly dramatic to patients — the phrasing implies something more severe than simple therapy
- Rami acknowledged this is an old version and the questionnaire may have been updated since Maccabi requested changes

## Data Extraction Methodology

Rami showed Rivi the patient data document structure:
- Each patient has a single Google Docs file containing: questionnaire responses, case manager transcript, case manager notes, psychiatrist transcript, and summary
- Rami can run automated AI extraction across all patient files, but it takes time and costs money per run
- **Proposed approach (ping-pong):** Rivi builds an initial Excel table with column headers for all extractable fields from the questionnaire + rubrics, then Rami completes and validates
- Rivi should start with structured data (questionnaire fields) before tackling unstructured content (transcripts)
- Rami shared the patient docs folder with Rivi for review
- Noam previously preferred capturing as much data as possible; Dekkel preferred cleaning/structuring after

## Related
![[related.base#All]]