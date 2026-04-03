---
cluster_sources:
- '[[note/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[conversation/Patient Data Research and AI Summary Quality Meeting 2025-11-11]]'
- '[[conversation/AI Diagnostic Paper Research Meeting 2026-02-22]]'
- '[[task/Investigate Dataset Size Discrepancy Between Excel Exports]]'
confidence: medium
created: '2026-03-31'
name: Research Data Pipeline Requires Multi-Stage Manual Translation Between Clinical
  and Analytical Domains
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[constraint/Key Demographic Variables Only Available Through NLP Extraction From
  Unstructured Text]]'
- '[[synthesis/Research Paper Delivery Bottlenecked by Sequential Single-Person Dependencies]]'
status: draft
supports:
- '[[constraint/All Data Exports Depend on Single Provider Shmulik]]'
- '[[constraint/Patient Clinical Records Stored as Individual Google Docs Files]]'
- '[[assumption/Automated AI Extraction Can Reliably Parse Unstructured Patient Google
  Docs]]'
type: synthesis
---

# Research Data Pipeline Requires Multi-Stage Manual Translation Between Clinical and Analytical Domains

## Insight

Despite operating a digital clinical infrastructure (Xano backend, BigQuery warehouse, Google Docs patient records), the research data pipeline requires at least four manual translation stages before clinical data becomes analytically usable. Each stage introduces a human intermediary with domain-specific knowledge, and each handoff creates potential for data loss, schema drift, or interpretation errors.

## Evidence

From the 2025-11-11 meeting: Rami directed Rivi to manually build Excel tables from patient Google Docs, reviewed questionnaire field meanings (not self-evident from raw data), and established a "ping-pong" iterative approach for data table construction — implying the task requires both clinical and technical expertise.

From the 2026-02-22 meetings: Noam compiled methodology from multiple separate documents Rami had sent piecemeal, revealing missing pipeline stages. Shmulik's data exports showed a 340-record discrepancy between two exports of the same date range (6,041 vs ~5,700), and Rami's AI analysis covered only ~3,000 of those records.

The translation chain: Shmulik (database export) → Rami (NLP extraction from unstructured Google Docs) → Rivi (clinical interpretation into structured tables) → Noam (statistical compilation and analysis).

## Implications

- Research reproducibility depends on documenting each translation step and its assumptions
- Dataset discrepancies (like the 340-record gap) may originate at any translation stage
- The pipeline cannot be fully automated because clinical domain knowledge is required at the interpretation stage
- Future research projects should consider building direct analytical views into the clinical infrastructure

## Applicability

Applies to the current AI diagnostic research paper and any future research using Telia'z clinical data. Also relevant to the operational efficiency of the clinic's data infrastructure.
