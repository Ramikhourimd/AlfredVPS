---
alfred_tags:
- healthcare/commitment-expiry
- proactive-alerts
- workflow-automation
approved_by: []
based_on:
- '[[constraint/No Commitment Renewal Workflow Exists in Retool]]'
- '[[constraint/No Renewal Commitment Entry Mechanism Exists in Retool]]'
challenged_by: []
confidence: medium
created: '2026-02-28'
decided_by: []
janitor_note: 'LINK001: Telia''z wikilink is valid YAML apostrophe escaping (Telia''''z
  → Telia''z), not a broken link. Base view embeds learn-decision.base#Based On and
  learn-decision.base#Related reference _bases/ infrastructure that does not yet exist
  — embeds preserved. ORPHAN001 acknowledged — decision may gain inbound links as
  related records grow.'
name: Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Add Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[task/Build Commitment Renewal Workflow in Retool]]'
session: null
source: Requirements discussion with Shachar mock-up
source_date: '2025-01-12'
status: draft
supports: []
tags: []
type: decision
---

# Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds

## Context

Patients have a finite number of sessions under each Maccabi commitment (e.g., intake + 16 CM follow-ups + 4 psychiatric follow-ups). Psychiatrists entering sessions have no visibility into whether the patient's commitment is about to expire. Without alerts, sessions may proceed without renewal arrangements, creating billing and continuity issues.

## Options Considered

1. **No alert** — Rely on administrative tracking outside the system
2. **Single alert at last session** — Pop-up only when commitment is fully exhausted
3. **Two-tier alert** — Warning at 2 sessions before last, critical at last session

## Decision

Implement a two-tier pop-up alert system: a warning pop-up appears when the patient has 2 sessions remaining under the current commitment, and a critical pop-up appears on the last session.

## Rationale

Two tiers give psychiatrists advance notice to discuss renewal with the patient before the commitment expires, rather than discovering it at the final session when it may be too late to arrange continuity. Shachar demonstrated a mock-up concept for this pattern.

## Consequences

- Requires session balance tracking logic integrated with the meeting screen
- Pop-ups must trigger on meeting screen entry, before the session starts
- Depends on commitment renewal workflow being built (currently no entry mechanism exists)
- Warning message: "Commitment expiring soon — X sessions remaining"
- Critical message: "This is the last session under the current commitment — renewal required"

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]