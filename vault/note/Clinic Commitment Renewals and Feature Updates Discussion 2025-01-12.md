---
alfred_tags:
- clinic/commitment-renewals
- features/updates
created: '2025-01-12'
description: Meeting between Rami and Shira covering patient commitment renewal workflows
  in Retool, psychiatrist feature feedback coordination, case manager vs psychiatrist
  screen design responsibilities, and agreement file issues
janitor_note: LINK001 — Telia'z and org wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which does not
  exist — vault-wide infrastructure issue, embed preserved.
name: Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Nadav Blatt]]'
- '[[person/Alice]]'
- '[[person/Ori Shukron]]'
- '[[person/Rana Khouri]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[org/Telia''z]]'
relationships:
- confidence: 0.93
  context: Chronological discussions on commitments & updates
  source: note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12.md
  target: note/Commitment Processes and Feature Updates Meeting 2025-08-01.md
  type: related-to
- confidence: 0.97
  context: Same-day renewal & feature updates discussions
  source: note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12.md
  target: note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12

## Context

Recurring operational sync between Rami (Chief Medical & Innovation Officer) and Shira (Clinic Manager) covering patient commitment renewal workflows, psychiatrist feature communication, and meeting screen UI design. Meeting held via Zoom on January 12, 2025.

## 1. Patient Commitment Renewals (Primary Topic)

The clinic's Maccabi HMO patients receive two initial commitments (referrals): one for intake and one for follow-up sessions (16 case manager follow-ups + 4 psychiatric follow-ups). When these are exhausted, patients need a renewal commitment.

**Current problem:**
- At least one patient has already sent a renewal commitment, but there is no place in Retool to enter it
- The original flow was: patient fills questionnaire, attaches commitment number, which auto-populates into Retool
- Renewal commitments have no equivalent workflow yet
- Secretaries must validate each commitment against the Maccabi web portal (check session balance, confirm validity) before approving for billing
- The exact terms of the renewal commitment (session count, structure) are unclear even to the clinic team

**Requirements identified:**
1. **New input field in Retool** for entering renewal commitment numbers, with the same validation workflow as initial commitments
2. **Expiry alerts for psychiatrists** — pop-up notification when entering the last session under a commitment, warning "this is the last session, commitment renewal needed"
3. **Pre-expiry alerts** — warnings appearing 2 sessions before the last one
4. **Secretary task automation** — automatic tasks for secretaries to phone patients before commitment expiry, reminding them to send a new commitment
5. **Session balance tracking update** — when a new commitment is entered, the remaining sessions counter must refresh

Alice (Elis) is investigating the exact commitment renewal process with Maccabi.

## 2. Psychiatrist Feature Communication and Feedback

**Problem:** Psychiatrists are not consistently adopting new features. Some still edit summaries in Google Docs (expecting changes to sync back), unaware that the new in-app summary editing replaced that workflow. Sending training booklets or WhatsApp updates does not guarantee adoption.

**Current channels:**
- WhatsApp group for improvement suggestions — psychiatrists use it for complaints and consultations, not just structured feedback
- Feature update WhatsApp group — used for announcing new features
- Training booklet from Nadav and Ori (from a previous training session by Ori Shukron)

**Actions decided:**
- Rami assigned Alice to be the point person for psychiatrist feature feedback and adoption tracking
- Need to connect Nadav and Alice so there is clear ownership of psychiatrist communication
- For significant feature changes, frontal (live) training sessions are necessary — WhatsApp messages and booklets are insufficient
- Rami to coordinate with Alice on the liaison role between product team and psychiatrists

## 3. Case Manager vs Psychiatrist Meeting Screen Design

**Context:** The team is redesigning the Retool meeting screens for both case managers and psychiatrists. There is overlap in what both professionals cover during sessions, leading to duplication.

**Key question:** What topics should be assigned to the case manager screen vs the psychiatrist screen, so both don't cover the same ground (background, symptoms, DSM criteria)?

**Current state:**
- Rami previously sat with Shira and Ori to define case manager agenda topics/headings
- Shira flagged that some items were removed (e.g., niche psychiatric history questions the case managers never reach)
- DSM symptom criteria breakdown needs refinement — current system has high-level categories but lacks the granular criterion-by-criterion structure (e.g., PTSD Criterion A, B, C with sub-items)

**Decisions:**
- The case manager screen design is blocked until Shira's team finalizes which clinical responsibilities belong to the case manager vs the psychiatrist
- This must be resolved before Rami's team builds the screens — otherwise they would build and then have to reduce
- Rami targeting: psychiatrist meeting screen design finalized by end of week, case manager screen the following week
- Joint meeting tomorrow with Ori and Alice to close the responsibility split question
- The output of this clinical split directly feeds into the AI prompts (what to ask, what to display)

## 4. Agreement File Issue

Rami noticed the employment agreement file sent to Rana Khouri was heavily corrupted/garbled. Shira confirmed she also saw formatting issues when opening it on her phone. However, Rana had already signed and returned it. Rami requested Shira send a clean replacement file.

## 5. Scheduling

Brief discussion about rescheduling the meeting with Nadav — Rami is unavailable Mondays between 10-12, which conflicts. Options to move to Sunday discussed but Sunday also has conflicts.

## Related
![[related.base#All]]