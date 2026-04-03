---
alfred_tags:
- taliaz/reporting
- clinic-analytics
description: Quality assurance skill that performs comprehensive data validation and
  generates audit reports before finalizing monthly reports. Identifies bugs, errors,
  anomalies, and data quality issues to ensure report accuracy.
name: taliaz-report-auditor
---

# Taliaz Report Auditor Skill

A quality assurance skill that validates all report data and generates a comprehensive audit report identifying issues before the final report is delivered.

## Overview

This skill performs 7 categories of validation checks:

| Check | Description |
|-------|-------------|
| **Hours Anomalies** | Negative values, worked > scheduled, zero availability |
| **Meeting Consistency** | Total = done + noshow + cancelled + active |
| **Payment Calculations** | Payment = hours × rate, totals add up |
| **Income Consistency** | Therapist total = Clinic total |
| **Margin Analysis** | Margin = Income - Payment, negative margins |
| **Cross-Sheet Consistency** | Same therapists in all sheets |
| **Outlier Detection** | High noshow rates, low margins |

## Usage

### Python API

```python
from report_auditor import ReportAuditor

auditor = ReportAuditor()

# Audit calculated data before Excel generation
audit_result = auditor.audit_report_data(
    hours_summary=hours_df,
    meeting_counts=meetings_df,
    payment_summary=payment_df,
    income_by_therapist=income_therapist_df,
    income_by_clinic=income_clinic_df,
    margin_analysis=margin_df,
    raw_meetings=raw_meetings_df,
    availability=availability_df
)

# Check results
print(f"Critical issues: {audit_result.critical_count}")
print(f"Warnings: {audit_result.warning_count}")

# Generate audit report
audit_report_path = auditor.generate_audit_report(
    audit_result,
    output_dir="/path/to/output/",
    month="2026-01"
)

# Add audit sheet to Excel report
auditor.add_audit_sheet_to_excel(
    excel_path="/path/to/report.xlsx",
    audit_result=audit_result
)
```

### Command Line

```bash
# Audit an existing Excel report
python3 scripts/report_auditor.py \
    --report /path/to/monthly_report.xlsx \
    --output /path/to/output/

# Audit with raw data for deeper analysis
python3 scripts/report_auditor.py \
    --report /path/to/monthly_report.xlsx \
    --raw-data /path/to/raw_meetings.csv \
    --output /path/to/output/
```

## Audit Result Structure

```python
@dataclass
class AuditResult:
    issues: List[AuditIssue]
    checks_passed: List[str]
    summary: Dict[str, Any]
    
    @property
    def critical_count(self) -> int
    
    @property
    def warning_count(self) -> int
    
    @property
    def info_count(self) -> int
    
    @property
    def has_critical_issues(self) -> bool
```

## Issue Severity Levels

| Level | Description | Action |
|-------|-------------|--------|
| **CRITICAL** | Data integrity issues that make the report unreliable | Must fix before delivery |
| **WARNING** | Data quality issues that may affect accuracy | Should fix or acknowledge |
| **INFO** | Operational insights or anomalies | Review for business decisions |

## Validation Checks

### 1. Hours Summary Checks
- No negative values in any hours column
- Worked hours ≤ Scheduled hours
- Therapists with meetings should have available hours
- Utilization rate ≤ 100% (or flag as overtime)

### 2. Meeting Counts Checks
- Total = done + noshow + cancelled + active
- Adult + Youth = Total
- Intake + Followup = Total
- Flag any unknown status values

### 3. Payment Calculation Checks
- Worked payment = worked hours × worked rate
- Total payment = sum of all payment components
- No zero payment rates for active therapists
- Efficiency rate calculated correctly

### 4. Income Consistency Checks
- Therapist income total = Clinic income total
- No zero income for therapists with completed meetings
- Intake + Followup income = Total income

### 5. Margin Analysis Checks
- Margin = Income - Payment
- Margin rate = Margin / Income
- Flag negative margins
- Flag unusually low margin rates (<50%)

### 6. Cross-Sheet Consistency
- Same therapist list in all sheets
- Hours match between Hours_Summary and Payment_Summary
- Meeting counts match between sheets

### 7. Data Quality Checks
- No malformed names (newlines, extra spaces)
- No "Unknown" therapist types
- All therapists have payment rates

## Output Files

### Audit Report (Markdown)
A human-readable report with:
- Executive summary
- Critical issues with root cause analysis
- Warnings with recommendations
- Data quality issues
- Required actions (code fixes and data updates)
- List of passed validation checks

### Audit Sheet (Excel)
An additional sheet added to the report with:
- Summary statistics
- Issue list with severity
- Affected therapists
- Recommendations

## Integration with taliaz-reporter

The auditor is automatically called by `taliaz-reporter` before generating the final Excel file:

```python
# In taliaz-reporter
auditor = ReportAuditor()
audit_result = auditor.audit_report_data(...)

if audit_result.has_critical_issues:
    print("⚠️  Critical issues found - review audit report")

# Add audit sheet to Excel
auditor.add_audit_sheet_to_excel(report_path, audit_result)

# Generate separate audit report
auditor.generate_audit_report(audit_result, output_dir, month)
```

## Dependencies

- pandas
- openpyxl
- dataclasses (Python 3.7+)

## Notes

- The auditor does not modify any data - it only reports issues
- All issues include root cause analysis and recommendations
- The audit report is generated alongside the main report
- Critical issues are highlighted but do not block report generation