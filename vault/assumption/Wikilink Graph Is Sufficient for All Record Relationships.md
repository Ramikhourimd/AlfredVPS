---
alfred_tags:
- alfred-os/core
- obsidian/system
- ai-assistant
based_on:
- '[[Start Here]]'
confidence: medium
created: '2026-02-25'
janitor_note: '"LINK001 — [[wikilinks]] in body is a conceptual reference, not an
  actual record link. Broken base view embeds: \![[learn-assumption.base#Depends On
  This]] and \![[learn-assumption.base#Related]]. The file _bases/learn-assumption.base
  does not exist. Create it or remove the embeds. Do NOT auto-remove — base view embeds
  require human decision."'
name: Wikilink Graph Is Sufficient for All Record Relationships
related:
- '[[decision/Unified Operational System Over Specialized Tools]]'
relationships:
- confidence: 0.85
  context: Wikilink assump supports Alfred
  source: assumption/Wikilink Graph Is Sufficient for All Record Relationships.md
  target: project/Alfred Development.md
  type: supports
- confidence: 0.8
  context: Linking assumption for vault
  source: assumption/Wikilink Graph Is Sufficient for All Record Relationships.md
  target: README.md
  type: supports
source: Start Here.md onboarding documentation
source_date: '2025-02-25'
status: active
type: assumption
---

# Wikilink Graph Is Sufficient for All Record Relationships

## Claim

All record relationships in Alfred OS can be expressed and discovered through wikilinks in YAML frontmatter fields. No relational database, join tables, or external index is needed — Obsidian's link graph plus Dataview/base queries provide sufficient connectivity.

## Basis

The Start Here onboarding note states: "Records link to each other via `[[wikilinks]]` in frontmatter. The graph connects everything." The entire system architecture depends on this — every template uses wikilink fields (project, assigned, owner, org, related, etc.) as the sole mechanism for inter-record relationships.

## Evidence Trail

- 20 record types all use wikilink frontmatter for relationships (confirmed in templates)
- Base views use `file.hasLink(this.file)` to aggregate related records automatically
- No external database or indexing system exists in the architecture

## Impact

If wikilinks prove insufficient (e.g., for complex multi-hop queries, performance at scale, or bidirectional relationship integrity), the entire record system would need a fundamentally different connectivity layer. Every template, every base view, and every dynamic section depends on this assumption.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]