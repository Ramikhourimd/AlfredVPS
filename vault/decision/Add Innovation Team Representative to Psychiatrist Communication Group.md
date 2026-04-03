---
alfred_tags:
- psychiatry/on-call
- clinical-operations
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-03-03'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 false positives: [[project/Telia''z AI Clinical Platform]]
  uses valid YAML single-quote escaping. [[learn-decision.base#Based On]] and [[learn-decision.base#Related]]
  are base view embeds referencing _bases/ infrastructure, not broken wikilinks. This
  is a vault-wide infrastructure gap.'
name: Add Innovation Team Representative to Psychiatrist Communication Group
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
- '[[person/Stav Zamir]]'
relationships:
- confidence: 0.7
  context: Psychiatrist comm for on-call escalation
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Adopt Negative-Feedback Only Alerting for On-Call Escalation.md
  type: related-to
- confidence: 0.85
  context: Psychiatrist workflow improvements
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Build ER Referral Form Feature for Psychiatrists.md
  type: related-to
- confidence: 0.65
  context: Comm aids partner drills
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Conduct Practice Drills at Various Hours Including With Partners.md
  type: supports
- confidence: 0.8
  context: Psychiatrist complaint handling
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Delegate Psychiatrist System Complaint Triage to Rivi Idelman.md
  type: related-to
- confidence: 0.8
  context: Psychiatrist ER referral process
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Deliver ER Referral Letters via HealthyMind App Not Email.md
  type: related-to
- confidence: 0.6
  context: On-call monitoring and comm
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Deploy Real-Time On-Call Status Dashboard for Remote Monitoring.md
  type: related-to
- confidence: 0.55
  context: On-call project team comm
  source: decision/Add Innovation Team Representative to Psychiatrist Communication
    Group.md
  target: decision/Rami Owns On-Call Project Management End-to-End.md
  type: related-to
session: null
source: Rami Khouri directive during clinic meeting with Shira
source_date: '2025-11-10'
status: final
supports:
- '[[task/Compile Prioritized System Complaint List for Clinical Staff]]'
tags: []
type: decision
---

# Add Innovation Team Representative to Psychiatrist Communication Group

## Context

Clinical staff (psychiatrists) were reporting system complaints through informal channels (WhatsApp groups) with no technical team member present to respond. Complaints included deleted clinical summaries, system freezing, and authentication lockouts. These went unaddressed because the psychiatrist communication group had no one with technical visibility.

## Options Considered

1. **Keep current structure** — Psychiatrists report issues informally; complaints are compiled periodically by clinical leadership and relayed to R&D.
2. **Add Innovation Team member to psychiatrist group** — Stav Zamir joins the group to directly field system-related complaints and triage them.

## Decision

Rami directed that Stav Zamir (Innovation Team) be added to the psychiatrist communication group so she can respond to system-related complaints directly and triage technical issues.

## Rationale

Having a technical team member embedded in the clinical communication channel reduces the feedback loop from complaint to triage. Rather than waiting for periodic compilations, issues can be acknowledged and routed immediately.

## Consequences

- Faster response time for system complaints from psychiatrists.
- Innovation Team gains direct visibility into clinical pain points.
- Risk of Stav being overwhelmed if complaint volume is high.
- Creates an informal triage channel that may need formalization later.

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]