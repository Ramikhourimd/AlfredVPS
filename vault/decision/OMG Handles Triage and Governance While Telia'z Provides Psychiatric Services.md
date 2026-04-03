---
alfred_tags:
- uk/clinic-launch
- cqc/partnerships
- revenue-sharing
approved_by: []
based_on:
- '[[note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Adiel Levin]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: All Telia''z wikilinks (project, task, assumption) are YAML
  escaping false positives (files exist). learn-decision.base embeds (#Based On, #Related)
  reference missing _bases/learn-decision.base — vault-wide gap. Note: base embeds
  appear duplicated at end of file. ORPHAN001: no inbound links — consider linking
  from UK expansion project.'
name: OMG Handles Triage and Governance While Telia'z Provides Psychiatric Services
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[task/Define Data Requirements for OMG-to-Telia''z Patient Handoff]]'
- '[[assumption/OMG CQC Registration Covers Joint Service Delivery With Telia''z]]'
relationships:
- confidence: 0.8
  context: Shared UK clinic ops strategy
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Operate UK Clinic Under Leon CQC License as Launch Strategy.md
  type: related-to
- confidence: 0.8
  context: Shared UK clinic ops strategy
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Operate UK Clinic Under Leon CQC Registration.md
  type: related-to
- confidence: 0.6
  context: Alternative CQC ops approaches
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Operate Under GP Confed CQC Rather Than Obtaining Own Registration.md
  type: related-to
- confidence: 0.85
  context: Defines service provider roles
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Position as Service Provider First Then Layer Technology.md
  type: supports
- confidence: 0.7
  context: UK launch regulatory strategy
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Pursue Dual-Track CQC Strategy for UK Launch.md
  type: related-to
- confidence: 0.7
  context: UK market entry ops alignment
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Pursue Dual-Track UK Market Entry Strategy.md
  type: related-to
- confidence: 0.8
  context: Leon-integrated UK patient flow
  source: decision/OMG Handles Triage and Governance While Telia'z Provides Psychiatric
    Services.md
  target: decision/Route UK Patients Through Leon Practice Website.md
  type: related-to
session: null
source: Adiel Levin / Rami Khouri — pathway design meeting
source_date: '2025-07-03'
status: draft
supports:
- '[[assumption/OMG Will Handle Initial Patient Triage for NHS ADHD Pathway]]'
tags: []
type: decision
---

# OMG Handles Triage and Governance While Telia'z Provides Psychiatric Services

## Context

The UK NHS ADHD service requires multiple organizational capabilities: regulatory compliance (CQC), clinical governance, patient triage, physical clinic infrastructure, and psychiatric expertise. Neither OMG nor Telia'z covers all capabilities alone.

## Options Considered

1. **Telia'z handles everything** — Requires own CQC, own governance framework, own facilities. Slow and expensive.
2. **OMG handles everything, Telia'z as technology vendor** — Reduces Telia'z to a software provider, losing clinical control and margin.
3. **Division of labor: OMG handles regulatory/triage/governance, Telia'z handles psychiatric assessment/technology** — Each partner contributes core strength.

## Decision

Clear division: OMG handles CQC registration, clinical governance, safeguarding, physical infrastructure, and initial patient triage (inclusion/exclusion screening). Telia'z provides the psychiatric clinical expertise, AI platform, clinical workflow, and assessment delivery.

## Rationale

OMG already has CQC, physical clinics, and 100,000+ GP patients. Telia'z has the psychiatric workflow, AI platform, and Israel-proven clinical model. The division plays to each organization's strengths. OMG's triage screens patients before they enter the more expensive psychiatric assessment phase, improving efficiency.

## Consequences

Critical dependency on data handoff between OMG triage and Telia'z assessment — format, timing, and content must be defined. Telia'z loses direct control over patient intake quality. OMG's triage decisions directly affect Telia'z patient volume and case mix.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]