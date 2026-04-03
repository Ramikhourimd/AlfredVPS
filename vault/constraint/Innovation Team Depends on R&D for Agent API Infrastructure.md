---
authority: Shachar (CTO / R&D lead)
created: '2026-02-27'
janitor_note: 'LINK001 false positives: Telia''z wikilinks use YAML single-quote escaping
  (targets exist). ORPHAN001: no inbound links — consider linking from project or
  task records.'
name: Innovation Team Depends on R&D for Agent API Infrastructure
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z Innovation Program]]'
related:
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
- '[[person/Shachar]]'
- '[[person/Rami Khouri]]'
source: Organizational structure — cross-team dependency
source_date: '2026-02-12'
status: active
type: constraint
---

# Innovation Team Depends on R&D for Agent API Infrastructure

## Constraint

The Innovation team cannot independently build or deploy new AI agents. Each new agent requires API endpoints and infrastructure that only Shachar's R&D team can provide. This creates a cross-team dependency where Innovation's delivery timeline is gated by R&D's availability and priorities.

## Source

Organizational division of responsibilities: R&D (Shachar) controls the production platform APIs, database access, and deployment infrastructure. Innovation (Rami) designs clinical AI features but cannot ship without R&D support.

## Implications

- Every new agent (file classification, future agents) requires an explicit coordination meeting with Shachar
- Innovation team's roadmap is partially hostage to R&D's sprint priorities
- Delays in R&D API delivery directly delay clinical AI feature rollout
- Rami is actively working to reduce this dependency by building own agent infrastructure, but this is aspirational

## Expiry / Review

This constraint expires if/when the Innovation team successfully builds its own agent infrastructure. Review when Innovation team technical capabilities are reassessed.
