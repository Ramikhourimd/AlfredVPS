---
authority: Maccabi Healthcare Services
created: '2026-03-03'
janitor_note: 'LINK001 false positives: project/Telia''z Clinic Israel and project/Telia''z
  AI Clinical Platform wikilinks resolve correctly (YAML single-quote escaping produces
  Telia''''z in raw YAML, which is valid). No base view embed issues. No structural
  problems found. Swept 2026-03-15.'
location:
- '[[project/Telia''z Clinic Israel]]'
name: Maccabi HMO Prohibits Email-Based Patient Document Delivery
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
- '[[org/Maccabi Healthcare Services]]'
- '[[decision/Deliver ER Referral Letters via HealthyMind App Not Email]]'
source: Maccabi Healthcare Services policy
source_date: '2025-11-10'
status: active
type: constraint
---

# Maccabi HMO Prohibits Email-Based Patient Document Delivery

## Constraint

Maccabi Healthcare Services has objected to email-based delivery of clinical documents to patients. Patient-facing documents (referral letters, reports, clinical summaries) must be delivered through the HealthyMind app or Clickx system rather than via email as the default channel.

## Source

Maccabi HMO policy communicated during previous interactions. Referenced by Rami during the 2025-11-10 clinic meeting when discussing the ER referral form delivery mechanism.

## Implications

- All patient-facing document delivery features must default to app-based delivery (HealthyMind / Clickx).
- Email delivery cannot be the primary channel for any clinical document type.
- An emergency override for email delivery may be acceptable for urgent clinical situations (e.g., ER referrals), but must not be the default path.
- This constraint applies across the platform, not just to referral letters — any new feature involving patient document delivery must comply.

## Expiry / Review

No expiry known. This appears to be a standing policy from Maccabi. Should be re-validated if document delivery architecture changes or if Maccabi updates their policy.
