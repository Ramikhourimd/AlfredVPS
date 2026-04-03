---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Output layer skill for generating comprehensive Excel reports and dashboards.
  Orchestrates all other skills (data-loader, name-mapper, meeting-analytics, payment,
  income) to produce professional monthly reports with multiple sheets, formatting,
  and KPI dashboards.
name: taliaz-reporter
---

# Taliaz Reporter Skill

The output layer skill that orchestrates all other Taliaz skills to generate comprehensive Excel reports and dashboards. This is the main entry point for monthly report generation.

## Overview

This skill combines data from:
- **taliaz-data-loader**: Raw data from API and reference files
- **taliaz-name-mapper**: Hebrew/English name normalization
- **taliaz-meeting-analytics**: Hours and meeting calculations
- **taliaz-payment**: Therapist payment calculations
- **taliaz-income**: Clinic income calculations

## Report Structure

The generated Excel report contains the following sheets:

| Sheet | Description |
|-------|-------------|
| **Dashboard** | KPIs, totals, and high-level metrics |
| **Hours_Summary** | Hours breakdown per therapist |
| **Meeting_Counts** | Meeting counts by status, type, patient type |
| **Payment_Summary** | Payment breakdown per therapist |
| **Income_By_Therapist** | Income generated per therapist |
| **Income_By_Clinic** | Income breakdown per clinic |
| **Margin_Analysis** | Profit margin per therapist |

## Usage

### Command Line

```bash
# Generate monthly report
python3 scripts/report_generator.py \
    --month 2025-12 \
    --availability /path/to/availability.csv \
    --output /path/to/output/

# Generate with custom filename
python3 scripts/report_generator.py \
    --month 2025-12 \
    --availability /path/to/availability.csv \
    --output /path/to/output/ \
    --filename "December_2025_Report.xlsx"
```

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-reporter/scripts")))

from report_generator import TaliazReporter

# Initialize reporter
reporter = TaliazReporter()

# Generate report
report_path = reporter.generate_monthly_report(
    month="2025-12",
    availability_path="/path/to/availability.csv",
    output_dir="/path/to/output/"
)

print(f"Report generated: {report_path}")
```

## Input Requirements

### Availability CSV

The availability file must have 3 columns:
1. **Therapist Name** (Hebrew)
2. **Available Hours** (monthly)
3. **Additional Payment** (₪)

Example:
```csv
Therapists Name,Available Hours,Additional Payment
אורי שוקרון,60,500
סעיד חלאילי,40,1000
```

## Output Format

### Dashboard Sheet

The dashboard includes:

**Organization Totals**
- Total Income
- Total Expenses (Payments)
- Net Margin
- Margin Rate

**Meeting Metrics**
- Total Meetings
- Completed Meetings
- Noshow Rate
- Average Income per Meeting

**Efficiency Metrics**
- Overall Utilization Rate
- Average Efficiency Rate

**Top Performers**
- Top 5 Therapists by Income
- Top 5 Therapists by Meetings
- Top 5 Clinics by Income

### Excel Formatting

The report includes professional formatting:
- Header styling with colors
- Number formatting (₪ for currency, % for rates)
- Column auto-width
- Conditional formatting for KPIs
- Frozen header rows

## Dependencies

This skill depends on all other Taliaz skills:
- `taliaz-data-loader`
- `taliaz-name-mapper`
- `taliaz-meeting-analytics`
- `taliaz-payment`
- `taliaz-income`

Required Python packages:
- pandas
- openpyxl
- requests

## Error Handling

The reporter handles common errors gracefully:

| Error | Behavior |
|-------|----------|
| Missing availability file | Generates report without availability data |
| Unmapped therapist names | Warns and continues with available mappings |
| API connection failure | Raises error with clear message |
| Missing pricing data | Uses default prices (₪0) |

## Notes

- All monetary values are in Israeli Shekels (₪)
- Reports are generated in Excel format (.xlsx)
- The reporter automatically normalizes Hebrew names to English
- Dashboard KPIs are calculated from the underlying data sheets