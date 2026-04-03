---
based_on:
- '[[note/Voice Memo Fragment Historical Data From Shachar 2025-11-13]]'
challenged_by:
- '[[note/Voice Memo Fragment Historical Data From Shachar 2025-11-13]]'
confidence: low
confirmed_by: []
created: '2026-03-10'
invalidated_by: []
janitor_note: 'LINK001 — Telia''z wikilink is valid (YAML escaping false positive).
  Base view embeds (learn-assumption.base#Depends On This, #Related) reference _bases/learn-assumption.base
  which does not exist — vault-wide infrastructure issue; embeds preserved per policy.
  ORPHAN001 — no inbound wikilinks; consider linking from project/Telia''z AI Diagnostic
  Research Paper.'
name: Data Exports From Different Providers Share Compatible Schema
project:
- '[[project/Telia''z AI Diagnostic Research Paper]]'
related:
- '[[contradiction/Patient Dataset Record Count Discrepancy Between Exports]]'
- '[[contradiction/Data Export Provider Role Discrepancy Between Shachar and Shmulik]]'
- '[[constraint/All Data Exports Depend on Single Provider Shmulik]]'
source: Voice memo fragment from Rami Khouri, 2025-11-13
source_date: '2025-11-13'
status: challenged
type: assumption
---

# Data Exports From Different Providers Share Compatible Schema

## Claim

The research team implicitly assumes that patient data exports obtained from different providers (Shachar vs Shmulik) and from different time periods maintain a compatible schema and data structure, allowing them to be analyzed by the same AI diagnostic pipeline without structural adaptation.

## Basis

The AI diagnostic pipeline was developed against one dataset, and the team plans to run final analyses on the verified dataset from Shmulik. The assumption is that all exports feed cleanly into the same extraction and prediction pipeline. No explicit schema validation or compatibility check has been documented.

## Evidence Trail

- 2025-11-13: Rami noted in a voice memo that historical data sent by Shachar was "fundamentally different" (שונה מהותית) from what was previously being analyzed, suggesting a structural or methodological gap between historical and current data exports.
- 2026-02-22: Dataset size discrepancy (5,700 vs 6,041 records) between exports for the same inclusion period further suggests exports are not guaranteed to be identical.

## Impact

If data exports have incompatible schemas, the AI pipeline may silently produce incorrect extractions or predictions on records that don't match expected structure. All diagnostic accuracy figures could be affected. The team should explicitly validate schema compatibility before running final analyses across merged datasets.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
