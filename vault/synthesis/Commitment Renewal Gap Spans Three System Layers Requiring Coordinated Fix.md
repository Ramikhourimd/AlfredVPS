---
alfred_tags:
- clinic/operations
- patient/commitment-gaps
- system/lifecycle
cluster_sources:
- '[[constraint/No Commitment Renewal Workflow Exists in Retool]]'
- '[[constraint/No System Entry Point for Commitment Renewal Numbers]]'
- '[[constraint/Commitment Renewal Validation Requires Manual Secretary Check Against
  Maccabi Portal]]'
- '[[decision/Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds]]'
- '[[task/Build Commitment Renewal Workflow in Retool]]'
- '[[task/Add Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[task/Add Secretary Tasks for Commitment Renewal Reminders]]'
confidence: medium
created: '2026-03-03'
janitor_note: LINK001 — constraint wikilink is valid (YAML line-wrap false positive,
  target verified). Telia'z AI Clinical Platform wikilink is valid (YAML escaping
  false positive). ORPHAN001 — no inbound links; synthesis is recent (2026-03-03),
  consider linking from project/Telia'z AI Clinical Platform.
name: Commitment Renewal Gap Spans Three System Layers Requiring Coordinated Fix
project:
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.7
  context: Shared issues in process tracking & coord
  source: synthesis/Commitment Renewal Gap Spans Three System Layers Requiring Coordinated
    Fix.md
  target: synthesis/Operational Improvement Requirements Recur Verbatim Across Sessions
    Without Implementation Tracking.md
  type: related-to
- confidence: 0.85
  context: Overlapping commitment lifecycle gaps
  source: synthesis/Commitment Renewal Gap Spans Three System Layers Requiring Coordinated
    Fix.md
  target: synthesis/Patient Commitment Lifecycle Gap Persisted Unresolved Across Seven
    Months.md
  type: related-to
- confidence: 0.8
  context: Gap depends on platform lifecycle limits
  source: synthesis/Commitment Renewal Gap Spans Three System Layers Requiring Coordinated
    Fix.md
  target: synthesis/Retool Clinical Platform Designed for Intake Funnel Without Patient
    Lifecycle Management.md
  type: depends-on
status: draft
supports:
- '[[decision/Two-Tier Commitment Expiry Alert at Warning and Critical Thresholds]]'
type: synthesis
---

# Commitment Renewal Gap Spans Three System Layers Requiring Coordinated Fix

## Insight

The commitment renewal problem is not a single missing feature — it spans three distinct system layers that must all be addressed for the workflow to function. Separately filed tasks and constraints all trace back to the same root gap, but none can be solved in isolation.

## Evidence

Three separate constraints document the gap:
- No input field exists for renewal commitment numbers (UI layer)
- Validation requires manual secretary checks against Maccabi portal (validation layer)
- No alerts warn psychiatrists when sessions are running out (alerting layer)

Three separate tasks attempt to address it:
- Build Commitment Renewal Workflow — UI input and validation
- Add Commitment Expiry Alerts — psychiatrist session warnings
- Add Secretary Tasks for Commitment Renewal Reminders — workflow integration

A decision has been made on the alert thresholds (two-tier warning and critical), but the underlying input and validation infrastructure does not exist yet.

## Implications

These three layers have implicit dependencies: alerts cannot fire without session balance data, session balances cannot update without renewal input, and renewal input requires validation. The work must be sequenced — UI input and validation first, then session balance tracking, then alerts. Attempting to build any single layer without the others produces an incomplete, non-functional workflow.

## Applicability

This pattern — a single business need requiring coordinated changes across UI, data, and notification layers — is likely to recur with other Maccabi integration points (e.g., new commitment types, different HMO providers in the UK expansion).