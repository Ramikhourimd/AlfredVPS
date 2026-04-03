---
alfred_tags:
- taliaz/knowledge-base
- data-ingestion
- protocols
description: Ingest missing data identified by taliaz-kb-gap-audit into the Supabase
  KB. Consumes gap audit JSON reports and orchestrates ingestion using existing skills
  (taliaz-email-ingest for emails, taliaz-transcript-ingest for transcripts). Triggers
  on "ingest the gaps", "fill the missing data", "ingest missing emails and transcripts",
  "process the gap report", or any request to act on gap audit results. Always run
  taliaz-kb-gap-audit first to produce the input report.
name: taliaz-kb-gap-ingest
---

# Taliaz KB Gap Ingestion

Consumes gap audit reports from `taliaz-kb-gap-audit` and orchestrates ingestion of missing data using existing ingestion skills.

## Prerequisites

Run the gap audit first to produce a report:
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-audit/scripts/audit_all.py \
  --after 2026-01-01 --before 2026-02-22 --output /tmp/kb_full_gap_report.json
```

## Quick Start

### Ingest All Gaps
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-ingest/scripts/ingest_gaps.py /tmp/kb_full_gap_report.json
```

### Dry Run (Preview)
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-ingest/scripts/ingest_gaps.py /tmp/kb_full_gap_report.json --dry-run
```

### Ingest Only Emails
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-ingest/scripts/ingest_gaps.py /tmp/kb_full_gap_report.json --only gmail
```

### Ingest Only Transcripts
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-ingest/scripts/ingest_gaps.py /tmp/kb_full_gap_report.json --only transcripts
```

### Limit Batch Size
```bash
python3 /home/ubuntu/skills/taliaz-kb-gap-ingest/scripts/ingest_gaps.py /tmp/kb_full_gap_report.json --limit 10
```

## How It Works

### Input
Accepts any JSON report produced by `taliaz-kb-gap-audit`:
- Full forensic report (`audit_all.py` output)
- Individual Gmail report (`audit_gmail.py` output)
- Individual transcript report (`audit_transcripts.py` output)
- Individual Slack report (`audit_slack.py` output)

### Ingestion Strategy Per Source

| Source | Strategy | Underlying Skill |
|--------|----------|------------------|
| Gmail | Groups missing emails by date, calls `ingest_emails.py --date` per date batch | `taliaz-email-ingest` |
| Transcripts | Groups by `extracted_date`, calls `ingest_transcripts.py --date` per date | `taliaz-transcript-ingest` |
| Slack | Lists uncovered messages for manual review (no auto-ingest) | `taliaz-doc-processor` (manual) |

### Gmail Ingestion Flow
```
Gap report -> group emails by date -> for each date:
  -> call ingest_emails.py --date YYYY-MM-DD
  -> script fetches from Gmail MCP + inserts to email_digests
```

### Transcript Ingestion Flow
```
Gap report -> group transcripts by extracted_date -> for each date:
  -> call ingest_transcripts.py --date YYYY-MM-DD
  -> script fetches from Google Drive + AI analysis + inserts to all KB tables
Undated files -> listed for manual processing via taliaz-doc-processor
```

### Slack Handling
Slack messages cannot be auto-ingested (no 1:1 mapping). The script lists uncovered significant messages for manual review and processing via `taliaz-doc-processor`.

## Parameters

| Parameter | Description |
|-----------|-------------|
| `report` | Path to gap audit JSON report (required) |
| `--dry-run` | Preview what would be ingested without actually inserting |
| `--only gmail\|transcripts\|slack` | Process only one source type |
| `--limit N` | Max items to process per source |

## Output

Produces a results JSON file alongside the input report:
```
/tmp/kb_full_gap_report_ingestion_results.json
```

Contains per-source stats: processed, success, failed, skipped counts.

## Typical Workflow

```
1. Run gap audit:     taliaz-kb-gap-audit -> /tmp/kb_full_gap_report.json
2. Review gaps:       Check the report for what's missing
3. Dry run:           ingest_gaps.py report.json --dry-run
4. Ingest:            ingest_gaps.py report.json
5. Re-audit:          Run gap audit again to verify coverage improved
```

## Requirements

- Gap audit report JSON file (from `taliaz-kb-gap-audit`)
- `taliaz-email-ingest` skill installed (for email ingestion)
- `taliaz-transcript-ingest` skill installed (for transcript ingestion)
- Supabase credentials, Gmail MCP, rclone configured