---
alfred_tags:
- psychiatry/product-development
- feature-requirements
- patient-compliance
approved_by: []
based_on:
- '[[decision/Require Protocol Definition Before Feature Development]]'
- '[[decision/Active Patient Discharge Protocol Over Passive Churn]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Wikilinks to Teliaz projects use YAML double-apostrophe escaping
  — valid YAML, likely false positive. Base view embeds (learn-decision.base#Based
  On, #Related) are intentional Obsidian patterns — do not remove. ORPHAN001: No inbound
  links — review if this decision should be linked from a project.'
name: Formal Patient Discharge Requires Completed Psychiatry Intake Examination
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[task/Define Complex Patient Protocol Criteria]]'
- '[[decision/Adopt Structured Patient Discharge Targets for Capacity Management]]'
relationships:
- confidence: 0.7
  context: Both involve complex patient care features
  source: decision/Formal Patient Discharge Requires Completed Psychiatry Intake Examination.md
  target: decision/Require Literature Review Before Complex Patient Feature Development.md
  type: related-to
- confidence: 0.65
  context: Discharge as feature needing dev protocols
  source: decision/Formal Patient Discharge Requires Completed Psychiatry Intake Examination.md
  target: decision/Require Protocol Definition Before Feature Development.md
  type: related-to
session: null
source: Protocol framework discussion during product development meeting
source_date: '2026-02-12'
status: draft
supports:
- '[[decision/Implement Active Patient Discharge Protocol]]'
- '[[decision/Target Patient Discharge Rates of 10-30-30-30 Percent]]'
tags: []
type: decision
---

# Formal Patient Discharge Requires Completed Psychiatry Intake Examination

## Context

During the 2026-02-12 product development meeting, Basel requested a feature to alert psychiatrists about complex patients. Rami responded by outlining a protocol-first approach that defines a multi-stage clinical checkpoint flow. A key governance question emerged: at which stage can the clinic formally discharge a patient deemed unsuitable?

## Options Considered

1. **Discharge at any stage** — Allow questionnaire or case manager stages to formally discharge unsuitable patients early
2. **Discharge only after psychiatry intake** — Require a completed medical examination before any formal discharge action

## Decision

Formal patient discharge can only occur after the psychiatry intake stage (medical examination). Earlier stages — questionnaire screening and case manager assessment — can flag patients as potentially unsuitable and recommend escalation, but they cannot formally discharge. Only after a licensed psychiatrist has conducted an intake examination does the clinic have the clinical and likely legal authority to discharge.

## Rationale

This is both a clinical governance and a legal protection decision. Discharging a psychiatric patient without a medical examination could expose the clinic to liability. The multi-stage flow (questionnaire → case manager → psychiatrist) creates escalation points where concerns are raised, but the discharge authority rests exclusively with the psychiatrist who has conducted a formal examination.

## Consequences

- The discharge protocol must route all "unsuitable" patients through psychiatry intake before discharge, even if earlier stages identify clear unsuitability
- This increases psychiatrist workload for patients who will ultimately be discharged
- Case managers need clear guidance on how to flag without discharging
- System features (alerts, flags) must distinguish between "flagged for review" and "approved for discharge"

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]