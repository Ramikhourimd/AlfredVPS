---
alfred_tags:
- ai-agent/bottlenecks
- r&d/dependencies
cluster_sources:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
- '[[task/Deliver Full API Schemas for Clinical Platform]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z AI Clinical Platform wikilink is YAML-escape false
  positive (Telia''''z = Telia''z, verify target exists). Base view embeds (learn-synthesis.base#Sources,
  #Related) reference _bases/learn-synthesis.base which does not exist — vault-wide
  infrastructure gap, embeds preserved. ORPHAN001 — no inbound links from other records.'
name: Cross-Team Dependencies Between Innovation and R&D Slow Multiple Workstreams
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams]]'
- '[[person/Shachar]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.95
  context: Specific Innovation-R&D deps support R&D bottleneck
  source: synthesis/Cross-Team Dependencies Between Innovation and R&D Slow Multiple
    Workstreams.md
  target: synthesis/Cross-Team R&D Dependencies Are a Systemic Bottleneck.md
  type: supports
- confidence: 0.8
  context: Both recurring blockers in cross-team workstreams
  source: synthesis/Cross-Team Dependencies Between Innovation and R&D Slow Multiple
    Workstreams.md
  target: synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams.md
  type: related-to
status: draft
supports:
- '[[assumption/Innovation Team Needs Independent Agent Infrastructure]]'
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
type: synthesis
---

# Cross-Team Dependencies Between Innovation and R&D Slow Multiple Workstreams

## Insight

The Innovation team (Rami, Rivi, Ohad) and the R&D team (Shachar) operate as separate functions with API-mediated coordination. Nearly every new capability the Innovation team wants to build requires API availability, database views, or technical coordination from R&D. This creates a recurring serialization bottleneck where Innovation work queues behind R&D availability.

## Evidence

1. **File classification agent** (2026-02-12): Blocked waiting for Sunday meeting with Shachar to define API approach for PDF/image preprocessing
2. **AI agent pipeline** (2026-02-03): All agents depend on APIs from Shachar's team for data access
3. **KPI dashboards** (2025-12-05, 2026-02-12): Require Shmulik to create additional database views; Roy mapping metrics to DB columns reveals gaps
4. **API schemas** (2026-02-25): Full API schema delivery is a cross-team deliverable
5. **Retool fixes** (2025-12-05): Login, Teams integration, and secretary workflows all require R&D development capacity

This is distinct from the existing "Data Access Fragmentation" synthesis, which focuses on scattered data sources. This pattern is about organizational coordination overhead — even when the data architecture is understood, getting the implementation done requires cross-team scheduling.

## Implications

- Innovation velocity is capped by R&D availability and prioritization
- Every new agent or feature requires a coordination meeting before development can begin
- The API-first approach (already decided) partially addresses this by creating stable interfaces, but the initial API creation still requires R&D
- Independent agent infrastructure for Innovation would decouple the teams for agent-level work

## Applicability

Applies to all workstreams where Innovation team produces AI agents, dashboards, or analytical tools that depend on production data access or platform APIs. Most acute for AI agent development and KPI dashboard creation.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]