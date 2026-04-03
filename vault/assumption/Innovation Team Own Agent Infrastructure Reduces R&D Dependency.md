---
alfred_tags:
- innovation-team/agent-infrastructure
- r&d/dependency-reduction
based_on:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-27'
invalidated_by: []
janitor_note: 'LINK001 false positives: project/Telia''z wikilinks flagged due to
  YAML single-quote escaping — all targets verified to exist. Base view embeds (learn-assumption.base)
  reference non-existent _bases/ file — preserved per vault rules; base file may need
  creation.'
name: Innovation Team Own Agent Infrastructure Reduces R&D Dependency
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
related:
- '[[assumption/Simple Orchestrator Without MCP Is Sufficient for Initial AI Pipeline]]'
- '[[decision/Adopt API-First Approach Over Manual Data Exports]]'
relationships:
- confidence: 0.6
  context: Infra benefit supports feature production readiness
  source: assumption/Innovation Team Own Agent Infrastructure Reduces R&D Dependency.md
  target: assumption/Patient File Upload Feature Is Near Production Readiness.md
  type: related-to
source: Rami Khouri in product development meeting
source_date: '2026-02-12'
status: active
type: assumption
---

# Innovation Team Own Agent Infrastructure Reduces R&D Dependency

## Claim

Once the Innovation team has its own agent infrastructure (API access, preprocessing capabilities, prompt management), it will be significantly less dependent on Shachar's R&D team for building and iterating on AI agents. This would unblock the Innovation team to develop, test, and deploy agents on their own timeline.

## Basis

Rami stated during the 2026-02-12 product meeting that the Innovation team's dependency on R&D for agent-related APIs is a bottleneck. The file classification agent, for example, requires APIs from Shachar's team for preprocessing (PDF/image to text conversion). Rami planned to meet Shachar on Sunday specifically to resolve this dependency. The belief is that establishing an independent agent infrastructure would eliminate this recurring coordination overhead.

## Evidence Trail

- 2026-02-12: Rami identifies R&D API dependency as blocking file classification agent development
- 2026-02-03: Training session shows agents depend on specific API data flows controlled by R&D
- Multiple tasks blocked on cross-team API coordination (file upload agent, API schemas)

## Impact

If true, this justifies investment in building independent agent infrastructure for the Innovation team. If false (e.g., R&D APIs are too deeply coupled to the production system for independent operation), the team will need a different coordination model — possibly embedding an R&D engineer in the Innovation team or establishing formal API contracts.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]