---
alfred_tags:
- ai/clinical-pipeline
- multi-agent/architecture
- llm/fusion
approved_by:
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
based_on:
- '[[assumption/Case Manager DSM-Oriented Questioning Makes Transcripts Stronger Diagnostic
  Source]]'
- '[[assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured Format]]'
- '[[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]'
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
- '[[decision/Keep Symptom Attribution General Not Disorder-Specific]]'
- '[[constraint/Questionnaire Instrument Structurally Limited to PHQ Depression Anxiety
  and PCL-5 PTSD Domains]]'
challenged_by: []
confidence: high
created: '2026-02-27'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — All wikilinks verified as valid: assumption and constraint
  targets exist (scanner resolution issue with long filenames), Telia''z project link
  is YAML escaping false positive. Base view embeds (learn-decision.base) reference
  _bases/learn-decision.base which does not exist — vault-wide infrastructure gap,
  embeds preserved.'
name: Five-Stage Sequential Agent Architecture for Diagnostic Prediction
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
- '[[synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages]]'
- '[[task/Create Methodology Figures for Record Analysis Stage]]'
session: '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
source: Rami Khouri — presented as core methodology across all meeting records
source_date: '2026-02-22'
status: final
supports:
- '[[decision/First Paper Covers Methodology Plus Basic Clinical Results]]'
- '[[decision/Defer Fusion and Bias Agent Coverage to Paper 2]]'
- '[[decision/Limit Paper 1 Methodology to Three Figures]]'
tags: []
type: decision
---

# Five-Stage Sequential Agent Architecture for Diagnostic Prediction

## Context

The AI diagnostic pipeline needed an architecture that could evaluate each data source independently, combine them, and then apply clinical reasoning. The team needed to determine how many prediction stages to use and how they relate to each other.

## Options Considered

1. **Single combined model** — Feed all data sources into one model simultaneously. Rejected because it provides no visibility into per-source diagnostic value.
2. **Per-source prediction only** — Run S1, S2, S3 independently without fusion. Rejected because it wastes the opportunity to combine complementary signals.
3. **Per-source prediction + fusion + expert reasoning** — Five-stage sequential architecture with increasing context at each level. Selected.

## Decision

Use a five-stage sequential agent architecture:

| Stage | Agent | Input | Purpose |
|-------|-------|-------|---------|
| 1 | S1 (Questionnaire-only) | Questionnaire symptoms | Baseline from structured self-report |
| 2 | S2 (Transcript-only) | Case manager transcript | Richer signal from clinical interaction |
| 3 | S3 (Notes-only) | Case manager notes | Additional clinical observations |
| 4 | Fusion | All three source outputs | LLM-based integration of complementary signals |
| 5 | Expert Agent | Fusion output + DSM persona | Clinical reasoning with psychiatrist persona prompting |

A sixth variant — the Biased Agent (Expert + contextual priming) — exists for Paper 2's bias analysis but is not part of the core architecture.

## Rationale

The sequential architecture serves dual purposes: (1) it enables per-source accuracy measurement, revealing which data sources carry the most diagnostic signal, and (2) each subsequent stage adds context, allowing the paper to demonstrate incremental improvement from data integration and expert reasoning. The architecture also naturally maps to the paper's methodology figures.

## Consequences

- Paper 1 covers stages 1-3 (per-source prediction). Paper 2 covers stages 4-5 (fusion, expert, bias).
- Three methodology figures are needed: extraction, per-source prediction, and (for Paper 2) fusion/expert.
- The architecture creates a natural data hierarchy that validates the assumption that richer clinical data produces better diagnoses.
- Each stage's performance can be independently measured and compared.

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]