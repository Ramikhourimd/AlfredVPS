---
based_on:
- '[[decision/Three-Track Approach to Retool System Improvements]]'
- '[[decision/Rebuild Clinic Management Platform from Scratch]]'
confidence: medium
created: '2026-03-07'
janitor_note: LINK001 — Telia'z wikilink is valid (YAML escaping false positive).
  Record is missing base view embeds (learn-assumption.base sections) — consider adding
  \![[learn-assumption.base#Depends On This]] and \![[learn-assumption.base#Related]]
  to body. ORPHAN001 — no inbound wikilinks; consider linking from project/Telia'z
  AI Clinical Platform.
name: UI Design Changes During Platform Rewrite Are Cost-Neutral
project:
- '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[note/Retool System Prioritization and Data Access Discussion 2025-12-05]]'
- '[[note/Retool Prioritization and Data Access Discussion 2025-12-05]]'
- '[[task/Start Next-Generation System Prototype Brainstorm]]'
- '[[task/Survey Existing Clinical Systems for Next-Generation Prototype]]'
source: Shachar
source_date: '2025-12-05'
status: active
type: assumption
---

# UI Design Changes During Platform Rewrite Are Cost-Neutral

## Claim

Design changes to the new platform UI carry zero marginal cost compared to replicating the old design, because Shachar is rebuilding from scratch. This means Track 2 (New System UI Design) improvements are effectively free — the development effort is the same whether the team keeps the old layout or designs a better one.

## Basis

During the 2025-12-05 prioritization discussion, Shachar explicitly framed Track 2 as cost-neutral: "Design decisions made now cost the same as keeping the old design — so better to get it right." This assumption drives the three-track improvement framework, making UI redesign a low-risk, high-value investment window.

## Evidence Trail

- 2025-12-05: Shachar proposed three-track framework with Track 2 as cost-neutral UI redesign opportunity
- Task created for next-generation system prototype brainstorm (unconstrained vision exercise)
- Multiple tasks spawned for gathering staff UX requirements (secretaries, psychiatrists, case managers)

## Impact

This assumption justifies investing significant effort in UI/UX research and vision prototyping. If it proves false (e.g., custom UI designs require substantially more development time than replicating existing layouts), the Track 2 scope would need to be reduced or deprioritized against Track 1 critical fixes.
