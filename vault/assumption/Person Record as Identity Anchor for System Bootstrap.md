---
alfred_tags:
- alfred-os/core
- obsidian/system
- ai-assistant
based_on:
- '[[Start Here]]'
confidence: high
created: '2026-02-25'
janitor_note: '"LINK001 — broken base view embeds: \![[learn-assumption.base#Depends
  On This]] and \![[learn-assumption.base#Related]]. The file _bases/learn-assumption.base
  does not exist. Create it or remove the embeds. Do NOT auto-remove — base view embeds
  require human decision. ORPHAN001 — no inbound wikilinks from other records. Consider
  linking from a relevant project or decision record."'
name: Person Record as Identity Anchor for System Bootstrap
related:
- '[[decision/Base Views With hasLink for Automatic Record Aggregation]]'
- '[[assumption/Wikilink Graph Is Sufficient for All Record Relationships]]'
relationships:
- confidence: 0.85
  context: Identity assump supports Alfred
  source: assumption/Person Record as Identity Anchor for System Bootstrap.md
  target: project/Alfred Development.md
  type: supports
- confidence: 0.8
  context: Foundational system assumption
  source: assumption/Person Record as Identity Anchor for System Bootstrap.md
  target: README.md
  type: supports
source: Start Here.md onboarding documentation
source_date: '2025-02-25'
status: active
type: assumption
---

# Person Record as Identity Anchor for System Bootstrap

## Claim

The entire Alfred OS system bootstraps from a single Person record per user. The Home view, task assignments, session participation, conversation tracking, and all personal aggregation flows from linking to this one record. Without it, the system has no concept of "your stuff."

## Basis

The Start Here onboarding note instructs: "Create a file in `person/` using the Person template. This is your identity in the system." The Home view requires setting `owner:` to the Person record, and its bases use `file.hasLink(this.file)` — meaning all personal visibility depends on this single anchor point.

## Evidence Trail

- Step 1 of Quick Setup: create Person record
- Step 2: link Home view to Person record via `owner:` field
- All task assignment uses `assigned:` linking to Person
- Session participation uses `participants:` linking to Person
- The entire Home view collapses without this link

## Impact

This assumption means: (1) shared vaults with multiple users need careful identity separation, (2) renaming or moving a Person record could break all personal views, (3) there is no anonymous or unlinked mode of operation. If multi-user vaults or identity federation is ever needed, this assumption would need revisiting.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]