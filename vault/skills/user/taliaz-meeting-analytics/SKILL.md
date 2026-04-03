---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Core business logic skill for calculating therapist hours, meeting counts,
  and utilization metrics. Consumes data from taliaz-data-loader and provides calculated
  metrics to taliaz-payment and taliaz-income skills. Use this skill for any meeting-based
  analytics or hours calculations.
name: taliaz-meeting-analytics
---

# Taliaz Meeting Analytics Skill

The core business logic skill for calculating therapist hours, meeting counts, and utilization metrics. This skill consumes clean data from `taliaz-data-loader` and produces calculated metrics that feed into `taliaz-payment` and `taliaz-income` skills.

## Metrics Calculated

### Hours Metrics (Per Therapist)

| Metric | Description | Formula |
|--------|-------------|---------|
| **Scheduled Hours** | Total hours of scheduled meetings | Sum of meeting durations (based on meeting type) |
| **Worked Hours** | Hours of completed meetings | Sum of durations where status = "done" |
| **Noshow Hours** | Hours of noshow meetings | Sum of durations where status = "noshow" |
| **Unscheduled Hours** | Available hours not scheduled | Available Hours - Scheduled Hours |
| **Utilization Rate** | Percentage of available time used | Scheduled Hours / Available Hours × 100 |

### Meeting Counts (Per Therapist)

| Metric | Description |
|--------|-------------|
| **Total Meetings** | Count of all meetings |
| **Done Meetings** | Count of completed meetings |
| **Noshow Meetings** | Count of noshow meetings |
| **Cancelled Meetings** | Count of cancelled meetings |
| **By Patient Type** | Breakdown by Adult/Youth |
| **By Meeting Type** | Breakdown by Intake/FollowUp |

### Aggregations

| Level | Description |
|-------|-------------|
| **Per Therapist** | Individual therapist metrics |
| **Per Clinic** | Aggregated by clinic |
| **Per Patient Type** | Aggregated by Adult/Youth |
| **Per Meeting Type** | Aggregated by meeting type |
| **Total** | Organization-wide totals |

## Meeting Duration Logic

Meeting durations are determined by the therapist's configuration in the reference data:

| Meeting Type | Patient Type | Column in Reference |
|--------------|--------------|---------------------|
| Intake | Adult | `Intake Length Minutes - Adults` |
| FollowUp | Adult | `Followup Length Minutes - Adults` |
| Intake | Youth | `Intake Length Minutes - Youth` |
| FollowUp | Youth | `Followup Length Minutes - Youth` |

Default durations if therapist not found:
- Intake: 30 minutes
- FollowUp: 15 minutes

## Usage

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-meeting-analytics/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-data-loader/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-name-mapper/scripts")))

from meeting_analytics import MeetingAnalytics
from data_loader import TaliazDataLoader
from name_mapper import TaliazNameMapper

# Load data
loader = TaliazDataLoader()
data = loader.load_monthly_data("2025-12", "/path/to/availability.csv")

# Initialize name mapper and normalize availability
mapper = TaliazNameMapper(loader.therapists_df)
data["availability"]["therapist_name"] = mapper.normalize_column(
    data["availability"]["therapist_name"]
)

# Initialize analytics
analytics = MeetingAnalytics(loader)

# Calculate all metrics
results = analytics.calculate_all(
    meetings_df=data["meetings"],
    availability_df=data["availability"]
)

# Access results
hours_summary = results["hours_summary"]        # Per-therapist hours
meeting_counts = results["meeting_counts"]      # Per-therapist meeting counts
clinic_summary = results["clinic_summary"]      # Per-clinic aggregation
totals = results["totals"]                      # Organization-wide totals

# Get specific metrics
therapist_hours = analytics.get_therapist_hours("Ori Shukrun", data["meetings"])
# Returns: {"scheduled": 45.5, "worked": 40.0, "noshow": 5.5}

utilization = analytics.get_utilization("Ori Shukrun", data["meetings"], available_hours=60)
# Returns: 0.758 (75.8%)
```

### Command Line

```bash
# Calculate and display summary for a month
python3 scripts/meeting_analytics.py \
  --month 2025-12 \
  --availability /path/to/availability.csv

# Export results to CSV
python3 scripts/meeting_analytics.py \
  --month 2025-12 \
  --availability /path/to/availability.csv \
  --output /path/to/output/
```

## Output DataFrames

### Hours Summary (`hours_summary`)

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name (English) |
| `therapist_type` | str | "Case Manager" or "Psychiatrist" |
| `available_hours` | float | Monthly available hours (from availability CSV) |
| `scheduled_hours` | float | Total scheduled meeting hours |
| `worked_hours` | float | Hours of completed meetings |
| `noshow_hours` | float | Hours of noshow meetings |
| `unscheduled_hours` | float | Available - Scheduled |
| `utilization_rate` | float | Scheduled / Available (0-1) |

### Meeting Counts (`meeting_counts`)

| Column | Type | Description |
|--------|------|-------------|
| `therapist_name` | str | Therapist name (English) |
| `total_meetings` | int | Total meeting count |
| `done_meetings` | int | Completed meetings |
| `noshow_meetings` | int | Noshow meetings |
| `cancelled_meetings` | int | Cancelled meetings |
| `adult_meetings` | int | Adult patient meetings |
| `youth_meetings` | int | Youth patient meetings |
| `intake_meetings` | int | Intake meetings |
| `followup_meetings` | int | FollowUp meetings |

### Clinic Summary (`clinic_summary`)

| Column | Type | Description |
|--------|------|-------------|
| `clinic_name` | str | Clinic name |
| `total_meetings` | int | Total meetings at clinic |
| `done_meetings` | int | Completed meetings |
| `noshow_meetings` | int | Noshow meetings |
| `total_hours` | float | Total scheduled hours |
| `worked_hours` | float | Completed hours |

### Totals (`totals`)

| Key | Type | Description |
|-----|------|-------------|
| `total_meetings` | int | Organization-wide meeting count |
| `total_done` | int | Total completed meetings |
| `total_noshow` | int | Total noshow meetings |
| `total_scheduled_hours` | float | Total scheduled hours |
| `total_worked_hours` | float | Total worked hours |
| `total_noshow_hours` | float | Total noshow hours |
| `overall_utilization` | float | Average utilization rate |
| `noshow_rate` | float | Noshow / Total meetings |

## Business Rules

### Status Mapping

| API Status | Category | Counts As |
|------------|----------|-----------|
| `done` | Completed | Worked Hours |
| `noshow` | Noshow | Noshow Hours |
| `cancelled` | Cancelled | Neither (excluded from hours) |
| `rescheduled` | Cancelled | Neither (excluded from hours) |

### Patient Type Normalization

| Input Values | Normalized To |
|--------------|---------------|
| `Adult`, `Adults`, `adult` | `Adult` |
| `Youth`, `Youth/Kids`, `Kids`, `youth` | `Youth` |

### Meeting Type Detection

| Contains | Classified As |
|----------|---------------|
| `Intake` | Intake |
| `FollowUp`, `Followup`, `Follow Up` | FollowUp |

## Dependencies

- pandas
- `taliaz-data-loader` (for reference data and meeting durations)
- `taliaz-name-mapper` (for normalizing availability names)

## Notes

- All calculations are based on the meeting's scheduled duration, not actual duration
- Cancelled and rescheduled meetings are excluded from hours calculations
- Utilization rate is only calculated for therapists with available hours > 0
- Meeting durations are therapist-specific based on reference data