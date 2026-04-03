---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Loads, validates, and provides access to all Taliaz operational data.
  This is the foundational data skill for all Taliaz reporting. Provides clean DataFrames
  for therapists, clinics, meeting types, pricing, meetings (from API), and monthly
  availability. Use this skill FIRST before any other Taliaz reporting skill.
name: taliaz-data-loader
relationships:
- confidence: 0.85
  context: provides data for income calc
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-income/SKILL.md
  type: supports
- confidence: 0.7
  context: provides data for analytics
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-meeting-analytics/SKILL.md
  type: supports
- confidence: 0.85
  context: provides data for payments
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-payment/SKILL.md
  type: supports
- confidence: 0.8
  context: provides data for auditing
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-report-auditor/SKILL.md
  type: supports
- confidence: 0.9
  context: provides data for reporting
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-reporter/SKILL.md
  type: supports
- confidence: 0.9
  context: loads from Xano data source
  source: skills/user/taliaz-data-loader/SKILL.md
  target: skills/user/taliaz-xano-data/SKILL.md
  type: depends-on
---

# Taliaz Data Loader Skill

The single source of truth for all Taliaz operational data. This foundational skill loads, validates, and standardizes data from all sources (reference files and APIs) and provides clean, consistent DataFrames to all other reporting skills.

## Data Sources

### Static Reference Tables (Bundled in Skill)

| Table | Source File | Description |
|-------|-------------|-------------|
| **Therapists** | `references/User_type+User_Fee.xlsx` | Master list of therapists with payment rates and meeting lengths |
| **Clinics** | `references/HealthyMind_Pricing_Complete.xlsx` (Clinics sheet) | Clinic master data |
| **Meeting Types** | `references/HealthyMind_Pricing_Complete.xlsx` (Meeting_Types sheet) | Meeting type definitions |
| **Pricing** | `references/HealthyMind_Pricing_Complete.xlsx` (Pricing_Detailed sheet) | Income pricing matrix by clinic × patient_type × meeting_type |

### Variable Monthly Data

| Table | Source | Description |
|-------|--------|-------------|
| **Meetings** | API: `https://dev-backend.taliaz-cm.com/agent_meeting_report` | Real-time meeting records |
| **Availability** | User-provided CSV (monthly) | Therapist availability hours and additional payments |

## Schema Definitions

### Therapists DataFrame (`therapists_df`)

| Column | Type | Description |
|--------|------|-------------|
| `ID` | int | Unique therapist identifier |
| `English Name` | str | Therapist name in English (canonical) |
| `Hebrew Name` | str | Therapist name in Hebrew |
| `Worked Hour` | float | Payment rate per worked hour (₪) |
| `Noshow Hour` | float | Payment rate per noshow hour (₪) |
| `Unscheduled Hour` | int | Payment rate per unscheduled hour (₪) |
| `Non-Clinical Hour` | int | Payment rate per non-clinical hour (₪) |
| `Type` | str | "Case Manager" or "Psychiatrist" |
| `Intake Length Minutes - Adults` | int | Default intake meeting length for adults |
| `Followup Length Minutes - Adults` | int | Default followup meeting length for adults |
| `Intake Length Minutes - Youth` | int | Default intake meeting length for youth |
| `Followup Length Minutes - Youth` | int | Default followup meeting length for youth |

### Clinics DataFrame (`clinics_df`)

| Column | Type | Description |
|--------|------|-------------|
| `clinic_id` | int | Unique clinic identifier |
| `clinic_name` | str | Clinic name |
| `id_prefix` | str | HM ID prefix for the clinic |
| `prompt_prefix` | str | Patient type indicator (Adult/Youth/UK) |

### Meeting Types DataFrame (`meeting_types_df`)

| Column | Type | Description |
|--------|------|-------------|
| `meeting_type_id` | int | Unique meeting type identifier |
| `meeting_type_name` | str | Meeting type name in English |
| `heb_name` | str | Meeting type name in Hebrew |
| `user_type` | str | "case_manager" or "doctor" |

### Pricing DataFrame (`pricing_df`)

