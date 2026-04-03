---
alfred_tags:
- telia'z/restructuring
- clinical-operations/scaling
- partnerships/uk
cluster_sources:
- '[[constraint/Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility
  Split]]'
- '[[assumption/CM vs Psychiatrist Screen Split Determines AI Prompt Content]]'
- '[[constraint/DSM Criteria Require Criterion-Level Granularity in Screen Design]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
confidence: high
created: '2026-03-07'
janitor_note: 'LINK001: project wikilink [[project/Telia''z AI Clinical Platform]]
  uses YAML apostrophe escaping (Telia''''z) which is valid, not broken. ORPHAN001:
  no inbound links — newly created synthesis, may gain links as cluster sources reference
  it.'
name: Clinical Screen Responsibility Split Is a Single Decision Gating Multiple Workstreams
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[constraint/No Inter-Session Documentation Capability in Current System]]'
- '[[decision/All Case Manager Questions Delivered Dynamically From Prompt]]'
status: draft
supports:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
type: synthesis
---

# Clinical Screen Responsibility Split Is a Single Decision Gating Multiple Workstreams

## Insight

The case manager vs psychiatrist clinical responsibility split is not just a UX design question — it is a single decision point that gates at least four dependent workstreams: (1) meeting screen UI design for both roles, (2) AI agent prompt content and question generation, (3) DSM criteria granularity in the psychiatrist interface, and (4) inter-session documentation scope. Until this split is finalized, all four workstreams remain blocked or built on unstable assumptions.

## Evidence

- **Screen design blocked**: The case manager screen cannot be designed until the responsibility split is finalized (constraint: Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility Split)
- **AI prompts dependent**: The CM vs psychiatrist split directly determines what each AI agent asks and summarizes (assumption: CM vs Psychiatrist Screen Split Determines AI Prompt Content)
- **DSM criteria affected**: The psychiatrist screen requires criterion-level granularity for DSM classification, which depends on knowing exactly what falls under psychiatric vs case manager scope (constraint: DSM Criteria Require Criterion-Level Granularity in Screen Design)
- **Task duplication signals urgency**: Two separate tasks exist for finalizing this split (Finalize Case Manager vs Psychiatrist Screen Responsibility Split; Finalize Case Manager vs Psychiatrist Screen Content Split), suggesting the issue has been raised in multiple contexts without resolution
- **Multiple people involved**: Rami, Shira, Ori, Alice, and Nadav are all named as participants in resolving this, indicating cross-functional coordination complexity

## Implications

This responsibility split should be treated as a critical-path decision. Resolving it unlocks parallel progress on screen design, AI prompt engineering, DSM classification, and documentation workflows. Delaying it creates compounding delays across all four workstreams.

## Applicability

Applies to all Telia'z clinical platform development — both the existing Retool system and the new platform rebuild. The split also affects the UK expansion, where screen designs will need to accommodate UK-specific clinical workflows.