---
alfred_tags:
- telia'z/restructuring
- clinical-operations/scaling
- partnerships/uk
cluster_sources:
- '[[task/Finalize Case Manager vs Psychiatrist Screen Responsibility Split]]'
- '[[note/AI Agent Pipeline Training and Onboarding Session 2026-02-03]]'
- '[[task/Create AI Agent Inventory and Input-Output Breakdown]]'
- '[[task/Finalize Case Manager vs Psychiatrist Screen Content Split]]'
confidence: medium
created: '2026-03-01'
janitor_note: LINK001 — Telia'z AI Clinical Platform wikilink is YAML escaping false
  positive (target exists). constraint/Case Manager Screen Design... and synthesis/AI
  Agent Pipeline Complexity... both VERIFIED to exist — YAML escape false positives,
  not broken links. ORPHAN001 — no inbound wikilinks from other records.
name: Clinical Workflow Design Decisions Cascade Into AI Agent Quality
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[constraint/Case Manager Screen Design Blocked by Unfinalized Clinical Responsibility
  Split]]'
- '[[synthesis/AI Agent Pipeline Complexity Outpacing Formal Documentation and Knowledge
  Transfer]]'
- '[[decision/All Case Manager Questions Delivered Dynamically From Prompt]]'
status: draft
supports:
- '[[assumption/CM vs Psychiatrist Screen Split Determines AI Prompt Content]]'
- '[[decision/Five-Agent Sequential Pipeline for Clinical AI Summaries]]'
type: synthesis
---

# Clinical Workflow Design Decisions Cascade Into AI Agent Quality

## Insight

Clinical workflow design decisions — particularly the responsibility split between case managers and psychiatrists — directly determine the quality and accuracy of AI-generated summaries and agendas. The dependency chain runs: clinical role definitions → screen content design → AI prompt parameterization → agent output quality. This means delays or mistakes in upstream clinical decisions propagate as quality issues in downstream AI agents, and changes to clinical workflows require corresponding AI prompt re-engineering.

## Evidence

1. **Screen split → AI prompts**: The task to finalize the CM vs psychiatrist screen split explicitly states "This split directly feeds into AI prompts (what to ask in each session type)." This is the strongest signal — a direct, stated dependency.

2. **Dynamic prompt architecture**: The AI Agent Pipeline Training session (2026-02-03) revealed that agents use variable injection with fixed structural templates adapted by session type. This confirms that session-type clinical decisions (what each role covers) parameterize agent behavior.

3. **All questions from prompts**: The decision that all case manager questions are delivered dynamically from the prompt (not hardcoded in UI) means the prompt IS the clinical workflow definition — there is no UI safety net if the prompt is wrong.

4. **Blocking cascade**: The CM screen design is blocked by the unfinalized clinical split, which in turn blocks AI prompt finalization for CM agents. Three layers of work are queued behind a single clinical decision.

## Implications

- Clinical workflow decisions should be treated as AI architecture decisions — they have technical consequences beyond UX
- Changes to the CM/psychiatrist responsibility split should trigger a review of all affected agent prompts
- The team needs a lightweight change propagation process: when clinical roles change, flag affected agents for prompt review
- Quality measurement of AI agents is only meaningful after the upstream clinical definitions are stable

## Applicability

This pattern applies to the entire Telia'z AI Clinical Platform wherever clinical role definitions feed into AI prompt content. It is particularly relevant for: CM Agenda Agent, CM Summary Agent, Psychiatrist Summary Agent, and any future agents parameterized by session type or clinical role.