---
alfred_tags:
- clinic/commitment-renewals
- features/updates
created: '2025-08-01'
description: Rami and Shira discuss patient HMO commitment renewal workflow gaps in
  Retool, psychiatrist feature rollout coordination via WhatsApp groups, case manager
  vs psychiatrist meeting screen redesign, and corrupted Rana employment agreement.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML apostrophe escaping false
  positive). Broken wikilink [[conversation/Clinic Operations Commitment Renewal and
  Feature Updates Meeting 2025-08-01]] — target may have been renamed or not yet created;
  verify conversation record name. Base view embed (related.base#All) references _bases/related.base
  which does not exist — create base file to enable dynamic views.
name: Commitment Processes and Feature Updates Meeting 2025-08-01
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Operations Commitment Renewal and Feature Updates Meeting
  2025-08-01]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Alice]]'
- '[[person/Nadav Blatt]]'
- '[[person/Ori Shukron]]'
- '[[person/Rana Khouri]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
relationships:
- confidence: 0.91
  context: Linked commitment processes & workflow topics
  source: note/Commitment Processes and Feature Updates Meeting 2025-08-01.md
  target: note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Commitment Processes and Feature Updates Meeting 2025-08-01

## Context

Operational meeting between Rami Khouri and Shira Lachman covering patient commitment renewal workflows, psychiatrist feature rollout coordination, and case manager meeting screen redesign. The meeting addressed several urgent operational gaps in the Telia'z clinic Retool system.

## Patient Commitment Renewal Workflow

The primary topic was the gap in handling HMO commitment renewals (התחייבויות). Currently:

- Patients initially receive two commitments: **intake commitment** and **follow-up commitment** (limited to 16 case manager sessions + 4 psychiatric sessions)
- When the initial commitment expires, patients need a **continuation commitment** — but there is no field in Retool to enter this new commitment number
- One patient has already submitted a renewal commitment with nowhere to record it
- The secretarial team must validate each commitment against the Maccabi website to confirm it has a valid session balance before scheduling
- Without validation, the clinic cannot issue payment demands (דרישת שלום)

**Required system changes:**
1. New field in Retool for entering renewal commitment numbers
2. Automated alerts 2 sessions before commitment expiry, warning psychiatrists during session entry
3. Pop-up notification on the last session: "This is the last session under current commitment — renewal required"
4. Secretary tasks auto-generated to call patients before their last sessions to remind them to send a new commitment
5. Updated session balance counter reflecting the new commitment allocation

Alice is investigating with Maccabi exactly how the continuation commitment process works (number of sessions, structure).

## Psychiatrist Feature Rollout Process

Rami observed that some psychiatrists are still editing clinical summaries in Google Docs (the old workflow) rather than using the new in-system summary feature. Issues identified:

- Psychiatrists expect their Docs edits to propagate back to the system, which they don't
- Sending a training booklet or WhatsApp message is insufficient — many don't read it
- Ori Shukron previously conducted a frontal training session covering Retool basics, but the summary feature may not have been covered in depth
- **Decision:** For significant feature changes that replace old workflows, a frontal training session should be conducted before disabling the legacy feature
- Rami assigned Alice to coordinate psychiatrist feature training and feedback collection, working with Nadav Blatt

### WhatsApp Group Management

- There is a "Suggestions for Improvement" WhatsApp group where psychiatrists post feedback, complaints, and consultations
- Rami needs this feedback channeled in a structured way — not just informal chatter
- Rami proposed connecting Nadav to the admin WhatsApp group to maintain visibility
- Shira confirmed she is in the group monitoring summary-related issues
- Privacy check requested: Can psychiatrists see each other's messages in the group?

## Psychiatrist Feedback Survey

Rami mentioned a planned psychiatrist questionnaire with two purposes:
1. **Psychological/engagement questions** — understanding energy levels and motivation
2. **Summary feature satisfaction** — establishing a baseline metric for measuring the success of the next feature rollout (the "like" feedback mechanism)

The survey would serve as a baseline measurement before the next feature launch.

## Case Manager Meeting Screen Redesign

The team discussed a significant UX question: how to split responsibilities between the case manager and psychiatrist meeting screens to avoid duplication.

- Currently, both professionals cover overlapping ground (background, symptoms, questions)
- Shira and Ori had discussed a more targeted division — each screen showing only what that role needs
- This directly impacts the AI system's prompt design: what should the case manager be guided to ask, and what should be presented to the psychiatrist at session start
- **Blocker:** The case manager agenda structure (titles, sub-titles, topic categories) has not been finalized
- DSM criteria breakdown was discussed — Shira noted the current system lacks granular symptom checklists (e.g., PTSD Criterion A sub-items)
- Rami pushed for rapid resolution: goal is psychiatrist meeting screen design finalized by end of week, case manager screen the week after

## Rana Employment Agreement Issue

Rami flagged that the employment agreement sent to Rana Khouri was severely corrupted/garbled. Shira confirmed she noticed the formatting issues when viewing on her phone. Unfortunately, Rana had already signed. Rami committed to sending a corrected version.

## Related
![[related.base#All]]