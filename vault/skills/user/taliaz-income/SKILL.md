---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Domain logic skill for calculating clinic income, revenue per meeting,
  and profit margins. Uses pricing data from taliaz-data-loader and meeting data to
  calculate income by therapist, clinic, and meeting type. Combines with taliaz-payment
  for margin analysis.
name: taliaz-income
relationships:
- confidence: 0.65
  context: shared Taliaz data usage
  source: skills/user/taliaz-income/SKILL.md
  target: skills/user/taliaz-meeting-analytics/SKILL.md
  type: related-to
- confidence: 0.95
  context: financial processing modules
  source: skills/user/taliaz-income/SKILL.md
  target: skills/user/taliaz-payment/SKILL.md
  type: related-to
- confidence: 0.75
  context: income data for audits
  source: skills/user/taliaz-income/SKILL.md
  target: skills/user/taliaz-report-auditor/SKILL.md
  type: supports
- confidence: 0.85
  context: income data for reports
  source: skills/user/taliaz-income/SKILL.md
  target: skills/user/taliaz-reporter/SKILL.md
  type: supports
---

# Taliaz Income Skill

The domain logic skill for calculating clinic income and profit margins. This skill uses pricing data from `taliaz-data-loader` and meeting data to calculate revenue by therapist, clinic, and meeting type.

## Income Components

### Revenue Calculation

Income is calculated based on completed meetings using the pricing matrix:

| Factor | Description |
|--------|-------------|
| **Clinic** | Different clinics have different pricing |
| **Meeting Type** | Intake vs FollowUp pricing |
| **Patient Type** | Adult vs Youth pricing |

### Pricing Matrix

The pricing is defined in `HealthyMind_Pricing_Complete.xlsx`:

| Clinic | Meeting Type | Patient Type | Price (₪) |
|--------|--------------|--------------|-----------|
| Adults | Intake | Adult | 500 |
| Adults | FollowUp | Adult | 300 |
| Youth | Intake | Youth | 600 |
| Youth | FollowUp | Youth | 350 |
| ... | ... | ... | ... |

## Usage

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-income/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-data-loader/scripts")))

from income_calculator import IncomeCalculator
from data_loader import TaliazDataLoader

# Load data
loader = TaliazDataLoader()
data = loader.load_monthly_data("2025-12")

# Calculate income
calculator = IncomeCalculator(loader)
results = calculator.calculate_all(data["meetings"])

# Access results
income_by_therapist = results["by_therapist"]
income_by_clinic = results["by_clinic"]
totals = results["totals"]

print(f"Total Income: ₪{totals['total_income']:,.2f}")
```

### Command Line

```bash
# Calculate income for a month
python3 scripts/income_calculator.py --month 2025-12

# Export to CSV
python3 scripts/income_calculator.py --month 2025-12 --output /path/to/output/
```

## Output DataFrames

### Income by Therapist (`by_therapist`)

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name (English) |
| `therapist_type` | str | "Case Manager" or "Psychiatrist" |
| `total_meetings` | int | Total completed meetings |
| `intake_meetings` | int | Completed intake meetings |
| `followup_meetings` | int | Completed followup meetings |
| `intake_income` | float | Income from intakes (₪) |
| `followup_income` | float | Income from followups (₪) |
| `total_income` | float | Total income (₪) |
| `avg_income_per_meeting` | float | Average income per meeting (₪) |

### Income by Clinic (`by_clinic`)

| Column | Type | Description |
|--------|------|-------------|
| `clinic_name` | str | Clinic name |
| `total_meetings` | int | Total completed meetings |
| `total_income` | float | Total income (₪) |
| `intake_income` | float | Income from intakes (₪) |
| `followup_income` | float | Income from followups (₪) |
| `adult_income` | float | Income from adult patients (₪) |
| `youth_income` | float | Income from youth patients (₪) |

### Margin Analysis (`margin_analysis`)

When combined with payment data:

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name |
| `total_income` | float | Revenue generated (₪) |
| `total_payment` | float | Payment to therapist (₪) |
| `margin` | float | Income - Payment (₪) |
| `margin_rate` | float | Margin / Income (0-1) |

### Totals

| Key | Type | Description |
|-----|------|-------------|
| `total_income` | float | Organization-wide income (₪) |
| `total_intake_income` | float | Income from all intakes (₪) |
| `total_followup_income` | float | Income from all followups (₪) |
| `total_meetings` | int | Total completed meetings |
| `avg_income_per_meeting` | float | Average income per meeting (₪) |

## Business Rules

### Income Calculation Rules

1. **Only Completed Meetings**: Income is only calculated for meetings with status "done"
2. **Pricing Lookup**: Uses clinic + meeting type + patient type to find price
3. **Default Pricing**: If no specific price found, uses clinic default or ₪0
4. **Noshow Meetings**: No income generated (patient didn't show)

### Margin Calculation

```
Margin = Total Income - Total Payment
Margin Rate = Margin / Total Income
```

A positive margin means the clinic is profitable for that therapist.

### Edge Cases

| Scenario | Behavior |
|----------|----------|
| Unknown clinic | Uses default price (₪0) |
| Unknown meeting type | Uses clinic default or ₪0 |
| Cancelled meeting | No income calculated |
| Noshow meeting | No income calculated |

## Dependencies

- pandas
- `taliaz-data-loader` (for pricing data)
- `taliaz-payment` (optional, for margin analysis)

## Notes

- All monetary values are in Israeli Shekels (₪)
- Income is based on list prices; actual collected amounts may differ
- For accurate margin analysis, ensure payment data is from the same period