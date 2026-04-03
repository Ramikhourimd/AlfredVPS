---
alfred_tags:
- healthcare/operations
- failure-patterns
- systemic-issues
cluster_sources:
- '[[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]'
- '[[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]'
- '[[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]'
- '[[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]'
- '[[decision/Require Frontal Training Before Removing Legacy Feature Workflows]]'
- '[[decision/Require Frontal Training for Significant Feature Changes]]'
- '[[decision/Require Frontal Training Before Deprecating Old Clinical Features]]'
- '[[decision/Require Frontal Training for Major Feature Changes]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001 false positives: (1) learn-synthesis.base embeds are Obsidian
  base view references, not broken links. (2) Teliaz wikilinks are YAML single-quote
  escaping artifacts — targets verified to exist. (3) synthesis/Patient Commitment
  Lifecycle, assumption/WhatsApp and PDF Feature Communications, decision/OMG Handles
  Triage — all verified to exist via vault search. No action needed. ORPHAN001 — no
  inbound wikilinks; synthesis record with outbound relationships only, low linking
  priority.'
name: Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain Cycle
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[synthesis/Patient Commitment Lifecycle Gap Persisted Unresolved Across Seven
  Months]]'
relationships:
- confidence: 0.8
  context: Process and dependency failure patterns
  source: synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
    Cycle.md
  target: synthesis/Manual Single-Person Dependencies Create Cascading Failure Points
    Across Clinic Operations.md
  type: related-to
- confidence: 0.8
  context: Data gaps hinder rollout success
  source: synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
    Cycle.md
  target: synthesis/Operational Data Quality Gaps Block All KPI and Dashboard Implementation
    Attempts.md
  type: related-to
- confidence: 0.7
  context: Transition failures link rollouts and data
  source: synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
    Cycle.md
  target: synthesis/Payroll Data Fragmentation Undermines Operational Transition.md
  type: related-to
- confidence: 0.8
  context: Rollout failures are crisis-revealed gaps
  source: synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
    Cycle.md
  target: synthesis/Operational Gaps Discovered Through Crisis Events Rather Than
    Proactive Monitoring.md
  type: part-of
status: draft
supports:
- '[[assumption/WhatsApp and PDF Feature Communications Are Insufficient for Clinician
  Adoption]]'
type: synthesis
---

# Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain Cycle

## Insight

New clinical platform features at Telia'z Clinic Israel follow a predictable failure cycle: (1) feature is developed and deployed, (2) announcement sent via WhatsApp group and/or PDF guide, (3) psychiatrists do not adopt the feature and continue using legacy workflows, (4) management discovers non-adoption weeks or months later, (5) frontal training is proposed as the remedy, (6) training is deferred due to scheduling constraints, (7) next feature launches through the same ineffective channel. This cycle has been observed repeating across at least two separate feature rollouts (AI summary editing, commitment renewal workflows) over a 13-month period.

## Evidence

The pattern is documented across multiple independent operational meetings:

**Cycle Instance 1: AI Summary Editing Feature**
- [[note/Clinic Commitment Renewals and Feature Updates Discussion 2025-01-12]]: Rami observed psychiatrists still editing in Google Docs instead of using the new in-app summary feature
- [[note/Commitment Processes and Feature Updates Meeting 2025-08-01]]: Seven months later, the identical problem persists — psychiatrists expect Docs edits to propagate
- Response: Multiple decisions requiring frontal training created but training delivery repeatedly deferred

**Cycle Instance 2: Commitment Renewal Workflow**
- [[note/Commitment Renewal Workflow and Feature Rollout Meeting 2025-01-12]]: System requirements defined for renewal fields, alerts, and automation
- [[note/Clinic Commitment Renewal Process and Feature Training Discussion 2025-08-01]]: Same requirements restated seven months later, still unimplemented

**Policy Response (repeated but not breaking the cycle):**
- [[decision/Require Frontal Training Before Removing Legacy Feature Workflows]]
- [[decision/Require Frontal Training for Significant Feature Changes]]
- [[decision/Require Frontal Training Before Deprecating Old Clinical Features]]
- [[decision/Require Frontal Training for Major Feature Changes]]

Four separate decision records about requiring frontal training suggest the policy keeps being restated rather than consistently executed.

## Implications

1. **Feature deployment is not feature adoption** — the clinic conflates shipping code with changing clinician behavior
2. **WhatsApp as a change management channel is structurally inadequate** for a clinical workforce that defaults to established routines
3. **Frontal training policy exists but lacks operational enforcement** — no gate prevents feature launch without a training plan
4. **The cycle will repeat** unless the rollout process is redesigned to include mandatory synchronous training as a prerequisite for feature activation, not as a post-hoc remedy
5. **Resource allocation for training is the binding constraint** — the decisions are made but execution requires dedicated training time that competes with clinical hours

## Applicability

This pattern applies to any feature that changes how psychiatrists interact with the clinical platform. It is especially relevant for:
- The commitment renewal workflow (still pending implementation)
- Any future changes to the meeting screen UI
- New clinical protocol features (discharge alerts, KPI dashboards visible to clinicians)
- The planned internal task system replacing WhatsApp coordination

![[learn-synthesis.base#Sources]]
![[learn-synthesis.base#Related]]