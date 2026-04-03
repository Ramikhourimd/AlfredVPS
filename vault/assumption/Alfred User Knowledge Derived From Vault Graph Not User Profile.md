---
based_on:
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03]]'
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03 2026-03-03]]'
confidence: high
created: '2026-03-07'
janitor_note: 'LINK001: Base view embeds reference _bases/ files not yet created (systemic).
  Body uses escaped embeds (\\![[) instead of \![[ — needs manual body fix. ORPHAN001:
  No inbound links.'
name: Alfred User Knowledge Derived From Vault Graph Not User Profile
project:
- '[[project/Alfred Development]]'
source: Rami Khouri conversation with Alfred 2026-03-03
source_date: '2026-03-03'
status: active
type: assumption
---

# Alfred User Knowledge Derived From Vault Graph Not User Profile

## Claim

Alfred derives its personalization and user knowledge from traversing vault records (person, project, org, conversation entities) rather than from the dedicated user-profile.md file. The system functions with full contextual awareness even when user-profile.md is completely empty.

## Basis

In multiple conversations on 2026-03-03, when Rami asked "what do you know about me?", Alfred responded with extensive personal, professional, and family details — all sourced from vault records. Alfred itself noted: "Your user-profile.md is actually empty — the sections for About Me, My Work, etc. are all blank."

## Evidence Trail

- 2026-03-03: Four separate conversation records confirm Alfred disclosed detailed knowledge despite empty user-profile.md
- Knowledge included: professional role (psychiatrist/CMO at Teliaz), active projects, family members, geographic roots — all from vault graph traversal

## Impact

- The user-profile.md file is currently non-essential for Alfred personalization
- If user-profile.md is intended as the canonical source of user context, the current behavior bypasses it entirely
- Privacy implications: vault-wide traversal exposes all linked personal data on request

\![[learn-assumption.base#Depends On This]]
\![[learn-assumption.base#Related]]
