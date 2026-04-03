---
authority: Israeli Ministry of Health
created: '2026-03-14'
janitor_note: LINK001 — Telia'z wikilink is valid YAML escaping (false positive).
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z Clinic Israel.
name: Cross-Institution Patient Data Sharing Requires Explicit Consent Under Israeli
  Law
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Patient Summary Consent and Delivery Workflow Discussion 2025-09-22]]'
source: Israeli Patient Rights Law
source_date: '2025-09-22'
status: active
type: constraint
---

# Cross-Institution Patient Data Sharing Requires Explicit Consent Under Israeli Law

## Constraint

Under Israeli patient rights law, two practitioners at different institutions require explicit patient consent to share clinical information. Practitioners within the same institution operate under implied consent. This directly affects the patient summary delivery workflow — summaries cannot be sent to referring therapists at external organizations without prior signed consent from the patient.

## Source

Rami Khouri explained this legal framework during the 2025-09-22 on-call incident review meeting. The rule was surfaced because the on-call incident deviated from normal workflow: no consent form was collected, no patient file was created, and the summary had to be sent manually.

## Implications

- Patient consent forms must be collected before any cross-institution data sharing
- The automated summary delivery workflow depends on consent being captured at intake
- When the consent workflow breaks (as in the on-call incident), manual workarounds are needed with legal risk
- Platform must enforce consent collection as a prerequisite for summary delivery

## Expiry / Review

Permanent regulatory requirement. Review when consent workflow is redesigned or when new institutional partnerships (Clalit, UK) change the data sharing landscape.
