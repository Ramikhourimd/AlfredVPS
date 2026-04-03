---
alfred_tags:
- prescriptions/regulations
- clinics/uk
- pharmacies/israel
authority: Clalit Health Services
created: '2025-11-09'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  related_to value migrated to related array (2026-03-31). Base view embeds (learn-constraint.base)
  reference non-existent _bases/ file — vault-wide issue, embeds preserved.
name: Clalit Pharmacies Do Not Accept External Prescriptions
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[org/Clalit Health Services]]'
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
- '[[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]]'
related_to: ''
relationships:
- confidence: 0.7
  context: Similar internal prescription system needs
  source: constraint/Clalit Pharmacies Do Not Accept External Prescriptions.md
  target: constraint/UK Clinic Launch Requires Prescription System Not Yet Built.md
  type: related-to
- confidence: 0.95
  context: Illustrates Israel difference for UK req
  source: constraint/Clalit Pharmacies Do Not Accept External Prescriptions.md
  target: constraint/UK Clinic Requires Actual Prescription Issuance Unlike Israel.md
  type: supports
- confidence: 0.55
  context: Prescription compliance parallels
  source: constraint/Clalit Pharmacies Do Not Accept External Prescriptions.md
  target: constraint/UK Controlled Substance Prescriptions Require Specialized Regulatory
    Compliance.md
  type: related-to
- confidence: 0.55
  context: Prescription system/format parallels
  source: constraint/Clalit Pharmacies Do Not Accept External Prescriptions.md
  target: constraint/UK Controlled Substance Prescriptions Require Specific Format
    and System.md
  type: related-to
- confidence: 0.6
  context: Issuance constraint parallels
  source: constraint/Clalit Pharmacies Do Not Accept External Prescriptions.md
  target: constraint/UK Prescription Issuance Requires Separate Regulatory Compliance.md
  type: related-to
source: Clalit Health Services internal pharmacy policy
source_date: '2025-11-09'
status: active
type: constraint
---

# Clalit Pharmacies Do Not Accept External Prescriptions

## Constraint

Clalit-owned pharmacies do not accept private or external prescriptions (unlike Maccabi's Haidok system which allows this). Only a limited number of private pharmacies (e.g., Super-Pharm) accept private prescriptions, and even fewer of those work with Clalit billing. This means Telia'z psychiatrists cannot directly prescribe medications that Clalit patients can fill at their usual pharmacy.

## Source

Identified during Telia'z team preparation meeting (2025-11-09) ahead of operational partnership kickoff with Clalit. Based on team's operational knowledge of the Israeli HMO pharmacy landscape.

## Implications

- Telia'z psychiatric recommendations must be routed through the patient's Clalit family doctor (GP), who then issues the prescription within the Clalit system
- Each patient encounter potentially generates an additional GP visit, increasing Clalit's internal workload
- This may create budget concerns for the Clalit partnership contact, as more GP referrals mean more internal costs
- Alternative: request Clicks (Clalit EHR) access solely for prescription entry — but this risks scope creep and added demands from Clalit
- This is a structural blocker for starting clinical operations with Clalit patients

## Expiry / Review

Ongoing constraint tied to Clalit pharmacy policy. Review if Clalit changes external prescription acceptance policies.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]



## Reconfirmed (2025-11-10)

This constraint was reconfirmed during the [[conversation/Clalit South Referral System Setup Meeting 2025-11-10]]. Workaround options include using non-Clalit pharmacies or routing prescriptions through the patient's Clalit primary care physician.