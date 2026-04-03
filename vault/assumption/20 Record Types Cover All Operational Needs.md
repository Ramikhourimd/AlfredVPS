---
based_on: []
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-25'
invalidated_by: []
janitor_note: 'ORPHAN001 — no inbound wikilinks. This assumption is referenced by
  the decision record via related: but no other record links back to it. Consider
  adding [[assumption/20 Record Types Cover All Operational Needs]] to the decision
  record or a project record.'
name: 20 Record Types Cover All Operational Needs
project: []
related:
- '[[decision/Unified Operational System Over Specialized Tools]]'
source: Start Here.md record type taxonomy
status: active
type: assumption
---

# 20 Record Types Cover All Operational Needs

## Claim

The current taxonomy of 20 record types (project, task, session, conversation, input, person, org, location, account, asset, event, note, process, run, decision, assumption, constraint, contradiction, synthesis, view) is sufficient to model all operational data without requiring additional types.

## Basis

The system was designed around these 20 types and Start Here.md presents them as the complete set. The taxonomy spans work management (project, task), communication (conversation, input), knowledge (note, session), entities (person, org, location), operations (process, run, account, asset, event), and learning (decision, assumption, constraint, contradiction, synthesis).

## Evidence Trail

- Start Here.md lists "20 record types" as the foundational structure
- Templates exist for all 20 types, suggesting the taxonomy has been validated through use

## Impact

If a 21st type is needed, it would require new templates, base views, and potentially CLI updates. The decision to keep types fixed means edge cases must fit existing types (e.g., using note subtypes rather than new types).
