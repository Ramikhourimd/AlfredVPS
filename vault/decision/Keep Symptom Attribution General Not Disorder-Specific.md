---
approved_by: []
based_on:
- '[[note/AI Diagnostic Paper Methodology and Results Review 2026-02-22]]'
challenged_by: []
confidence: high
created: '2026-02-26'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: LINK001 — Telia'z AI Diagnostic Research Paper wikilink is valid (YAML
  escaping false positive). Base view embeds (learn-decision.base#Based On, learn-decision.base#Related)
  reference non-existent _bases/learn-decision.base — vault-wide infrastructure gap.
  Body has duplicate base embed block after --- at end — remove the duplicate manually.
  ORPHAN001 — no inbound wikilinks from other records. Swept 2026-02-27.
name: Keep Symptom Attribution General Not Disorder-Specific
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[decision/Use Three Granularity Levels for Diagnostic Match Scoring]]'
session: ''
source: Rami Khouri — pipeline design choice
source_date: '2026-02-22'
status: final
supports:
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
tags:
- methodology
- symptom-extraction
- expert-agent
type: decision
---

# Keep Symptom Attribution General Not Disorder-Specific

## Context

When the Expert Agent processes symptoms for diagnostic reasoning, individual symptoms (e.g., insomnia, fatigue, concentration difficulties) can appear across multiple DSM disorders. A design choice was needed: should the pipeline attribute each symptom to a specific disorder during extraction, or keep symptoms general and let the diagnostic reasoning stage determine attribution?

## Options Considered

1. **Disorder-specific attribution** — Tag each extracted symptom with the most likely associated disorder during extraction (e.g., "insomnia → PTSD" or "insomnia → MDD")
2. **General attribution with contextual grouping** — Keep symptoms unattributed to specific disorders and group them contextually, letting the diagnostic reasoning stage determine which disorder they support

## Decision

Option 2: Symptoms like insomnia are kept general (not attributed to a specific disorder) and grouped with related symptoms contextually. The Expert Agent then applies DSM reasoning across the full symptom profile to make diagnostic determinations.

## Rationale

Many symptoms are transdiagnostic — insomnia, for example, appears in criteria for PTSD, MDD, GAD, and several other disorders. Premature attribution would force an early commitment that could bias downstream reasoning. By keeping symptoms general, the Expert Agent can consider the full clinical picture before making attributions, mirroring how clinicians actually reason.

## Consequences

- The Expert Agent must handle symptom-to-disorder mapping as part of its reasoning, increasing its cognitive load.
- Match scoring at different granularity levels (specific, group, block) remains valid because attribution happens at diagnosis time, not extraction time.
- This approach is more robust to comorbid presentations where the same symptom supports multiple diagnoses.

![[learn-decision.base#Based On]]
![[learn-decision.base#Related]]

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
