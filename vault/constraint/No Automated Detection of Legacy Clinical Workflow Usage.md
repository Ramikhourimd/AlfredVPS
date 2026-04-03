---
alfred_tags:
- healthcare/constraints
- psychiatrist/authentication
- clinical-workflow
authority: System limitation in Retool and HoViD clinical platform
created: '2026-02-27'
janitor_note: 'LINK001 — Telia''z wikilinks are valid (YAML escaping false positive).
  Synthesis and assumption wikilinks in related field are valid targets. Base view
  embeds (learn-constraint.base#Affected Projects, #Related) reference _bases/learn-constraint.base
  which does not exist — create base file to enable dynamic views. ORPHAN001 — no
  inbound wikilinks; consider linking from project/Telia''z Clinic Israel.'
name: No Automated Detection of Legacy Clinical Workflow Usage
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[decision/Require Frontal Training Before Removing Legacy Feature Workflows]]'
- '[[decision/Require Frontal Training Before Deprecating Old Clinical Features]]'
- '[[synthesis/Feature Rollout Failures Follow Predictable Announce-Ignore-Retrain
  Cycle]]'
- '[[assumption/Asynchronous Digital Announcements Insufficient for Clinician Feature
  Adoption]]'
relationships:
- confidence: 0.75
  context: Legacy workflows link to auth disruptions
  source: constraint/No Automated Detection of Legacy Clinical Workflow Usage.md
  target: constraint/Psychiatrist Authentication Issues Cause Repeated Workflow Disruptions.md
  type: related-to
source: Observed during operational meetings when psychiatrists found still using
  Google Docs
source_date: '2025-01-12'
status: active
type: constraint
---

# No Automated Detection of Legacy Clinical Workflow Usage

## Constraint

The clinic has no automated mechanism to detect when clinicians bypass new platform features and continue using legacy workflows. When the in-app summary editing feature was rolled out, some psychiatrists continued editing in Google Docs (the old workflow) without management's knowledge. This was only discovered when Rami manually investigated during operational meetings — first on 2025-01-12, and again on 2025-08-01 when the same issue persisted.

## Source

System limitation in the clinical platform (HoViD/Retool). Neither system tracks which workflow path a clinician uses for a given task, nor alerts management when legacy tools (Google Docs) are used instead of new in-platform features.

## Implications

- Feature adoption cannot be measured without manual auditing
- The "ignore" phase of the announce-ignore-retrain cycle persists undetected until someone manually checks
- Management cannot distinguish between "feature works but isn't used" and "feature has a bug preventing adoption"
- Each feature rollout requires follow-up manual verification, adding to management workload
- Without detection, the frontal training decision cannot be triggered proactively — it only happens reactively after discovering non-adoption

## Expiry / Review

This constraint persists until the clinical platform adds usage analytics or workflow tracking. Should be reviewed when HoViD platform updates are planned.

![[learn-constraint.base#Affected Projects]]
![[learn-constraint.base#Related]]