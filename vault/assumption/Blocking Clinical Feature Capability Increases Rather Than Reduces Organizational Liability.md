---
based_on:
- '[[note/Clinic Platform Referral Form and System Performance Discussion 2025-11-10]]'
confidence: medium
created: '2026-03-03'
janitor_note: 'LINK001: Wikilink to project/Teliaz AI Clinical Platform uses YAML
  double-apostrophe escaping — valid YAML, likely false positive. ORPHAN001: No inbound
  links — review if this assumption should be linked from a project or decision.'
name: Blocking Clinical Feature Capability Increases Rather Than Reduces Organizational
  Liability
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Build ER Referral Form Feature for Psychiatrists]]'
- '[[decision/Deliver ER Referral Letters via HealthyMind App Not Email]]'
source: Rami Khouri legal reasoning during referral form discussion with Shira
source_date: '2025-11-10'
status: active
type: assumption
---

# Blocking Clinical Feature Capability Increases Rather Than Reduces Organizational Liability

## Claim

When a clinician needs to perform a clinical action (e.g., issue an ER referral letter) and the organization's platform blocks that capability, the organization's liability increases rather than decreases. The organization has a duty to enable clinicians to exercise their professional judgment, and preventing them from doing so creates greater legal exposure.

## Basis

During the referral form discussion, Shira raised a liability concern: if a psychiatrist refers a patient to the ER but the patient self-harms before arriving, is the psychiatrist liable? Rami clarified that liability rests with the individual psychiatrist (as in any clinical setting), but the organization must enable them to issue referral letters. Blocking the capability actually increases organizational liability because the organization is preventing the clinician from completing a standard clinical action.

## Evidence Trail

- 2025-11-10: Rami stated this principle during clinic meeting with Shira when discussing the ER referral form feature.
- This reasoning directly drove the decision to build the referral form feature rather than defer it.

## Impact

This principle applies beyond just the referral form — it creates a general framework for evaluating clinical feature requests. Any feature that enables a clinician to perform a recognized clinical action (referral, documentation, prescription) should be prioritized on liability grounds, not just convenience.
