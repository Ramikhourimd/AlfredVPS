---
alfred_tags:
- ehr-integration/api
- uk/nhs-interoperability
based_on:
- '[[note/UK ADHD Platform Demo Rehearsal Notes 2025-02-11]]'
confidence: medium
created: '2026-02-27'
janitor_note: LINK001 — Telia'z UK Expansion wikilink valid (YAML escaping false positive).
  ORPHAN001 — No inbound wikilinks found; may need linking from a project or decision
  record.
name: Platform Is EHR-Agnostic Via API Integration
project:
- '[[project/Telia''z UK Expansion]]'
relationships:
- confidence: 0.9
  context: Agnosticism enables NHS interoperability
  source: assumption/Platform Is EHR-Agnostic Via API Integration.md
  target: assumption/EHR API Integration Will Meet UK NHS Interoperability Requirements.md
  type: supports
- confidence: 0.9
  context: Agnosticism supports partner integration
  source: assumption/Platform Is EHR-Agnostic Via API Integration.md
  target: assumption/EHR Integration Via API Sufficient for UK Partner Systems.md
  type: supports
source: Demo rehearsal 2025-02-11, Adiel Levin
source_date: '2025-02-11'
status: active
type: assumption
---

# Platform Is EHR-Agnostic Via API Integration

## Claim

The Telia'z/HealthyMind platform can integrate with any UK Electronic Health Record (EHR) system via API, and is not locked to a specific EHR vendor. This was positioned as a key selling point during demo preparation — the platform's openness to multiple integration targets.

## Basis

During the demo rehearsal (2025-02-11), Adiel scripted a key framing point: "EHR integrations are possible via API — not locked to any single system." This was positioned as something to emphasize to GP Confederation stakeholders who would need the service to integrate with their existing clinical systems.

## Evidence Trail

- 2025-02-11: Demo rehearsal — EHR-agnostic integration via API explicitly scripted as a talking point
- 2025-01-22: GP Confed meeting — data flow and GP system integration discussed as a governance requirement

## Impact

If confirmed technically, this removes a significant barrier to UK partnerships — each GP practice, NHS trust, or partner organization can maintain their existing EHR while integrating Telia'z's service. If the API integration layer is not mature or requires significant custom work per EHR vendor, this could become a hidden cost and timeline risk for each new partnership.