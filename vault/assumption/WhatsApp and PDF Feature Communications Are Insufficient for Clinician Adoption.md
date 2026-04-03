---
based_on:
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
confidence: high
confirmed_by:
- '[[decision/Require Frontal Training Before Removing Legacy Feature Workflows]]'
- '[[decision/Require Frontal Training for Significant Feature Changes]]'
- '[[decision/Require Frontal Training Before Deprecating Old Clinical Features]]'
created: '2026-02-27'
janitor_note: 'LINK001 false positives: Telia''z wikilink is valid YAML single-quote
  escaping (Telia''''z = Telia''z). Base view embeds (learn-assumption.base#Depends
  On This, #Related) reference _bases/learn-assumption.base which does not exist yet
  — vault-wide infrastructure gap, not a per-record issue. ORPHAN001: no inbound wikilinks
  detected; consider linking from a project or planning record.'
name: WhatsApp and PDF Feature Communications Are Insufficient for Clinician Adoption
project:
- '[[project/Telia''z Clinic Israel]]'
source: Repeated observation across Jan 2025 and Aug 2025 operational meetings
source_date: '2025-01-12'
status: confirmed
type: assumption
---

# WhatsApp and PDF Feature Communications Are Insufficient for Clinician Adoption

## Claim

Announcing new clinical platform features to psychiatrists via WhatsApp group messages and PDF instruction documents does not produce meaningful adoption. Psychiatrists continue using legacy workflows (e.g., editing summaries in Google Docs) despite receiving WhatsApp notifications about new in-app features. Only frontal (in-person or synchronous video) training sessions produce reliable feature adoption.

## Basis

Observed repeatedly across operational meetings:
- [[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]: Rami observed psychiatrists still editing in Google Docs despite WhatsApp-communicated availability of the new in-app summary feature
- [[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]: Seven months later, the same problem persists — psychiatrists expect Google Docs edits to propagate, unaware the workflow has changed
- [[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]: Same observation documented independently

The pattern is consistent: WhatsApp announcements and PDF guides are read but do not change behavior. Psychiatrists default to familiar workflows unless actively trained.

## Evidence Trail

- 2025-01-12: First documented observation of psychiatrists ignoring WhatsApp feature announcements
- 2025-08-01: Same adoption failure observed seven months later, confirming the pattern
- Multiple decisions to require frontal training created in response, confirming leadership accepts this as fact:
  - [[decision/Require Frontal Training Before Removing Legacy Feature Workflows]]
  - [[decision/Require Frontal Training for Significant Feature Changes]]
  - [[decision/Require Frontal Training Before Deprecating Old Clinical Features]]

## Impact

This assumption directly drives:
- The policy requiring frontal training before deprecating old features
- Resource allocation for synchronous training sessions when rolling out new features
- The cadence and method of feature communication to clinical staff
- Risk assessment for any feature rollout that relies solely on asynchronous communication

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
