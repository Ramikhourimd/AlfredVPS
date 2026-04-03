---
approved_by: []
based_on:
- '[[note/Research Paper Scope and Data Extraction Plan 2025-11-09]]'
challenged_by: []
confidence: high
created: '2026-03-03'
decided_by:
- '[[person/Dekkel Taliaz]]'
- '[[person/Noam]]'
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference missing _bases/learn-decision.base
  — preserve embeds, base file needs creation.'
name: Limit Statistical Analyses to Avoid Bonferroni Correction Penalties
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related: []
session: null
source: Research team consensus at paper scope meeting
source_date: '2025-11-09'
status: final
supports:
- '[[decision/Focus First Paper on System Presentation and PTSD Outcomes]]'
tags: []
type: decision
---

# Limit Statistical Analyses to Avoid Bonferroni Correction Penalties

## Context

The research paper has multiple data dimensions (demographics, timing, diagnostic prediction, outcomes) and numerous potential statistical comparisons. Running many tests increases false positive risk and triggers Bonferroni correction requirements, which raise significance thresholds and weaken borderline findings.

## Options Considered

1. **Comprehensive analyses across all variables** — Maximizes findings but requires Bonferroni correction, potentially losing significance on marginal results
2. **Focused, limited analyses** — Fewer tests, lower correction burden, stronger individual findings

## Decision

Keep statistical analyses focused to avoid Bonferroni correction penalties. The team will constrain the number of hypotheses tested rather than running exhaustive comparisons.

## Rationale

By limiting the number of analyses, the team avoids multiple comparison corrections that could weaken otherwise significant findings. This is pragmatic for a methodology-heavy paper that already has limited space for results. The methods section already constitutes roughly half the paper, leaving little room for extensive result tables.

## Consequences

- Some potentially interesting correlations will go unexplored in Paper 1
- Deferred analyses can be investigated in Paper 2 or follow-up studies
- Trade-off: stronger statistical rigor on fewer, more focused findings
- Aligns with the decision to keep Paper 1 tightly scoped to methodology + PTSD clinical results

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
