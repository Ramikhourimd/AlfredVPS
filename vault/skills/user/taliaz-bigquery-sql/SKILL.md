---
name: taliaz-bigquery-sql
description: Generate SQL queries for Taliaz HealthyMind clinic's BigQuery data warehouse. Use when asked to query patient data, clinical outcomes, appointments, medications, marketing/CRM data, lead conversion, campaign performance, or any analytics on the DWH (HubSpot/marketing) or XanoView (clinical backend) datasets. Triggers on requests like "how many patients", "show me meetings", "conversion rate", "campaign performance", "revenue by", "patient outcomes", or any data analysis question about Taliaz operations.
---

# Taliaz BigQuery SQL Generator

Generate SQL queries for Taliaz's BigQuery datasets based on natural language requests.

## Quick Reference

**Datasets**:
- `taliazdwh.DWH.*` - Marketing, CRM, leads, deals, campaigns
- `taliazdwh.XanoView.*` - Clinical data: patients, meetings, medications

**Key Tables**:
| Need | Table |
|------|-------|
| Patients | `XanoView.Patient` |
| Appointments | `XanoView.Meeting` + `MeetingType` |
| Staff | `XanoView.user` |
| Medications | `XanoView.medications` + `medication_type` |
| Assessments | `XanoView.patient_questionnaire` |
| Leads/Contacts | `DWH.Contacts` |
| Sales | `DWH.Deals` + `ContactDeals` |
| Interactions | `DWH.Engagements` + `EngagementContacts` |
| Ad Campaigns | `DWH.Campaigns` + `CampaignsReport` |

**Cross-Dataset Link**: `DWH.Contacts.Patient_ID` ↔ `XanoView.Patient.hs_id`

## Query Generation Process

1. **Identify data domain**: Clinical (XanoView) vs Marketing/CRM (DWH) vs both
2. **Select tables**: Reference `references/schema.md` for column details
3. **Apply joins**: Check relationships in schema reference
4. **Add filters**: Use appropriate status/date filters
5. **Reference examples**: See `references/examples.md` for common patterns

## Key Field Mappings

### Patient Status Values
- `Waiting-for-obligations` - Pending paperwork/payment
- `Waiting-for-approval` - Clinical review
- `Active` - In treatment
- `Finish` - Completed
- `Cancel`, `Reject` - Dropped/rejected

### Meeting Types (meetingtype_id)
- 1 = CM Intake (45 min)
- 2 = Doctor Meeting (30 min)
- 3 = Doctor Followup (20 min)
- 4 = CM Followup (20 min)

### Meeting Status
- `active` - Scheduled
- `done` - Completed
- `canceled` - Canceled
- `noshow` - Patient didn't attend

### Clinical Outcomes (PHQ-8/GAD-7)
- **Remission**: Score ≤ 5
- **Response**: Score > 5 but ≤ 50% of baseline
- **Non-response**: Score > 50% of baseline

### Lifecycle Stages (Contacts)
subscriber → lead → marketingqualifiedlead → salesqualifiedlead → opportunity → customer

## Common Patterns

### Count with grouping
```sql
SELECT {dimension}, COUNT(*) as count
FROM `taliazdwh.{Dataset}.{Table}`
GROUP BY {dimension}
ORDER BY count DESC
```

### Join patient with staff
```sql
SELECT p.*, d.name as doctor, cm.name as case_manager
FROM `taliazdwh.XanoView.Patient` p
LEFT JOIN `taliazdwh.XanoView.user` d ON p.doctor_id = d.id
LEFT JOIN `taliazdwh.XanoView.user` cm ON p.case_manager_id = cm.id
```

### Date filtering
```sql
WHERE {timestamp_col} >= TIMESTAMP('2024-01-01')
WHERE {timestamp_col} >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
WHERE {timestamp_col} >= TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), MONTH)
```

### Cross-dataset join
```sql
FROM `taliazdwh.DWH.Contacts` c
JOIN `taliazdwh.XanoView.Patient` p ON c.Patient_ID = CAST(p.hs_id AS STRING)
```

## Resources

- **Full schema**: Read `references/schema.md` for complete table/column documentation
- **Query examples**: Read `references/examples.md` for common query patterns

## Output Format

When generating queries:
1. Use fully qualified table names: `taliazdwh.DATASET.TABLE`
2. Include meaningful column aliases
3. Add comments for complex logic
4. Suggest appropriate LIMIT for exploratory queries
5. Explain what the query does in plain language
