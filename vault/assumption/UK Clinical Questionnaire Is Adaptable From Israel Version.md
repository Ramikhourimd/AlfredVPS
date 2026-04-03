---
based_on:
- '[[note/Telia''z Team Meeting UK Launch Patient Capacity and Recruitment 2026-02-15]]'
- '[[note/GP Confederation ADHD Partnership Meeting Notes 2025-01-22]]'
confidence: medium
created: '2026-03-07'
janitor_note: 'LINK001 for Telia''z links is YAML single-quote escaping false positive
  (vault-wide pattern). LINK001 for assumption link is false positive (Israel Three-Step
  Clinical Workflow file confirmed via search). Has unusual escaped embeds (\\![[...]])
  instead of standard \![[...]] — needs human review. Base embed links reference _bases/
  infrastructure not yet created (vault-wide gap). ORPHAN001: no inbound links.'
name: UK Clinical Questionnaire Is Adaptable From Israel Version
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[assumption/Israel Three-Step Clinical Workflow Translates to UK Without Major
  Modification]]'
- '[[task/Build UK Prescription and Scheduling Features]]'
source: Team meeting discussion and GP Confederation presentation
source_date: '2026-02-15'
status: active
type: assumption
---

# UK Clinical Questionnaire Is Adaptable From Israel Version

## Claim

The team assumes the UK ADHD clinical questionnaire (ASRS, DIVA, and broader screening tools) can be adapted from the existing Israel version rather than built from scratch. The adaptation involves language, regulatory alignment, and UK-specific clinical requirements, but the core questionnaire structure and digital delivery mechanism remain the same.

## Basis

In the February 15, 2026 team meeting, the UK questionnaire was discussed as a product backlog item requiring adaptation — not as a new build. Stav referenced it alongside report formats and other UK-specific modifications, treating it as a configuration/adaptation task within the existing platform rather than a new feature.

The Israel platform already delivers digital questionnaires (ASRS, DIVA for ADHD) as Step 1 of the three-step workflow. The assumption is that this infrastructure transfers to the UK with content modifications.

## Evidence Trail

- 2025-01-22: GP Confederation meeting — Adiel presented the Israel questionnaire flow as directly applicable to UK
- 2026-02-15: Team meeting — questionnaire listed as UK product requirement alongside report formats (adaptation framing, not new-build framing)

## Impact

If this assumption holds, questionnaire delivery is a moderate effort (content adaptation). If it fails — for example, if UK regulatory requirements demand fundamentally different questionnaire delivery, validation, or data handling — the development timeline extends significantly.

\![[learn-assumption.base#Depends On This]]
\![[learn-assumption.base#Related]]
