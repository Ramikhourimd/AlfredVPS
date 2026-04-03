---
alfred_tags:
- psychiatry/on-call
- clinical-operations
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2025-11-10'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: '"LINK001 — Telia''z wikilinks are valid (YAML apostrophe escaping false
  positive). Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which may not exist — vault-wide issue, embeds preserved. BODY — duplicate base
  view embeds at end of file; second set of \![[learn-decision.base#Based On]] and
  \![[learn-decision.base#Related]] should be removed manually."'
name: Build ER Referral Form Feature for Psychiatrists
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]'
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
- '[[org/Maccabi Healthcare Services]]'
- '[[person/Shira]]'
session: null
source: Rami Khouri directive during clinical operations meeting
source_date: '2025-11-10'
status: final
supports: []
tags: []
type: decision
---

# Build ER Referral Form Feature for Psychiatrists

## Context

Psychiatrists sometimes need to refer patients to the emergency room (e.g., suicidal patients). Currently there is no mechanism in the clinical platform to generate a formal referral letter. This creates both a clinical gap and a potential liability issue — if the system prevents psychiatrists from documenting their referral, it increases organizational exposure.

## Options Considered

1. **Add referral template button alongside existing AI summary feature** — Similar to the existing "star" button for summaries, add a button that generates a referral letter from a template. Default delivery via app/Clickx.
2. **Email-only referral letters** — Generate and send referral letters via email directly. Rejected because Maccabi HMO previously objected to email-based document delivery.
3. **Do nothing** — Rejected because it blocks psychiatrists from a basic clinical function and increases liability.

## Decision

Build a referral form template feature as a new button in the psychiatrist workflow. Default output goes to the HealthyMind app / Clickx system. Emergency override allows email delivery for urgent cases.

## Rationale

- Psychiatrists bear individual clinical responsibility for their patients — the organization must not block their ability to issue referral letters.
- Maccabi conflict avoided by defaulting to app-based delivery rather than email.
- Feature logic is delivery-agnostic — can be built independently of final routing decision.
- Similar UX pattern to existing AI summary generation reduces development and training friction.

## Consequences

- Requires product/engineering work to build the template and button.
- Need to define the referral letter template content.
- Maccabi relationship preserved by avoiding email as default.
- Psychiatrists gain a critical clinical tool for emergency situations.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]