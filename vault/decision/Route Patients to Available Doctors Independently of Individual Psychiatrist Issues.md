---
alfred_tags:
- clinic/operations
- management/restructuring
- leadership/transition
approved_by: []
based_on:
- '[[note/Clinic Operations Coordination 2025-12-02]]'
- '[[note/Clinic Israel Operations Discussion 2025-12-02]]'
challenged_by: []
confidence: high
created: '2026-03-12'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001s for Telia''z project and synthesis links are false positives
  (files exist). Base embed LINK001s (learn-decision.base) are vault-wide infrastructure
  gap. Duplicate base embeds in body noted but NOT removed per rules. ORPHAN001: no
  inbound links — human review needed. Flagged 2026-03-15.'
name: Route Patients to Available Doctors Independently of Individual Psychiatrist
  Issues
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Acute Clinical Supervision Depends on Single-Clinician Ad Hoc Availability]]'
- '[[synthesis/Manual Single-Person Dependencies Create Cascading Failure Points Across
  Clinic Operations]]'
session: ''
source: Rami Khouri during operations coordination call
source_date: '2025-12-02'
status: final
supports: []
tags: []
type: decision
---

# Route Patients to Available Doctors Independently of Individual Psychiatrist Issues

## Context

During the 2025-12-02 operations call, Basel raised that psychiatrist Elias had no available patient slots. Basel's instinct was to address this as a single problem — have another clinician take Elias's patients. Rami intervened to separate two distinct concerns that were being conflated.

## Options Considered

1. **Treat as one problem** — Reassign Elias's patients to another clinician, addressing both patient access and the Elias situation simultaneously
2. **Separate the two problems** — Route patients to any available doctor immediately (patient access issue), while independently and separately addressing Elias's performance/availability (management issue)

## Decision

Always separate patient access urgency from individual staff performance management. When a specific psychiatrist is unavailable or underperforming:
- **Immediate action**: Check if other doctors have available capacity and route patients there — this is a clinic operations problem, not an Elias-specific problem
- **Separate track**: Address the individual psychiatrist's situation as a distinct management matter with its own timeline and considerations

## Rationale

Conflating the two issues causes delays in patient access while the management situation is being resolved. The clinic's obligation to patients should not wait for resolution of staff issues. Additionally, the management response to an individual psychiatrist requires different considerations (employment law, relationship management, clinical assessment) than the operational task of filling appointment slots.

## Consequences

- Patients get faster access to care when individual providers are unavailable
- Management has space to address staff issues thoughtfully without time pressure from patient backlog
- Requires the operations team to maintain visibility into real-time provider availability across all psychiatrists
- Establishes a principle that patient access is never held hostage to any single provider's situation

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]