---
alfred_tags:
- ehr-integration/api
- uk/nhs-interoperability
based_on:
- '[[note/UK ADHD Platform Demo Rehearsal Notes 2025-02-11]]'
confidence: low
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML single-quote escaping false
  positive). ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  UK Expansion or related records.
name: EHR API Integration Will Meet UK NHS Interoperability Requirements
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[task/Define Data Requirements for OMG-to-Telia''z Patient Handoff]]'
- '[[task/Map CQC and Clinical Governance Framework for Joint ADHD Service]]'
relationships:
- confidence: 0.9
  context: Both assume API suffices for UK systems
  source: assumption/EHR API Integration Will Meet UK NHS Interoperability Requirements.md
  target: assumption/EHR Integration Via API Sufficient for UK Partner Systems.md
  type: related-to
- confidence: 0.85
  context: Specific UK NHS vs general API agnosticism
  source: assumption/EHR API Integration Will Meet UK NHS Interoperability Requirements.md
  target: assumption/Platform Is EHR-Agnostic Via API Integration.md
  type: related-to
source: Stated in platform demo rehearsal
source_date: '2025-02-11'
status: active
type: assumption
---

# EHR API Integration Will Meet UK NHS Interoperability Requirements

## Claim

The team assumes that the platform's API-based EHR integration capability will be sufficient to meet UK NHS interoperability requirements. During the demo rehearsal, Adiel emphasized that "EHR integrations are possible via API — not locked to any single system." The implicit assumption is that connecting to UK primary care systems (EMIS, SystmOne, TPP) and NHS data standards (HL7 FHIR, NHS Digital specifications) will be achievable through generic API integration rather than requiring bespoke NHS-specific development.

## Basis

The demo rehearsal (2025-02-11) positioned API integration as a solved capability. However, UK NHS has specific interoperability standards including NHS Digital's compliance requirements, GP Connect specifications, and data sharing agreements that go beyond generic API connectivity. The OMG pathway design (2025-07-03) raised the question of how data physically transfers from OMG to Telia'z systems but did not resolve it.

## Evidence Trail

- 2025-02-11: API integration presented as platform capability in demo rehearsal
- 2025-07-03: Data handoff mechanism flagged as unresolved by Shachar (CTO)
- No evidence of assessment against NHS Digital interoperability standards

## Impact

If NHS interoperability requirements exceed generic API capability, significant development work would be needed. This could delay launch and affect the data flow between OMG triage, Telia'z assessment, GP records, and prescription systems. The task to define OMG-to-Telia'z data requirements is still open.