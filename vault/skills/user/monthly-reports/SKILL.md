---
name: monthly-reports
description: Generate comprehensive monthly reports for HealthyMind/Taliaz clinic operations. Triggers on requests for monthly reports, therapist hours reports, payment calculations, income analysis, meeting summaries, clinic metrics, or dashboard generation. Covers hours tracking (available, scheduled, worked, noshow, unscheduled), meeting counts by patient type and meeting type, payment breakdowns, income per therapist/clinic, and master dashboard with KPIs.
---

# Monthly Reports Skill

Generate comprehensive monthly reports for HealthyMind/Taliaz psychiatric clinic operations.

## Data Sources

### 1. Raw Monthly Meetings API
```
URL: https://dev-backend.taliaz-cm.com/agent_meeting_report?api_key=e2c471e9-c73f-4c22-9bb5-8dc86229b670
Filter: Keep only is_test=FALSE
Fields: id, clinic_id, patient_id, user_id, meetingtype_id, start, end, status, 
        re_intake, HM_ID, patient_type, is_test, meeting_type, clinic_name, therpaist_name
```

### 2. Reference Files (bundled in skill)
- `references/income_fees.csv` - Income fees per clinic × meeting type × provider type
- `references/payment_fees.csv` - Payment rates per therapist (hourly + per-meeting)

### 3. User-Provided Data (REQUIRED)
**Before generating a report, ask the user to upload `Additional_Payment_Active` as a CSV file.**
This file contains:
- Therapist availability hours for the month
- Additional payment amounts

### 4. Static Reference Tables
See `references/data_schemas.md` for Meeting_Type, User_type, Clinic_type schemas.

## Report Generation Workflow

### Step 0: Request User Data (REQUIRED FIRST)
**Before starting, ask the user to upload the `Additional_Payment_Active` CSV file** containing:
- Column A: Therapist Name
- Column B: Available Hours (monthly)
- Column C: Additional Payment Amount

### Step 1: Load All Data Sources

```python
import pandas as pd
import requests
from pathlib import Path

# 1. Fetch API data
api_url = "https://dev-backend.taliaz-cm.com/agent_meeting_report?api_key=e2c471e9-c73f-4c22-9bb5-8dc86229b670"
meetings_df = pd.DataFrame(requests.get(api_url).json())
meetings_df = meetings_df[meetings_df['is_test'] == False]

# 2. Load reference files (bundled in skill)
skill_path = Path(__file__).parent.parent / "references"
income_fees_df = pd.read_csv(skill_path / "income_fees.csv")
payment_fees_df = pd.read_csv(skill_path / "payment_fees.csv")

# 3. Load user-provided availability data
availability_df = pd.read_csv("user_provided_additional_payment_active.csv")
```

### Step 2: Determine Report Period (Automatic)

The report automatically determines the target month:
1. Calculates the **previous month** from current date (e.g., running in Jan 2026 → Dec 2025)
2. If previous month has data in meetings table, uses it
3. Otherwise, uses the **most recent month with data**

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

meetings_df['start_dt'] = pd.to_datetime(meetings_df['start'], unit='ms')
meetings_df['month'] = meetings_df['start_dt'].dt.to_period('M')

# Auto-detect: previous month or most recent with data
current_date = datetime.now()
previous_month = (current_date - relativedelta(months=1)).strftime('%Y-%m')
available_months = sorted([str(m) for m in meetings_df['month'].unique()], reverse=True)
target_month = previous_month if previous_month in available_months else available_months[0]

monthly_df = meetings_df[meetings_df['month'] == target_month]
```

## Output Tables

### Table 1: Hours Summary Per Therapist

**Columns:** Therapist_name, Meeting_type, Available_Hours, Total_Scheduled_Hours, Total_Worked_Hours, Total_Noshow_Hours, Unscheduled_Hours

**Meeting type default lengths (minutes):**
- Case manager Intake: 30
- Psychiatrist Intake: 30
- Psychiatrist FollowUp: 15
- Case manager FollowUp: 15
- Psychiatrist FollowUp 30 min: 30

**Calculations:**
- Available Hours: From user-provided "Additional_Payment_Active" CSV Column B
- Scheduled Hours: Sum default_length for status IN ('done', 'noshow')
- Worked Hours: Sum default_length for status='done'
- Noshow Hours: Sum default_length for status='noshow'
- Unscheduled Hours: Available_Hours - Scheduled_Hours

### Table 2: Meeting Counts Per Therapist

**Hierarchy:** Therapist → Patient_type (Adult/Youth) → Meeting_type → Status (done/noshow)

### Table 3: Payment Per Therapist

**Columns:**
1. Payments for Worked Hours (absolute + %)
2. Payments for Noshow Hours (absolute + %)
3. Payment for Unscheduled Hours (absolute + %)
4. Payment for Non-Clinical Hours (absolute + %)
5. Additional Payment (absolute + %) - from user-provided CSV Column C
6. Total Payment
7. Payment Efficiency = Worked Payment / Total Payment

### Table 4: Income Per Therapist
Income calculated per meeting based on: clinic × meeting_type × provider_type

**Fee lookup logic:**
```python
# Map meeting_type to fee columns
def get_income_fee(row, income_fees_df):
    clinic = row['clinic_name']
    meeting_type = row['meeting_type']
    
    # Determine fee column based on meeting type
    if 'Intake' in meeting_type:
        if 'Psychiatrist' in meeting_type:
            col = 'Intake Psy'
        else:
            col = 'Intake CM'
    else:  # Followup
        if 'Psychiatrist' in meeting_type:
            col = 'Followup Psy'
        else:
            col = 'Followup CM'
    
    # Look up fee for clinic
    clinic_row = income_fees_df[income_fees_df.iloc[:, 0] == clinic]
    return clinic_row[col].values[0] if len(clinic_row) > 0 else 0
```

Sum (done meetings × income_fee for that clinic/meeting_type combination)

### Table 5: Income Per Clinic
Sum (done meetings × income_fee for that clinic/meeting_type combination), grouped by clinic

### Master Dashboard

| Category | Metrics |
|----------|---------|
| Income | Total Income, Income by Clinic/Patient Type, Trend |
| Expenses | Total Payments, Payment by Category, Trend |
| Margin | Gross Margin, Margin % |
| Efficiency | Avg Payment Efficiency, Hours Utilization, Show Rate |
| Clinic | Meetings/Clinic, Noshow Rate, Income/Clinic |
| Therapist | Top Performers by Income/Efficiency |

## Script Usage

```bash
# Auto-detect month with availability data (RECOMMENDED)
python3 scripts/generate_monthly_report.py --availability /path/to/additional_payment_active.csv --output /path/to/output

# Specify month explicitly
python3 scripts/generate_monthly_report.py --month 2025-12 --availability /path/to/availability.csv --output /path/to/output

# Without availability data (hours/additional payment will be empty)
python3 scripts/generate_monthly_report.py --output /path/to/output
```

See `scripts/generate_monthly_report.py` for complete implementation.
