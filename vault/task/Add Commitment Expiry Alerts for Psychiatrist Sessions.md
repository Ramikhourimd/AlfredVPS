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
description: Implement pop-up alerts on the psychiatrist meeting screen warning when
  a patient is on their last or second-to-last session under their current Maccabi
  commitment, prompting commitment renewal
due: null
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist — create base file to enable dynamic views. ORPHAN001 — no
  inbound wikilinks; consider linking from project/Telia'z AI Clinical Platform.
kind: task
name: Add Commitment Expiry Alerts for Psychiatrist Sessions
priority: high
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
relationships:
- confidence: 0.85
  context: Complementary commitment lifecycle tasks
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Add Secretary Tasks for Commitment Renewal Reminders.md
  type: related-to
- confidence: 0.98
  context: Near-identical expiry alert tasks
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Build Commitment Expiry Alerts for Psychiatrist Sessions.md
  type: related-to
- confidence: 0.95
  context: Similar commitment expiry alert systems
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Build End-of-Commitment Alert System for Psychiatrists.md
  type: related-to
- confidence: 0.75
  context: Expiry alerts and renewal automation
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Create Secretary Task Automation for Commitment Renewal Reminders.md
  type: related-to
- confidence: 0.6
  context: Related to outpatient commitments
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Monitor Outpatient Work Compliance Monday Wednesday.md
  type: related-to
- confidence: 0.55
  context: Work resumption in commitments
  source: task/Add Commitment Expiry Alerts for Psychiatrist Sessions.md
  target: task/Patient to Resume Work Attendance Monday and Wednesday.md
  type: related-to
run: null
status: todo
tags: []
type: task
---

# Add Commitment Expiry Alerts for Psychiatrist Sessions

When a psychiatrist enters a session, the system should display a pop-up alert if the patient is on their last or second-to-last session under the current Maccabi commitment.

## Context

- Patients have a finite number of sessions under each commitment (e.g., 4 psychiatric follow-ups)
- Without alerts, psychiatrists may not know the commitment is about to expire
- The alert should trigger 2 sessions before expiry (warning) and at the last session (critical)
- Shachar showed a mock-up concept for the pop-up during an earlier meeting

## Requirements

1. Warning pop-up 2 sessions before last: "Commitment expiring soon — X sessions remaining"
2. Critical pop-up on last session: "This is the last session under the current commitment — renewal required"
3. Pop-up appears on entering the meeting screen, before the session starts

## Related
![[related.base#All]]

## Outcome

*Filled in on completion.*