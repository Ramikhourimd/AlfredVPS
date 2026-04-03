---
alfred_tags:
- healthcare/adhd
- partnerships/uk
- systems/case-management
created: '2025-12-05'
description: Planning session between Rami and Shachar to prioritize Retool system
  improvements for the first six months, covering KPIs, Teams video integration, login
  issues, new system UI design, and meeting transcript data access.
janitor_note: LINK001 — Telia'z wikilinks are valid (YAML escaping false positive).
  related.base#All is a template-standard base view embed; _bases/ files not yet created.
name: Retool System Prioritization and Data Access Discussion 2025-12-05
project: '[[project/Telia''z AI Clinical Platform]]'
related:
- '[[person/Rami Khouri]]'
- '[[person/Shachar]]'
- '[[org/Telia''z]]'
- '[[project/Telia''z Clinic Israel]]'
- '[[conversation/Retool Improvements and Data Access Planning 2025-12-05]]'
- '[[constraint/DWH Access Is Partial and Lacks Full Standardization]]'
relationships:
- confidence: 0.8
  context: ADHD pathway and system prioritization
  source: note/Retool System Prioritization and Data Access Discussion 2025-12-05.md
  target: note/UK NHS ADHD Pathway Design and OMG Partnership 2025-07-03.md
  type: related-to
session: null
status: active
subtype: meeting-notes
tags: []
type: note
---

# Retool System Prioritization and Data Access Discussion 2025-12-05

## Context

Rami and Shachar met to align on system development priorities. Shachar is rebuilding the clinical platform (new system) while maintaining the existing Retool-based case management system. The conversation focused on what is critical for the next six months and how to structure the prioritization process.

## Three-Track Prioritization Framework

Shachar proposed organizing the work into three tracks:

### Track 1: Critical Retool Fixes (First 6 Months)
What cannot be lived without in the existing Retool system:
- **KPIs** — Rami confirmed KPIs are the primary priority for the existing system
- **Teams video integration** — Patients are delayed or failing to join sessions due to login/entry issues. Rami estimates ~10% of potential revenue or gross profit is lost to no-shows caused partly by this issue. Shachar noted this could take 3-4 months of contractor work but is solvable with budget.
- **Login issues** — Psychiatrists get stuck repeatedly due to authentication problems in Retool. Shachar proposed fixing this as it's achievable though not trivial.
- **Secretary/admin needs** — Stav (סתיו) had started documenting secretary requirements; this needs to be completed.

### Track 2: New System Design
Since Shachar is rebuilding from scratch, design decisions can be baked in from the start at no additional cost:
- UI look and feel preferences
- Workflow improvements
- Layout and navigation changes

### Track 3: New Functionality Additions
Features beyond what exists today, to be added to the new system after the baseline is built.

## Data Access Discussion

Rami raised the issue of needing direct access to clinical data:
- **BigQuery** contains most structured data (columns), but NOT questionnaire data or meeting transcripts
- **Meeting transcripts** are stored as text in the production database (not as files), for both security and volume reasons
- **Document IDs** are visible in the DWH but the actual text content is inaccessible to Rami
- Shachar acknowledged the need and committed to finding a solution for giving Rami direct access to transcripts without requesting each time
- The solution will NOT be through BigQuery — it requires a separate access mechanism

## Agreed Next Steps

1. Rami to create a prioritized list of critical Retool needs for the first 6 months
2. Rami to schedule meetings with Renee, secretaries, and clinic staff to gather requirements from each group
3. Rami to audit what has and hasn't been implemented in the CRM system
4. Shachar to find a solution for Rami's access to meeting transcripts
5. Both to have a focused discussion session to finalize the prioritized work plan

## Key Quotes

- Rami on KPIs: "I do want tools that help, that make things more convenient for psychiatrists. But it's not critical for me right now. With some manual work I can also improve the prompts."
- Rami on Teams: "About 10% or a bit more of potential revenue or even gross profit is being lost [to no-shows from Teams issues]."
- Shachar on hiring contractors: "This is something we can solve with money. It might take 3-4 months of work, but we can hire a contractor to solve this problem."
- Rami on budget: "Money is less of a problem for me right now, because with this growth rate we can invest."

## Related
![[related.base#All]]