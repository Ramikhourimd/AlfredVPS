---
name: taliaz-weekly-summary
description: Generate weekly operational summary reports for HealthyMind clinic. Pulls activity metrics, wait times, satisfaction, and staffing data from BigQuery, collects HR pipeline data from organizational sources, and produces a comprehensive Markdown report with capacity projections and a KPI scorecard. This is an operational/clinical/admin report — no financial data. Use when asked for "weekly summary", "weekly report", "this week's numbers", "weekly update for Rami", "clinic activity this week", or any request for a periodic operational summary of HealthyMind. Differentiates from work-periodic-summary (which covers personal work items like emails/calendar) by focusing on clinic-wide operational and clinical metrics.
---

# Taliaz Weekly Summary Report

Generate a comprehensive weekly operational summary for HealthyMind clinic combining BigQuery metrics, HR pipeline data, and capacity projections.

**Important**: This is an operational/clinical/admin report. Do NOT include revenue, financial data, or cost metrics. Financial reporting is handled separately.

## Scope Distinction

- **This skill**: Clinic-wide operational metrics (meetings, wait times, staffing, capacity). Data from BigQuery + HR sources.
- **work-periodic-summary**: Personal work items (emails, calendar, transcripts). Data from Gmail/Calendar/Drive.

## Report Generation Process

1. Determine the reporting week (default: last 7 days ending Saturday)
2. Query BigQuery for weekly and MTD metrics
3. Query BigQuery for comparison period (same week last month)
4. Collect HR pipeline data from organizational sources
5. Calculate capacity projections using formulas
6. Generate the report using the template
7. Deliver as Markdown file

## Step 1: Determine Date Ranges

Calculate these date ranges from the target week:

```
week_start       = Monday of target week (e.g., 2026-03-09)
week_end         = Sunday + 1 day (e.g., 2026-03-16)
prev_week_start  = Same dates minus 1 month (e.g., 2026-02-09)
prev_week_end    = Same dates minus 1 month (e.g., 2026-02-16)
month_start      = First of current month (e.g., 2026-03-01)
prev_month_start = First of previous month (e.g., 2026-02-01)
prev_month_same_day = Previous month, same day number (e.g., 2026-02-15)
today            = Report generation date
```

## Step 2: Query BigQuery

Use the `taliaz-bigquery-sql` skill patterns. Read `references/bigquery-queries.md` for all query templates.

Run these queries (can be parallelized in batches):

**Batch 1 — Weekly activity:**
- Meetings by status (this week)
- Meetings by status (same week last month)
- Meetings by type (this week)
- Meetings by type (same week last month)

**Batch 2 — MTD and comparison:**
- Meetings by status (MTD current month)
- Meetings by status (MTD previous month)
- Worked hours (MTD current)
- Worked hours (MTD previous)
- Full previous month totals

**Batch 3 — Wait times, quality:**
- Wait times (current month)
- Wait times (previous month)
- Patient backlog
- Satisfaction scores (this week)
- Satisfaction scores (same week last month)

**Batch 4 — Referrals and therapists:**
- New patient registrations by funding entity (this week) — uses `p.created_at` (Registered, not Approved)
- New patient registrations by funding entity (same week last month)
- Active therapists with meeting counts (this week)

**Mandatory query filters** (apply to ALL queries):
- `JOIN Clinic c ON ... WHERE c.intake = true AND c.demo = false`
- Funding entity labels: `Patient` → `פרטי`, `Taliaz` → `תרומות`
- Do NOT use `patient_history` table
- Referrals use **Registered** count (`XanoView.Patient.created_at`), NOT Approved (`DWH.Patients_raw.approvedDate`)

## Step 3: Collect HR Pipeline Data

Read `references/hr-pipeline.md` for collection workflow.

Sources (try in order):
1. Gmail — search for HR updates from Shira Lachmann
2. Supabase KB — query employees table for recent additions
3. Ask user if no recent data found

Categorize each person into: **Active**, **Started**, **Onboarding**, **HR Intake**, or **Pipeline**.

Record: name (Hebrew + English), role (CM/Psychiatrist), phase, notes, expected start date.

## Step 4: Calculate Capacity Projections

Read `references/capacity-formulas.md` for all formulas.

Key calculations:
1. **Current baseline**: Project MTD hours/meetings to full month
2. **Expansion timeline**: For each HR phase, add `count × 40h/month`
3. **Intake capacity**: `active_CMs × 10 intakes/week`
4. **Backlog clearance**: `backlog / (weekly_capacity - weekly_referrals)`
5. **Bottleneck detection**: Flag any meeting type > 90% utilization; check CM/Psychiatrist pipeline ratio

## Step 5: Generate Report

Use the template at `templates/weekly-report-template.md`. Fill in all `{placeholders}` with calculated values.

**Writing guidelines:**
- Lead each section with an interpretive paragraph, not just tables
- Highlight the single most important signal in the Executive Summary
- Use specific numbers and percentages, not vague language
- Flag risks with concrete thresholds (e.g., "95.4% utilization" not "high utilization")
- Compare everything: this week vs last month, MTD vs previous MTD
- Project forward: what does this week's pace mean for the full month?
- Note data quality issues (e.g., low satisfaction survey response rates)
- Do NOT include any revenue, financial, or cost data

**Scorecard status thresholds** (from `references/capacity-formulas.md`):
- ✅ = On target
- ⚠️ = Close/watch
- 🔴 = Needs attention

## Step 6: Deliver

Save the report as: `HealthyMind_Weekly_Summary_{week_start}-{day}_{year}.md`

Attach the file and provide a brief summary message highlighting:
1. Top-line numbers (meetings, patients, therapists)
2. The single most important trend
3. The biggest risk or attention item
4. Capacity outlook

## Resources

- **BigQuery queries**: `references/bigquery-queries.md` — All SQL templates with mandatory filters
- **HR pipeline**: `references/hr-pipeline.md` — Data collection workflow and capacity assumptions
- **Capacity formulas**: `references/capacity-formulas.md` — All projection calculations and scorecard thresholds
- **Report template**: `templates/weekly-report-template.md` — Full Markdown template with placeholders
