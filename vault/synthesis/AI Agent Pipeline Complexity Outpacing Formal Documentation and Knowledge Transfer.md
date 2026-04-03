---
alfred_tags:
- ai-agent/bottlenecks
- r&d/dependencies
cluster_sources:
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[note/Product and Development Update Meeting 2026-02-12]]'
- '[[task/Create AI Agent Inventory and Input-Output Breakdown]]'
- '[[task/Coordinate File Upload Agent API With Shachar]]'
confidence: medium
created: '2026-02-27'
janitor_note: LINK001 — Telia'z wikilink (project/Telia'z AI Clinical Platform) is
  valid (YAML escaping false positive). ORPHAN001 — no inbound wikilinks; consider
  linking from project/Telia'z AI Clinical Platform or related AI pipeline records.
name: AI Agent Pipeline Complexity Outpacing Formal Documentation and Knowledge Transfer
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Ohad Edri]]'
- '[[person/Rami Khouri]]'
relationships:
- confidence: 0.75
  context: Both highlight workstream delays from complexity and deps
  source: synthesis/AI Agent Pipeline Complexity Outpacing Formal Documentation and
    Knowledge Transfer.md
  target: synthesis/Cross-Team Dependencies Between Innovation and R&D Slow Multiple
    Workstreams.md
  type: related-to
- confidence: 0.7
  context: Complexity ties to systemic R&D dependency issues
  source: synthesis/AI Agent Pipeline Complexity Outpacing Formal Documentation and
    Knowledge Transfer.md
  target: synthesis/Cross-Team R&D Dependencies Are a Systemic Bottleneck.md
  type: related-to
- confidence: 0.65
  context: Both block progress via knowledge/data access gaps
  source: synthesis/AI Agent Pipeline Complexity Outpacing Formal Documentation and
    Knowledge Transfer.md
  target: synthesis/Data Access Fragmentation Is a Recurring Blocker Across Workstreams.md
  type: related-to
status: draft
type: synthesis
---

# AI Agent Pipeline Complexity Outpacing Formal Documentation and Knowledge Transfer

## Insight

The clinical AI agent pipeline is growing in scope and complexity faster than the team's ability to document and transfer knowledge about it. New agents are being added (file classification agent), new team members require hands-on training sessions, and the team has recognized the need for a formal agent inventory — but the inventory does not yet exist. Knowledge about agent inputs, outputs, prompt structures, and data flows currently resides in the heads of a few individuals.

## Evidence

1. **Training session required for onboarding** (2026-02-03): Ohad led a multi-hour hands-on training covering the full technical stack for a new team member. This indicates the system cannot be understood from documentation alone.
2. **Agent inventory task created but not completed** (2026-02-03): Ohad explicitly assigned the creation of a comprehensive agent input/output mapping document, confirming no such document exists.
3. **New agents being added without formal architecture review** (2026-02-12): The file classification agent was proposed and approved in a product sync meeting without reference to an existing architecture document or agent registry.
4. **Pipeline has 5+ agents with interdependencies**: CM Agenda, CM Summary, Triage, Cross-Session, Patient Summary — each with variable injection patterns and data dependencies that are not formally documented.

## Implications

- **Bus factor risk**: If Ohad or Rami are unavailable, agent pipeline knowledge is difficult to recover
- **Onboarding cost**: Each new team member requires significant hands-on training time
- **Integration risk**: New agents (file classification) may introduce conflicts or redundancies with existing agents without a formal registry to cross-reference
- **The agent inventory task is a critical enabler** — its completion would significantly reduce these risks

## Applicability

Applies to the Telia'z AI Clinical Platform and any team expanding the AI agent pipeline. The pattern of growing complexity without documentation is common in early-stage AI product teams and tends to create escalating coordination costs if not addressed.