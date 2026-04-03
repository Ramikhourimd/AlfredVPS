---
authority: Data security best practice
created: '2026-03-11'
janitor_note: 'LINK001: base view embeds reference _bases/ files that do not exist
  (learn-constraint.base) — vault-wide structural gap, not a per-file fix. ORPHAN001:
  no inbound wikilinks — human review needed to determine if this record should be
  linked from a project or decision.'
location: []
name: Vault Source Recordings Contain Unredacted Financial Credentials
project: []
related:
- '[[note/Personal Credit Card Transaction Voice Memo 2025-09-01]]'
source: Personal credit card transaction voice memo
source_date: '2025-09-01'
status: active
tags: []
type: constraint
---

# Vault Source Recordings Contain Unredacted Financial Credentials

## Constraint

At least one source voice memo recording in the vault inbox contains full, unredacted credit card credentials (card number, expiry date, and security code). The note record itself redacted the data, but the original source recording file remains.

## Source

Discovered during the 2025-09-01 voice memo processing. An American Express card's full credentials were spoken aloud during a phone payment transaction and captured by ambient recording.

## Implications

- The vault ingestion pipeline does not automatically detect or redact financial credentials from source audio
- Any compromise of the source inbox files could expose payment credentials
- Similar unredacted sensitive data (medical records, passwords, personal identifiers) may exist in other ambient recordings
- Source recordings containing credentials should be flagged for deletion after note extraction

## Expiry / Review

Active until a source file audit confirms all credential-containing recordings have been deleted or the ingestion pipeline adds credential detection.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
