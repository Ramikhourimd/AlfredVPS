---
confidence: high
created: '2026-02-25'
janitor_note: 'LINK001 false positives: (1) Telia''z wikilinks use YAML double single-quote
  escaping — project/Telia''z AI Clinical Platform.md and project/Telia''z AI Diagnostic
  Research Paper.md both exist. (2) Base view embeds \![[learn-assumption.base#Depends
  On This]] and \![[learn-assumption.base#Related]] preserved per policy. ORPHAN001:
  record is a standalone assumption derived from product meeting — no inbound links
  expected.'
name: Edit Time Measurement Is Only Reliable in Real-Time Mode
project:
- '[[project/Telia''z AI Clinical Platform]]'
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[conversation/Product Meeting Report Logic API and AI Architecture]]'
- '[[note/Product Meeting Report Logic API and AI Architecture 2026-02-25]]'
- '[[decision/Measure Summary Approval as Delta From Session End]]'
source: Product meeting technical discussion
source_date: '2026-02-25'
status: active
type: assumption
---

# Edit Time Measurement Is Only Reliable in Real-Time Mode

## Claim

Measuring the time clinicians spend editing AI-generated summaries is only reliable when captured in real-time mode. Google Docs "modified" events are not valid start-of-editing markers and cannot be used to reconstruct edit duration retroactively.

## Basis

Google Docs modification timestamps reflect background saves and auto-sync, not user-initiated editing actions. Only the real-time event stream from the summary editor captures actual edit start/end times accurately.

## Evidence Trail

- 2026-02-25: Confirmed in product meeting that Google Docs modified events are unreliable for edit timing

## Impact

- Research paper timing analysis must rely only on real-time captured data
- Historical data without real-time capture cannot provide edit duration metrics
- Strengthens the existing decision to measure approval time as delta from session end

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
