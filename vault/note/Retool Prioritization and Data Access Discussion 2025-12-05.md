---
alfred_tags:
- healthcare/adhd
- partnerships/uk
- systems/case-management
created: '2026-02-25'
description: 'Meeting between Rami and Shachar about prioritizing Retool system improvements
  across three tracks: critical H1 fixes (KPIs, login, Teams), new system UI design,
  and new functionality. Also addressed transcript data access gap and action plan
  for stakeholder consultations.'
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  Base view embed (related.base#All) references _bases/related.base which may not
  exist. Create it to enable dynamic views.
name: Retool Prioritization and Data Access Discussion 2025-12-05
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Retool System Priorities and Data Access Discussion 2025-12-05]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
- '[[constraint/Transcript Data Not Available in BigQuery]]'
- '[[task/Compile Retool Improvement Priority List]]'
- '[[task/Resolve Teams Video Integration Issue for Clinic]]'
- '[[task/Provide Rami Direct Access to Session Transcripts]]'
relationships:
- confidence: 0.95
  context: Same date, near-identical Retool topics
  source: note/Retool Prioritization and Data Access Discussion 2025-12-05.md
  target: note/Retool System Prioritization and Data Access Discussion 2025-12-05.md
  type: related-to
- confidence: 0.8
  context: ADHD pathway and system prioritization
  source: note/Retool Prioritization and Data Access Discussion 2025-12-05.md
  target: note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Retool Prioritization and Data Access Discussion 2025-12-05

## Context

Rami and Shachar held a planning call to align on priorities for the Retool-based case management and CRM systems. Shachar is rebuilding the platform and needs clear requirements from the clinical operations side. This is a critical coordination touchpoint between the Innovation/CMO function (Rami) and the CTO function (Shachar).

## Three-Track Improvement Framework

Shachar proposed structuring Retool work into three tracks:

### Track 1: Critical Fixes for First 6 Months (H1 2026)
Things the clinic cannot operate without. Rami identified:
- **KPI dashboards** — the primary need for operational visibility
- **Teams/video integration** — currently causing patient no-shows and approximately 10% revenue loss. Patients get stuck entering calls due to technical issues; during that time, appointment slots are wasted and the clinic pays for half the session. Shachar noted this could take 3-4 months of development but suggested hiring a contractor to solve it.
- **Login issues** — therapists/psychiatrists experience system lockouts that disrupt their workflow. Shachar raised this from WhatsApp feedback.
- **Secretary-specific needs** — Stav (secretary) has started compiling requirements. Rami will gather more from Renee and the team.

Rami noted that money is less of a concern given the clinic's growth trajectory — the budget exists to invest in fixing these issues.

### Track 2: New System UI Design
Since Shachar is rebuilding the system from scratch, this is the time to define how the new UI should look. Design decisions made now cost the same as keeping the old design — so better to get it right. This includes layout, navigation, and user experience for psychiatrists and staff.

### Track 3: New Functionality
Additional features beyond what exists today, to be built on top of the new system. Lower priority than Tracks 1 and 2.

## Retool Case Management vs CRM

Rami clarified that the case management system (Retool) does not need new features urgently — he can improve prompts manually. The CRM side needs more investigation to determine what has and hasn't been implemented from previous plans.

## Data Access Gap: Transcript Texts

A critical data access issue was identified:
- **All structured data** (columns, patient metadata) is available in BigQuery
- **Questionnaire data** is mostly available in BigQuery
- **Session transcript texts are NOT in BigQuery** — stored only in the production database (no longer as files)
- **Rami cannot access transcripts independently** — has to request them from Shachar each time
- Shachar acknowledged this is a problem and committed to finding a solution for direct access
- The file IDs exist in the meeting text table but the actual text content is database-stored
- Security and data volume are the reasons transcripts are not replicated to BigQuery

## Action Items

1. Rami to compile a prioritized list of must-have Retool features for H1 2026
2. Rami to meet with Renee and the secretaries this week to understand their needs
3. Rami to meet with clinic staff to gather broader requirements
4. Shachar to find a solution for giving Rami direct transcript access
5. Both to have a follow-up discussion to finalize the priority list and create a work plan
6. Consider hiring a contractor for the Teams integration fix (3-4 month timeline)

## Revenue Impact of Teams Issue

Rami estimated that the Teams/video calling integration problem causes approximately 10% or more loss of potential revenue (or gross profit). The mechanism: patients experience technical difficulties joining the video call, causing delays or no-shows. The clinic pays for the reserved session time regardless, creating a direct financial loss that scales with patient volume.

## Related
![[related.base#All]]