---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-02-25'
decided_by:
- '[[person/Rami Khouri]]'
janitor_note: 'LINK001 — Telia''z wikilinks valid (YAML escaping false positive).
  Base view embeds (learn-decision.base#Based On, #Related) reference _bases/learn-decision.base
  which does not exist yet. ORPHAN001 — no inbound wikilinks; consider linking from
  project/Telia''z AI Diagnostic Research Paper.'
name: Use Three Granularity Levels for Diagnostic Match Scoring
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Document Percentage Calculation Method for Paper]]'
session: null
source: Rami Khouri — analysis methodology
source_date: '2026-02-22'
status: final
supports: []
tags: []
type: decision
---

# Use Three Granularity Levels for Diagnostic Match Scoring

## Context

The AI diagnostic pipeline predicts DSM diagnoses and compares them against psychiatrist diagnoses. A method was needed to measure how closely AI predictions match human diagnoses at different levels of specificity.

## Options Considered

1. **Single-level exact match** — Binary match on full ICD code. Too strict — misses clinically meaningful partial matches.
2. **Three-level granularity** — Score matches at Specific, Group, and Block levels to capture both exact and category-level agreement.

## Decision

Diagnostic match percentages are calculated at three granularity levels:
- **Specific** — Full ICD code with specifier (e.g., F43.10). Exact diagnostic match.
- **Group** — ICD code without specifier (e.g., F43). Same diagnostic family.
- **Block** — Diagnostic category (e.g., all trauma-related, all affective disorders). Same broad domain.

## Rationale

A single match level would miss clinically relevant agreement. A psychiatrist diagnosing F43.10 (PTSD) when the AI predicts F43.12 (PTSD with delayed expression) represents meaningful agreement at the Group level despite failing Specific match. Block-level captures whether the AI identified the correct diagnostic domain even if the specific disorder differs.

## Consequences

- Results tables must report all three match levels per agent
- Provides nuanced view of where AI prediction succeeds and fails
- The percentage calculation method must be documented in the paper's methods section (currently missing — flagged by Noam)

---
![[learn-decision.base#Based On]]

![[learn-decision.base#Related]]
