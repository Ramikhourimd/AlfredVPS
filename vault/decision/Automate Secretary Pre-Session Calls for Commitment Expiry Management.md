---
alfred_tags:
- healthcare/commitment-expiry
- proactive-alerts
- workflow-automation
approved_by: []
based_on:
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are false positives (YAML apostrophe escaping).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist. Note: duplicate base view embeds at end of file body — consider
  removing duplicates manually.'
name: Automate Secretary Pre-Session Calls for Commitment Expiry Management
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[decision/Implement Proactive Commitment Expiry Alerts for Psychiatrists]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.9
  context: Both address commitment expiry management
  source: decision/Automate Secretary Pre-Session Calls for Commitment Expiry Management.md
  target: decision/Implement Proactive Commitment Expiry Alerts for Psychiatrists.md
  type: related-to
- confidence: 0.85
  context: Both proactive expiry management tactics
  source: decision/Automate Secretary Pre-Session Calls for Commitment Expiry Management.md
  target: decision/Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds.md
  type: related-to
session: null
source: Rami Khouri
source_date: '2025-08-01'
status: draft
supports:
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
tags: []
type: decision
---

# Automate Secretary Pre-Session Calls for Commitment Expiry Management

## Context

When patients approach commitment expiry, secretaries need to call them proactively during pre-session preparation to remind them to obtain and submit a renewal commitment from Maccabi. Currently this happens ad hoc or not at all.

## Options Considered

1. **Automated task triggers** — System generates secretary tasks when patients approach commitment expiry, integrated into pre-session preparation workflow
2. **Manual tracking** — Secretaries maintain a separate list of patients nearing expiry
3. **Psychiatrist-only responsibility** — Leave it to psychiatrists to verbally remind patients

## Decision

Implement automated administrative tasks for secretaries: when a patient approaches commitment expiry, the system should generate a task for the secretary to call the patient before their next session, prompting them to obtain and submit a new commitment from Maccabi.

## Rationale

Secretaries already perform pre-session preparation calls. Adding commitment expiry checks to this existing workflow is operationally efficient. Manual tracking is error-prone at scale. Psychiatrist-only reminders happen too late in the cycle and burden clinical time with administrative tasks.

## Consequences

- Requires commitment session counting logic in the platform
- Depends on accurate initial commitment data and renewal tracking
- Adds a new task type to the secretarial workflow
- Must be coordinated with the psychiatrist alert system for consistent patient messaging

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]