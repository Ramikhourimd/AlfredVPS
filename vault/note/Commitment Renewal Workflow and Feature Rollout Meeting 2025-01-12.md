---
alfred_tags:
- clinic/commitment-renewals
- features/updates
created: '2025-01-12'
description: Rami-Shira working session on patient commitment renewal gaps in Retool,
  psychiatrist feature training process, WhatsApp group management, case manager meeting
  screen redesign, and corrupted employment agreement issue
janitor_note: LINK001 — Telia'z wikilinks are YAML-escape false positives (files exist).
  related.base#All is a base view embed referencing _bases/related.base which does
  not exist — vault-wide infrastructure gap, embed preserved.
name: Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Commitment Renewals and Feature Updates Meeting 2025-01-12]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Nadav Blatt]]'
- '[[person/Alice]]'
- '[[person/Ori Shukron]]'
- '[[person/Rana Khouri]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[task/Clarify Maccabi Commitment Renewal Terms]]'
- '[[task/Build Commitment Renewal Entry Field in Retool]]'
- '[[task/Build Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
- '[[task/Resend Corrected Employment Agreement to Rana]]'
- '[[task/Coordinate Nadav and Alice on Psychiatrist Feature Feedback Pipeline]]'
- '[[person/Rana Khouri]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[task/Build Commitment Renewal Entry in Retool]]'
- '[[task/Build Commitment Expiry Alerts for Psychiatrist Sessions]]'
- '[[task/Clarify Maccabi Commitment Renewal Terms]]'
- '[[task/Coordinate Nadav and Alice on Psychiatrist Feature Feedback Pipeline]]'
- '[[task/Resend Corrected Employment Agreement to Rana]]'
- '[[decision/Tab-Based Navigation for Case Manager Questionnaire Screen]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12

## Context

Regular working session between Rami (CMO/Innovation) and Shira (Clinic Manager) covering several operational and product topics at the Telia'z clinic. The meeting focused heavily on the patient commitment (התחייבות) renewal process gap and coordination around feature rollouts to psychiatrists.

## 1. Patient Commitment Renewal Workflow (Primary Topic)

### The Problem
Patients initially receive two Maccabi commitments — one for intake and one for follow-up (16 case manager sessions + 4 psychiatric sessions). When these commitments expire, patients need a **renewal commitment**. Currently:
- There is no field in Retool to enter the renewal commitment number
- At least one patient has already sent a renewal commitment with nowhere to record it
- The original flow auto-populated commitment numbers from the intake questionnaire to Retool, but no equivalent path exists for renewals
- The exact terms of renewal commitments (session count, structure) are unclear and need clarification with Maccabi

### Required System Changes
1. **New field in Retool** for entering renewal commitment numbers
2. **Expiry alerts** — Pop-up warning when psychiatrist opens a session that is 1-2 sessions before commitment expiry ("This is the last session under the current commitment — renewal needed")
3. **Secretarial task triggers** — Automatic administrative tasks for secretaries to call patients approaching commitment expiry during pre-session preparation calls, reminding them to send new commitments
4. **Updated session counter** — The remaining sessions tracker needs to reset/update when a new commitment is entered (e.g., "X of 22" becomes "Y of [new total]")

### Validation Process
Every commitment (original and renewal) must be validated against the Maccabi portal (MADAC) to verify:
- The commitment is valid and active
- Sufficient session balance remains
- The commitment is properly approved (otherwise billing claims fail)

### Next Step
Alice (Elis) is investigating the renewal commitment details with Maccabi. System changes cannot proceed to development until this is clarified.

## 2. Psychiatrist Feature Training and WhatsApp Group Management

### Feature Rollout Gap
- A new summary feature was rolled out, but some psychiatrists still edit in Google Docs expecting changes to persist (they do not)
- Sending a training booklet is insufficient — psychiatrists (part-time workers) often do not read documentation
- Shira recalled that Ori did conduct a frontal training session earlier, but it may not have covered the summary feature specifically

### WhatsApp Group Issues
- A "suggestions for improvement" WhatsApp group exists where psychiatrists post feedback, complaints, and consultations
- Rami cannot effectively monitor this group and needs structured feedback collection
- Proposed solution: Connect Nadav (product) with Alice to create a structured feedback pipeline from psychiatrists

### Decision
- Alice assigned to manage psychiatrist feedback and feature training coordination
- For significant feature changes, frontal training sessions should precede feature removal of old workflows
- Rami to coordinate linkage between Nadav and Alice for this purpose

## 3. Case Manager Meeting Screen Redesign

### Context
The team is redesigning both the case manager and psychiatrist meeting screens in the clinical platform. A key question emerged: should certain clinical assessment sections (background, symptoms, DSM criteria) be covered by **both** the case manager and psychiatrist, or divided between them?

### Current Discussion
- Shira and her team raised the idea of splitting the clinical assessment more distinctly — so the same ground is not covered twice
- This has a direct impact on UI design: removing sections from one screen means not building them
- The case manager screen agenda (what topics/questions to present) is not yet defined at the title/subtitle level

### Urgency
- Rami wants the psychiatrist meeting screen design finalized by end of the current week
- Case manager screen design targeted for the following week
- The team is "on borrowed time" as leadership meetings may redirect priorities once the Negev region onboarding begins

### Blocker
The case manager screen cannot be designed until the clinical role division (what the case manager covers vs. the psychiatrist) is finalized. A joint meeting with Rami, Shira, Ori, and Alice is needed.

## 4. Employment Agreement Issue

Rami noticed that the agreement document sent to Rena was corrupted/garbled. Shira confirmed she had seen the formatting issues when viewing on her phone. Rami asked Shira to have Rena not sign the corrupted version and said he would send a corrected file. However, Shira reported that Rena had already signed and submitted it. A corrected version needs to be re-sent.

## 5. Other Items Noted

- Rami is preparing a psychiatrist feedback questionnaire with both psychological and feature-satisfaction questions, intended to establish a baseline for measuring future feature effectiveness
- Brief mention of a second agreement issue — a complaint was received about agreement terms not matching what was originally agreed

## Related
![[related.base#All]]