---
alfred_tags:
- finance/mortgage-refinancing
- analysis/assumptions
- analysis/constraints
authority: Bank Hapoalim mortgage terms
created: '2026-02-27'
janitor_note: 'LINK001 — Base view embeds (learn-constraint.base#Affected Projects,
  #Related) reference _bases/learn-constraint.base which does not exist. Create base
  file to enable dynamic views.'
location: []
name: Four-Track Mortgage Structure Requires Coordinated Restructuring
project:
- '[[project/Rami Mortgage Refinancing]]'
related:
- '[[note/Mortgage Refinancing Consultation Summary 2026-01-26]]'
- '[[note/RiseUp Mortgage Refinancing Consultation 2026-01-26]]'
- '[[assumption/CPI-Indexed Track Causes Negative Amortization]]'
relationships:
- confidence: 0.75
  context: Both involve mortgage restructuring/refinancing
  source: constraint/Four-Track Mortgage Structure Requires Coordinated Restructuring.md
  target: constraint/RiseUp Service Fee Required Before Refinancing Proceeds.md
  type: related-to
source: RiseUp consultation 2026-01-26
source_date: '2026-01-26'
status: active
tags: []
type: constraint
---

# Four-Track Mortgage Structure Requires Coordinated Restructuring

## Constraint

The current Bank Hapoalim mortgage comprises four distinct tracks, each with different risk profiles and rate mechanisms:
1. **Prime-linked track** — variable rate, responsive to Bank of Israel rate changes
2. **Fixed non-indexed track** — stable payments, no CPI or rate exposure
3. **Variable CPI-indexed track** — principal adjusts with CPI, currently experiencing negative amortization
4. **Short-term track** — 14-year duration, different amortization schedule

Any refinancing must address all four tracks simultaneously. The tracks cannot be restructured independently — the total package must be renegotiated as a coordinated whole, limiting the flexibility of restructuring options.

## Source

Bank Hapoalim mortgage structure established May 2020. Documented during RiseUp consultation on 2026-01-26.

## Implications

- Refinancing proposals must account for interactions between tracks (e.g., eliminating CPI-indexed track shifts risk to other track types)
- The four-track structure increases negotiation complexity with the bank
- RiseUp's advisory value is partly in navigating this multi-track complexity
- Option A specifically targets elimination of the inefficient CPI-indexed track while restructuring the remaining exposure

## Expiry / Review

Constraint expires upon successful refinancing completion. Review when refinancing terms are presented by the bank.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]