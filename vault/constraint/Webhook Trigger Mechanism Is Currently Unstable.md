---
alfred_tags:
- clinical-dataset/limitations
- data-quality/issues
- ai-analysis/constraints
authority: R&D/Engineering
created: '2026-02-25'
janitor_note: LINK001 — project/Teliaz AI Clinical Platform wikilink is valid (YAML
  single-quote escaping false positive, target exists). Base view embeds learn-constraint.base#Affected
  Projects and learn-constraint.base#Related reference non-existent _bases/learn-constraint.base
  — embeds preserved, create base file to enable dynamic views.
name: Webhook Trigger Mechanism Is Currently Unstable
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
source: Engineering assessment at product meeting
source_date: '2026-02-25'
status: active
type: constraint
---

# Webhook Trigger Mechanism Is Currently Unstable

## Constraint

The webhook-based trigger mechanism for initiating AI summary generation is not yet reliable. Until stabilized, the Start API must serve as an interim trigger mechanism.

## Source

Engineering assessment during product meeting. Webhooks are the target architecture but are not yet production-ready.

## Implications

- AI pipeline triggers must use Start API as interim solution
- Start API needs enrichment with mandatory parameters: user ID, clinic, meeting type/ID
- Webhook stabilization is a prerequisite for fully automated pipeline
- Dual-path support (Start API + Webhook) needed during transition

## Expiry / Review

Review when Engineering reports webhook stabilization is complete. Target: before Q2 2026.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]