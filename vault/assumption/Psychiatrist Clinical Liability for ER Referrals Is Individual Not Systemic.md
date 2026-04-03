---
based_on:
- '[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-10'
invalidated_by: []
janitor_note: 'FM001: Duplicate frontmatter block in body — second ---...--- block
  needs manual removal. Fields from duplicate block have been merged into primary
  frontmatter.'
name: Psychiatrist Clinical Liability for ER Referrals Is Individual Not Systemic
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[decision/Build ER Referral Form Feature for Psychiatrists]]'
- '[[decision/Deliver ER Referral Letters via HealthyMind App Not Email]]'
- '[[assumption/Blocking Clinical Feature Capability Increases Rather Than Reduces
  Organizational Liability]]'
source: Rami Khouri — stated during ER referral form discussion
source_date: '2025-11-10'
status: active
tags: []
type: assumption
---

---
type: assumption
status: active
confidence: medium
source: "Rami Khouri — stated during ER referral form discussion"
source_date: 2025-11-10
project: ["[[project/Telia'z AI Clinical Platform]]"]
based_on: ["[[conversation/Clinic Platform Referral Form and System Issues Discussion 2025-11-10]]"]
confirmed_by: []
challenged_by: []
invalidated_by: []
related: ["[[decision/Build ER Referral Form Feature for Psychiatrists]]", "[[decision/Deliver ER Referral Letters via HealthyMind App Not Email]]", "[[assumption/Blocking Clinical Feature Capability Increases Rather Than Reduces Organizational Liability]]"]
created: "2026-03-10"
tags: []
---

# Psychiatrist Clinical Liability for ER Referrals Is Individual Not Systemic

## Claim

When a psychiatrist refers a patient to the emergency room (e.g., due to suicidal ideation), liability for the patient's outcome rests with the individual psychiatrist who made the clinical decision, not with the clinic organization or the system that facilitated the referral.

## Basis

Rami stated this explicitly during the 2025-11-10 discussion with Shira about the ER referral form feature. Shira raised the concern that if a psychiatrist refers a patient to the ER and the patient subsequently self-harms, there could be liability implications. Rami clarified that clinical liability is personal to the treating psychiatrist, but that the system must still enable the referral capability — blocking the feature would itself increase organizational risk.

## Evidence Trail

- 2025-11-10: Rami stated position clearly in response to Shira's liability question
- No legal review or formal organizational policy has been cited to confirm this position

## Impact

This assumption shapes the ER referral feature design: the system enables psychiatrists to issue referral letters without additional organizational approval gates. If this assumption is incorrect (i.e., organizational liability exists), the feature might need additional safeguards such as supervisor co-sign or audit trails.
