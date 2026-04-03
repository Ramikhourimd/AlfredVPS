---
alfred_instructions: null
alfred_tags:
- psychiatry/commitments
- expiry-alerts
- outpatient-compliance
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on: []
description: Create automated secretary tasks that trigger when a patient approaches
  commitment expiry, prompting secretaries to phone the patient during pre-session
  calls and remind them to send a renewal commitment
due: null
janitor_note: '"LINK001 — \![[related.base#All]] references missing base file (_bases/
  not found in vault). Embed preserved per vault infrastructure rules. Telia''z wikilinks
  are valid (YAML escaping false positive)."'
kind: task
name: Add Secretary Tasks for Commitment Renewal Reminders
priority: medium
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Rana Khouri]]'
relationships:
- confidence: 0.8
  context: Renewal reminders and expiry alerts
  source: task/Add Secretary Tasks for Commitment Renewal Reminders.md
  target: task/Build Commitment Expiry Alerts for Psychiatrist Sessions.md
  type: related-to
- confidence: 0.8
  context: Renewal tasks and end-commitment alerts
  source: task/Add Secretary Tasks for Commitment Renewal Reminders.md
  target: task/Build End-of-Commitment Alert System for Psychiatrists.md
  type: related-to
- confidence: 0.97
  context: Similar secretary renewal tasks
  source: task/Add Secretary Tasks for Commitment Renewal Reminders.md
  target: task/Create Secretary Task Automation for Commitment Renewal Reminders.md
  type: related-to
- confidence: 0.6
  context: Compliance reminders via secretary
  source: task/Add Secretary Tasks for Commitment Renewal Reminders.md
  target: task/Monitor Outpatient Work Compliance Monday Wednesday.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Add Secretary Tasks for Commitment Renewal Reminders

Secretaries make preparation calls to patients before their sessions. When a patient is approaching commitment expiry, an automated task should appear for the secretary to remind the patient to send a new commitment.

## Context

- Secretaries already call patients as part of session preparation
- The renewal reminder should integrate into this existing workflow
- Without the reminder, patients may show up to sessions without a valid commitment, blocking billing

## Requirements

1. Auto-generated task for secretaries when patient is within 2 sessions of commitment expiry
2. Task appears in the secretary's task queue with patient name and session count remaining
3. Task marked complete when secretary confirms patient has been notified

## Related
![[related.base#All]]

## Outcome

*Filled in on completion.*