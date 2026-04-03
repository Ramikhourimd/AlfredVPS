---
alfred_tags:
- innovation-team/agent-infrastructure
- r&d/dependency-reduction
based_on:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 false positive: Telia''z wikilinks use valid YAML single-quote
  escaping; targets exist in vault. learn-assumption.base embeds are a systemic vault
  issue (_bases/ files not yet created).'
name: Innovation Team Needs Independent Agent Infrastructure
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[assumption/Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline]]'
relationships:
- confidence: 0.88
  context: Infra benefit supports independence need
  source: assumption/Innovation Team Needs Independent Agent Infrastructure.md
  target: assumption/Innovation Team Own Agent Infrastructure Reduces R&D Dependency.md
  type: supports
- confidence: 0.6
  context: Infra need relates to feature dev independence
  source: assumption/Innovation Team Needs Independent Agent Infrastructure.md
  target: assumption/Patient File Upload Feature Is Near Production Readiness.md
  type: related-to
source: Rami Khouri, Product and Development Update Meeting 2026-02-12
source_date: '2026-02-12'
status: active
type: assumption
---

# Innovation Team Needs Independent Agent Infrastructure

## Claim

The Innovation team needs its own AI agent infrastructure independent from the R&D team (Shachar) to maintain development velocity. Currently, every new agent capability (file classification, preprocessing, new data access) requires API coordination with R&D, which creates blocking dependencies.

## Basis

During the 2026-02-12 product update meeting, Rami stated that "once the Innovation team has its own agent infrastructure, it will be less dependent on R&D." The file classification agent specifically was blocked waiting for a Sunday coordination meeting with Shachar to define the technical approach for APIs.

## Evidence Trail

- 2026-02-12: File upload agent blocked on R&D API coordination
- 2026-02-03: AI agent pipeline training showed all agents depend on APIs from Shachar's team
- 2025-12-05: Retool prioritization discussion showed similar cross-team dependency patterns

## Impact

If this assumption is wrong (i.e., tight R&D coupling is acceptable long-term), the team risks permanent velocity constraints on AI agent development. If correct, investment in independent infrastructure would unblock parallel development of new agents.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]