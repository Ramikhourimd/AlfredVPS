---
alfred_tags:
- psychiatry/product-development
- feature-requirements
- patient-compliance
approved_by: []
based_on:
- '[[task/Define Complex Patient Protocol Criteria]]'
challenged_by: []
confidence: high
created: '2026-02-12'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  synthesis/Protocol Development Fragmented Across Individuals Without Systematic
  Inventory or Lifecycle may not exist — verify target name. Base view embeds (learn-decision.base#Based
  On, #Related) reference missing _bases/learn-decision.base — vault-wide gap. Note:
  base embeds appear duplicated at end of file body. ORPHAN001 — no inbound links;
  consider linking from a project or conversation.'
name: Require Literature Review Before Complex Patient Feature Development
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
- '[[synthesis/Protocol Development Fragmented Across Individuals Without Systematic
  Inventory or Lifecycle]]'
relationships:
- confidence: 0.95
  context: Parallel pre-feature dev requirements
  source: decision/Require Literature Review Before Complex Patient Feature Development.md
  target: decision/Require Protocol Definition Before Feature Development.md
  type: related-to
session: null
source: Rami Khouri during product development meeting
source_date: '2026-02-12'
status: draft
supports:
- '[[decision/Two-Domain Protocol Framework for Clinic Scaling]]'
- '[[decision/Formal Patient Discharge Requires Completed Psychiatry Intake Examination]]'
tags: []
type: decision
---

# Require Literature Review Before Complex Patient Feature Development

## Context

During the 2026-02-12 product development meeting, Basel requested a platform feature to alert psychiatrists about complex patients. Rather than immediately building the feature, Rami insisted on a protocol-first approach: define what "complex patient" means clinically through literature review and internal data analysis before any feature development begins.

## Options Considered

1. **Option A** — Build an alerting feature immediately based on informal clinical judgement of what makes a patient complex
2. **Option B** — Conduct a formal literature review, analyze internal patient data to define complexity criteria, design a multi-stage clinical checkpoint flow, then build features that implement the protocol

## Decision

Option B — protocol-first. The feature must be grounded in evidence-based criteria, not ad-hoc clinical impressions. The protocol spans three stages (questionnaire, case manager, psychiatry) with different escalation paths at each. A key design constraint: formal patient discharge can only happen after psychiatry intake (medical examination); earlier stages can flag and recommend but cannot discharge.

## Rationale

- "Complex patient" lacks a standardized definition — building a feature without defining the protocol creates arbitrary alerting
- Internal data can reveal natural dropout patterns (when patients leave, at which stage, why) that inform protocol design
- Multi-stage checkpoint flow ensures appropriate clinical authority at each decision point
- Aligns with the broader protocol-first philosophy: define the process, then build technology to support it

## Consequences

- Feature development is delayed until literature review and data analysis are complete
- A formal task was created to conduct the review (assigned to Rami)
- The resulting protocol will govern not just the alerting feature but the entire complex patient management pathway
- Establishes precedent: clinical features require evidence-based protocol definition before development

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]