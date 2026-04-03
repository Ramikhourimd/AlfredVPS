---
alfred_instructions: null
channel: email
created: '2026-03-01'
date: '2025-11-10'
external_id: null
fork_reason: null
forked_from: null
janitor_note: 'LINK001 — base view embeds (conversation-detail.base#Messages, #Tasks,
  #Related) reference _bases/conversation-detail.base which does not exist. All Telia''z
  wikilinks are valid (YAML escaping false positive).'
last_activity: '2025-11-10'
message_count: 0
opened: '2025-11-10'
org: null
participants:
- '[[person/Rami Khouri]]'
- '[[person/Dekkel Taliaz]]'
- '[[person/Roy Shur]]'
project: null
related: []
related_to:
- '[[org/Clalit Health Services]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[note/Clalit South Psychiatric Referral and Subscription System Design 2025-11-10]]'
- '[[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09]]'
relationships: []
status: resolved
subject: Clalit South Referral System Setup Meeting 2025-11-10
tags:
- clalit
- referral-system
- subscription
- psychiatry
type: conversation
---

# Clalit South Referral System Setup Meeting 2025-11-10

## Context

This was the operational meeting with Tzachi from Clalit Health Services (South District) to establish the psychiatric referral and subscription system between Telia'z and Clalit. This meeting followed the [[conversation/Clalit Partnership Operational Planning Meeting 2025-11-09|internal preparation meeting held the day before]].

## Attendees

- **Rami Khouri** ([[person/Rami Khouri]]) — Medical Director, Telia'z
- **Dekkel** ([[person/Dekkel Taliaz]]) — Telia'z
- **Roy/Roui** ([[person/Roy Shur]]) — Operations, Telia'z
- **Tzachi** — Clalit Health Services, South District representative
- **Michal Boguz** ([[person/Michal Boguz]]) — Clalit administrative manager, South District (mentioned)

## Key Discussion Topics

### 1. Subscription Types and Authorization Flow

Tzachi explained the two subscription pathways available through Clalit:

- **Diagnostic Subscription**: A single-visit referral for psychiatric evaluation. Form 17 is generated automatically and does not require manual district approval.
- **Treatment Subscription**: An ongoing treatment subscription that requires Form 17 approval from the district contact (Tzachi or Michal Boguz).

The team agreed to [[decision/Clalit South Pilot Starts With Diagnostic Subscriptions Only|start with diagnostic subscriptions only]] for the pilot phase, since these do not require manual Form 17 approval and can scale faster.

### 2. Form 17 Process

- For diagnostic subscriptions, Form 17 is generated automatically by the Clalit system when the referring physician creates the referral.
- For treatment subscriptions, Form 17 requires manual approval from the district level (Tzachi or [[person/Michal Boguz]]).
- The existing constraint [[constraint/Clalit Form 17 Requires Manual Approval by District Contact]] applies specifically to treatment subscriptions, not diagnostic ones.

### 3. Patient Continuation Policy

Tzachi confirmed that [[decision/Clalit South Patients Can Continue Treatment Indefinitely|patients referred through Clalit can continue treatment indefinitely]] — there is no built-in limit on the number of sessions or duration. This is a significant advantage over some other HMO referral models.

### 4. Volume Projections

Tzachi indicated that Clalit South District handles a large patient volume. The team discussed [[assumption/Clalit South Will Generate 200 Patients Per Week Within Three Months|a projection of approximately 200 patients per week within three months]] of launch.

### 5. Prescription and Pharmacy Constraints

The existing constraint [[constraint/Clalit Pharmacies Do Not Accept External Prescriptions]] was discussed. Prescriptions written by Telia'z psychiatrists cannot be filled at Clalit pharmacies. Patients would need to use non-Clalit pharmacies or have prescriptions routed through their Clalit primary care physician.

### 6. Billing Codes and Rates

Billing codes for psychiatry consultations were discussed. The standard Clalit billing framework applies, with specific codes for diagnostic evaluations versus ongoing treatment sessions.

### 7. Target Launch Date

The team agreed on a target launch date of November 20, 2025 for the pilot program.

### 8. Hosen Patient Overflow

The closure of Hosen (a mental health facility in the south) was discussed as a potential source of patients who need to be absorbed into the new system. This represents an immediate pipeline opportunity. See [[task/Contact Former Hosen Patients for Clalit South Pipeline]].

### 9. Clalit System Characteristics

The Clalit IT system was described as slower and heavier compared to Maccabi's system. The team needs to [[task/Evaluate Platform Adaptation for Clalit Subscription Workflow|evaluate whether the Telia'z platform needs adaptation]] to accommodate Clalit's system workflow.

### 10. BI System Integration

Discussion about connecting to Clalit's BI (Business Intelligence) system for data tracking and reporting. A fax number is needed for certain referral communications — see [[task/Obtain Clalit South District Fax Number]].

## Outcomes

1. Diagnostic subscriptions will be the starting point (no Form 17 approval needed)
2. Treatment subscriptions to be added later once Form 17 workflow is streamlined
3. Target launch: November 20, 2025
4. Telia'z to pilot the Form 17 process — see [[task/Pilot Form 17 Process With Clalit South District]]
5. Need to obtain fax number and evaluate platform adaptation

## Source

Processed from inbox recording transcript (2025-11-10).

---
## Messages
![[conversation-detail.base#Messages]]

## Tasks
![[conversation-detail.base#Tasks]]

## Related
![[conversation-detail.base#Related]]
