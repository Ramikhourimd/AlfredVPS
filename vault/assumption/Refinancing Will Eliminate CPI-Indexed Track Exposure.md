---
alfred_tags:
- finance/mortgage-refinancing
- analysis/assumptions
- analysis/constraints
based_on:
- '[[note/Mortgage Refinancing Consultation Summary 2026-01-26]]'
- '[[note/RiseUp Mortgage Refinancing Consultation 2026-01-26]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-02-27'
invalidated_by: []
janitor_note: 'LINK001 + ORPHAN001 — Base view embeds (learn-assumption.base#Depends
  On This, #Related) reference _bases/learn-assumption.base which does not exist.
  Embeds preserved per policy. No inbound wikilinks — consider linking from project/Rami
  Mortgage Refinancing.'
name: Refinancing Will Eliminate CPI-Indexed Track Exposure
project:
- '[[project/Rami Mortgage Refinancing]]'
related:
- '[[assumption/CPI-Indexed Track Causes Negative Amortization]]'
- '[[assumption/Refinancing Expected to Save Approximately 200000 NIS]]'
- '[[decision/Refinance for Total Cost Savings Over Monthly Reduction]]'
- '[[constraint/Four-Track Mortgage Structure Requires Coordinated Restructuring]]'
relationships:
- confidence: 0.95
  context: Refi effect needs approval
  source: assumption/Refinancing Will Eliminate CPI-Indexed Track Exposure.md
  target: assumption/Bank Hapoalim Will Approve Mortgage Restructuring.md
  type: depends-on
source: RiseUp consultation 2026-01-26
source_date: '2026-01-26'
status: active
tags: []
type: assumption
---

# Refinancing Will Eliminate CPI-Indexed Track Exposure

## Claim

Option A refinancing will restructure the mortgage to eliminate the variable CPI-indexed track, thereby stopping the negative amortization that has caused the principal on that track to grow from 260,000 NIS to 267,000 NIS despite 5.5 years of payments.

## Basis

Both consultation notes explicitly state that Option A involves "restructuring tracks to eliminate inefficient CPI-indexed exposure." The RiseUp advisor presented this as achievable within the refinancing package. The ~200,000 NIS total savings figure likely assumes successful elimination of this track.

## Evidence Trail

- 2026-01-26: RiseUp advisor presented CPI-indexed track elimination as part of Option A restructuring
- Pending: Actual refinancing terms from Bank Hapoalim will confirm or challenge whether full elimination is achievable

## Impact

This assumption underpins the core value proposition of refinancing:
- If CPI-indexed exposure cannot be fully eliminated, the 200,000 NIS savings estimate may be overstated
- The decision to pursue total cost savings over monthly reduction depends partly on this structural fix
- Partial elimination (reducing rather than removing CPI exposure) would change the risk profile of the restructured mortgage

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]