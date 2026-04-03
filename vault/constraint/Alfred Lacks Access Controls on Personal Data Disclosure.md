---
authority: system design
created: '2026-03-08'
janitor_note: 'Previous janitor_note was incorrect: _bases/ directory EXISTS and learn-constraint.base
  embeds are valid. LINK001 flags are false positives. Cleared by vault-janitor 2026-03-14.'
name: Alfred Lacks Access Controls on Personal Data Disclosure
project:
- '[[project/Alfred Development]]'
related:
- '[[assumption/Alfred User Knowledge Derived From Vault Graph Not User Profile]]'
- '[[conversation/Alfred Chat — Untitled Chat 2026-03-03]]'
source: Alfred chat conversations 2026-03-03
source_date: '2026-03-03'
status: active
type: constraint
---

# Alfred Lacks Access Controls on Personal Data Disclosure

## Constraint

When a user asks Alfred "what do you know about me?", the system traverses the full vault graph and discloses all linked records — including family members, medical roles, project details, geographic roots, and organizational affiliations — without filtering, scoping, or access controls.

## Source

Observed in four near-identical Alfred chat sessions on 2026-03-03. Alfred responded to "what do you know about me?" by enumerating: professional role (psychiatrist, CMO at Telia'z), active projects (clinic operations, UK expansion, AI research, Alfred Development), family members (mother, relative), geographic origins (Galilee region), and clinical supervision details. All derived from vault graph traversal.

## Implications

- Any user with access to Alfred can surface all linked personal, family, and professional data in a single query
- No sensitivity tiers or disclosure scoping exist — clinical, family, and professional data are treated identically
- If Alfred is ever exposed to additional users or shared contexts, this becomes a privacy risk
- The current design assumes a single-user vault; multi-user or delegated access would require disclosure controls

## Expiry / Review

Review when: (1) multi-user access is considered, (2) Alfred is exposed beyond local CLI, or (3) vault contains sensitive third-party data requiring access controls.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
