---
approved_by: []
based_on:
- '[[decision/On-Call Arrangement Continues Through December 2025]]'
challenged_by: []
confidence: medium
created: '2025-09-21'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 false-positive: project/Telia''z Clinic Israel wikilink is
  valid (YAML single-quote escaping). learn-decision.base embeds are base view references
  — _bases/ directory does not exist. BODY issue: entire record body is duplicated
  (two complete copies of all sections plus duplicate base view embeds) — owner should
  remove the duplicate content below the first --- separator.'
name: Implement Automated Backup for On-Call Doctors
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/On-Call Backup System Discussion 2025-09-21]]'
- '[[conversation/Rami Oren On-Call Compensation Discussion 2025-09-01]]'
- '[[person/Roy Shur]]'
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
- '[[task/Add Acknowledgment Button to On-Call Alert Calls]]'
session: null
source: On-call backup system discussion 2025-09-21
source_date: '2025-09-21'
status: draft
supports: []
tags: []
type: decision
---

# Implement Automated Backup for On-Call Doctors

## Context

The on-call system at [[project/Telia'z Clinic Israel]] relies on a single on-call doctor at any given time. If that doctor becomes unexpectedly unavailable (illness, accident, emergency), there is no automated fallback — creating a gap in patient coverage. This was discussed on 2025-09-21 as a follow-up to the on-call compensation framework agreed in [[decision/On-Call Arrangement Continues Through December 2025]].

## Options Considered

1. **Automated backup with escalation** — Always designate a secondary on-call doctor. If the primary does not acknowledge within a defined window, the system automatically calls the backup.
2. **Manual backup** — Rely on the primary doctor to manually call a colleague if unavailable.
3. **No backup** — Accept the risk of a gap in rare cases.

## Decision

Option 1: Implement an automated backup system where a designated backup doctor receives escalated calls when the primary on-call doctor fails to acknowledge.

## Rationale

- The system handles rare but critical scenarios (illness, accident) without relying on the unavailable doctor to initiate their own coverage
- The backup role carries lower readiness expectations, which is acceptable given the rarity of use
- Automated escalation removes human coordination delay in emergencies

## Consequences

- Requires identifying and scheduling a backup doctor for each on-call rotation
- The platform or phone system needs to support two-tier escalation logic
- Backup doctors need to understand their role is emergency-only, not routine

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]

# Implement Automated Backup for On-Call Doctors

## Context

The on-call system at [[project/Telia'z Clinic Israel]] relies on a single on-call doctor at any given time. If that doctor becomes unexpectedly unavailable (illness, accident, emergency), there is no automated fallback — creating a gap in patient coverage. This was discussed on 2025-09-21 as a follow-up to the on-call compensation framework agreed in [[decision/On-Call Arrangement Continues Through December 2025]].

## Options Considered

1. **Automated backup with escalation** — Always designate a secondary on-call doctor. If the primary does not acknowledge within a defined window, the system automatically calls the backup.
2. **Manual backup** — Rely on the primary doctor to manually call a colleague if unavailable.
3. **No backup** — Accept the risk of a gap in rare cases.

## Decision

Option 1: Implement an automated backup system where a designated backup doctor receives escalated calls when the primary on-call doctor fails to acknowledge.

## Rationale

- The system handles rare but critical scenarios (illness, accident) without relying on the unavailable doctor to initiate their own coverage
- The backup role carries lower readiness expectations, which is acceptable given the rarity of use
- Automated escalation removes human coordination delay in emergencies

## Consequences

- Requires identifying and scheduling a backup doctor for each on-call rotation
- The platform or phone system needs to support two-tier escalation logic
- Backup doctors need to understand their role is emergency-only, not routine

![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