| Column | Type | Description |
|--------|------|-------------|
| `business_unit` | str | Business unit (Clalit, Maccabi, Taliaz Funding, etc.) |
| `business_sub_unit` | str | Sub-unit for more granular categorization |
| `clinic_id` | float | Clinic ID (nullable for ITC) |
| `patient_type` | str | "Adult" or "Youth/Kids" |
| `meeting_type_id` | int | Meeting type ID |
| `meeting_type_name` | str | Meeting type name |
| `price` | float | Income price for this combination (₪) |

### Meetings DataFrame (`meetings_df`)

| Column | Type | Description |
|--------|------|-------------|
| `id` | int | Unique meeting identifier |
| `clinic_id` | int | Clinic ID |
| `patient_id` | int | Patient ID |
| `user_id` | int | Therapist ID |
| `meetingtype_id` | int | Meeting type ID |
| `start` | int | Start timestamp (milliseconds) |
| `end` | int | End timestamp (milliseconds) |
| `status` | str | "done", "noshow", "cancelled", etc. |
| `patient_type` | str | "Adult" or "Youth" |
| `is_test` | bool | Test record flag |
| `meeting_type` | str | Meeting type name |
| `clinic_name` | str | Clinic name |
| `therpaist_name` | str | Therapist name (English) |
| `start_dt` | datetime | Parsed start datetime (added by loader) |
| `month` | period | Month period (added by loader) |

### Availability DataFrame (`availability_df`)

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name (Hebrew in source, normalized to English) |
| `available_hours` | float | Available hours for the month |
| `additional_payment` | float | Additional payment amount (₪) |

## Usage

### Command Line

```bash
# Load all reference data and validate
python3 scripts/data_loader.py --validate

# Load data for a specific month
python3 scripts/data_loader.py --month 2025-12 --availability /path/to/availability.csv

# Export reference data to CSV for inspection
python3 scripts/data_loader.py --export-refs /path/to/output/
```

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-data-loader/scripts")))

from data_loader import TaliazDataLoader

# Initialize the loader (automatically loads all reference data)
loader = TaliazDataLoader()

# Access reference DataFrames directly
therapists_df = loader.therapists_df      # 28 therapists
clinics_df = loader.clinics_df            # 22 clinics
meeting_types_df = loader.meeting_types_df # 5 meeting types
pricing_df = loader.pricing_df            # 74 pricing rules

# Load monthly data (meetings from API + availability from CSV)
monthly_data = loader.load_monthly_data(
    month="2025-12",
    availability_path="/path/to/availability.csv"
)

# Access all data through the returned dictionary
meetings_df = monthly_data["meetings"]
availability_df = monthly_data["availability"]
therapists_df = monthly_data["therapists"]
pricing_df = monthly_data["pricing"]

# Get meeting duration for a specific therapist and meeting type
duration = loader.get_meeting_duration(
    therapist_name="Ori Shukrun",
    meeting_type="Case manager Intake",
    patient_type="Adult"
)
# Returns: 30 (minutes)

# Get income price for a meeting
price = loader.get_income_price(
    clinic_id=3,
    meeting_type_id=1,
    patient_type="Adult"
)
# Returns: 220.0 (₪)

# Get payment rate for a therapist
rate = loader.get_payment_rate(
    therapist_name="Ori Shukrun",
    rate_type="worked"
)
# Returns: 130.0 (₪/hour)
```

## Validation

The loader performs automatic validation on load:

1. **Schema Validation**: Ensures all required columns exist
2. **Type Validation**: Ensures correct data types
3. **Referential Integrity**: Checks that clinic_ids and meeting_type_ids in pricing exist in master tables
4. **Completeness**: Reports on missing values

```python
# Run validation and get report
validation_report = loader.validate()
print(validation_report)
```

## Error Handling

| Error | Behavior |
|-------|----------|
| Reference file not found | Raises `FileNotFoundError` with clear message |
| API timeout/failure | Returns cached data if available, otherwise raises `ConnectionError` |
| Invalid schema | Raises `ValueError` with details on missing/invalid columns |
| Missing availability file | Returns empty DataFrame with warning |

## Dependencies

- pandas
- requests
- openpyxl (for Excel file reading)

## Notes

- All reference files are bundled in the `references/` directory
- The API key is stored securely in the script (not exposed in SKILL.md)
- Test records (`is_test=True`) are automatically filtered out from meetings
- Timestamps are automatically converted to datetime objects