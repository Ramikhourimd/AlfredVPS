---
authority: Published clinical research benchmarks
created: '2026-02-26'
janitor_note: LINK001 — Teliaz wikilink (project/Teliaz AI Diagnostic Research Paper)
  is YAML-escape false positive (Teliaz = Telias single quote). Base view embeds (learn-constraint.base#Affected
  Projects, learn-constraint.base#Related) reference non-existent _bases/learn-constraint.base
  — embeds preserved per rules, base file needs to be created.
location: []
name: Clinical Paperwork Literature Benchmark of 10 Minutes
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[task/Obtain Approval Time Data by Session Type]]'
- '[[task/Request Segmented Timing Data From Shmulik]]'
- '[[assumption/Real-Time Summary Mode Reduces Approval to Near Zero]]'
source: Published clinical literature
source_date: '2026-02-22'
status: active
tags:
- benchmark
- timing-data
- literature
type: constraint
---

# Clinical Paperwork Literature Benchmark of 10 Minutes

## Constraint

The published clinical literature establishes approximately 10 minutes as the standard benchmark for clinical paperwork (documentation/summary completion) per patient session. The paper's timing data and real-time mode improvement claims must be contextualized against this external benchmark.

## Source

Referenced during the 2026-02-22 research meeting as the comparison point for the Telia'z system's summary approval times. The 8-column timing data segmentation was specifically designed to enable comparison against this benchmark.

## Implications

- Summary approval times significantly above 10 minutes would not demonstrate improvement over standard practice.
- The real-time summary mode is expected to reduce approval time to near-zero, which would represent a significant improvement over the 10-minute benchmark.
- Paper 1 must cite the specific literature source for this benchmark — the actual citation needs to be identified and included.
- The benchmark applies to the delta between session end and summary approval, not summary generation time.

## Expiry / Review

This benchmark should be re-validated against current literature before paper submission. Clinical documentation standards may have shifted with EHR adoption.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
