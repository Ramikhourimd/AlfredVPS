---
alfred_tags:
- maccabi/commitments
- renewal/constraints
- retool/limitations
authority: Retool platform configuration
created: '2026-02-26'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — vault-wide infrastructure gap.'
name: No System Support for Maccabi Commitment Renewals in Retool
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[constraint/Clinic Revenue Dependent on HMO Contracts With Maccabi and Clalit]]'
relationships:
- confidence: 1.0
  context: No support explains manual process
  source: constraint/No System Support for Maccabi Commitment Renewals in Retool.md
  target: constraint/Commitment Renewal Validation Requires Manual Secretary Check
    Against Maccabi Portal.md
  type: supports
source: System limitation identified in operational meetings
source_date: '2025-08-01'
status: active
type: constraint
---

# No System Support for Maccabi Commitment Renewals in Retool

## Constraint

The clinic's Retool system has no support for the patient commitment renewal lifecycle. When patients exhaust their initial Maccabi commitment (16 case manager sessions + 4 psychiatric follow-ups), the system cannot process renewals. Specifically:

1. **No renewal field** — There is no field in Retool to enter a renewal commitment number
2. **No validation workflow** — No process to verify renewal commitments against the Maccabi portal
3. **No expiry alerts** — Psychiatrists receive no warning when a patient is approaching the end of their commitment
4. **No secretary automation** — No automated task triggers for secretaries to prompt patients about renewals
5. **No session counter reset** — The remaining sessions tracker cannot reset or update when a new commitment is entered

At least one patient has already submitted a renewal commitment with nowhere to record it.

## Source

Identified in two separate operational meetings (2025-01-12 and 2025-08-01) between Rami Khouri and Shira Lachman. The gap was confirmed in both meetings, indicating it remained unresolved for at least 7 months.

## Implications

- Patients who complete their initial commitment cycle hit a dead-end in the system
- Renewal commitments arrive with no place to record them, risking lost data
- Psychiatrists cannot proactively manage commitment transitions during sessions
- Secretaries cannot systematically track which patients need renewal prompts
- The clinic may be performing sessions against expired commitments, creating billing risk

## Expiry / Review

This constraint persists until Retool is updated with renewal fields, validation, and automation. Review when the product team schedules commitment renewal system work.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]