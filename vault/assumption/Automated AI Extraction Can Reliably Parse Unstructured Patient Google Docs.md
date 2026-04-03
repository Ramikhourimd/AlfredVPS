---
based_on:
- '[[note/Patient Data Research and AI Summary Quality Discussion 2025-11-11]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: LINK001 — Telia'z AI Diagnostic Research Paper wikilink is valid (YAML
  escaping false positive). constraint/Key Demographic Variables link VERIFIED VALID
  (target exists). ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  AI Diagnostic Research Paper.
name: Automated AI Extraction Can Reliably Parse Unstructured Patient Google Docs
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Build Initial Patient Data Excel Table With Column Headers]]'
- '[[task/Extract Structured Patient Data Tables From Database]]'
- '[[constraint/Key Demographic Variables Only Available Through NLP Extraction From
  Unstructured Text]]'
source: Rami Khouri, Patient Data Research Meeting 2025-11-11
source_date: '2025-11-11'
status: active
type: assumption
---

# Automated AI Extraction Can Reliably Parse Unstructured Patient Google Docs

## Claim

The research data preparation methodology assumes that AI/LLM-based extraction can reliably convert unstructured patient clinical records (stored as Google Docs containing questionnaires, transcripts, case manager notes, and summaries) into structured tabular data suitable for research analysis. Rami proposed a "ping-pong" approach where Rivi builds the Excel column structure and Rami fills the data using automated AI extraction.

## Basis

- Rami's experience building the multi-agent diagnostic pipeline, which already uses LLM extraction for transcript symptoms
- The successful switch from rule-based to LLM-based extraction for case manager transcripts during pipeline development
- The general capability of LLMs to extract structured information from semi-structured clinical text

## Evidence Trail

- 2025-11-11: Rami proposed the automated extraction approach during meeting with Rivi
- The diagnostic pipeline itself serves as partial validation — it extracts symptoms from transcripts successfully
- No formal validation of extraction accuracy for demographic/history fields has been documented

## Impact

- If this assumption holds, data preparation is fast and scalable across ~6000 patient records
- If it fails, manual extraction would be required — a significant time and resource constraint
- The accuracy of extracted demographic data directly affects the validity of the paper's demographic analysis section
- Related constraint: [[constraint/Key Demographic Variables Only Available Through NLP Extraction From Unstructured Text]] means there is no fallback to structured database fields for many variables
