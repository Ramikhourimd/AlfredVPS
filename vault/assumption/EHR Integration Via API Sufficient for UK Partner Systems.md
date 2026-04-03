---
alfred_tags:
- ehr-integration/api
- uk/nhs-interoperability
based_on:
- '[[note/UK ADHD Platform Demo Rehearsal Notes 2025-02-11]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z UK Expansion wikilink is valid (YAML escaping false
  positive). Base view embeds (learn-assumption.base#Depends On This, #Related) reference
  _bases/learn-assumption.base which does not exist — embeds preserved but non-functional.
  ORPHAN001 — no inbound links; consider linking from project/Telia''z UK Expansion
  or a related record.'
name: EHR Integration Via API Sufficient for UK Partner Systems
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[constraint/UK Clinical Report Formats Require Adaptation From Israel Templates]]'
relationships:
- confidence: 0.85
  context: UK partners sufficiency vs general agnostic
  source: assumption/EHR Integration Via API Sufficient for UK Partner Systems.md
  target: assumption/Platform Is EHR-Agnostic Via API Integration.md
  type: related-to
source: Adiel Levin, demo rehearsal preparation
source_date: '2025-02-11'
status: active
type: assumption
---

# EHR Integration Via API Sufficient for UK Partner Systems

## Claim

The Telia'z platform can integrate with UK partner electronic health record (EHR) systems via API, and this API-based approach is sufficient for the clinical data exchange requirements of GP Confederation, OMG Healthcare, and Leon's practice. The platform is positioned as "not locked to any single system."

## Basis

During the GP Confederation demo rehearsal (2025-02-11), Adiel explicitly framed the platform as EHR-agnostic with API integrations available. This was part of the demo pitch to Jason Brook and Rebecca Wilson. No specific UK EHR systems (e.g., EMIS, SystmOne, TPP) have been tested or confirmed as compatible.

## Evidence Trail

- 2025-02-11: Demo rehearsal notes state "EHR integrations are possible via API — not locked to any single system"
- No subsequent evidence of UK EHR integration testing or validation

## Impact

If UK EHR integration proves more complex than assumed (e.g., NHS Spine connectivity, GP system compatibility, information governance requirements for data flow), this could delay both the Leon track and the GP Confed/OMG track significantly. Rebecca Wilson's IG governance review may surface this as a blocker.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]