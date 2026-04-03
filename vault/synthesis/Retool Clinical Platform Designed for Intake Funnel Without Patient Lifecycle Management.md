---
alfred_tags:
- clinic/operations
- patient/commitment-gaps
- system/lifecycle
cluster_sources:
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
confidence: high
created: '2026-02-27'
janitor_note: 'LINK001: (1) Telia''z wikilinks are valid — YAML escaping false positive.
  (2) [[synthesis/Operational Improvement Requirements Recur Verbatim Across Sessions
  Without Implementation Tracking]] and [[synthesis/Patient Commitment Lifecycle Gap
  Persisted Unresolved Across Seven Months]] — verify targets exist or were renamed.
  (3) Base view embeds (learn-synthesis.base#Sources, #Related) reference non-existent
  _bases/learn-synthesis.base — embeds preserved per policy. ORPHAN001: No inbound
  links — human review needed.'
name: Retool Clinical Platform Designed for Intake Funnel Without Patient Lifecycle
  Management
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/No System Support for Maccabi Commitment Renewals in Retool]]'
- '[[assumption/Maccabi Follow-Up Commitment Renewal Structure Unknown to Clinic Operations]]'
- '[[synthesis/Operational Improvement Requirements Recur Verbatim Across Sessions
  Without Implementation Tracking]]'
relationships:
- confidence: 0.9
  context: Platform flaw explains lifecycle gap
  source: synthesis/Retool Clinical Platform Designed for Intake Funnel Without Patient
    Lifecycle Management.md
  target: synthesis/Patient Commitment Lifecycle Gap Persisted Unresolved Across Seven
    Months.md
  type: supports
- confidence: 0.85
  context: Platform flaw underlies renewal gap
  source: synthesis/Retool Clinical Platform Designed for Intake Funnel Without Patient
    Lifecycle Management.md
  target: synthesis/Commitment Renewal Gap Spans Three System Layers Requiring Coordinated
    Fix.md
  type: supports
- confidence: 0.8
  context: Design flaw causes recurrences
  source: synthesis/Retool Clinical Platform Designed for Intake Funnel Without Patient
    Lifecycle Management.md
  target: synthesis/Operational Improvement Requirements Recur Verbatim Across Sessions
    Without Implementation Tracking.md
  type: supports
status: active
supports:
- '[[synthesis/Patient Commitment Lifecycle Gap Persisted Unresolved Across Seven
  Months]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
type: synthesis
---

# Retool Clinical Platform Designed for Intake Funnel Without Patient Lifecycle Management

## Insight

The Retool clinical platform was architected exclusively for the patient intake phase — the questionnaire-to-first-appointment pipeline. The original design auto-populates commitment numbers from the intake questionnaire into Retool, but no equivalent pathway exists for any subsequent lifecycle stage (commitment renewal, session tracking through renewal, proactive expiry management, or discharge). This intake-only architecture explains why four separate meetings across seven months (January 2025 x2, August 2025 x2) identified the identical five missing capabilities — new Retool field, validation workflow, expiry alerts, secretary task automation, session counter refresh — without any being implemented. The gaps are not feature oversights; they reflect a platform designed for a single funnel stage being asked to support a full patient lifecycle.

## Evidence

1. **Intake flow works end-to-end:** Patient fills questionnaire → commitment number auto-populates into Retool → secretaries validate against Maccabi portal → scheduling proceeds. This is the only fully functional patient pathway.
2. **Renewal flow has no pathway at all:** When patients exhaust initial 20 sessions, there is no field to enter a renewal commitment, no validation workflow, no alerts, no automation. At least one patient submitted a renewal commitment with nowhere to record it.
3. **Discharge flow does not exist:** No structured patient discharge protocol was implemented in the system (addressed only in 2026 discussions).
4. **Session counter is static:** The remaining sessions tracker was built for the initial commitment allocation and cannot reset or update for renewals.
5. **The identical gap specification appeared in four separate meeting notes** — two from January 12, 2025 and two from August 1, 2025 — suggesting the requirements were re-derived from scratch each time rather than tracked as product backlog items.

## Implications

- Patching the Retool system for lifecycle management would require retrofitting architecture designed for a single stage, which explains the decision to rebuild from scratch (Shachar's rebuild decision, December 2025)
- Any future platform (the rebuild) must be designed around the full patient lifecycle — intake, active treatment, commitment renewal, and discharge — not just the acquisition funnel
- The intake-only design reflects the clinic's early-stage priority on patient acquisition over retention management, a priority that no longer matches operational reality at 7,000+ patient scale

## Applicability

Directly relevant to the platform rebuild project. The new system's architecture should be validated against the full patient lifecycle before development begins, not just the intake funnel.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]