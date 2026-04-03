---
cluster_sources:
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03]]'
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03 2026-03-03]]'
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03 2026-03-03 2026-03-03]]'
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03 2026-03-03 2026-03-03 2026-03-03]]'
confidence: high
created: '2026-03-09'
janitor_note: LINK001 — Base view embeds (learn-synthesis.base#Sources, learn-synthesis.base#Related)
  reference _bases/learn-synthesis.base which may not exist yet — vault-wide infrastructure
  gap. ORPHAN001 — no inbound links; content is substantive, should be linked from
  Alfred Development project or related records.
name: Alfred Personalization Has Two Distinct Layers Config Identity and Vault Graph
  Knowledge
project:
- '[[project/Alfred Development]]'
related:
- '[[constraint/Alfred Lacks Access Controls on Personal Data Disclosure]]'
- '[[person/Rami Khouri]]'
status: active
supports:
- '[[assumption/Alfred User Knowledge Derived From Vault Graph Not User Profile]]'
type: synthesis
---

# Alfred Personalization Has Two Distinct Layers: Config Identity and Vault Graph Knowledge

## Insight

Alfred's personalization operates through two distinct mechanisms: (1) **identity recognition** via hardcoded configuration, and (2) **detailed knowledge** via vault graph traversal. When asked "how did you know I am Rami?", Alfred explicitly stated the name is "baked into my configuration" and "hardcoded". But when asked "what do you know about me?", Alfred traversed the vault graph to surface projects, family, roles, and organizational relationships — none of which came from the empty `user-profile.md`.

## Evidence

Across four near-identical conversations on 2026-03-03, Alfred consistently:
- Attributed name recognition to hardcoded config ("whoever set up this assistant hardcoded that in")
- Derived detailed knowledge from vault records (projects, orgs, persons, family links)
- Noted that `user-profile.md` is empty, confirming knowledge comes from the graph, not the profile

This two-layer pattern was consistent across all four conversation instances.

## Implications

- **Layer 1 (Config)**: If the hardcoded name is wrong, Alfred will misidentify the user — there's no self-correcting mechanism from vault data.
- **Layer 2 (Vault Graph)**: Knowledge quality depends entirely on vault record completeness and accuracy. The empty user-profile.md is irrelevant because the graph provides richer data anyway.
- The user-profile.md file may be unnecessary if vault graph traversal is the primary knowledge source.

## Applicability

Applies to Alfred Development — specifically the personalization architecture and any future work on user identity or knowledge retrieval.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]
