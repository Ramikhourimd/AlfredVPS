---
created: '2025-11-10'
description: Discussion between Rami and Shira about building an ER referral form
  feature, handling Maccabi document routing, triaging psychiatrist system complaints
  through Rivi, and addressing platform performance degradation
janitor_note: LINK001 — Telia'z and org/Telia'z wikilinks are valid (YAML escaping
  false positive). Base view embed (related.base#All) references _bases/related.base
  which does not exist. Link to synthesis/Feature Rollout Failures... is valid (target
  exists).
name: Clinic Platform Referral Form and System Performance Discussion 2025-11-10
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]'
- '[[person/Rami Khouri]]'
- '[[person/Shira]]'
- '[[person/Stav Zamir]]'
- '[[person/Rivi Idelman]]'
- '[[person/Shachar]]'
- '[[org/Maccabi Healthcare Services]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[decision/Build ER Referral Form Feature for Psychiatrists]]'
- '[[synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
  Cycle]]'
relationships: []
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Clinic Platform Referral Form and System Performance Discussion 2025-11-10

## Context

Meeting between Rami (CMO) and Shira (Clinical Director) at the clinic office on November 10, 2025. Two main topics: building an emergency referral form feature for psychiatrists, and addressing persistent system complaints from clinical staff.

## 1. Emergency Referral Form Feature

Shira raised the need for a feature that allows psychiatrists to generate a referral form (הפניה למיון) — a formal referral letter to send patients to the emergency room (ER). Currently, no such template exists in the platform.

### Clinical Rationale

- When a psychiatrist sees a patient who needs emergency evaluation (e.g., suicidal ideation), they should be able to generate a formal referral letter directly from the system.
- Shira raised a liability concern: if a psychiatrist sees a patient, refers them to ER, but the patient self-harms before arriving — is the psychiatrist liable?
- Rami clarified: liability rests with the individual psychiatrist (as in any clinical setting), but the organization must **enable** them to issue referral letters. Blocking the capability actually increases liability.

### Technical Approach (Decided)

- Similar to the existing "star" button that generates AI summaries, add another button that generates a referral letter from a template.
- **Default delivery:** Upload to the HealthyMind app / Clickx system (not email).
- **Emergency override:** Option to send via email for urgent cases.
- This avoids conflict with Maccabi HMO, which previously objected to email-based document delivery.
- The feature can be built independently of whether delivery is via app or Clickx — the template and generation logic is the same.

## 2. System Complaint Triage and Staff Response

### Stav Zamir Added to Psychiatrist Group

Rami directed that Stav Zamir (Innovation Team) should be added to the psychiatrist communication group (likely WhatsApp/Teams) so she can respond to system-related complaints directly. Lena (a team member) was asked to add her.

### Rivi Idelman as Complaint Triage Lead

Rivi Idelman is beginning to characterize and triage all clinical staff complaints:
- Mapping each complaint to the appropriate handler (Stav for innovation/product, Shachar for R&D, Shira for operations).
- Creating a tracking table showing status, responsible party, and resolution stage.
- This structure should reduce Shira's feeling of being overwhelmed by unstructured complaints.

### Key Instruction from Rami

Shira should forward specific system issues or psychiatrist frustrations to Rivi, who will characterize them and route appropriately. Shira remains the primary relationship holder for the clinical team.

## 3. Platform Performance Issues

Shira reported persistent and worsening system problems affecting psychiatrists:

- **Retool response time:** Slow page loads and screen transitions.
- **Summary deletion:** Clinical summaries being lost — one psychiatrist wrote a summary three times because it kept getting deleted.
- **System freezing:** Platform becoming unresponsive during sessions.
- **Summary upload time:** Delays in AI summary availability.

### Shachar's Position

When Shira raised these with Shachar (VP R&D), his response was that resources are focused on building the new UK system, making immediate fixes "not possible." This creates tension because clinicians are increasingly frustrated.

### Resolution Path

- Shira to compile a prioritized list of system complaints.
- Rami to use the list for visibility into where issues are stuck.
- Priority should go to items that are "quick wins" or deeply affecting clinician experience.
- Rami emphasized: staff must feel their complaints are acknowledged even if not immediately resolved.

## 4. Staff Satisfaction and Communication

Rami stressed the importance of proactive communication with frustrated staff:
- Responding in the group chat (even "I'm looking into it") is better than silence.
- Noa was cited as an example: after a one-on-one conversation, she calmed down significantly.
- The telepsychiatry work model amplifies frustration because clinicians work in isolation — small system issues compound.
- Complaints should be filtered objectively; some clinicians (e.g., Elinor) may overstate issues, while others (e.g., Elias) understate them.

## Related
![[related.base#All]]
