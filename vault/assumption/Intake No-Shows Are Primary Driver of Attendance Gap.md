---
based_on:
- '[[asset/Clinic Flow Dashboard v4]]'
confidence: medium
created: '2026-02-25'
janitor_note: 'FM001 — FIXED: Added missing type and created fields. LINK001 — Telia''z
  wikilink is valid (YAML escaping false positive). Base view embeds (learn-assumption.base#Depends
  On This, #Related) reference _bases/learn-assumption.base which does not exist —
  vault-wide structural issue, embeds preserved.'
name: Intake No-Shows Are Primary Driver of Attendance Gap
project:
- '[[project/Telia''z Clinic Israel]]'
related:
- '[[note/Clinic Flow Dashboard v4 Design Analysis]]'
- '[[decision/Four Core KPI Targets for Clinic Operations Dashboard]]'
source: Dashboard v4 Layer 2 attendance drill-down (demo data)
status: active
type: assumption
---

# Intake No-Shows Are Primary Driver of Attendance Gap

## Claim

Intake appointments have a significantly lower attendance rate (80%) compared to follow-up appointments (92-93%), making first-visit no-shows the primary contributor to the overall attendance gap. Strengthening pre-intake reminders and double-confirmation protocols would have the highest impact on improving aggregate attendance.

## Basis

Layer 2 attendance breakdown in the Flow Dashboard v4 prototype shows:
- Intake: 48/60 attended = 80% (below 85% target)
- Follow-up CM: 23/25 = 92% (above target)
- Follow-up Psychiatrist: 14/15 = 93% (above target)

No-show reasons: 8 no-shows, 10 patient cancellations, 2 clinic cancellations, 5 rescheduled. The dashboard insight attributes most non-attendance to intake no-shows.

## Evidence Trail

- Dashboard v4 demo data supports this pattern (pending validation with production data)
- Needs confirmation once API integration provides real attendance data

## Impact

If confirmed with production data, this assumption would direct operational improvement efforts toward intake-specific interventions (reminder protocols, double-confirmation) rather than across-the-board attendance programs.

![[learn-assumption.base#Depends On This]]
![[learn-assumption.base#Related]]
