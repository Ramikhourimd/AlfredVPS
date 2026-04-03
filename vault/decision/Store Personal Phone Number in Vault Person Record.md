---
approved_by: []
based_on:
- '[[conversation/Alfred Chat — Knowledge Base Q&A Session

  Knowledge Base Q&A Session Refin 2026-03-09]]'
challenged_by: []
confidence: high
created: '2026-03-10'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — based_on contains malformed multiline wikilink (conversation
  filename has literal newlines — filesystem issue, not a vault link error). Base
  view embeds (learn-decision.base) reference missing _bases/ infrastructure (vault-wide
  gap). DUPLICATE base view embeds after --- separator in body need manual removal
  (vault CLI lacks body-edit). ORPHAN001 — no inbound wikilinks.
name: Store Personal Phone Number in Vault Person Record
project:
- '[[project/Alfred Development]]'
related: []
session: null
source: Rami Khouri — explicit opt-in during Q&A session
source_date: '2026-03-09'
status: final
supports:
- '[[assumption/Alfred User Knowledge Derived From Vault Graph Not User Profile]]'
tags: []
type: decision
---

# Store Personal Phone Number in Vault Person Record

## Context

During a structured Q&A knowledge base audit session, Alfred identified that Rami's person record had no phone number stored. Alfred asked whether Rami wanted to share and store his phone number.

## Options Considered

1. **Share and store** — Add phone number to the vault person record for completeness
2. **Don't store** — Keep phone number out of the vault for privacy reasons

## Decision

Rami chose to share his phone number (+972528769737) and have it stored in the vault person record.

## Rationale

Completeness of person records improves vault data quality. Rami, as the vault owner, made an explicit informed choice to store his own contact information.

## Consequences

- Person record now contains sensitive contact information
- Reinforces the need for access controls on personal data disclosure (see [[constraint/Alfred Lacks Access Controls on Personal Data Disclosure]])
- Sets precedent that personal contact details are acceptable to store in the vault when the owner consents

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
