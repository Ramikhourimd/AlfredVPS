---
name: summary-delay-analysis
description: Analyze time delays between summary generation, editing, approval, and sending for specific patients or across the clinic. Use when asked about summary workflow efficiency, delay patterns, psychiatrist performance metrics, or to investigate specific patient cases. Triggers on requests like "summary delay for patient HM-XXX-000", "how long does it take to send summaries", "summary approval time", or "workflow bottlenecks".
---

# Summary Delay Analysis Skill

Analyze time between AI summary generation and workflow actions (save, approve, send) for HealthyMind clinical meetings.

## Key Tables (BigQuery)

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `XanoView.patient_history` | Action timestamps | action, created_at, meeting_id |
| `XanoView.patient_files` | File sent timestamps | sent_date, meeting_id, patient_file_type_id=10 |
| `XanoView.Patient` | Patient identifiers | ID_serial, id, clinic_id, doctor_id |
| `XanoView.Meeting` | Meeting context | id, patient_id, user_id, start |
| `XanoView.user` | Staff names | id, name |

## Action Types in patient_history

| Action | Description |
|--------|-------------|
| `Generate summary` | AI generates summary |
| `Summary saved` | Clinician saves edits |
| `Summary approved` / `Summary Approved` | Summary approved |
| `Summary sent` | Sent to patient (legacy) |

## Key Metrics

- **Generation to Send Time**: from first "Generate summary" to patient_files.sent_date
- **Generation to Save Time**: from "Generate summary" to first "Summary saved"
- **Geometric Mean**: preferred measure for skewed time data (use LOG transform)

## Core Query Pattern (Specific Patient)

```sql
WITH patient_filter AS (
  SELECT id as patient_id, ID_serial, doctor_id, clinic_id
  FROM `taliazdwh.XanoView.Patient`
  WHERE ID_serial IN ('HM-MCB-001')
),
generate_events AS (
  SELECT ph.meeting_id, ph.created_at as generate_time,
    pf.ID_serial, pf.doctor_id, pf.clinic_id,
    ROW_NUMBER() OVER (PARTITION BY ph.meeting_id ORDER BY ph.created_at) as rn
  FROM `taliazdwh.XanoView.patient_history` ph
  JOIN `taliazdwh.XanoView.Meeting` m ON ph.meeting_id = m.id
  JOIN patient_filter pf ON m.patient_id = pf.patient_id
  WHERE ph.action = 'Generate summary' AND ph.meeting_id IS NOT NULL
),
send_events AS (
  SELECT meeting_id, MIN(sent_date) as sent_time
  FROM `taliazdwh.XanoView.patient_files`
  WHERE patient_file_type_id = 10 AND sent_to_patient = TRUE
  GROUP BY meeting_id
)
SELECT g.ID_serial, g.meeting_id, u.name as psychiatrist, c.name as clinic,
  g.generate_time, snd.sent_time,
  ROUND(TIMESTAMP_DIFF(snd.sent_time, g.generate_time, SECOND) / 60.0, 1) as gen_to_send_minutes
FROM generate_events g
LEFT JOIN send_events snd ON g.meeting_id = snd.meeting_id
LEFT JOIN `taliazdwh.XanoView.user` u ON g.doctor_id = u.id
LEFT JOIN `taliazdwh.XanoView.Clinic` c ON g.clinic_id = c.id
WHERE g.rn = 1
ORDER BY g.ID_serial, g.generate_time
```

## Aggregate by Psychiatrist

Use geometric mean (EXP(AVG(LN(delay_seconds)))) for skewed data.
Filter: delay between 1 and 604800 seconds (1 week max).
Include n, geometric_mean_minutes, median_minutes, p90_minutes, pct_delayed_24h.

## Time Thresholds

| Category | Threshold |
|----------|-----------|
| Excellent | < 5 min |
| Good | 5-30 min |
| Acceptable | 30 min - 2 hr |
| Delayed | 2-24 hr |
| Critical | > 24 hr |

## Effect Size (Cohen's d)

Large: |d| >= 0.8, Medium: 0.5-0.8, Small: 0.2-0.5, Negligible: < 0.2

## Variance Explained Benchmarks

Psychiatrist: 25-35%, Time of Day: 5-10%, Day of Week: 3-7%, Clinic: 2-5%
