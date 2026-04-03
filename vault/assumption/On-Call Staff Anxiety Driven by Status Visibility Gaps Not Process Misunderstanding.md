---
alfred_tags:
- psychiatry/on-call
- system-gaps
based_on:
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
confidence: high
confirmed_by:
- '[[decision/Deploy Real-Time On-Call Status Dashboard for Remote Monitoring]]'
created: '2026-03-30'
janitor_note: 'LINK001 — base view embeds (learn-assumption.base#Depends On This,
  #Related) reference _bases/learn-assumption.base which does not exist — vault-wide
  infrastructure gap, embeds preserved per rules. ORPHAN001 — no inbound wikilinks;
  consider linking from project/Telia''z Clinic Israel or related on-call operations
  records. Swept 2026-03-31.'
name: On-Call Staff Anxiety Driven by Status Visibility Gaps Not Process Misunderstanding
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[assumption/On-Call Alert Failure Caused by Caller ID Anonymization Not Process
  Ignorance]]'
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
- '[[decision/Adopt Negative-Feedback Only Alerting for On-Call Escalation]]'
source: Ra'ut's experience during first on-call alert activation, September 2025
source_date: '2025-09-22'
status: confirmed
type: assumption
---

# On-Call Staff Anxiety Driven by Status Visibility Gaps Not Process Misunderstanding

## Claim

When on-call alerts are activated, staff anxiety is driven primarily by inability to see whether the alert was received and acted upon — not by misunderstanding the process or doubting that an on-call system exists. Ra'ut understood the system, followed the correct steps, and knew an on-call psychiatrist was designated. Her distress came entirely from the black box between "alert sent" and "response delivered."

## Basis

During the first real on-call activation (September 2025), Ra'ut opened a ticket correctly and expected a callback within 30 minutes per the agreement. The callback didn't come (due to caller ID anonymization — Atef didn't recognize the call). Ra'ut tried to reach Rami (abroad), escalated via message, and experienced significant stress. The patient WAS ultimately seen — the service delivered — but the communication gap caused unnecessary staff anxiety.

Key clarification from the debrief: Ra'ut DID understand the on-call system existed. Her issue was NOT the absence of an on-call doctor, but the lack of visibility into whether the process was working.

## Evidence Trail

- **2025-09-21:** First real on-call alert — caller ID issue caused missed callback, Ra'ut experienced stress despite correct process execution
- **2025-09-22:** Case review confirmed the root cause was visibility, not process. Shachar built a real-time dashboard as the solution
- **Confirmed:** The dashboard deployment directly addresses this assumption, validating that visibility was the core issue

## Impact

- System design should prioritize transparency and status visibility over process documentation
- Future on-call improvements should focus on making the response chain observable, not just reliable
- Applies to other operational workflows where staff handoffs occur without confirmation (e.g., secretary scheduling, commitment renewals)

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]