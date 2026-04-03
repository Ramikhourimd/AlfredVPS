---
authority: Retool platform architecture
created: '2026-03-11'
janitor_note: 'LINK001: learn-constraint.base embeds reference missing _bases/ infrastructure
  — vault-wide gap, not per-file issue. Telia''z project link is valid. ORPHAN001:
  Record has related links to tasks/decisions — not truly orphaned.'
location: []
name: Retool Platform Performance Limits UI Component Complexity
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[task/Build Case Manager Tab-Based Questionnaire Screen in Retool]]'
- '[[decision/Tab-Based Navigation for Case Manager Questionnaire Screen]]'
source: Retool platform technical limitations
source_date: '2025-01-16'
status: active
tags: []
type: constraint
---

# Retool Platform Performance Limits UI Component Complexity

## Constraint

The Retool platform has performance and flow limitations that constrain how complex UI screens can be. The case manager questionnaire screen (13+ topic tabs with dynamic question slots) must be designed within these limits, requiring coordination with Lidar Ben-Dor on what is technically feasible.

## Source

Identified during the innovation sprint meeting on 2025-01-16 when Li Yamin was tasked with building the tab-based case manager screen. The task explicitly requires coordination with Lidar on "Retool performance and flow constraints" — indicating known platform limitations that affect screen design.

## Implications

- Screen designs must be validated against Retool's rendering and state management capabilities before implementation
- Complex features (dynamic question slots, bookmark/flag features, team notes panels) may need to be simplified or phased
- The tab-based navigation pattern was chosen partly because it avoids rendering all 13+ topics simultaneously
- This constraint becomes moot once the platform is rebuilt from scratch (per Shachar's rebuild decision), but affects all current Retool development

## Expiry / Review

This constraint expires when the Retool platform is fully replaced by Shachar's rebuilt system. Until then, all UI feature requests for the existing platform must account for these performance limits.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]
