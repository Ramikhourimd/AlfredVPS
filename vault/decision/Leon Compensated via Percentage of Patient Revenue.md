---
alfred_tags:
- uk/clinic-launch
- cqc/partnerships
- revenue-sharing
approved_by: []
based_on:
- '[[note/Telia''z Team Meeting UK Launch and Operations Review 2026-02-15]]'
challenged_by: []
confidence: medium
created: '2026-02-27'
decided_by:
- '[[person/Adiel Levin]]'
janitor_note: LINK001 — Telia'z wikilinks and note/conversation links are valid (YAML
  escaping false positives). Base view embeds (learn-decision.base#Based On, learn-decision.base#Related)
  reference _bases/learn-decision.base which does not exist — vault-wide infrastructure
  gap. Duplicate base view embeds at end of file need manual cleanup. ORPHAN001 —
  no inbound wikilinks; decision record should be linked from project or meeting records.
name: Leon Compensated via Percentage of Patient Revenue
project:
- '[[project/Telia''z UK Expansion]]'
related:
- '[[decision/Route UK Patients Through Leon Practice Website]]'
- '[[constraint/Leon Contract Signing Is Critical Path for All UK Launch Activities]]'
relationships:
- confidence: 0.98
  context: Both describe Leon revenue share model
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Leon Partnership Structured as Percentage Revenue Share.md
  type: related-to
- confidence: 0.98
  context: Both describe Leon revenue share model
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Leon Partnership Uses Percentage Revenue Share Model.md
  type: related-to
- confidence: 0.85
  context: Partnership enables Leon CQC usage
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Operate UK Clinic Under Leon CQC License as Launch Strategy.md
  type: supports
- confidence: 0.85
  context: Partnership enables Leon CQC usage
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Operate UK Clinic Under Leon CQC Registration.md
  type: supports
- confidence: 0.7
  context: Fits service provider model
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Position as Service Provider First Then Layer Technology.md
  type: related-to
- confidence: 0.75
  context: Leon partnership as CQC track
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Pursue Dual-Track CQC Strategy for UK Launch.md
  type: related-to
- confidence: 0.75
  context: Leon partnership as entry track
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Pursue Dual-Track UK Market Entry Strategy.md
  type: related-to
- confidence: 0.85
  context: Partnership enables patient routing
  source: decision/Leon Compensated via Percentage of Patient Revenue.md
  target: decision/Route UK Patients Through Leon Practice Website.md
  type: supports
session: ''
source: Adiel Levin, team meeting 2026-02-15
source_date: '2026-02-15'
status: draft
supports:
- '[[decision/Operate UK Clinic Under Leon CQC License as Launch Strategy]]'
tags:
- uk-launch
- leon-partnership
- commercial
type: decision
---

# Leon Compensated via Percentage of Patient Revenue

## Context

The partnership with Leon (UK family doctor with CQC registration) required a commercial arrangement. Telia'z operates under Leon's CQC license and routes patients through his practice website. Leon provides the regulatory umbrella; Telia'z provides the clinical service and technology.

## Options Considered

1. **Fixed fee per month** — Predictable cost but misaligned with patient volume
2. **Percentage of patient revenue** — Variable, scales with volume, aligns incentives
3. **One-time licensing fee** — Simple but doesn't reflect ongoing regulatory hosting

## Decision

Leon is compensated via a percentage arrangement — patients flowing through his practice generate revenue of which Leon receives an agreed percentage. The exact percentage is in the contract pending signature.

## Rationale

A percentage model aligns Leon's incentives with patient throughput. It minimizes Telia'z's fixed costs during the uncertain early phase when patient volume is unproven. It also gives Leon ongoing motivation to support the partnership since his income scales with success.

## Consequences

- Commercial viability depends on patient volume reaching sufficient scale
- Leon's percentage must be factored into unit economics alongside NHS tariff pricing constraints
- The percentage arrangement must be compatible with CQC regulations around clinical independence
- Contract terms define the financial relationship and are therefore critical path

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]