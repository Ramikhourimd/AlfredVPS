---
alfred_tags:
- psychiatry/product-development
- feature-requirements
- patient-compliance
approved_by: []
based_on:
- '[[task/Define Complex Patient Protocol Criteria]]'
- '[[conversation/Product Development Update Meeting 2026-02-12]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001: Telia''z wikilinks are valid (YAML escaping false positive
  — targets confirmed to exist). Base view embeds (learn-decision.base#Based On, #Related)
  reference _bases/learn-decision.base which does not exist yet — preserve per policy;
  create base file to enable dynamic views. ORPHAN001: No inbound wikilinks; consider
  linking from project/Telia''z Clinic Israel or project/Telia''z AI Clinical Platform.'
name: Require Protocol Definition Before Feature Development
project:
- '[[project/Telia''z Clinic Israel]]'
- '[[project/Telia''z AI Clinical Platform]]'
related: []
session: ''
source: Rami Khouri
source_date: '2026-02-12'
status: final
supports:
- '[[decision/Two-Domain Protocol Framework for Clinic Scaling]]'
tags: []
type: decision
---

# Require Protocol Definition Before Feature Development

## Context

During the 2026-02-12 product development meeting, Basel Kanaaneh requested a feature to alert psychiatrists about complex patients. Rather than jumping to implementation, Rami outlined a protocol-first approach: clinical criteria must be formally defined before any product features are built around them.

## Options Considered

1. **Feature-first** — Build the alert system based on Basel's description, iterate on criteria later. Rejected because undefined criteria would produce unreliable alerts.
2. **Protocol-first** — Conduct literature review and internal data analysis to define complex patient criteria, then design features to support the protocol. Adopted.

## Decision

All clinical features that involve patient classification, escalation, or discharge must be preceded by a formal protocol definition. For the complex patient workflow specifically:
1. Define what constitutes a "complex" or "unsuitable" patient via literature review and internal data
2. Map the multi-stage clinical checkpoint flow (questionnaire, case manager, psychiatry) with consent mechanisms
3. Only then build product features to support the defined protocol

Key constraint: formal patient discharge can only occur after a completed psychiatry intake (medical examination). Earlier stages can flag and recommend, but cannot discharge.

## Rationale

Clinical features without underlying clinical protocols produce inconsistent behavior and potential patient safety issues. The protocol defines the rules; the feature automates them. This also aligns with the two-domain protocol framework already adopted for clinic scaling.

## Consequences

- Slower initial feature delivery but higher clinical validity
- Requires clinician time for protocol design (literature review, data analysis)
- Creates reusable framework for future clinical feature requests
- Establishes that product development follows clinical governance, not the reverse

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]