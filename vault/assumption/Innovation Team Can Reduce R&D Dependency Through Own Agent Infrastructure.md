---
alfred_tags:
- innovation-team/agent-infrastructure
- r&d/dependency-reduction
based_on:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
confidence: low
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilinks use valid YAML single-quote escaping (false
  positive). ORPHAN001 — no inbound links; consider linking from project/Telia'z AI
  Clinical Platform or project/Telia'z Innovation Program.
name: Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
relationships:
- confidence: 0.85
  context: Own infra capability supports need
  source: assumption/Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure.md
  target: assumption/Innovation Team Needs Independent Agent Infrastructure.md
  type: supports
- confidence: 0.95
  context: Similar claims on infra reducing dep
  source: assumption/Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure.md
  target: assumption/Innovation Team Own Agent Infrastructure Reduces R&D Dependency.md
  type: related-to
- confidence: 0.6
  context: Infra independence linked to feature readiness progress
  source: assumption/Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure.md
  target: assumption/Patient File Upload Feature Is Near Production Readiness.md
  type: related-to
source: Rami Khouri — implied during product sync discussion
source_date: '2026-02-12'
status: active
type: assumption
---

# Innovation Team Can Reduce R&D Dependency Through Own Agent Infrastructure

## Claim

Once the Innovation team has its own agent infrastructure, it will be significantly less dependent on Shachar's R&D team for building and deploying new AI agents. This would allow the Innovation team to iterate on clinical AI features independently.

## Basis

Rami stated during the 2026-02-12 product sync that once "the Innovation team has its own agent infrastructure, it will be less dependent" on R&D. This belief is driving the strategic direction of building internal agent capabilities rather than routing all agent work through R&D.

## Evidence Trail

- 2026-02-12: Rami explicitly mentions desire for Innovation team infrastructure independence
- Multiple tasks show cross-team API dependencies (file upload agent, agent pipeline training)
- Current state: every new agent requires API coordination with Shachar

## Impact

- Drives investment in Innovation team's own technical capabilities
- If incorrect (R&D APIs remain necessary for all agents), the Innovation team may under-invest in the R&D relationship
- Shapes hiring and resource allocation decisions for the Innovation team