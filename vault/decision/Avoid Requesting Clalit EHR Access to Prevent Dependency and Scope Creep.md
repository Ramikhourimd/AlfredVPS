---
approved_by: []
based_on:
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
challenged_by: []
confidence: high
created: '2026-03-08'
decided_by: '[[person/Rami Khouri]]'
janitor_note: 'FM001 FIXED — frontmatter fields restored from body (type, created,
  name, status, confidence, source, source_date, decided_by, based_on, project, related,
  approved_by, challenged_by, supports, tags). BODY ISSUE: raw YAML lines remain at
  top of body — manual cleanup needed to remove duplicate field text. LINK001 — Telia''z
  wikilinks are valid (YAML escaping false positive). Base view embeds reference _bases/learn-decision.base
  which does not exist — systemic vault gap, embeds preserved. ORPHAN001 — no inbound
  wikilinks; consider linking from project/Telia''z Clinic Israel.'
name: Avoid Requesting Clalit EHR Access to Prevent Dependency and Scope Creep
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[constraint/Clalit Pharmacies Do Not Accept External Prescriptions]]'
- '[[decision/Clickx Retained for Diagnoses Medications and Referrals]]'
source: Rami Khouri and colleague during Clalit partnership preparation
source_date: '2025-11-09'
status: final
supports: []
tags: []
type: decision
---

approved_by: []
based_on:
- '[[note/Clalit Partnership Operational Planning 2025-11-09]]'
challenged_by: []
confidence: high
created: '2026-03-08'
decided_by:
- '[[person/Rami Khouri]]'
name: Avoid Requesting Clalit EHR Access to Prevent Dependency and Scope Creep
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[constraint/Clalit Form 17 Requires Manual Approval by District Contact]]'
- '[[constraint/Clalit Pharmacies Do Not Accept External Prescriptions]]'
- '[[decision/Clickx Retained for Diagnoses Medications and Referrals]]'
session: null
source: Rami Khouri and colleague during Clalit partnership preparation
source_date: '2025-11-09'
status: final
supports: []
tags: []
type: decision
# Avoid Requesting Clalit EHR Access to Prevent Dependency and Scope Creep
## Context
During the 2025-11-09 Clalit partnership preparation meeting, the team debated whether to request access to Clalit's internal EHR system (Clicks) to facilitate prescription entry. While Clicks access would solve the pharmacy prescription workflow problem (Clalit pharmacies do not accept external prescriptions), the team identified significant strategic risks.
## Options Considered
1. **Option A** — Request Clicks access for prescription entry only, accepting the operational convenience
2. **Option B** — Avoid requesting Clicks access entirely, route prescriptions through family doctors (GPs) instead
## Decision
Avoid requesting Clalit EHR (Clicks) access. Route psychiatric medication recommendations through Clalit family doctors who can issue prescriptions within the Clalit system.
## Rationale
The team identified that requesting any level of Clicks access would:
- Create dependency on Clalit's internal systems and their availability
- Invite scope creep from the Clalit district contact (Eli/Tzachi), who already demonstrates controlling behavior over Form 17 approvals and patient summary reviews
- Set a precedent where Clalit could demand additional system integration or reporting requirements
- Undermine the clinic's operational independence from HMO infrastructure
The colleague specifically warned that requesting access "would invite scope creep from the Clalit contact." The team chose to accept the indirect prescription pathway (via GPs) rather than accept the strategic risk of system dependency.
## Consequences
- Each Clalit patient requiring medication generates an additional GP visit, with budget implications for the Clalit district
- The prescription workflow is slower and less direct than the Maccabi Haidok system
- The clinic maintains operational independence from Clalit's internal infrastructure
- Reduces leverage that the Clalit contact can exercise over the partnership
![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]
