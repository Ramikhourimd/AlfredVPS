---
alfred_tags:
- innovation-team/tools
- innovation-team/processes
approved_by: []
based_on:
- '[[assumption/Innovation Team Needs Independent Agent Infrastructure]]'
- '[[assumption/Innovation Team Own Agent Infrastructure Reduces R&D Dependency]]'
challenged_by: []
confidence: medium
created: '2026-03-08'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: DUPLICATE base view embeds at end of body — remove the "---" divider
  and second set of \![[learn-decision.base#Based On]] and \![[learn-decision.base#Related]]
  embeds. Manual body edit required (CLI lacks body-replace). ORPHAN001 — no inbound
  wikilinks.
name: Innovation Team Adopts No-Code Tools for Rapid System Development
project:
- '[[project/Telia''z Innovation Program]]'
related:
- '[[note/Conference Discussion Sentiment Analysis Ethnic Disparities and Clinic Scale
  2025-11-13]]'
- '[[constraint/Innovation Team Depends on R&D for Agent API Infrastructure]]'
relationships:
- confidence: 0.8
  context: Both Innovation Team tool adoptions
  source: decision/Innovation Team Adopts No-Code Tools for Rapid System Development.md
  target: decision/Migrate Innovation Team From Manus AI to Claude Desktop.md
  type: related-to
- confidence: 0.6
  context: Innovation Team process improvements
  source: decision/Innovation Team Adopts No-Code Tools for Rapid System Development.md
  target: decision/Transition to Notion Slack-First Communication for Innovation Team.md
  type: related-to
session: null
source: Rami Khouri
source_date: '2025-11-13'
status: draft
supports:
- '[[assumption/Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure]]'
tags: []
type: decision
---

# Innovation Team Adopts No-Code Tools for Rapid System Development

## Context

The Innovation team needs to build and iterate on systems faster than the R&D/CTO team can accommodate in their development backlog. Cross-team dependencies on Shachar's engineering team create bottlenecks for innovation projects.

## Options Considered

1. **Wait for R&D backlog capacity** — Queue all innovation development needs through Shachar's team
2. **Hire dedicated developers for innovation** — Build a separate engineering team under innovation
3. **Adopt no-code/low-code tools** — Use platforms that allow non-engineers to build functional systems rapidly

## Decision

The Innovation team will use no-code development tools (Vibe coding, Label, Base44) to build systems from scratch, staffed by people from non-software backgrounds who have some development experience. This approach can stand up a functional system within a week.

## Rationale

No-code tools allow the Innovation team to operate independently from the CTO's engineering backlog while maintaining rapid iteration capability. The challenge remains giving these systems technical robustness and eventually integrating them with the core software team's infrastructure.

## Consequences

- Innovation team can prototype and validate concepts within days rather than waiting weeks/months for R&D capacity
- Reduces the R&D dependency constraint that blocks multiple innovation workstreams
- Creates a potential technical debt risk if no-code prototypes become production systems without proper engineering review
- Requires a handoff protocol for when no-code prototypes need to become production-grade

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]