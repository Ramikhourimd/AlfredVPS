---
alfred_tags:
- clinic/commitment-renewals
- features/updates
created: '2026-02-26'
description: Meeting between Rami and Shira covering patient commitment renewal workflow
  gaps in Retool, psychiatrist feedback management via WhatsApp, feature rollout training
  process, case manager screen redesign priorities, and a corrupted employment agreement
  for Rana
janitor_note: LINK001 — Telia'z wikilinks (project, conversation) are valid (YAML
  apostrophe escaping false positive). Base view embed (related.base#All) references
  _bases/related.base which does not exist — embed preserved per policy. project/Telia'z
  AI Clinical Platform link unverified — may be valid or broken, needs human check.
name: Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Clinic Operations Commitment Renewal and Feature Updates Meeting
  2025-08-01]]'
- '[[person/Shira]]'
- '[[person/Rami Khouri]]'
- '[[person/Nadav Blatt]]'
- '[[person/Alice]]'
- '[[person/Rana Khouri]]'
- '[[project/Telia''z AI Clinical Platform]]'
- '[[process/Clinic Israel Patient Intake Flow]]'
- '[[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]'
relationships:
- confidence: 0.95
  context: Similar commitment renewal & feature discussions
  source: note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01.md
  target: note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12.md
  type: related-to
- confidence: 0.98
  context: Same-day meetings on commitment processes & features
  source: note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01.md
  target: note/Commitment Processes and Feature Updates Meeting 2025-08-01.md
  type: related-to
- confidence: 0.92
  context: Related renewal process & feature rollout topics
  source: note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01.md
  target: note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01

## Context

Regular operations meeting between Rami Khouri (Chief Medical & Innovation Officer) and Shira Lachman (Clinic Manager) at Telia'z. The meeting focused on operational gaps in the patient commitment renewal workflow, psychiatrist feature training, and upcoming UI redesign for the case manager and psychiatrist meeting screens.

## Patient Commitment Renewal (התחייבויות)

The core operational issue discussed: when patients complete their initial Maccabi commitment (16 case manager sessions + 4 psychiatric follow-ups), they need to obtain a new follow-up commitment from Maccabi. Currently there are several gaps:

1. **No Retool field for renewal commitments** — The system only handles the initial commitment. When a patient sends a new commitment number, there is no place to enter it in the system.
2. **No validation workflow for renewals** — The secretarial team needs to verify new commitments on the Maccabi website (checking validity, remaining session balance) before scheduling can proceed. This validation process exists for initial commitments but not for renewals.
3. **No proactive alerts** — Psychiatrists are not warned when a patient is approaching the end of their commitment. Rami proposed:
   - A pop-up alert when opening the last 2 sessions of a commitment cycle
   - A prominent warning on the final session: "This is the last session under the current commitment — renewal required"
4. **No secretary task automation** — Secretaries should receive automated tasks to call patients before the commitment expires, prompting them to obtain and submit a renewal.
5. **Unclear Maccabi terms for renewals** — Neither Rami nor Shira fully understand the structure of the follow-up commitment (how many sessions, what types). Alice (Elis) is investigating the details with Maccabi.

## Psychiatrist Feedback and WhatsApp Group Management

Rami raised concerns about the WhatsApp "Suggestions for Improvement" group:
- Psychiatrists are using it for complaints, consultations, and general discussion rather than structured product feedback
- The feedback is not being systematically channeled to the product team
- Rami asked Shira about creating a separate admin WhatsApp group (confirmed one already exists with Shira, Rana, and Avital)
- **Decision:** Rami will coordinate between Nadav (product) and Alice to establish a structured feedback loop from psychiatrists to the product team

## Feature Rollout and Training Process

Discussion about how new features (particularly the AI session summary feature) are communicated to psychiatrists:
- The team had been sending training booklets and WhatsApp updates, but some psychiatrists are not reading them
- Some psychiatrists are still editing summaries in Google Docs, not realizing those edits do not persist in the new system
- Ori Shukron had previously conducted a frontal training session for psychiatrists on Retool, which was effective
- **Conclusion:** Significant feature changes (like the summary workflow) require in-person/frontal training sessions, not just written materials. Sending a booklet is insufficient for ensuring adoption.
- Shira suggested that when a new feature replaces an old workflow, the old option should be removed entirely to prevent confusion — but only after confirming all users are trained.

## Case Manager and Psychiatrist Screen Redesign

A key design discussion about the upcoming meeting screen UI:
- Currently both the case manager and psychiatrist review the same information (background, questions, symptoms), causing duplication of work
- Shira and her team had been discussing a potential split: some content exclusively on the case manager screen, other content exclusively on the psychiatrist screen
- This split directly impacts what Rami's team builds — they are designing the AI prompts and screen layouts for both roles
- **Blocker:** The case manager agenda (what topics/questions the case manager covers) has not been finalized. Rami described this as titles and subtitles (e.g., DSM criteria, symptom categories) that determine the structure of the case manager screen.
- Rami expressed urgency — the psychiatrist meeting screen design should be locked by end of week, with the case manager screen the following week.
- **Next step:** Meeting scheduled with Nadav and Li (today at 2pm), plus a joint meeting with Ori and Alice the next day to finalize the clinical content split.

## Rana Employment Agreement Issue

Rami noticed that the employment agreement PDF sent to Rana was severely corrupted/garbled. Shira confirmed Rana had already signed it. Rami requested a corrected version be sent — he will prepare and send a clean file.

## Related
![[related.base#All]]