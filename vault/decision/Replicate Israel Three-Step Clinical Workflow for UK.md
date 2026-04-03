---
alfred_tags:
- clinic/scaling
- psychiatrist/management
- operations/structures
approved_by: []
based_on:
- '[[note/GP Confederation ADHD Partnership Meeting Notes 2025-01-22]]'
- '[[note/UK ADHD Platform Demo Rehearsal Notes 2025-02-11]]'
- '[[note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Adiel Levin]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 + ORPHAN001 — (1) Telia''z UK Expansion link is YAML escaping
  false positive (target likely exists). (2) Base view embeds (learn-decision.base#Based
  On, #Related) reference _bases/learn-decision.base which does not exist. Embeds
  preserved per policy. (3) No inbound wikilinks — new record, consider linking from
  project or assumption records.'
name: Replicate Israel Three-Step Clinical Workflow for UK
project:
- '[[project/Telia''z UK Expansion]]'
related: []
session: null
source: Multiple meetings, consistent across all UK partnership discussions
source_date: '2025-01-22'
status: final
supports:
- '[[assumption/International Clinics Can Replicate Israel District Model]]'
tags: []
type: decision
---

# Replicate Israel Three-Step Clinical Workflow for UK

## Context

Telia'z needed to define the clinical pathway for UK ADHD services. The Israel clinic had established a proven three-step workflow over 2+ years with 2,700+ patients and strong metrics (3.5-day average to psychiatrist, 81.3% NPS).

## Options Considered

1. **Replicate the Israel three-step workflow exactly** — digital questionnaire, case manager session, psychiatrist consultation, with AI throughout
2. **Design a UK-specific pathway** — adapted to NHS norms, potentially different staffing model or assessment sequence
3. **Hybrid approach** — keep core workflow but add UK-specific steps (e.g., GP triage layer)

## Decision

The core three-step workflow is replicated identically for the UK: (1) digital questionnaire (ASRS, DIVA), (2) case manager session (30-45 min intake with AI transcription), (3) psychiatrist consultation (30-60 min with AI-generated summary and agenda). When partnering with OMG, an additional pre-step (OMG triage) is added before the Telia'z workflow begins.

## Rationale

The Israel model has strong evidence: 2,700+ patients, 9,600+ sessions, 60% operational time savings for psychiatrists, and 81.3% NPS. Replicating a proven model reduces risk. The three-step workflow is the core IP and competitive advantage. Adapting it unnecessarily would lose the efficiency gains that make the NHS tariff pricing viable.

## Consequences

- UK product development focuses on localizing the existing workflow (report formats, questionnaire language, prescription integration) rather than redesigning it
- Case manager training in the UK follows the same protocol as Israel
- AI models and summary generation can leverage Israel training data
- Any UK-specific regulatory requirements (e.g., additional screening tools) are additive layers, not replacements

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]