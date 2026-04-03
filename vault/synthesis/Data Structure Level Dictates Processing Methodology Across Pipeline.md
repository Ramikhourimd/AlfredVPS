---
alfred_tags:
- multi-agent/diagnostic-pipeline
- insights/patterns
cluster_sources:
- '[[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]'
- '[[assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured Format]]'
- '[[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001: project field contains Telia''z with apostrophe — YAML single-quote
  escaping produces false positive broken link. ORPHAN001: no inbound links — may
  need linking from pipeline architecture or AI research paper records.'
name: Data Structure Level Dictates Processing Methodology Across Pipeline
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline Stages]]'
relationships:
- confidence: 0.9
  context: Structure dictates LLM trend
  source: synthesis/Data Structure Level Dictates Processing Methodology Across Pipeline.md
  target: synthesis/LLM Approaches Progressively Replace Rule-Based Methods Across
    Pipeline Stages.md
  type: supports
- confidence: 0.85
  context: Structure-method in arch evolution
  source: synthesis/Data Structure Level Dictates Processing Methodology Across Pipeline.md
  target: synthesis/Pipeline Architecture Emerged Through Iterative Failure Correction.md
  type: part-of
- confidence: 0.75
  context: Structure-based methods boost clinical data perf
  source: synthesis/Data Structure Level Dictates Processing Methodology Across Pipeline.md
  target: synthesis/Clinical Interaction Data Outperforms Self-Report Across Pipeline
    Stages.md
  type: supports
status: draft
supports:
- '[[assumption/Expert Persona Prompting Improves LLM Diagnostic Accuracy]]'
type: synthesis
---

# Data Structure Level Dictates Processing Methodology Across Pipeline

## Insight

Across the multi-agent diagnostic pipeline, there is a consistent pattern: the less structured the data source, the more the processing methodology requires LLM-based reasoning rather than algorithmic/rule-based approaches. This applies at every pipeline stage — extraction, per-source prediction, and multi-source integration.

## Evidence

- **Structured data (questionnaire):** Algorithmic extraction works well. The questionnaire's clear, rule-based format makes LLM extraction unnecessary (see [[assumption/Questionnaire Extraction Is Purely Algorithmic Due to Structured Format]]).
- **Semi-structured data (transcripts):** Rule-based extraction was initially attempted but proved too strict and limited. Switching to LLM-based extraction dramatically improved symptom capture (see [[decision/Switch Transcript Extraction From Rule-Based to LLM-Based]]).
- **Integration layer (fusion):** Non-LLM fusion mechanically picked one source's diagnosis rather than truly synthesizing across sources. LLM-based fusion successfully reasoned across inputs to produce integrated diagnoses (see [[decision/Abandon Non-LLM Fusion for LLM-Based Diagnostic Fusion]]).
- **Expert reasoning layer:** Adding psychiatrist persona prompting to the LLM further improved diagnostic accuracy, demonstrating that higher-level clinical reasoning benefits from additional LLM framing.

## Implications

For clinical NLP pipelines, the decision between rule-based and LLM-based processing should be driven by the structure level of the input data. Structured instruments (questionnaires, rating scales) may not benefit from LLM processing, while unstructured clinical text (transcripts, notes, narratives) consistently requires it. Integration of multiple data sources also requires LLM reasoning, as mechanical combination fails to capture cross-source patterns.

## Applicability

- Any multi-source clinical diagnostic system
- Pipeline design that mixes structured and unstructured clinical data
- Cost-optimization: use simpler algorithms where data is structured, reserve LLM compute for unstructured sources