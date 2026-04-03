---
alfred_tags:
- finance/mortgage-refinancing
- analysis/assumptions
- analysis/constraints
based_on:
- '[[note/Mortgage Refinancing Consultation Summary 2026-01-26]]'
- '[[note/RiseUp Mortgage Refinancing Consultation 2026-01-26]]'
confidence: high
created: '2026-02-26'
janitor_note: LINK001 — Base view embeds (learn-assumption.base#Depends On This, learn-assumption.base#Related)
  reference _bases/learn-assumption.base which does not exist. Embeds preserved. ORPHAN001
  — No inbound wikilinks from other records.
name: CPI-Indexed Track Causes Negative Amortization
project:
- '[[project/Rami Mortgage Refinancing]]'
relationships:
- confidence: 0.7
  context: Loan dynamics and affordability
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Family Can Sustain Current 4600 NIS Monthly Payment.md
  type: related-to
- confidence: 0.75
  context: Principal vs payment change causes
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Payment Increase Primarily Driven by Prime Rate Rises.md
  type: related-to
- confidence: 0.9
  context: Neg amort justifies refinance savings
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Refinancing Expected to Save Approximately 200000 NIS.md
  type: supports
- confidence: 0.9
  context: Neg amort explains primary savings from elim CPI
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism.md
  type: supports
- confidence: 0.95
  context: Refi eliminates cause of neg amort
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Refinancing Will Eliminate CPI-Indexed Track Exposure.md
  type: supports
- confidence: 0.7
  context: Both make current terms unfavorable
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Interest Rate Environment Will Not Revert to Make Current Terms
    Favorable.md
  type: related-to
- confidence: 0.8
  context: Neg amort avoided by holding refi to term
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Mortgage Will Be Held to Full Term for Projected Savings to Materialize.md
  type: related-to
- confidence: 0.7
  context: Same payment avoids future neg amort
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Restructured Monthly Payment Remains Approximately 4600 NIS.md
  type: related-to
- confidence: 0.9
  context: Neg amort inflates current balance
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: constraint/Early Repayment Balance of 705000 NIS Sets Refinancing Baseline.md
  type: related-to
- confidence: 0.85
  context: CPI track part of multi-track structure
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: constraint/Four-Track Mortgage Structure Requires Coordinated Restructuring.md
  type: part-of
- confidence: 0.8
  context: Justifies need for restructuring
  source: assumption/CPI-Indexed Track Causes Negative Amortization.md
  target: assumption/Bank Hapoalim Will Approve Mortgage Restructuring.md
  type: supports
source: Mortgage balance data reviewed during RiseUp consultation
source_date: '2026-01-26'
status: active
type: assumption
---

# CPI-Indexed Track Causes Negative Amortization

## Claim

The variable CPI-indexed mortgage track is experiencing negative amortization — the principal has grown from 260,000 NIS to 267,000 NIS despite 5.5 years of regular payments, because CPI indexation increases the principal faster than payments reduce it.

## Basis

Factual observation from the mortgage balance data. Both notes confirm the principal growth from 260K to 267K on this track. This is a structural feature of CPI-indexed loans during periods of inflation — the principal adjusts upward with the consumer price index.

## Evidence Trail

- 2026-01-26: Mortgage balance reviewed — CPI track principal grew 260K → 267K over 5.5 years
- This is consistent with Israeli CPI inflation since May 2020

## Impact

This is a key driver of Rami's dissatisfaction and the "freier" feeling. It validates the refinancing strategy of eliminating CPI-indexed exposure. Option A explicitly aims to restructure away from this track.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]