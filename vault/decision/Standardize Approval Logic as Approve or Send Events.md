---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist. Create base file to enable
  dynamic views. Note: duplicate base embeds in body (appears twice). All Telia''z
  and org wikilinks are valid (YAML escaping false positive).'
name: Standardize Approval Logic as Approve or Send Events
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[org/Telia''z]]'
session: null
source: Product meeting consensus
source_date: '2026-02-25'
status: final
supports: []
tags: []
type: decision
---

# Standardize Approval Logic as Approve or Send Events

## Context

Different clinic centers use different event types to signal summary approval. Maccabi uses `approve`, other centers use `send`. The `save` event was previously sometimes confused with approval, leading to inflated approval counts and unreliable timing metrics.

## Options Considered

1. **Option A** — Treat `approve`, `send`, and `save` all as approval signals
2. **Option B** — Treat only `approve` and `send` as approval; ignore `save` entirely

## Decision

Option B: Use `approve` (Maccabi) or `send` (other centers) as the canonical approval events. The `save` event is not an approval action and must be excluded from approval logic across all reports and analytics.

## Rationale

`save` is an interim action — clinicians save drafts repeatedly before approving. Including `save` contaminates timing metrics and inflates approval counts. Standardizing on `approve`/`send` aligns the logic across all clinic centers.

## Consequences

- Shmulik's existing reports need revalidation under this logic
- Historical data before March 10 is mostly test data and should be excluded
- Report generation code must be updated to filter on `approve`/`send` only

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
