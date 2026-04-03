---
alfred_tags:
- ai-agent/bottlenecks
- r&d/dependencies
cluster_sources:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
- '[[task/Deliver Full API Schemas for Clinical Platform]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 — base view embeds (learn-synthesis.base#Sources, learn-synthesis.base#Related)
  reference _bases/learn-synthesis.base which does not exist. Vault-wide infrastructure
  issue: _bases/ directory is missing entirely. Embeds preserved pending _bases creation.
  Telia''z wikilinks are valid (YAML escaping false positive).'
name: Cross-Team R&D Dependencies Are a Systemic Bottleneck
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
related:
- '[[synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams]]'
- '[[decision/Design APIs as Low-Level Entity Endpoints with Sub-Resources]]'
relationships:
- confidence: 0.8
  context: Systemic R&D deps and data access both bottlenecks
  source: synthesis/Cross-Team R&D Dependencies Are a Systemic Bottleneck.md
  target: synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams.md
  type: related-to
status: draft
supports:
- '[[assumption/Innovation Team Own Agent Infrastructure Reduces R&D Dependency]]'
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
type: synthesis
---

# Cross-Team R&D Dependencies Are a Systemic Bottleneck

## Insight

Multiple Innovation team workstreams are blocked or slowed by dependencies on Shachar's R&D team for API access, infrastructure changes, and platform modifications. This is not an isolated coordination issue but a structural pattern: the Innovation team generates requirements faster than the R&D team can expose the necessary interfaces. The existing "Data Access Fragmentation" synthesis captures the data layer of this problem, but the dependency extends beyond data to APIs, agent infrastructure, and platform architecture.

## Evidence

1. **File classification agent** (2026-02-12): Blocked on R&D APIs for PDF/image-to-text preprocessing. Rami must meet Shachar specifically to unblock this.
2. **Agent pipeline infrastructure** (2026-02-03): Training session reveals agents depend on specific API data flows controlled by R&D — variables injection, patient data retrieval, and output storage all flow through R&D-owned systems.
3. **API schema delivery** (2026-02-25): Full API schemas for the clinical platform are a pending deliverable from R&D.
4. **Retool system fixes** (2025-12-05): Teams integration, login fixes, and KPI dashboards all require R&D capacity. Shachar proposed hiring a contractor specifically to address capacity constraints.
5. **Platform rebuild** (2025-12-05): Shachar is simultaneously rebuilding the platform from scratch while maintaining the existing system, splitting R&D attention.

## Implications

- Innovation team velocity is capped by R&D's available bandwidth, not by its own capacity
- The API-first decision was partly motivated by this bottleneck — formal APIs would create a stable interface layer
- Rami's push for independent agent infrastructure is a direct response to this pattern
- Hiring contractors (as Shachar suggested for Teams integration) may be needed across multiple workstreams, not just one
- Risk: if the platform rebuild absorbs most R&D capacity, Innovation team blockers could persist for 6+ months

## Applicability

This pattern affects any Telia'z workstream where the Innovation/Clinical team needs technical changes to production systems. It is particularly acute for AI agent development, where rapid iteration cycles clash with enterprise platform development timelines.

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]