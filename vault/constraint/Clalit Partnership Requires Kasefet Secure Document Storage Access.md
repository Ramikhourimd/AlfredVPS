---
authority: Clalit Health Services
created: '2026-03-17'
janitor_note: 'LINK001 false positives: project/Teliaz Clinic Israel wikilink is valid
  (YAML single-quote escaping). constraint/Clalit Referral System link target verified
  (exists). ORPHAN001 — no inbound wikilinks; consider linking from project/Teliaz
  Clinic Israel or related Clalit constraints.'
name: Clalit Partnership Requires Kasefet Secure Document Storage Access
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Obtain Clalit System Access and Contact Details]]'
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[constraint/Clalit Referral System Is Slower and Heavier Than Maccabi Requiring
  Platform Adaptation]]'
- '[[decision/Require Clalit Form 17 Approval Before Patient Referral to Clinic]]'
source: Clalit contract requirement for clinical summary sharing
source_date: '2025-11-09'
status: active
type: constraint
---

# Clalit Partnership Requires Kasefet Secure Document Storage Access

## Constraint

The Clalit partnership contract requires clinical summaries to be shared via Kasefet (כספת — "safe"), Clalit's secure document storage system. The clinic cannot fulfill its contractual obligation to share patient summaries with Clalit without active access to this system.

## Source

Identified during the 2025-11-09 Clalit partnership operational planning meeting. The team catalogued required system access, including Kasefet for document sharing, IT/admin contacts at Clalit, and potentially Clicks for prescription entry.

## Implications

- Clinic staff need Kasefet credentials provisioned before Clalit patients can be fully processed
- The access provisioning timeline is unknown and depends on Clalit IT responsiveness
- Without Kasefet access, clinical summaries cannot be shared per contract, potentially blocking patient flow
- This is an additional system (beyond Clickx and Retool) that staff must learn and maintain

## Expiry / Review

Active for the duration of the Clalit partnership. Review if Clalit introduces alternative document sharing mechanisms.
