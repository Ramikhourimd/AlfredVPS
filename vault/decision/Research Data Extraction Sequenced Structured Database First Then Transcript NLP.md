---
alternatives:
- NLP-first approach starting with transcript analysis
- Parallel extraction of structured and unstructured data simultaneously
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-03-03'
date_made: '2025-11-09'
decided_by:
- '[[person/Rami Khouri]]'
impact: paper
janitor_note: 'LINK001 — Base view embeds (learn-decision.base#Based On, #Related)
  reference non-existent _bases/learn-decision.base — vault-wide infrastructure issue,
  embeds preserved. ORPHAN001 — no inbound wikilinks, consider linking from a research
  project or methodology decision record.'
name: Research Data Extraction Sequenced Structured Database First Then Transcript
  NLP
project: []
rationale: Structured database fields (demographics, diagnosis codes, treatment dates)
  are immediately available and validated, while NLP-based transcript extraction requires
  additional tooling and validation. Starting with structured data establishes ground
  truth for later NLP cross-validation.
related:
- '[[conversation/Research Paper Scope and Methodology Planning Meeting 2025-11-09]]'
session: null
source: ''
source_date: null
status: final
supports: []
tags:
- research
- methodology
- data-extraction
- paper
type: decision
---

The research team decided to sequence data extraction for the paper by starting with structured database fields before attempting NLP-based transcript analysis.

## Context

During the November 9 research planning meeting, the team discussed how to approach data extraction for the 4-5 figure paper. Two data sources were available: structured clinical database fields (demographics, ICD codes, medication records, appointment dates) and unstructured session transcripts.

## Decision

Extract structured database fields first (demographics, diagnosis, treatment timing, medication), then layer NLP-based transcript analysis on top. The structured data provides a validated foundation that NLP results can be cross-referenced against.

## Rationale

- Structured fields are immediately available without additional tooling
- Database fields have known validation rules and completeness metrics
- Per-symptom scoring methodology depends on reliable baseline data
- NLP extraction introduces uncertainty that is easier to calibrate against known structured data
- The paper scope (4-5 figures) can potentially be achieved with structured data alone if NLP proves too complex

## Implications

- Paper timeline front-loads the achievable work
- NLP becomes an enhancement layer rather than a critical dependency
- Reduces risk of paper stalling on NLP tooling issues

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
