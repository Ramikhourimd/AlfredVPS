---
alfred_tags:
- maccabi/hmo-commitments
- clinic/uncompensated-sessions
based_on:
- '[[note/Clinic Manager KPI Framework and Bonus Structure 2025-03-27]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
confidence: medium
created: '2026-03-15'
janitor_note: 'LINK001 — (1) Telia''z and constraint wikilinks are valid (YAML escaping
  false positives — targets verified to exist). (2) Base view embeds (learn-assumption.base#Depends
  On This, learn-assumption.base#Related) reference _bases/learn-assumption.base which
  does not exist — vault-wide infrastructure gap, embeds preserved. Previous FM001
  fix: record was rebuilt from empty state on 2026-03-15. ORPHAN001 — no inbound links;
  consider linking from project/Telia''z Clinic Israel or constraint/Clinic Revenue
  Dependent on HMO Contracts.'
name: Unresolved HMO Commitment Gaps Represent Uncompensated Clinical Sessions
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[decision/Measure Clinic Efficiency by Monetary Utilization Gap]]'
- '[[constraint/Maccabi Commitment Validation Requires Manual Portal Check Against
  MADAC]]'
source: KPI framework meeting and operational discussions
source_date: '2025-03-27'
status: active
type: assumption
---

# Unresolved HMO Commitment Gaps Represent Uncompensated Clinical Sessions

## Claim

The clinic is performing clinical sessions against expired or incomplete HMO commitments, resulting in uncompensated work. Two specific gap types were identified in the KPI framework meeting:

1. **Pre-treatment hold gap:** Patients are approved for treatment but waiting because their HMO commitment (hithayvut) is incomplete. Sessions may proceed before the commitment is properly activated.
2. **Mid-treatment renewal gap:** Patients already in treatment who need a commitment renewal continue receiving sessions while the renewal is pending or unprocessed.

In both cases, the clinic delivers clinical services without confirmed billing authorization from Maccabi.

## Basis

The 2025-03-27 KPI meeting explicitly identified HMO Commitment Closure Rate as one of four core KPI domains. The target was set at 100% — "every patient should" have a valid commitment. The fact that this was flagged as a KPI target implies the current rate is materially below 100%. Combined with the known system gap (no renewal tracking in Retool), the clinic has no mechanism to prevent or even detect sessions delivered against expired commitments.

## Evidence Trail

- 2025-01-12: System gap in commitment renewals identified
- 2025-03-27: HMO commitment closure elevated to core KPI; 100% target set
- 2025-08-01: Same system gap still present; at least one patient submitted renewal with nowhere to record it

## Impact

- Direct revenue leakage: sessions performed without valid commitment may not be billable to Maccabi
- Scale amplifier: as patient volume grows toward 7,000+, the absolute number of gap sessions increases
- Feeds into the monetary utilization gap KPI — the gap between potential and actual revenue
- May affect HMO contract negotiations if Maccabi identifies billing anomalies

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
