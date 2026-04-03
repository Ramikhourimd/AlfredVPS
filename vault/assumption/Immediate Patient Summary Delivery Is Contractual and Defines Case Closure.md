---
alfred_tags:
- healthcare/patient-summary-delivery
- clinic/contractual-obligations
- workflow/consent
based_on:
- '[[note/Patient Summary Immediate Delivery Expectation Discussion 2025-09-22]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-13'
invalidated_by: []
janitor_note: 'LINK001 — base view embeds (learn-assumption.base#Depends On This,
  #Related) do not exist (vault-wide infrastructure issue). Telia''z wikilinks valid
  (targets exist). ORPHAN001 — no inbound wikilinks; consider linking from a parent
  record.'
name: Immediate Patient Summary Delivery Is Contractual and Defines Case Closure
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[project/Telia''z AI Clinical Platform]]'
relationships:
- confidence: 0.85
  context: Both cover PS delivery and contractual aspects
  source: assumption/Immediate Patient Summary Delivery Is Contractual and Defines
    Case Closure.md
  target: note/Patient Summary Consent and Delivery Workflow Discussion 2025-09-22.md
  type: related-to
- confidence: 0.95
  context: Direct overlap on immediate PS delivery expectations
  source: assumption/Immediate Patient Summary Delivery Is Contractual and Defines
    Case Closure.md
  target: note/Patient Summary Immediate Delivery Expectation Discussion 2025-09-22.md
  type: related-to
source: Patient Summary Immediate Delivery Expectation Discussion 2025-09-22
source_date: '2025-09-22'
status: active
tags: []
type: assumption
---

# Immediate Patient Summary Delivery Is Contractual and Defines Case Closure

## Claim

The clinic's agreement with HMO partners requires that patient summaries be delivered immediately after the clinical session. Furthermore, summary delivery is the operational event that constitutes "closing" a patient case — once the summary is generated and delivered, the patient encounter is considered complete from the clinic's workflow perspective.

## Basis

During a work call on 2025-09-22 (Rosh Hashanah eve), team members explicitly stated that "per the agreement, patient summaries must be delivered immediately after the session." They emphasized that since the entire operation is digital, there is no technical reason for delay. The speakers also articulated that "once the summary is generated and delivered, the patient is considered closed" — establishing summary delivery as the formal case closure trigger, not the session end itself.

## Evidence Trail

- 2025-09-22: Confirmed as contractual obligation during team call
- The digital nature of the system means this should be automatable without manual intervention

## Impact

This assumption has significant operational implications:
- Any delay in AI summary generation or delivery directly delays case closure
- Summary approval bottlenecks (e.g., psychiatrist review time) extend the case lifecycle beyond the session
- Measuring "summary delivery time" becomes a proxy for operational efficiency
- Platform reliability for summary generation is a contractual compliance requirement, not just a quality metric

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]