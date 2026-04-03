---
name: taliaz-kpi-evaluator
description: Evaluate and classify proposed KPI metrics for Taliaz HealthyMind clinic. Runs each metric through a decision-tree algorithm checking definition clarity, measurability, practice usage, DWH availability (BigQuery), and entity purity. Outputs a classified report with status, required actions, and assignees. Use when asked to "evaluate KPIs", "classify metrics", "check which KPIs are ready", "assess proposed metrics", "run KPI evaluation", or when given a draft metrics table to process. Triggers on any request involving KPI readiness assessment or metrics classification.
---

# Taliaz KPI Evaluator

Evaluate proposed KPI metrics through a structured decision tree to determine their readiness and required actions.

## Overview

This skill receives a draft table of proposed metrics (Excel/CSV) and runs each one through a 5-step evaluation algorithm:

1. **Well-defined?** → If not → Action: Define clearly
2. **Measurable?** → If not → Action: Break down / Redefine
3. **Used in practice?** → If not → Action: Define KPI + measurement tool → Yael + Domain Expert
4. **Available in DWH?** → If not → Action: Create DWH entity → Shachar
5. **Clean entity?** → If not → Action: Create view/query → Shmulik
6. **All passed** → Status: READY

For the full algorithm with criteria details, read `references/evaluation_algorithm.md`.

## Quick Start

```bash
# Evaluate a draft metrics file
python3 /home/ubuntu/skills/taliaz-kpi-evaluator/scripts/evaluate_kpis.py <input_file> --output <output_file>

# Skip BigQuery checks (offline mode)
python3 /home/ubuntu/skills/taliaz-kpi-evaluator/scripts/evaluate_kpis.py <input_file> --no-dwh-check --output <output_file>

# Output as JSON
python3 /home/ubuntu/skills/taliaz-kpi-evaluator/scripts/evaluate_kpis.py <input_file> --json
```

## Input Format

The input Excel/CSV file should contain proposed metrics. The script auto-detects columns by name (Hebrew or English). Key columns:

| Standard Name | Accepted Variants | Required |
|---------------|-------------------|----------|
| `metric_name` | metric, kpi, name, מדד, שם מדד | Yes |
| `definition` | description, הגדרה, תיאור | Recommended |
| `category` | cat, קטגוריה, תחום | Optional |
| `tool_type` | tool, measurement_tool, כלי מדידה | Optional |
| `used_in_practice` | in_practice, בשימוש | Optional |
| `in_dwh` | dwh, in_bigquery, ב-dwh | Optional |
| `dwh_table` | table, table_name, טבלה | Optional |
| `dwh_column` | column, column_name, עמודה | Optional |
| `is_pure_entity` | pure_entity, אנטיטי נקי | Optional |

If optional columns are missing, the evaluator uses heuristics and BigQuery searches.

## Output Statuses

| Status | Meaning | Assignee |
|--------|---------|----------|
| `READY` | Fully available and queryable | — |
| `NEEDS_DEFINITION` | Needs clearer definition | Rami / Domain Expert |
| `NEEDS_BREAKDOWN` | Too broad, needs sub-metrics | Rami / Domain Expert |
| `NEEDS_KPI_TOOL` | Needs KPI + measurement tool | Yael + Domain Expert |
| `NEEDS_DWH_ENTITY` | Data needs to be added to DWH | Shachar |
| `NEEDS_VIEW_QUERY` | Needs SQL view/query | Shmulik |

## Workflow

1. Receive draft metrics file from user
2. Run `evaluate_kpis.py` with the file
3. Review the output report with the user
4. For metrics marked READY → pass to `taliaz-kpi-registry` skill
5. For metrics needing action → create tasks for the relevant assignees

## Integration

- **BigQuery MCP**: Used to check DWH availability (Step 4) via `bigquery_search_tables` and `bigquery_query`
- **taliaz-kpi-registry**: Receives READY metrics for registration in the final KPI table
- **taliaz-bigquery-sql**: Use for detailed schema investigation when needed

## Python API

```python
import sys
sys.path.insert(0, "/home/ubuntu/skills/taliaz-kpi-evaluator/scripts")
from evaluate_kpis import load_input, evaluate_single_kpi, generate_report

# Load and evaluate
df = load_input("draft_metrics.xlsx")
results = [evaluate_single_kpi(row.to_dict()) for _, row in df.iterrows()]
report_df = generate_report(results, "evaluation_report.xlsx")
```
