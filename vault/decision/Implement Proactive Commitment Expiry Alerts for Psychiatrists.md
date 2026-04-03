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
name: Implement Proactive Commitment Expiry Alerts for Psychiatrists
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[decision/Automate Secretary Pre-Session Calls for Commitment Expiry Management]]'
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.8
  context: Two-tier details psychiatrist alerts
  source: decision/Implement Proactive Commitment Expiry Alerts for Psychiatrists.md
  target: decision/Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds.md
  type: supports
session: null
source: Rami Khouri
source_date: '2025-08-01'
status: draft
supports:
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
tags: []
type: decision
---

# Implement Proactive Commitment Expiry Alerts for Psychiatrists

## Context

When patients approach the end of their Maccabi commitment cycle (16 case manager sessions + 4 psychiatric follow-ups), there is no system-level warning. Psychiatrists discover mid-session that a patient's commitment has expired, creating awkward clinical situations and billing gaps.

## Options Considered

1. **Proactive in-session alerts** — Pop-up warnings when opening the last 2 sessions of a commitment cycle, with a prominent final-session warning
2. **Post-session administrative review** — Secretaries manually check commitment balances after sessions
3. **No intervention** — Continue current approach where expiry is discovered ad hoc

## Decision

Implement a two-tier alert system within the clinical platform:
- **Tier 1 (Warning):** Pop-up alert when psychiatrist opens a session that is within the last 2 sessions of the current commitment — "Commitment approaching expiry — renewal needed"
- **Tier 2 (Final):** Prominent warning on the final session under the current commitment — "This is the last session under the current commitment — renewal required"

## Rationale

Psychiatrists are the last clinical touchpoint before commitment expiry. Alerting them in-session gives patients and the administrative team time to obtain renewals before a gap occurs. Post-session review alone is too late — the session has already been delivered against an expiring commitment.

## Consequences

- Requires Retool/platform development work to implement session counting and alert triggers
- Depends on accurate commitment data being available in the system (currently not supported for renewals)
- Creates a clear clinical-administrative handoff: psychiatrist flags, secretary follows up

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]