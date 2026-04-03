---
alfred_tags:
- psychiatry/on-call
- clinical-operations
approved_by: []
based_on:
- '[[note/On-Call Case Review Ra''ut Communication Gaps 2025-09-22]]'
- '[[note/On-Call Alert System First Activation Issues 2025-09-21]]'
challenged_by: []
confidence: high
created: '2026-03-30'
decided_by:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
janitor_note: 'LINK001 — Telia''z and Ra''ut wikilinks are valid (YAML single-quote
  escaping false positive). Base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist — vault-wide infrastructure
  gap, embeds preserved. Duplicate base embeds in body noted but NOT removed per rules.'
name: Deploy Real-Time On-Call Status Dashboard for Remote Monitoring
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/On-Call Alert System Debriefing 2025-09-21]]'
- '[[constraint/On-Call Alert Chain Has No Automated Fallback When Manual Steps Fail]]'
session: null
source: Shachar (CTO) built after first on-call alert failure
source_date: '2025-09-22'
status: final
supports:
- '[[decision/Adopt Negative-Feedback Only Alerting for On-Call Escalation]]'
- '[[decision/Rami Owns On-Call Project Management End-to-End]]'
tags: []
type: decision
---

# Deploy Real-Time On-Call Status Dashboard for Remote Monitoring

## Context

After the first real on-call alert activation (September 2025), Ra'ut (case manager/intake coordinator) experienced significant stress — not because the on-call system was absent, but because she had no visibility into whether the on-call psychiatrist had received and acted on the alert. The psychiatrist (Atef) did not realize the incoming call was from the on-call system due to caller ID anonymization.

## Options Considered

1. **Text/call confirmation chain** — Manual confirmation via phone/WhatsApp that the on-call doctor received the alert
2. **Real-time status dashboard** — Mobile-friendly web dashboard showing live on-call status updates

## Decision

Shachar built a mobile-friendly live status dashboard that allows Rami (and other authorized staff) to monitor on-call status in real time. The dashboard shows when the on-call psychiatrist clicks the alert link and engages with the patient case, providing visibility without requiring manual confirmation.

## Rationale

The core problem was visibility, not process. Ra'ut followed the process correctly and knew an on-call system existed — her anxiety came from the black box between "alert sent" and "alert acted upon." A real-time dashboard solves this by making the on-call response chain transparent to all stakeholders.

## Consequences

- Reduces staff anxiety during on-call situations by providing real-time status
- Enables remote monitoring (Rami can check even when abroad)
- Feeds into the negative-feedback alerting model — if no click within timeout, escalation triggers
- Requires on-call doctors to interact with the dashboard link for the system to register their response

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]