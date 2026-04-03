---
based_on:
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Platform Questionnaire Direct-Send Verification Call 2025-10-09]]'
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-31'
invalidated_by: []
janitor_note: LINK001 — Telia'z wikilink is a YAML single-quote escaping false positive
  (target project/Telia'z AI Clinical Platform verified to exist). ORPHAN001 — no
  inbound wikilinks; consider linking from project/Telia'z AI Clinical Platform or
  related decision/Three-Track Approach to Retool System Improvements.
name: Shachar Can Simultaneously Maintain Existing Retool and Rebuild Platform
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[assumption/Contractor Can Resolve Teams Integration in 3 to 4 Months]]'
- '[[assumption/Budget Available for System Improvements Given Clinic Growth]]'
source: Implied across multiple planning discussions between Rami and Shachar
source_date: '2025-12-05'
status: active
tags:
- capacity
- r-and-d
type: assumption
---

# Shachar Can Simultaneously Maintain Existing Retool and Rebuild Platform

## Claim

Shachar (VP R&D) can simultaneously maintain and fix the existing Retool-based case management system (Track 1 critical fixes — KPIs, Teams integration, login issues, secretary needs) while also designing and building the entirely new platform from scratch (Tracks 2 and 3). The three-track improvement framework agreed in December 2025 implicitly depends on one person and team handling both workstreams concurrently.

## Basis

Multiple source records show Shachar being called upon for both existing system verification (e.g., confirming questionnaire direct-send deployment during a quick phone call on 2025-10-09) and simultaneously being responsible for the full platform rebuild. The three-track framework proposed by Shachar himself organizes work into "critical Retool fixes" and "new system design/functionality" — all flowing through his team. Rami confirmed budget availability for contractors (e.g., Teams integration fix), which partially mitigates load, but the architectural and coordination burden remains centralized.

## Evidence Trail

- 2025-10-09: Shachar verifying questionnaire direct-send while away from computer, fielding Ahmad's technical issue simultaneously
- 2025-12-05: Three-track framework established — all tracks owned by Shachar's R&D team
- 2025-12-05: Rami noted budget is available for contractors to supplement, but core ownership remains with Shachar
- Multiple existing constraints document Innovation team's dependency on R&D for API infrastructure

## Impact

If this assumption fails (Shachar is overloaded), both the critical fixes timeline and the new platform rebuild will slip. The three-track framework becomes a two-track reality where either existing system maintenance or new development suffers. The Innovation team's dependencies on R&D would become even more acute.
