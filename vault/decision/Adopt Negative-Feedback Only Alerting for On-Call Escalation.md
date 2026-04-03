---
alfred_tags:
- psychiatry/on-call
- clinical-operations
approved_by: []
based_on:
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
challenged_by: []
confidence: high
created: '2026-03-17'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z and Ra''ut wikilinks are valid (YAML single-quote
  escaping false positive, scanner artifact). Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist — vault-wide
  infrastructure gap, embeds preserved per policy.'
name: Adopt Negative-Feedback Only Alerting for On-Call Escalation
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Build Negative Feedback Alert for On-Call Dashboard]]'
- '[[decision/Implement Automated Backup for On-Call Doctors]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
relationships:
- confidence: 0.85
  context: On-call alerting and drills
  source: decision/Adopt Negative-Feedback Only Alerting for On-Call Escalation.md
  target: decision/Conduct Practice Drills at Various Hours Including With Partners.md
  type: related-to
- confidence: 0.75
  context: Triage feeds escalation alerts
  source: decision/Adopt Negative-Feedback Only Alerting for On-Call Escalation.md
  target: decision/Delegate Psychiatrist System Complaint Triage to Rivi Idelman.md
  type: supports
session: null
source: Team agreement during on-call case review discussion
source_date: '2025-09-22'
status: final
supports: []
tags: []
type: decision
---

# Adopt Negative-Feedback Only Alerting for On-Call Escalation

## Context

The on-call status dashboard needed an automated notification layer to ensure the on-call psychiatrist responds to alerts. The team debated between positive notifications (alert on every action) and negative-feedback alerting (alert only on inaction).

## Options Considered

1. **Positive notification** — Send Rami a notification for every on-call action taken by the psychiatrist. Rejected due to notification fatigue risk.
2. **Negative-feedback alerting** — Send Rami a notification ONLY when the on-call psychiatrist does NOT click the alert link within 10 minutes. Chosen as the approach.

## Decision

Implement negative-feedback only alerting: notify Rami exclusively when the on-call psychiatrist fails to respond within 10 minutes of a ticket being opened. No notification is sent when the psychiatrist responds in time.

## Rationale

Positive notifications for every action would cause notification fatigue, reducing the system's effectiveness over time. Negative-feedback alerting surfaces only the cases that require escalation, keeping the signal-to-noise ratio high.

## Consequences

- Rami only receives alerts that require action, preserving attention
- The 10-minute timeout window must be calibrated — too short creates false alarms, too long delays escalation
- Requires reliable dashboard infrastructure (missed clicks due to system failure could trigger false alerts)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]