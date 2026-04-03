---
alfred_instructions: null
alfred_tags:
- psychiatry/commitments
- expiry-alerts
- outpatient-compliance
assigned: null
blocked_by: []
created: '2025-01-12'
depends_on:
- '[[task/Clarify Maccabi Commitment Renewal Terms]]'
description: Implement pop-up alert in the psychiatrist meeting screen that warns
  when a patient is 1-2 sessions from commitment expiry, and a strong warning on the
  last session. Also trigger secretarial tasks for phone reminders.
due: null
janitor_note: 'LINK001: Wikilink targets may not exist yet. Base view embeds reference
  missing _bases/ files — vault-wide infrastructure gap.'
kind: task
name: Build Commitment Expiry Alerts for Psychiatrist Sessions
priority: high
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
relationships: []
run: null
status: todo
tags: []
type: task
---

# Build Commitment Expiry Alerts for Psychiatrist Sessions

Implement two alert mechanisms for commitment expiry:
1. A pop-up warning when a psychiatrist opens a session that is 1-2 sessions before the commitment expires
2. A prominent alert on the last session ("This is the final session under the current commitment — renewal required")
3. Automatic administrative task generation for secretaries to call the patient during pre-session preparation and remind them to submit a renewal commitment

## Context

From [[conversation/Commitment Process and Feature Updates Meeting 2025-01-12]]. Shachar had previously shown a prototype of such a pop-up.

## Related
![[related.base#All]]

## Outcome