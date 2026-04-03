---
approved_by: []
based_on:
- '[[assumption/Wikilink Graph Is Sufficient for All Record Relationships]]'
- '[[Start Here]]'
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by: []
janitor_note: '"LINK001 — broken base view embeds: \![[learn-decision.base#Based On]]
  and \![[learn-decision.base#Related]]. The file _bases/learn-decision.base does
  not exist. Create it or remove the embeds. Do NOT auto-remove — base view embeds
  require human decision. Also has DUPLICATE base view embeds at end of body (appears
  twice). Consider removing the duplicate set."'
name: Base Views With hasLink for Automatic Record Aggregation
project: []
related: []
session: null
source: Start Here.md onboarding documentation
source_date: '2025-02-25'
status: final
supports:
- '[[decision/Unified Operational System Over Specialized Tools]]'
tags: []
type: decision
---

# Base Views With hasLink for Automatic Record Aggregation

## Context

Alfred OS needed a mechanism for records to appear in the right views (project pages, person pages, Home view) without manual curation or duplication. The system needed "one record, many views."

## Options Considered

1. **Manual lists** — Maintain explicit lists of related records on each page. Simple but high-maintenance, prone to drift.
2. **Tag-based filtering** — Use tags to group records. Flexible but loses the specificity of direct relationships.
3. **`file.hasLink(this.file)` base views** — Let Obsidian's base/Dataview engine automatically aggregate any record that links to the current file.

## Decision

Use `file.hasLink(this.file)` in base views as the primary aggregation mechanism. When a task links to a project in its frontmatter, it automatically appears in that project's Tasks section. When it links to a person, it appears on their page. No manual curation needed.

## Rationale

This approach directly supports the "unified system" decision — a single record with wikilinks in frontmatter automatically surfaces in every relevant context. It eliminates duplication and maintenance burden. The mechanism is native to Obsidian's capabilities.

## Consequences

- Records MUST have correct wikilinks in frontmatter to be discoverable — a missing or typo'd link means the record is invisible in that context
- View performance depends on Obsidian's query engine scaling with vault size
- Adding a new view or context only requires a new base query, not data migration

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
