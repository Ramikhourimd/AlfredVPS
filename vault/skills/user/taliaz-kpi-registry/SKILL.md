---
name: taliaz-kpi-registry
description: Build and maintain the KPI registry table for Taliaz HealthyMind clinic in Supabase. Stores all approved KPI metrics with full metadata (category, type, tool, frequency, responsible, accountable, targets). Supports adding KPIs from Excel/CSV, importing evaluated metrics from taliaz-kpi-evaluator, exporting the registry, and generating KPI dashboards. Use when asked to "add KPIs to registry", "build KPI table", "export KPI list", "generate KPI dashboard", "update KPI targets", or any request to manage the KPI metrics database. Triggers on KPI registration, KPI table management, or KPI dashboard generation.
---

# Taliaz KPI Registry

Build and maintain the master KPI registry table in Supabase with full metadata and dashboard generation.

## Overview

The KPI Registry is the single source of truth for all HealthyMind KPI metrics. It stores each metric with its classification, measurement details, ownership, and targets. The registry receives metrics from the `taliaz-kpi-evaluator` skill after they pass evaluation.

## Quick Start

```bash
SCRIPT="/home/ubuntu/skills/taliaz-kpi-registry/scripts/kpi_registry.py"

# Step 1: Initialize the table (first time only)
python3 $SCRIPT init

# Step 2: Add KPIs from a file
python3 $SCRIPT add <input_file.xlsx>

# Step 3: Import evaluated metrics from evaluator output
python3 $SCRIPT import-evaluated <evaluation_report.xlsx>

# Step 4: List current KPIs
python3 $SCRIPT list [--category Clinical]

# Step 5: Export to Excel
python3 $SCRIPT export kpi_registry_export.xlsx

# Step 6: Generate dashboard
python3 $SCRIPT dashboard kpi_dashboard.xlsx
```

## Table Schema

The `kpi_registry` table in Supabase stores:

| Column | Type | Description |
|--------|------|-------------|
| `kpi_name` | text | Metric name (unique key) |
| `kpi_name_heb` | text | Hebrew name |
| `category` | text | Clinical / Administrative / Financial / HR / Marketing |
| `type` | text | Sub-type (Satisfaction, Remission, Efficiency, Revenue) |
| `tool_type` | text | SMS / Questionnaire / Review / System Log / CRM / DWH Query |
| `frequency` | text | Per Session / Weekly / Monthly / Quarterly |
| `subject_type` | text | Therapists / Patients / Clinic / System |
| `responsible` | text | R in RACI |
| `accountable` | text | A in RACI |
| `current_kpi` | float | Current baseline value |
| `target` | float | Target value |
| `unit` | text | Unit of measurement |
| `dwh_source` | text | BigQuery source table |
| `status` | text | active / draft / deprecated |

For full schema details, read `references/kpi_table_schema.md`.

## Workflow

### End-to-End KPI Pipeline

```
Draft Metrics (Excel from Basel)
  → taliaz-kpi-evaluator (evaluate & classify)
  → taliaz-kpi-registry (register approved metrics)
  → Dashboard (Excel with summary, categories, action items)
```

### Adding KPIs

The `add` command accepts Excel/CSV files with flexible column naming (Hebrew or English). The script auto-maps columns to the registry schema. Unrecognized columns are ignored.

### Importing from Evaluator

The `import-evaluated` command reads the output of `taliaz-kpi-evaluator` and:
- Marks `READY` metrics as `status: active`
- Marks other metrics as `status: draft` with their evaluation status
- Preserves action notes and assignee information

### Dashboard Generation

The `dashboard` command creates a multi-sheet Excel file:
1. **KPI Registry** — Full list of all KPIs
2. **Per Category** — Separate sheet per category (Clinical, Admin, etc.)
3. **Dashboard** — Summary metrics (total, active, draft, with targets)
4. **Action Items** — Metrics that still need work (non-READY)

## Integration

- **taliaz-kpi-evaluator**: Upstream — provides evaluated metrics
- **Supabase**: Storage backend for the registry table
- **BigQuery**: Referenced in `dwh_source` and `dwh_query` columns for data lineage
- **taliaz-bigquery-sql**: Use to write and validate `dwh_query` values
