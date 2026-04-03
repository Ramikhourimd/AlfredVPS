---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Domain logic skill for calculating therapist payments. Consumes hours
  data from taliaz-meeting-analytics and applies payment rates from taliaz-data-loader
  to calculate worked, noshow, unscheduled, non-clinical, and additional payments
  per therapist.
name: taliaz-payment
---

# Taliaz Payment Skill

The domain logic skill for calculating therapist payments. This skill consumes hours data from `taliaz-meeting-analytics` and applies payment rates from the therapist reference data to calculate comprehensive payment summaries.

## Payment Components

### Per-Therapist Payment Types

| Payment Type | Description | Formula |
|--------------|-------------|---------|
| **Worked Payment** | Payment for completed meetings | Worked Hours × Worked Hour Rate |
| **Noshow Payment** | Payment for noshow meetings | Noshow Hours × Noshow Hour Rate |
| **Unscheduled Payment** | Payment for available but unscheduled time | Unscheduled Hours × Unscheduled Hour Rate |
| **Non-Clinical Payment** | Payment for non-clinical work (admin, training) | Non-Clinical Hours × Non-Clinical Hour Rate |
| **Additional Payment** | Ad-hoc payments from monthly CSV | Direct value from availability CSV |
| **Total Payment** | Sum of all payment components | Sum of above |

### Payment Rates (From Reference Data)

Each therapist has individual payment rates defined in `User_type+User_Fee.xlsx`:

| Column | Description | Typical Range |
|--------|-------------|---------------|
| `Worked Hour` | Rate per worked hour | ₪100-200 |
| `Noshow Hour` | Rate per noshow hour | ₪50-150 |
| `Unscheduled Hour` | Rate per unscheduled hour | ₪0-130 |
| `Non-Clinical Hour` | Rate per non-clinical hour | ₪50-100 |

## Usage

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-payment/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-meeting-analytics/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-data-loader/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-name-mapper/scripts")))

from payment_calculator import PaymentCalculator
from meeting_analytics import MeetingAnalytics
from data_loader import TaliazDataLoader
from name_mapper import TaliazNameMapper

# Load data
loader = TaliazDataLoader()
data = loader.load_monthly_data("2025-12", "/path/to/availability.csv")

# Normalize availability names
mapper = TaliazNameMapper(loader.therapists_df)
data["availability"]["therapist_name"] = mapper.normalize_column(
    data["availability"]["therapist_name"]
)

# Calculate hours using meeting analytics
analytics = MeetingAnalytics(loader)
analytics_results = analytics.calculate_all(data["meetings"], data["availability"])

# Calculate payments
calculator = PaymentCalculator(loader)
payment_summary = calculator.calculate_payments(
    hours_summary=analytics_results["hours_summary"],
    availability_df=data["availability"]
)

# Access results
print(payment_summary[["therapist_name", "total_payment"]])

# Get payment for specific therapist
therapist_payment = calculator.get_therapist_payment(
    therapist_name="Ori Shukrun",
    hours_summary=analytics_results["hours_summary"],
    availability_df=data["availability"]
)
print(f"Total: ₪{therapist_payment['total_payment']:,.2f}")
```

### Command Line

```bash
# Calculate payments for a month
python3 scripts/payment_calculator.py \
  --month 2025-12 \
  --availability /path/to/availability.csv

# Export to CSV
python3 scripts/payment_calculator.py \
  --month 2025-12 \
  --availability /path/to/availability.csv \
  --output /path/to/payment_summary.csv
```

## Output DataFrame

### Payment Summary (`payment_summary`)

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name (English) |
| `therapist_type` | str | "Case Manager" or "Psychiatrist" |
| `worked_hours` | float | Hours of completed meetings |
| `worked_rate` | float | Payment rate per worked hour (₪) |
| `worked_payment` | float | Worked hours × rate (₪) |
| `noshow_hours` | float | Hours of noshow meetings |
| `noshow_rate` | float | Payment rate per noshow hour (₪) |
| `noshow_payment` | float | Noshow hours × rate (₪) |
| `unscheduled_hours` | float | Available but unscheduled hours |
| `unscheduled_rate` | float | Payment rate per unscheduled hour (₪) |
| `unscheduled_payment` | float | Unscheduled hours × rate (₪) |
| `nonclinical_hours` | float | Non-clinical work hours |
| `nonclinical_rate` | float | Payment rate per non-clinical hour (₪) |
| `nonclinical_payment` | float | Non-clinical hours × rate (₪) |
| `additional_payment` | float | Ad-hoc additional payment (₪) |
| `total_payment` | float | Sum of all payments (₪) |
| `efficiency_rate` | float | Worked Payment / Total Payment |

## Business Rules

### Payment Calculation Rules

1. **Worked Payment**: Always calculated based on actual worked hours
2. **Noshow Payment**: Therapist still gets paid (at noshow rate) for patient no-shows
3. **Unscheduled Payment**: Only calculated if therapist has available hours defined
4. **Non-Clinical Payment**: Currently set to 0 (can be added via availability CSV)
5. **Additional Payment**: Direct pass-through from availability CSV

### Efficiency Rate

The efficiency rate measures how much of the total payment comes from actual work:

```
Efficiency Rate = Worked Payment / Total Payment
```

Higher efficiency means more payment from actual patient work vs. noshow/unscheduled time.

### Edge Cases

| Scenario | Behavior |
|----------|----------|
| Therapist not in reference | Uses default rates (₪120/worked, ₪60/noshow) |
| No availability data | Unscheduled hours = 0, additional payment = 0 |
| Zero available hours | Unscheduled payment = 0 |
| Negative unscheduled hours | Clamped to 0 (over-scheduled) |

## Totals

The calculator also provides organization-wide payment totals:

```python
totals = calculator.calculate_totals(payment_summary)
# Returns:
{
    "total_worked_payment": 45000.0,
    "total_noshow_payment": 8000.0,
    "total_unscheduled_payment": 2000.0,
    "total_nonclinical_payment": 0.0,
    "total_additional_payment": 5000.0,
    "grand_total_payment": 60000.0,
    "average_efficiency": 0.75
}
```

## Dependencies

- pandas
- `taliaz-data-loader` (for payment rates)
- `taliaz-meeting-analytics` (for hours data)
- `taliaz-name-mapper` (for normalizing names)

## Notes

- All monetary values are in Israeli Shekels (₪)
- Payment rates are therapist-specific, not role-based
- The skill does not handle tax calculations or deductions
- For payroll integration, export to CSV and import into payroll system