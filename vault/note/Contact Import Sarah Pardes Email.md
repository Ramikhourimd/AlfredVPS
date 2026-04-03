---
alfred_tags:
- contacts/imports
created: '2026-03-01'
description: Contact import record matching sarah@healthymind.co.il to existing person
  record Sarah Pardes, Case Manager at Telia'z.
janitor_note: LINK001 — Telia'z wikilinks (project/Telia'z Clinic Israel, org/Telia'z)
  are valid (YAML escaping false positive). related.base#All is a template-standard
  base view embed referencing _bases/related.base which does not exist — vault-wide
  structural issue, embed preserved. ORPHAN001 — no inbound links; contact import
  record, consider linking from relevant project.
name: Contact Import Sarah Pardes Email
project: '[[project/Telia''z Clinic Israel]]'
related:
- '[[person/Sarah Pardes]]'
- '[[org/Telia''z]]'
- '[[asset/HealthyMind Platform]]'
relationships: []
session: null
status: active
subtype: reference
tags: []
type: note
---

# Contact Import Sarah Pardes Email

## Context

Imported from contact record (Firebase doc ID: `6jmnaawZFDzqBeN5z0Vg`). This contact contained only an email address with no name. Matched to existing person record [[person/Sarah Pardes]] based on the first-name prefix "sarah" at the `healthymind.co.il` staff email domain, and Sarah Pardes being the only Sarah employed at [[org/Telia'z]].

## Details

- **Email:** sarah@healthymind.co.il
- **Name:** Not provided in source (matched to Sarah Pardes)
- **Source:** Contact import (JSON)

## Actions Taken

- Updated `email` field on [[person/Sarah Pardes]] from null to `sarah@healthymind.co.il`

## Related
![[related.base#All]]