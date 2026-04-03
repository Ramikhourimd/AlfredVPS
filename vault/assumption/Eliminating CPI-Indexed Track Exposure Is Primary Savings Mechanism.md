---
alfred_tags:
- finance/mortgage-refinancing
- analysis/assumptions
- analysis/constraints
based_on:
- '[[note/RiseUp Mortgage Refinancing Consultation 2026-01-26]]'
- '[[note/Mortgage Refinancing Consultation Summary 2026-01-26]]'
confidence: medium
created: '2026-02-27'
janitor_note: 'LINK001: Base view embeds (learn-assumption.base#Depends On This, learn-assumption.base#Related)
  reference _bases/learn-assumption.base which may not exist yet — create base file
  to enable dynamic views. ORPHAN001: No inbound wikilinks — consider linking from
  project/Rami Mortgage Refinancing.'
name: Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism
project:
- '[[project/Rami Mortgage Refinancing]]'
related:
- '[[assumption/CPI-Indexed Track Causes Negative Amortization]]'
- '[[assumption/Refinancing Expected to Save Approximately 200000 NIS]]'
relationships:
- confidence: 0.95
  context: Primary mech behind expected savings
  source: assumption/Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism.md
  target: assumption/Refinancing Expected to Save Approximately 200000 NIS.md
  type: supports
- confidence: 0.95
  context: Assumes refi eliminates CPI exposure
  source: assumption/Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism.md
  target: assumption/Refinancing Will Eliminate CPI-Indexed Track Exposure.md
  type: depends-on
- confidence: 0.9
  context: Requires approved restructuring
  source: assumption/Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism.md
  target: assumption/Bank Hapoalim Will Approve Mortgage Restructuring.md
  type: depends-on
source: RiseUp consultation 2026-01-26
source_date: '2026-01-26'
status: active
type: assumption
---

# Eliminating CPI-Indexed Track Exposure Is Primary Savings Mechanism

## Claim

The approximately 200,000 NIS total savings projected under Option A are primarily achieved by restructuring the mortgage to eliminate the variable CPI-indexed track, which is currently experiencing negative amortization (principal grew from 260,000 to 267,000 NIS despite 5.5 years of payments).

## Basis

During the RiseUp consultation on 2026-01-26, Option A was described as restructuring tracks to "eliminate inefficient CPI-indexed exposure." This implies the CPI-indexed track is the primary source of excess cost, and removing it is the main lever for achieving the projected savings.

## Evidence Trail

- 2026-01-26: RiseUp consultation explicitly links Option A savings to CPI-indexed track elimination

## Impact

If Bank Hapoalim refuses to allow elimination of the CPI-indexed track during restructuring, the projected 200,000 NIS savings may not be achievable. This assumption should be validated early in the formal refinancing process with the bank.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]